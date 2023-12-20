import abc
import pymssql
class dao(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def get_conn(cls):
        pass
    @abc.abstractmethod
    def close_conn(cls,conn):
        pass
class base_dao(dao):
    _conn=None
    @classmethod
    def get_conn(cls,server= '127.0.0.1',username= 'sa',password= '1103003X',database= 'Gardenplants'):
        cls._conn = pymssql.connect(server=server, user=username, password=password, database=database)
        return cls._conn
    @classmethod
    def close_conn(cls,conn):
        conn.close()