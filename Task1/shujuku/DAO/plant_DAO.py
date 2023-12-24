
import abc
from DAO.dao import base_dao
from classes.plant import plant
class plant_dao(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def insert(self, plant):
        pass

    @abc.abstractmethod
    def update(self,id,value,choose,plant=None):
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
        cursor.execute("insert into plant (species_name,alia,morphology,value,key_tech,environment,created_by,created_at,updated_at) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)",(plant._species_name,plant._alies,plant._morphology,plant._value,plant._key_tech,plant._environment,plant._created_by,plant._created_at,plant._updated_at))
        self.connect.commit()
        cursor.close()
    def update(self,choose,id=None,value=None,plant=None):
        cursor = self.connect.cursor()
        if choose==0:
            cursor.execute("UPDATE plant SET species_name='%s',alia='%s',morphology='%s',value='%s',key_tech='%s',environment='%s',created_by='%s',created_at='%s',updated_at='%s'  where plant_id=%d", (
            plant._species_name,plant._alies,plant._morphology,plant._value,plant._key_tech,plant._environment,plant._created_by,plant._created_at,plant._updated_at,plant._plant_id))
            self.connect.commit()
        elif choose==1:
            cursor.execute("UPDATE plant SET species_name='%s' where plant_id=%s"%(value,id))
            self.connect.commit()
        elif choose==2:
            cursor.execute("UPDATE plant SET alia='%s' where plant_id=%s"%(value,id))
            self.connect.commit()
        elif choose==3:
            cursor.execute("UPDATE plant SET morphology='%s' where plant_id=%s"%(value,id))
            self.connect.commit()
        elif choose==4:
            cursor.execute("UPDATE plant SET value='%s' where plant_id=%s"%(value,id))
            self.connect.commit()
        elif choose==5:
            cursor.execute("UPDATE plant SET key_tech='%s' where plant_id=%s"%(value,id))
            self.connect.commit()
        elif choose==6:
            cursor.execute("UPDATE plant SET environment='%s' where plant_id=%s"%(value,id))
            self.connect.commit()
        cursor.close()
    def delete(self, value):
        cursor = self.connect.cursor()
        cursor.execute("delete from plant where plant_id=%s", (value))
        self.connect.commit()
        cursor.close()
    def select(self,sql):
        cursor = self.connect.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()
        cursor.close()
        return result
    def creatview(self,sql):
        cursor = self.connect.cursor()
        cursor.execute(sql)
        cursor.close()