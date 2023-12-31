from DAO.DAO import BaseDAO  # 假设有一个 BaseDAO 类，包含通用的数据库操作方法
from classes.plant_pest import plant_pest


class PlantPestDAO(BaseDAO):
    def __init__(self, db):
        super().__init__(db)

    def insert(self, plant_pest):
        query = """
            INSERT INTO plant_pest (plant_id, pest_id)
            VALUES (?, ?)
        """
        params = (plant_pest.get_plant_id(), plant_pest.get_pest_id())
        self.execute_query(query, params)

    def delete(self, plant_pest_row):
        query = """
            DELETE FROM plant_pest
            WHERE plant_id = ? AND pest_id = ?
        """
        params = (plant_pest_row.plant_id, plant_pest_row.pest_id)
        self.execute_query(query, params)

    def find(self, plant_id, pest_id):
        query = """
            SELECT * FROM plant_pest
            WHERE plant_id = ? AND pest_id = ?
        """
        params = (plant_id, pest_id)
        row = self.fetch_one(query, params)
        if row is not None:
            return plant_pest(*row)
        return None

    def find_by_pest_id(self, pest_id):
        query = "SELECT * FROM plant_pest WHERE pest_id = ?"
        params = (pest_id,)
        return self.fetch_all(query, params)
