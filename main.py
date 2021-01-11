import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Base

conexao = 'sqlite+pysqlite:///' + os.path.join(os.path.abspath(os.path.dirname(__file__)), 'storage.db')
engine = create_engine(f'{conexao}', echo=True)


def make_session():
    return sessionmaker(bind=engine)


if __name__ == '__main__':
    Base.metadata.create_all(engine, checkfirst=True)
    print('I\'m main!')
    print(Base.__dict__)
