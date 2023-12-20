
import abc
from DAO.dao import base_dao
from classes.plant_classes import plant_classes
class plant_classes_dao(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def insert(self, plant_classes):
        pass

    @abc.abstractmethod
    def delete(se1f, plant_classes):
        pass

    @abc.abstractmethod
    def select(se1f, sql):
        pass
class plant_classes_dao_Impl(base_dao,plant_classes_dao):
    @classmethod
    def __int__(self):
        self.connect=self.get_conn()
    def insert(self, plant_classes):
        cursor=self.connect.cursor()
        cursor.execute("insert into plant_classes values(%s,%s)",(plant_classes._plant_id, plant_classes._class_id))
        self.connect.commit()
        cursor.close()
    def delete(self, plant_classes):
        cursor = self.connect.cursor()
        cursor.execute("delete from plant_classes where plant_id=%s and class_id=%s", (plant_classes._plant_id,plant_classes._class_id))
        self.connect.commit()
        cursor.close()
    def select(self,sql):
        cursor = self.connect.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()
        cursor.close()
        return result