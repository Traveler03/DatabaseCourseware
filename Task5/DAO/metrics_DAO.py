import abc
from dao import base_dao
from metrics import metrics

class metrics_dao(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def insert(self, i1,i2,i3):
        pass

    @abc.abstractmethod
    def update(self, metrics):
        pass

    @abc.abstractmethod
    def delete(self, id):
        pass

    @abc.abstractmethod
    def select(self, id):
        pass


class metrics_dao_Impl(base_dao, metrics_dao):
    @classmethod
    def __init__(self):
        self.connect = self.get_conn()

    def insert(self, i1,i2,i3):
        cursor = self.connect.cursor()
        cursor.execute("insert into metrics (illumination, temperature, grow) values(%s,%s,%s)",(i1,i2,i3))
        self.connect.commit()
        cursor.close()

    def update(self, metrics):
        cursor = self.connect.cursor()
        cursor.execute("UPDATE metrics SET illumination=%s,temperature=%s,grow=%s  where metrics_ip=%s", (
         metrics._illumination,metrics._temperature,metrics._grow,metrics._metrics_ip))
        self.connect.commit()
        cursor.close()

    def delete(self, id):
        cursor = self.connect.cursor()
        cursor.execute("delete from metrics where  metrics_ip=%s", (id))
        self.connect.commit()
        cursor.close()

    def select(self, id):
        cursor = self.connect.cursor()
        cursor.execute("select * from metrics where metrics_ip=%s", (id))
        result = cursor.fetchall()
        cursor.close()
        return result

