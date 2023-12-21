import abc
from DAO.dao import base_dao
from classes.equipment_plant import equipment_plant

class equipment_plant_dao(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def insert(self, equipment_plant):
        pass

    @abc.abstractmethod
    def update(self, equipment_plant):
        pass

    @abc.abstractmethod
    def delete(self, equipment_plant):
        pass

    @abc.abstractmethod
    def select(self, sql):
        pass


class equipment_plant_dao_Impl(base_dao, equipment_plant_dao):
    @classmethod
    def __init__(self):
        self.connect = self.get_conn()

    def insert(self, equipment_plant):
        cursor = self.connect.cursor()
        cursor.execute("insert into equipment_plant (equipment_id, plant_id) values(%s,%s)",(equipment_plant._equipment_id,equipment_plant._plant_id))
        self.connect.commit()
        cursor.close()

    def update(self, equipment_plant):
        cursor = self.connect.cursor()
        cursor.execute("UPDATE equipment_plant SET plant_id=%s WHERE equipment_id=%s", (
            equipment_plant._plant_id, equipment_plant._equipment_id))
        self.connect.commit()
        cursor.close()

    def delete(self, equipment_plant):
        cursor = self.connect.cursor()
        cursor.execute("delete from equipment_plant where equipment_id=%s", (equipment_plant._equipment_id))
        self.connect.commit()
        cursor.close()

    def select(self, sql):
        cursor = self.connect.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()
        cursor.close()
        return result

