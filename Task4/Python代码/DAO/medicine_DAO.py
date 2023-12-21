from DAO import BaseDAO  # 假设有一个 BaseDAO 类，包含通用的数据库操作方法
from classes import medicine

class MedicineDAO(BaseDAO):
    def __init__(self, db):
        super().__init__(db)

    def insert(self, medicine):
        query = """
            INSERT INTO medicine (medicin_id, medicine_name, duration)
            VALUES (?, ?, ?)
        """
        params = (medicine.get_medicin_id(), medicine.get_medicine_name(), medicine.get_duration())
        self.execute_query(query, params)

    def update(self, medicine):
        query = """
            UPDATE medicine
            SET medicine_name = ?, duration = ?
            WHERE medicin_id = ?
        """
        params = (medicine.get_medicine_name(), medicine.get_duration(), medicine.get_medicin_id())
        self.execute_query(query, params)

    def delete(self, medicine):
        query = """
            DELETE FROM medicine
            WHERE medicin_id = ?
        """
        params = (medicine.get_medicin_id(),)
        self.execute_query(query, params)

    def find(self, medicin_id):
        query = """
            SELECT * FROM medicine
            WHERE medicin_id = ?
        """
        params = (medicin_id,)
        row = self.fetch_one(query, params)
        if row is not None:
            return medicine(*row)
        return None
