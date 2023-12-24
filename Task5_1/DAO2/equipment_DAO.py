import abc
from dao import base_dao
from equipment import equipment

class equipment_dao(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def insert(self, name):
        pass

    @abc.abstractmethod
    def update(self, equipment):
        pass

    @abc.abstractmethod
    def delete(self, id):
        pass

    @abc.abstractmethod
    def select(self, id):
        pass


class equipment_dao_Impl(base_dao, equipment_dao):
    @classmethod
    def __init__(self):
        self.connect = self.get_conn()

    def insert(self, name):
        cursor = self.connect.cursor()
        cursor.execute("insert into equipment ( equipment_name) values(%s)",(name))
        self.connect.commit()
        cursor.close()

    def update(self, equipment):
        cursor = self.connect.cursor()
        cursor.execute("UPDATE equipment SET equipment_name=%s WHERE equipment_id=%s", (
            equipment._equipment_name, equipment._equipment_id))
        self.connect.commit()
        cursor.close()

    def delete(self, id):
        cursor = self.connect.cursor()
        cursor.execute("delete from equipment where equipment_id=%s", (id))
        self.connect.commit()
        cursor.close()

    def select(self, id):
        cursor = self.connect.cursor()
        cursor.execute("select * from equipment where equipment_id=%s", (id))
        result = cursor.fetchall()
        cursor.close()
        return result

