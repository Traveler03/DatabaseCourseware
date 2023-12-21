import abc
from DAO.dao import base_dao
from classes.plant_metrics import plant_metrics

class plant_metrics_dao(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def insert(self, plant_metrics):
        pass

    @abc.abstractmethod
    def update(self, plant_metrics):
        pass

    @abc.abstractmethod
    def delete(self, plant_metrics):
        pass

    @abc.abstractmethod
    def select(self, sql):
        pass


class plant_metrics_dao_Impl(base_dao, plant_metrics_dao):
    @classmethod
    def __init__(self):
        self.connect = self.get_conn()

    def insert(self, plant_metrics):
        cursor = self.connect.cursor()
        cursor.execute("insert into plant_metrics (plant_id, metrics_ip) values(%s,%s)",(plant_metrics._plant_id,plant_metrics._metrics_ip))
        self.connect.commit()
        cursor.close()

    def update(self, plant_metrics):
        cursor = self.connect.cursor()
        cursor.execute("UPDATE plant_metrics SET metrics_ip=%s WHERE plant_id=%s", (
            plant_metrics._metrics_ip, plant_metrics._plant_id))
        self.connect.commit()
        cursor.close()

    def delete(self, plant_metrics):
        cursor = self.connect.cursor()
        cursor.execute("delete from plant_metrics where plant_id=%s", (plant_metrics._plant_id))
        self.connect.commit()
        cursor.close()

    def select(self, sql):
        cursor = self.connect.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()
        cursor.close()
        return result

