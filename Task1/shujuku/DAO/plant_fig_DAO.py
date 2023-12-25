
import abc
from DAO.dao import base_dao
from classes.plant_fig import plant_fig
class plant_fig_dao(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def insert(self, plant_fig):
        pass

    @abc.abstractmethod
    def delete(se1f, plant_fig):
        pass

    @abc.abstractmethod
    def select(se1f, sql):
        pass
class plant_fig_dao_Impl(base_dao,plant_fig_dao):
    @classmethod
    def __int__(self):
        self.connect=self.get_conn()
    def insert(self, plant_fig):
        cursor=self.connect.cursor()
        cursor.execute("insert into plant_fig values(%d,%d)",(plant_fig._plant_id, plant_fig._image_id))
        self.connect.commit()
        cursor.close()
    def delete(self, plant_fig):
        cursor = self.connect.cursor()
        cursor.execute("delete from plant_fig where plant_id=%s and fig_id=%s", (plant_fig._plant_id,plant_fig._image_id))
        self.connect.commit()
        cursor.close()
    def select(self,sql):
        cursor = self.connect.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()
        cursor.close()
        return result