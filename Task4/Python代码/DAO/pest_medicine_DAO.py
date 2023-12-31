from DAO.DAO import BaseDAO  # 假设有一个 BaseDAO 类，包含通用的数据库操作方法
from classes.pest_medicine import pest_medicine


class PestMedicineDAO(BaseDAO):
    def __init__(self, db):
        super().__init__(db)

    def insert(self, pest_medicine):
        query = """
            INSERT INTO pest_medicine (medicine_id, pest_id, dosage)
            VALUES (?, ?, ?)
        """
        params = (pest_medicine.get_medicine_id(), pest_medicine.get_pest_id(), pest_medicine.get_dosage())
        self.execute_query(query, params)

    def update(self, pest_medicine):
        query = """
            UPDATE pest_medicine
            SET dosage = ?
            WHERE medicine_id = ? AND pest_id = ?
        """
        params = (pest_medicine.get_dosage(), pest_medicine.get_medicine_id(), pest_medicine.get_pest_id())
        self.execute_query(query, params)

    def delete(self, pest_medicine_info):
        # Assuming pest_medicine_info is a single row
        query = """
            DELETE FROM pest_medicine
            WHERE medicine_id = ? AND pest_id = ?
        """
        params = (pest_medicine_info[0], pest_medicine_info[1])
        self.execute_query(query, params)

    def find(self, medicine_id, pest_id):
        query = """
            SELECT * FROM pest_medicine
            WHERE medicine_id = ? AND pest_id = ?
        """
        params = (medicine_id, pest_id)
        row = self.fetch_one(query, params)
        if row is not None:
            return pest_medicine(*row)
        return None

    def find_by_pest_id(self, pest_id):
        query = "SELECT * FROM pest_medicine WHERE pest_id = ?"
        params = (pest_id,)
        return self.fetch_all(query, params)
