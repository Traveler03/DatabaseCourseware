import abc
from dao import base_dao
from ExceptionLog import ExceptionLog

class ExceptionLog_dao(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def insert(self, ExceptionLog):
        pass

    @abc.abstractmethod
    def update(self, ExceptionLog):
        pass

    @abc.abstractmethod
    def delete(self, id):
        pass

    @abc.abstractmethod
    def select(self, id):
        pass


class ExceptionLog_dao_Impl(base_dao, ExceptionLog_dao):
    @classmethod
    def __init__(self):
        self.connect = self.get_conn()

    def insert(self, ExceptionLog):
        cursor = self.connect.cursor()
        cursor.execute("insert into ExceptionLog (monitor_id, exception_detail) values(%s,%s)",(ExceptionLog._monitor_id,ExceptionLog._exception_detail))
        self.connect.commit()
        cursor.close()

    def update(self, ExceptionLog):
        cursor = self.connect.cursor()
        cursor.execute("UPDATE ExceptionLog SET exception_detail=%s WHERE monitor_id=%s", (
            ExceptionLog._exception_detail, ExceptionLog._monitor_id))
        self.connect.commit()
        cursor.close()

    def delete(self, id):
        cursor = self.connect.cursor()
        cursor.execute("delete from ExceptionLog where monitor_id=%s", (id))
        self.connect.commit()
        cursor.close()

    def select(self):
        cursor = self.connect.cursor()
        cursor.execute("select * from ExceptionLog ")
        result = cursor.fetchall()
        cursor.close()
        return result

    def selectall(self):
        cursor = self.connect.cursor()
        cursor.execute("select * from ExceptionLog")
        result = cursor.fetchall()
        cursor.close()
        return result