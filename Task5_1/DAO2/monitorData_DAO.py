import abc
from dao import base_dao
from monitorData import monitorData

class monitorData_dao(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def insert(self, monitorData):
        pass

    @abc.abstractmethod
    def update(self, monitorData):
        pass

    @abc.abstractmethod
    def delete(self, id):
        pass

    @abc.abstractmethod
    def select(self, id):
        pass


class monitorData_dao_Impl(base_dao, monitorData_dao):
    @classmethod
    def __init__(self):
        self.connect = self.get_conn()

    def insert(self, monitorData):
        cursor = self.connect.cursor()
        cursor.execute("insert into monitorData (monitor_id, monitor_region, monitor_time, plant_id, monitor_temp, monitor_grow, monitor_illu) values(%s,%s,%s,%s,%s,%s,%s)",(monitorData._monitor_id, monitorData._monitor_region, monitorData._monitor_time, monitorData._plant_id, monitorData._monitor_temp, monitorData._monitor_grow, monitorData._monitor_illu))
        self.connect.commit()
        cursor.close()

    def update(self, monitorData):
        cursor = self.connect.cursor()
        cursor.execute("UPDATE monitorData SET monitor_region=%s, monitor_time=%s, plant_id=%s, monitor_temp=%s, monitor_grow=%s, monitor_illu=%s WHERE monitor_id=%s", (
            monitorData._monitor_region, monitorData._monitor_time, monitorData._plant_id, monitorData._monitor_temp, monitorData._monitor_grow, monitorData._monitor_illu, monitorData._monitor_id))
        self.connect.commit()
        cursor.close()

    def delete(self, id):
        cursor = self.connect.cursor()
        cursor.execute("delete from monitorData where monitor_id=%s", (id))
        self.connect.commit()
        cursor.close()

    def select(self, id):
        cursor = self.connect.cursor()
        cursor.execute("select * from monitorData where plant_id=%s", (id))
        result = cursor.fetchall()
        cursor.close()
        return result

