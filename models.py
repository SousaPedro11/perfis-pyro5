from sqlalchemy import Column, VARCHAR, ForeignKey, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

from Util import __generate_id__

Base = declarative_base()

pessoa_habilidade = Table(
    'pessoa_habilidade',
    Base.metadata,
    Column('pessoa_id', VARCHAR(36), ForeignKey('pessoa.email')),
    Column('habilidade_id', VARCHAR(36), ForeignKey('habilidade.id')),
)

pessoa_formacao = Table(
    'pessoa_formacao',
    Base.metadata,
    Column('pessoa_id', VARCHAR(36), ForeignKey('pessoa.email')),
    Column('formacao_id', VARCHAR(36), ForeignKey('formacao.id')),
)

pessoa_experiencia = Table(
    'pessoa_experiencia',
    Base.metadata,
    Column('pessoa_id', VARCHAR(36), ForeignKey('pessoa.email')),
    Column('experiencia_id', VARCHAR(36), ForeignKey('experiencia.id')),
)


class Pessoa(Base):
    __tablename__ = 'pessoa'

    email = Column(VARCHAR(100), primary_key=True)
    nome = Column(VARCHAR(100), nullable=False)
    sobrenome = Column(VARCHAR(100), nullable=False)
    residencia = Column(VARCHAR, nullable=False)
    foto = Column(VARCHAR, nullable=True)

    habilidades = relationship(
        'Habilidade',
        secondary=pessoa_habilidade,
        back_populates='pessoas'
    )
    formacoes = relationship(
        'Formacao',
        secondary=pessoa_formacao,
        back_populates='pessoas'
    )
    experiencias = relationship(
        'Experiencia',
        secondary=pessoa_experiencia,
        back_populates='pessoas'
    )

    def __repr__(self):
        return f'Email: {self.email}\n' \
               f'Nome: {self.nome} Sobrenome: {self.sobrenome}\n' \
               f'Foto: {self.foto if len(self.foto.strip()) > 0 else "Não possui"}\n' \
               f'Residência: {self.residencia}\n' \
               f'Formacao Acadêmica: {", ".join([str(x) for x in self.formacoes])}\n' \
               f'Habilidades: {", ".join([str(x) for x in self.habilidades])}\n' \
               f'Experiência: {", ".join([str(x) for x in self.experiencias])}\n'


class Formacao(Base):
    __tablename__ = 'formacao'
    id = Column(VARCHAR(36), primary_key=True, default=__generate_id__())
    nome = Column(VARCHAR, nullable=True, unique=True)
    pessoas = relationship(
        'Pessoa',
        secondary=pessoa_formacao,
        back_populates='formacoes'
    )

    def __repr__(self):
        return f'{self.nome}'


class Experiencia(Base):
    __tablename__ = 'experiencia'
    id = Column(VARCHAR(36), primary_key=True, default=__generate_id__())
    nome = Column(VARCHAR, nullable=True, unique=True)

    pessoas = relationship(
        'Pessoa',
        secondary=pessoa_experiencia,
        back_populates='experiencias'
    )

    def __repr__(self):
        return f'{self.nome}'


class Habilidade(Base):
    __tablename__ = 'habilidade'
    id = Column(VARCHAR(36), primary_key=True, default=__generate_id__())
    nome = Column(VARCHAR, nullable=True, unique=True)

    pessoas = relationship(
        'Pessoa',
        secondary=pessoa_habilidade,
        back_populates='habilidades'
    )

    def __repr__(self):
        return f'{self.nome}'
