
import abc
from DAO.dao import base_dao
from classes.region import region
class region_dao(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def insert(self, region):
        pass

    @abc.abstractmethod
    def update(self, region):
        pass

    @abc.abstractmethod
    def delete(se1f, region):
        pass

    @abc.abstractmethod
    def select(se1f, sql):
        pass
class region_dao_Impl(base_dao,region_dao):
    @classmethod
    def __int__(self):
        self.connect=self.get_conn()
    def insert(self, region):
        cursor=self.connect.cursor()
        cursor.execute("insert into region (parent,rank,class_name) values(%s,%s,%s)",( region._parent,region._rank,region._region_name))
        self.connect.commit()
        cursor.close()
    def update(self,region):
        cursor = self.connect.cursor()
        cursor.execute("UPDATE region SET region_parent=%s,region_rank=%s,region_class_name=%s  where region_id=%s", (
         region._parent,region._rank,region._region_name,region._region_id))
        self.connect.commit()
        cursor.close()
    def delete(self, region):
        cursor = self.connect.cursor()
        cursor.execute("delete from region where region_id=%s", (region._region_id))
        self.connect.commit()
        cursor.close()
    def select(self,sql):
        cursor = self.connect.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()
        cursor.close()
        return result