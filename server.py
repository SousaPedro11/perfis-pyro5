import os

import Pyro5.api
import Pyro5.server
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import DAO
from models import Experiencia, Formacao, Habilidade, Pessoa, Base

conexao = 'sqlite+pysqlite:///' + os.path.join(os.path.abspath(os.path.dirname(__file__)), 'storage.db')
engine = create_engine(f'{conexao}', echo=True)
Session = sessionmaker(bind=engine, autoflush=False)


@Pyro5.api.expose
class Server:

    session = None

    def cadastrar_perfil(self, experiencia_dict, formacao_dict, habilidade_dict, pessoa_dict):
        try:
            email = pessoa_dict['email']
            pessoa = DAO.buscar_por_criterio(self.session, Pessoa, email=email)
            experiencia = DAO.buscar_por_criterio(self.session, Experiencia, **experiencia_dict)
            formacao = DAO.buscar_por_criterio(self.session, Formacao, **formacao_dict)
            habilidade = DAO.buscar_por_criterio(self.session, Habilidade, **habilidade_dict)
            if experiencia is None:
                experiencia = Experiencia(**experiencia_dict)
            if formacao is None:
                formacao = Formacao(**formacao_dict)
            if habilidade is None:
                habilidade = Habilidade(**habilidade_dict)
            if pessoa is None:
                pessoa = Pessoa(**pessoa_dict)

            pessoa.experiencias.append(experiencia) if experiencia not in pessoa.experiencias else None
            pessoa.formacoes.append(formacao) if formacao not in pessoa.formacoes else None
            pessoa.habilidades.append(habilidade) if habilidade not in pessoa.habilidades else None

            DAO.transacao(self.session, pessoa)
            return f'Perfil Cadatrado!\n{pessoa}'
        except Exception as e:
            print(e)

    def pessoas_por_formacao(self, curso):
        pessoas = DAO.buscar_todos_por_join(session=self.session, table1=Pessoa, table2=Formacao, order_by=Pessoa.nome,
                                            nome=curso)
        return pessoas

    def listar_pessoas(self):
        pessoas = DAO.buscar_todos(self.session, Pessoa)
        return f'Listagem de Pessoas:\n{pessoas}\n'

    def open_session(self):
        self.session = Session()

    def close_session(self):
        self.session.close()


Base.metadata.create_all(engine, checkfirst=True)
daemon = Pyro5.server.Daemon()
ns = Pyro5.api.locate_ns()
uri = daemon.register(Server)
ns.register('perfis', uri)
daemon.requestLoop()
