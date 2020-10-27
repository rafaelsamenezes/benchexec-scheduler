from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

DATABASE = "../db/database.db"
Base = declarative_base()

class SqlAlchemyEngine(abc.ABC):
     """Abstract class for DB handling"""
    @abc.abstractmethod
    def get_db(self):
        raise NotImplementedError()

    def close_db(self):
        raise NotImplementedError()

class SQLiteDB(SqlAlchemyEngine):
    __instance = None

    def __init__(self):
        if SQLiteDB.__instance != None:
            raise Excepetion("This class is a singleton!")
        else:
            self.engine = None
            SQLiteDB.__instance = self

    @staticmethod
    def getInstance():
        if SQLiteDB.__instance == None:
            SQliteDB()
        return SQLiteDB.__instance

    def get_db(self):
        if self.engine is None:
            self.engine = create_engine(f'sqlite:///{DATABASE}:', echo=True)
        return self.engine

    def close_db():
        # This probably shouldn't be called at all
        if self.DB_CONN is not None:
            self.DB_CONN.close()
            self.DB_CONN = None
