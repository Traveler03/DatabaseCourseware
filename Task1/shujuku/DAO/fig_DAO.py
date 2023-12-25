
import abc
from DAO.dao import base_dao
from classes.fig import fig
class fig_dao(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def insert(self, fig):
        pass

    @abc.abstractmethod
    def update(self,choose,id=None,value=None,fig=None):
        pass

    @abc.abstractmethod
    def delete(se1f, fig):
        pass

    @abc.abstractmethod
    def select(se1f, sql):
        pass
class fig_dao_Impl(base_dao,fig_dao):
    @classmethod
    def __int__(self):
        self.connect=self.get_conn()
    def insert(self, fig):
        cursor=self.connect.cursor()
        cursor.execute("insert into fig (fig_path,fig_place,fig_people,fig_des,created_by,creater_at,updated_at) values(%s,%s,%s,%s,%s,%s,%s)",(fig._image_path,fig._image_location,fig._image_photographer,fig._image_description,fig._created_by,fig._created_at,fig._updated_at))
        self.connect.commit()
        cursor.close()
    def update(self,choose,id=None,value=None,fig=None):
        cursor = self.connect.cursor()
        if choose==0:
            cursor.execute("UPDATE fig SET fig_path='%s',fig_place='%s',fig_people='%s',fig_des='%s',created_by='%s',creater_at='%s',updated_at='%s')  where fig_id=%s", (
            fig._image_path,fig._image_location,fig._image_photographer,fig._image_description,fig._created_by,fig._created_at,fig._updated_at,fig._image_id))
            self.connect.commit()
        elif choose == 1:
            cursor.execute("UPDATE fig SET fig_path='%s' where fig_id=%s" % (value, id))
            self.connect.commit()
        elif choose == 2:
            cursor.execute("UPDATE fig SET fig_place='%s' where fig_id=%s" % (value, id))
            self.connect.commit()
        elif choose == 3:
            cursor.execute("UPDATE fig SET fig_people='%s' where fig_id=%s" % (value, id))
            self.connect.commit()
        elif choose == 4:
            cursor.execute("UPDATE fig SET fig_des='%s' where fig_id=%s" % (value, id))
            self.connect.commit()

        cursor.close()
    def delete(self, value):
        cursor = self.connect.cursor()
        cursor.execute("delete from fig where fig_id=%s", (value))
        self.connect.commit()
        cursor.close()
    def select(self,sql,path=None):
        cursor = self.connect.cursor()
        if path==None:
            cursor.execute(sql)
        else:
            cursor.execute(sql,(path))
        result = cursor.fetchall()
        cursor.close()
        return result