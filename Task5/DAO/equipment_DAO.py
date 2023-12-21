import abc
from DAO.dao import base_dao
from classes.equipment import equipment

class equipment_dao(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def insert(self, equipment):
        pass

    @abc.abstractmethod
    def update(self, equipment):
        pass

    @abc.abstractmethod
    def delete(self, equipment):
        pass

    @abc.abstractmethod
    def select(self, sql):
        pass


class equipment_dao_Impl(base_dao, equipment_dao):
    @classmethod
    def __init__(self):
        self.connect = self.get_conn()

    def insert(self, equipment):
        cursor = self.connect.cursor()
        cursor.execute("insert into equipment (equipment_id, equipment_name) values(%s,%s)",(equipment._equipment_id,equipment._equipment_name))
        self.connect.commit()
        cursor.close()

    def update(self, equipment):
        cursor = self.connect.cursor()
        cursor.execute("UPDATE equipment SET equipment_name=%s WHERE equipment_id=%s", (
            equipment._equipment_name, equipment._equipment_id))
        self.connect.commit()
        cursor.close()

    def delete(self, equipment):
        cursor = self.connect.cursor()
        cursor.execute("delete from equipment where equipment_id=%s", (equipment._equipment_id))
        self.connect.commit()
        cursor.close()

    def select(self, sql):
        cursor = self.connect.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()
        cursor.close()
        return result

