from DAO import BaseDAO  # 假设有一个 BaseDAO 类，包含通用的数据库操作方法
from classes import Maintenance


class MaintenanceDAO(BaseDAO):
    def __init__(self, db):
        super().__init__(db)

    def insert(self, maintenance):
        query = """
            INSERT INTO Maintenance (task_id, task_name, time, place, task_des)
            VALUES (?, ?, ?, ?, ?)
        """
        params = (
            maintenance.get_task_id(), maintenance.get_task_name(), maintenance.get_time(), maintenance.get_place(),
            maintenance.get_task_des())
        self.execute_query(query, params)

    def update(self, maintenance):
        query = """
            UPDATE Maintenance
            SET task_name = ?, time = ?, place = ?, task_des = ?
            WHERE task_id = ?
        """
        params = (
            maintenance.get_task_name(), maintenance.get_time(), maintenance.get_place(), maintenance.get_task_des(),
            maintenance.get_task_id())
        self.execute_query(query, params)

    def delete(self, maintenance):
        query = """
            DELETE FROM Maintenance
            WHERE task_id = ?
        """
        params = (maintenance.get_task_id(),)
        self.execute_query(query, params)

    def find(self, task_id):
        query = """
            SELECT * FROM Maintenance
            WHERE task_id = ?
        """
        params = (task_id,)
        row = self.fetch_one(query, params)
        if row is not None:
            return Maintenance(*row)
        return None
