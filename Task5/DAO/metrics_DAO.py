import abc
from DAO.dao import base_dao
from classes.metrics import metrics

class metrics_dao(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def insert(self, metrics):
        pass

    @abc.abstractmethod
    def update(self, metrics):
        pass

    @abc.abstractmethod
    def delete(self, metrics):
        pass

    @abc.abstractmethod
    def select(self, sql):
        pass


class metrics_dao_Impl(base_dao, metrics_dao):
    @classmethod
    def __init__(self):
        self.connect = self.get_conn()

    def insert(self, metrics):
        cursor = self.connect.cursor()
        cursor.execute("insert into metrics (metrics_ip, illumination, temperature, grow) values(%s,%s,%s,%s)",(metrics._metrics_ip,metrics._illumination,metrics._temperature,metrics._grow))
        self.connect.commit()
        cursor.close()

    def update(self, metrics):
        cursor = self.connect.cursor()
        cursor.execute("UPDATE metrics SET illumination=%s,temperature=%s,grow=%s  where metrics_ip=%s", (
         metrics._illumination,metrics._temperature,metrics._grow,metrics._metrics_ip))
        self.connect.commit()
        cursor.close()

    def delete(self, metrics):
        cursor = self.connect.cursor()
        cursor.execute("delete from metrics where metrics_ip=%s", (metrics._metrics_ip))
        self.connect.commit()
        cursor.close()

    def select(self, sql):
        cursor = self.connect.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()
        cursor.close()
        return result

