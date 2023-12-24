import abc
from dao import base_dao


class plant_region_dao(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def insert(self, plant_region):
        pass

    @abc.abstractmethod
    def update(self, plant_region):
        pass

    @abc.abstractmethod
    def delete(self, id):
        pass

    @abc.abstractmethod
    def select(self, id):
        pass


class plant_region_dao_Impl(base_dao, plant_region_dao):
    @classmethod
    def __init__(self):
        self.connect = self.get_conn()

    def insert(self, plant_region):
        cursor = self.connect.cursor()
        cursor.execute("insert into plant_region (plant_id, region) values(%s,%s)",(plant_region._plant_id,plant_region._region))
        self.connect.commit()
        cursor.close()

    def update(self, plant_region):
        cursor = self.connect.cursor()
        cursor.execute("UPDATE plant_region SET region=%s WHERE plant_id=%s", (
            plant_region._region,plant_region._plant_id))
        self.connect.commit()
        cursor.close()

    def delete(self, id):
        cursor = self.connect.cursor()
        cursor.execute("delete from plant_region where plant_id=%s", (id))
        self.connect.commit()
        cursor.close()

    def select(self, id):
        cursor = self.connect.cursor()
        cursor.execute("select * from plant_region where plant_id=%s", (id))
        result = cursor.fetchall()
        cursor.close()
        return result