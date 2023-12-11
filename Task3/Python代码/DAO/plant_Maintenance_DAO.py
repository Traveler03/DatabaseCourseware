from DAO import BaseDAO  # 假设有一个 BaseDAO 类，包含通用的数据库操作方法
from classes import plant_Maintenance

class PlantMaintenanceDAO(BaseDAO):
    def __init__(self, db):
        super().__init__(db)

    def insert(self, plant_maintenance):
        query = """
            INSERT INTO plant_Maintenance (plant_id, task_id)
            VALUES (?, ?)
        """
        params = (plant_maintenance.get_plant_id(), plant_maintenance.get_task_id())
        self.execute_query(query, params)

    def update(self, plant_maintenance):
        query = """
            UPDATE plant_Maintenance
            SET task_id = ?
            WHERE plant_id = ?
        """
        params = (plant_maintenance.get_task_id(), plant_maintenance.get_plant_id())
        self.execute_query(query, params)

    def delete(self, plant_maintenance):
        query = """
            DELETE FROM plant_Maintenance
            WHERE plant_id = ?
        """
        params = (plant_maintenance.get_plant_id(),)
        self.execute_query(query, params)

    def find(self, plant_id):
        query = """
            SELECT * FROM plant_Maintenance
            WHERE plant_id = ?
        """
        params = (plant_id,)
        row = self.fetch_one(query, params)
        if row is not None:
            return plant_Maintenance(*row)
        return None
