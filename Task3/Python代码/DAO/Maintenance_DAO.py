from DAO.DAO import BaseDAO
from classes.Maintenance import Maintenance


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

    def get_all(self):
        query = """
            SELECT * FROM Maintenance
        """
        rows = self.fetch_all(query)
        return [Maintenance(*row) for row in rows] if rows else []

    def get_last_task_id(self):
        query = """
            SELECT MAX(task_id) FROM Maintenance
        """
        result = self.fetch_one(query)
        return result[0] if result is not None else None

    def get_maintenance_users(self, task_id, man_user_dao):
        return man_user_dao.get_users_for_task(task_id)

    def get_maintenance_plants(self, task_id, plant_maintenance_dao):
        return plant_maintenance_dao.get_plants_for_task(task_id)
