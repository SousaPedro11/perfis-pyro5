import os

SQLALCHEMY_DATABASE_URI = 'sqlite+pysqlite:///' + os.path.join(os.path.abspath(os.path.dirname(__file__)), 'storage.db')
