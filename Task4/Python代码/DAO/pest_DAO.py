from DAO import BaseDAO  # 假设有一个 BaseDAO 类，包含通用的数据库操作方法
from classes import pest

class PestDAO(BaseDAO):
    def __init__(self, db):
        super().__init__(db)

    def insert(self, pest):
        query = """
            INSERT INTO pest (pest_id, pest_name, cm)
            VALUES (?, ?, ?)
        """
        params = (pest.get_pest_id(), pest.get_pest_name(), pest.get_cm())
        self.execute_query(query, params)

    def update(self, pest):
        query = """
            UPDATE pest
            SET pest_name = ?, cm = ?
            WHERE pest_id = ?
        """
        params = (pest.get_pest_name(), pest.get_cm(), pest.get_pest_id())
        self.execute_query(query, params)

    def delete(self, pest):
        query = """
            DELETE FROM pest
            WHERE pest_id = ?
        """
        params = (pest.get_pest_id(),)
        self.execute_query(query, params)

    def find(self, pest_id):
        query = """
            SELECT * FROM pest
            WHERE pest_id = ?
        """
        params = (pest_id,)
        row = self.fetch_one(query, params)
        if row is not None:
            return pest(*row)
        return None
