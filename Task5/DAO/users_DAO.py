import abc
from DAO.dao import base_dao
from classes.users import users

class users_dao(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def insert(self, user):
        pass

    @abc.abstractmethod
    def update(self, user):
        pass

    @abc.abstractmethod
    def delete(self, user):
        pass

    @abc.abstractmethod
    def select(self, sql):
        pass


class users_dao_Impl(base_dao, users_dao):
    @classmethod
    def __init__(self):
        self.connect = self.get_conn()

    def insert(self, user):
        cursor = self.connect.cursor()
        cursor.execute("insert into users (user_name, password, posts, Permissions) values(%s,%s,%s,%s)",(user._user_name,user._password,user._posts,user._Permissions))
        self.connect.commit()
        cursor.close()

    def update(self, user):
        cursor = self.connect.cursor()
        cursor.execute("UPDATE users SET user_name=%s,password=%s,posts=%s,Permissions=%s  where user_id=%s", (
         user._user_name,user._password,user._posts,user._Permissions,user._user_id))
        self.connect.commit()
        cursor.close()

    def delete(self, user):
        cursor = self.connect.cursor()
        cursor.execute("delete from users where user_id=%s", (user._user_id))
        self.connect.commit()
        cursor.close()

    def select(self, sql):
        cursor = self.connect.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()
        cursor.close()
        return result

