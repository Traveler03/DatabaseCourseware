
import abc
from DAO.dao import base_dao
from classes.user import user
class user_dao(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def insert(self, user):
        pass

    @abc.abstractmethod
    def update(self, choose,id=None,value=None,user=None):
        pass

    @abc.abstractmethod
    def delete(se1f, user):
        pass

    @abc.abstractmethod
    def select(se1f, sql):
        pass
class user_dao_Impl(base_dao,user_dao):
    @classmethod
    def __int__(self):
        self.connect=self.get_conn()
    def insert(self, user):
        cursor=self.connect.cursor()
        cursor.execute("insert into users (user_name, password, posts, Permissions) values(%s,%s,%s,%s)",(user._user_name,user._password,user._posts,user._Permissions))
        self.connect.commit()
        cursor.close()
    def update(self,choose,id=None,value=None,user=None):
        cursor = self.connect.cursor()
        if choose==0:
            cursor.execute("UPDATE users SET user_name='%s',password='%s',posts='%s',Permissions='%s'  where user_id=%s", (
            user._user_name,user._password,user._posts,user._Permissions,user._user_id))
            self.connect.commit()
        elif choose == 1:
            cursor.execute("UPDATE users SET user_name='%s' where user_id=%s" % (value, id))
            self.connect.commit()
        elif choose == 2:
            cursor.execute("UPDATE users SET password='%s' where user_id=%s" % (value, id))
            self.connect.commit()
        elif choose == 3:
            cursor.execute("UPDATE users SET posts='%s' where user_id=%s" % (value, id))
            self.connect.commit()
        elif choose == 4:
            cursor.execute("UPDATE users SET Permissions='%s' where user_id=%s" % (value, id))
            self.connect.commit()
        cursor.close()
    def delete(self, value):
        cursor = self.connect.cursor()
        cursor.execute("delete from users where user_id=%s", (value))
        self.connect.commit()
        cursor.close()
    def select(self,sql):
        cursor = self.connect.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()
        cursor.close()
        return result