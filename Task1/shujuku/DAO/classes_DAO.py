
import abc
from DAO.dao import base_dao
from classes.classes import classes
class classes_dao(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def insert(self, classes):
        pass

    @abc.abstractmethod
    def update(self, classes):
        pass

    @abc.abstractmethod
    def delete(se1f, classes):
        pass

    @abc.abstractmethod
    def select(se1f, sql):
        pass
class classes_dao_Impl(base_dao,classes_dao):
    @classmethod
    def __int__(self):
        self.connect=self.get_conn()
    def insert(self, classes):
        cursor=self.connect.cursor()
        cursor.execute("insert into classes (parent,rank,class_name) values(%s,%s,%s)",( classes._parent,classes._rank,classes._class_name))
        self.connect.commit()
        cursor.close()
    def update(self,classes):
        cursor = self.connect.cursor()
        cursor.execute("UPDATE classes SET classes_parent=%s,classes_rank=%s,classes_class_name=%s  where classes_id=%s", (
         classes._parent,classes._rank,classes._class_name,classes._class_id))
        self.connect.commit()
        cursor.close()
    def delete(self, classes):
        cursor = self.connect.cursor()
        cursor.execute("delete from classes where classes_id=%s", (classes._class_id))
        self.connect.commit()
        cursor.close()
    def select(self,sql):
        cursor = self.connect.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()
        cursor.close()
        return result