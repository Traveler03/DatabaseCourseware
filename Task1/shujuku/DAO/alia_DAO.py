import abc
from DAO.dao import base_dao

class alia_dao(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def insert(self, alia):
        pass
    @abc.abstractmethod
    def delete(se1f, alia):
        pass

    @abc.abstractmethod
    def select(se1f, sql):
        pass
class alia_dao_Impl(base_dao,alia_dao):
    @classmethod
    def __int__(self):
        self.connect=self.get_conn()
    def insert(self, alia):
        cursor=self.connect.cursor()
        cursor.execute("insert into alia values(%s,%s)",(alia._plant_id, alia._alias))
        self.connect.commit()
        cursor.close()
    def delete(self, alia):
        cursor = self.connect.cursor()
        cursor.execute("delete from alia where plant_id=%s and alias=%s", (alia._plant_id,alia._alias))
        self.connect.commit()
        cursor.close()
    def select(self,sql):
        cursor = self.connect.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()
        cursor.close()
        return result