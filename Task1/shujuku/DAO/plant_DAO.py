
import abc
from DAO.dao import base_dao

class plant_dao(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def insert(self, plant):
        pass

    @abc.abstractmethod
    def update(self, plant):
        pass

    @abc.abstractmethod
    def delete(se1f, plant):
        pass

    @abc.abstractmethod
    def select(se1f, sql):
        pass
class plant_dao_Impl(base_dao,plant_dao):
    @classmethod
    def __int__(self):
        self.connect=self.get_conn()
    def insert(self, plant):
        cursor=self.connect.cursor()
        cursor.execute("insert into plant values(%s,%s,%s,%s,%s,%s,%s,%s,%s)",(plant._plant_id, plant._species_name,plant._morphology,plant._value,plant._key_tech,plant._environment,plant._created_at,plant._created_by,plant._updated_at))
        self.connect.commit()
        cursor.close()
    def update(self,plant):
        cursor = self.connect.cursor()
        cursor.execute("UPDATE plant SET species_name=%s,morphology=%s,value=%s,key_tech=%s,key_tech=%s,environment=%s,created_by=%s,created_at=STR_TO_DATE('%s', '%Y-%m-%d'),updated_at=STR_TO_DATE('%s', '%Y-%m-%d'))  where plant_id=%s", (
         plant._species_name,plant._morphology,plant._value,plant._key_tech,plant._environment,plant._created_at,plant._created_by,plant._updated_at,plant._plant_id))
        self.connect.commit()
        cursor.close()
    def delete(self, plant):
        cursor = self.connect.cursor()
        cursor.execute("delete from plant where plant_id=%s", (plant._plant_id))
        self.connect.commit()
        cursor.close()
    def select(self,sql):
        cursor = self.connect.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()
        cursor.close()
        return result