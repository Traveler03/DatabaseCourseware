
import abc
from DAO.dao import base_dao
from classes.plant_region import plant_region
class plant_region_dao(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def insert(self, plant_region):
        pass

    @abc.abstractmethod
    def delete(se1f, plant_region):
        pass

    @abc.abstractmethod
    def select(se1f, sql):
        pass
class plant_region_dao_Impl(base_dao,plant_region_dao):
    @classmethod
    def __int__(self):
        self.connect=self.get_conn()
    def insert(self, plant_region):
        cursor=self.connect.cursor()
        cursor.execute("insert into plant_region values(%d,%d)",(plant_region._plant_id, plant_region._region_id))
        self.connect.commit()
        cursor.close()
    def delete(self, plant_region):
        cursor = self.connect.cursor()
        cursor.execute("delete from plant_region where plant_id=%s and region_id=%s", (plant_region._plant_id,plant_region._region_id))
        self.connect.commit()
        cursor.close()
    def select(self,sql):
        cursor = self.connect.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()
        cursor.close()
        return result