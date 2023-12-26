import abc
from dao import base_dao
from plantThreshold import plantThreshold

class plantThreshold_dao(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def insert(self, plantThreshold):
        pass

    @abc.abstractmethod
    def update(self, plantThreshold):
        pass

    @abc.abstractmethod
    def delete(self, id):
        pass



class plantThreshold_dao_Impl(base_dao, plantThreshold_dao):
    @classmethod
    def __init__(self):
        self.connect = self.get_conn()

    def insert(self, plantThreshold):
        cursor = self.connect.cursor()
        cursor.execute("insert into plantThreshold (plant_id, maxtemp,mintemp,maxgrow,mingrow,maxillu,minillu) values(%s,%s,%s,%s,%s,%s,%s)",(
            plantThreshold._plant_id,plantThreshold._maxtemp,plantThreshold._mintemp,plantThreshold._maxgrow,plantThreshold._mingrow,plantThreshold._maxillu,plantThreshold._minillu))
        self.connect.commit()
        cursor.close()

    def update(self, plantThreshold):
        cursor = self.connect.cursor()
        cursor.execute("UPDATE plantThreshold SET maxtemp=%s,mintemp=%s,maxgrow=%s,mingrow=%s,maxillu=%s,minillu=%s WHERE plant_id=%s", (
            plantThreshold._maxtemp,plantThreshold._mintemp,plantThreshold._maxgrow,plantThreshold._mingrow,plantThreshold._maxillu,plantThreshold._minillu,plantThreshold._plant_id))
        self.connect.commit()
        cursor.close()

    def delete(self, id):
        cursor = self.connect.cursor()
        cursor.execute("delete from plantThreshold where plant_id=%s", (id))
        self.connect.commit()
        cursor.close()

    def select(self):
        cursor = self.connect.cursor()
        cursor.execute("select * from plantThreshold")
        result = cursor.fetchall()
        cursor.close()
        return result

    def selectall(self):
        cursor = self.connect.cursor()
        cursor.execute("select * from plantThreshold")
        result = cursor.fetchall()
        cursor.close()
        return result