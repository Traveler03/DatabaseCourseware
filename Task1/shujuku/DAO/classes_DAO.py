
import abc
from DAO.dao import base_dao
from classes.classes import classes
class classes_dao(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def insert(self, classes):
        pass

    @abc.abstractmethod
    def update(self, choose,id=None,value=None,classes=None):
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
    def update(self,choose,id=None,value=None,classes=None):
        cursor = self.connect.cursor()
        if choose==0:
            cursor.execute("UPDATE classes SET parent='%s',rank='%s',classes_class_name='%s'  where class_id=%s", (
            classes._parent,classes._rank,classes._class_name,classes._class_id))
            self.connect.commit()
        elif choose == 1:
            cursor.execute("UPDATE classes SET parent='%s' where class_id=%s" % (value, id))
            self.connect.commit()
        elif choose == 2:
            cursor.execute("UPDATE classes SET rank='%s' where class_id=%s" % (value, id))
            self.connect.commit()
        elif choose == 3:
            cursor.execute("UPDATE classes SET class_name='%s' where class_id=%s" % (value, id))
            self.connect.commit()
        cursor.close()
    def delete(self,value):
        cursor = self.connect.cursor()
        cursor.execute("delete from classes where class_id=%s", (value))
        self.connect.commit()
        cursor.close()
    def select(self,sql):
        cursor = self.connect.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()
        cursor.close()
        return result