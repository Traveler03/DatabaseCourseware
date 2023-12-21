import abc
from DAO.dao import base_dao
from classes.equipment_metrics import equipment_metrics

class equipment_metrics_dao(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def insert(self, equipment_metrics):
        pass

    @abc.abstractmethod
    def update(self, equipment_metrics):
        pass

    @abc.abstractmethod
    def delete(self, equipment_metrics):
        pass

    @abc.abstractmethod
    def select(self, sql):
        pass


class equipment_metrics_dao_Impl(base_dao, equipment_metrics_dao):
    @classmethod
    def __init__(self):
        self.connect = self.get_conn()

    def insert(self, equipment_metrics):
        cursor = self.connect.cursor()
        cursor.execute("insert into equipment_metrics (equipment_id, metrics_ip) values(%s,%s)",(equipment_metrics._equipment_id,equipment_metrics._metrics_ip))
        self.connect.commit()
        cursor.close()

    def update(self, equipment_metrics):
        cursor = self.connect.cursor()
        cursor.execute("UPDATE equipment_metrics SET metrics_ip=%s WHERE equipment_id=%s", (
            equipment_metrics._metrics_ip, equipment_metrics._equipment_id))
        self.connect.commit()
        cursor.close()

    def delete(self, equipment_metrics):
        cursor = self.connect.cursor()
        cursor.execute("delete from equipment_metrics where equipment_id=%s", (equipment_metrics._equipment_id))
        self.connect.commit()
        cursor.close()

    def select(self, sql):
        cursor = self.connect.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()
        cursor.close()
        return result

