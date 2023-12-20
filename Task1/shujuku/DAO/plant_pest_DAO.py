
import abc
from DAO.dao import base_dao
from classes.plant_pest import plant_pest
class plant_pest_dao(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def insert(self, plant_pest):
        pass

    @abc.abstractmethod
    def delete(se1f, plant_pest):
        pass

    @abc.abstractmethod
    def select(se1f, sql):
        pass
class plant_pest_dao_Impl(base_dao,plant_pest_dao):
    @classmethod
    def __int__(self):
        self.connect=self.get_conn()
    def insert(self, plant_pest):
        cursor=self.connect.cursor()
        cursor.execute("insert into plant_pest values(%s,%s)",(plant_pest._plant_id, plant_pest._pest_id))
        self.connect.commit()
        cursor.close()
    def delete(self, plant_pest):
        cursor = self.connect.cursor()
        cursor.execute("delete from plant_pest where plant_id=%s and pest_id=%s", (plant_pest._plant_id,plant_pest._pest_id))
        self.connect.commit()
        cursor.close()
    def select(self,sql):
        cursor = self.connect.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()
        cursor.close()
        return result