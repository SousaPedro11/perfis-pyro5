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

            pessoa.nome = pessoa_dict['nome']
            pessoa.sobrenome = pessoa_dict['sobrenome']
            pessoa.residencia = pessoa_dict['residencia']
            pessoa.experiencias.append(experiencia) if experiencia not in pessoa.experiencias else None
            pessoa.formacoes.append(formacao) if formacao not in pessoa.formacoes else None
            pessoa.habilidades.append(habilidade) if habilidade not in pessoa.habilidades else None

            DAO.transacao(self.session, pessoa)
            return f'Perfil Cadatrado!\n{pessoa}'
        except Exception as e:
            print(e)

    def pessoas_por_formacao(self, formacao):
        query = self.session.query(Formacao).join(Pessoa, Formacao.pessoas).filter(
            Formacao.nome == formacao['nome']).first()
        result = None
        if Formacao is not None:
            result = '\n'.join([e.__repr__() for e in query.pessoas])
        return f'PESSOAS DO CURSO {formacao["nome"]}\n{result}'

    def pessoas_por_cidade(self, cidade):
        query = self.session.query(Pessoa).join(Habilidade, Pessoa.habilidades).filter(
            Pessoa.residencia == cidade).all()
        result = None
        if len(query) > 0:
            result = '\n'.join([f'Pessoa: {e.nome} {e.sobrenome}, Habilidades: {e.habilidades}' for e in query])
        return f'PESSOAS DA CIDADE {cidade}\n{result}\n'

    def adicionar_experiencia(self, pessoa_dict, experiencia_dict):
        pessoa = DAO.buscar_por_criterio(self.session, Pessoa, email=pessoa_dict['email'])
        if pessoa is None:
            return 'Pessoa não encontrada'
        experiencia = DAO.buscar_por_criterio(self.session, Experiencia, **experiencia_dict)
        if experiencia is None:
            experiencia = Experiencia(**experiencia_dict)
        pessoa.experiencias.append(experiencia) if experiencia not in pessoa.experiencias else None
        DAO.transacao(self.session, pessoa)
        return f'ADICIONAR EXPERIENCIA\nExperiencia {experiencia.nome} adicionada a {pessoa.nome} {pessoa.sobrenome}\n'

    def experiencia_por_perfil(self, email):
        query = self.session.query(Pessoa).join(Experiencia, Pessoa.experiencias).filter(Pessoa.email == email).first()
        if query is None:
            return 'Perfil não encontrado'
        return f'EXPERIENCIA DE {query.nome} {query.sobrenome}\n' \
               f'{query.experiencias}\n'

    def listar_pessoas(self):
        pessoas = DAO.buscar_todos(self.session, Pessoa)
        result = None
        if len(pessoas) > 0:
            result = '\n'.join([e.__repr__() for e in pessoas])
        return f'LISTAGEM DE PERFIS:\n{result}\n'

    def get_perfil_by_id(self, email):
        pessoa = self.session.query(Pessoa).filter(Pessoa.email == email).first()
        if pessoa is None:
            return 'Perfil não encontrado'
        return f'PERFIL COM EMAIL {email}\n{pessoa}'

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
