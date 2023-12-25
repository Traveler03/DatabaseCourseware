from DAO.DAO import BaseDAO  # 假设有一个 BaseDAO 类，包含通用的数据库操作方法
from classes.pest import pest


class PestDAO(BaseDAO):
    def __init__(self, db):
        super().__init__(db)

    def insert(self, pest):
        new_id = self.get_max_id() + 1
        pest.set_pest_id(new_id)
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

    def get_max_id(self):
        query = "SELECT MAX(pest_id) FROM pest"
        max_id = self.fetch_one(query)
        return max_id[0] if max_id[0] is not None else 0

    def map_to_object(self, row):
        if row is not None:
            pest_id, pest_name, cm = row
            return pest(pest_id=pest_id, pest_name=pest_name, cm=cm)
        return None

    def find_by_name(self, pest_name):
        query = "SELECT * FROM pest WHERE pest_name = ?"
        params = (pest_name,)
        result = self.fetch_one(query, params)
        return self.map_to_object(result)
