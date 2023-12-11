from DAO import BaseDAO  # 假设有一个 BaseDAO 类，包含通用的数据库操作方法
from classes import Maninternance_user


class ManinternanceUserDAO(BaseDAO):
    def __init__(self, db):
        super().__init__(db)

    def insert(self, user):
        query = """
            INSERT INTO Maninternance_user (task_id, user_id)
            VALUES (?, ?)
        """
        params = (user.get_task_id(), user.get_user_id())
        self.execute_query(query, params)

    def update(self, user):
        query = """
            UPDATE Maninternance_user
            SET task_id = ?
            WHERE user_id = ?
        """
        params = (user.get_task_id(), user.get_user_id())
        self.execute_query(query, params)

    def delete(self, user):
        query = """
            DELETE FROM Maninternance_user
            WHERE user_id = ?
        """
        params = (user.get_user_id(),)
        self.execute_query(query, params)

    def find(self, user_id):
        query = """
            SELECT * FROM Maninternance_user
            WHERE user_id = ?
        """
        params = (user_id,)
        row = self.fetch_one(query, params)
        if row is not None:
            return Maninternance_user(*row)
        return None
