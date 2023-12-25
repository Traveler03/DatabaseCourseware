from DAO.DAO import BaseDAO  # 假设有一个 BaseDAO 类，包含通用的数据库操作方法
from classes.medicine import medicine


class MedicineDAO(BaseDAO):
    def __init__(self, db):
        super().__init__(db)

    def insert(self, medicine):
        new_id = self.get_max_id() + 1
        medicine.set_medicin_id(new_id)
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

    def get_max_id(self):
        query = "SELECT MAX(medicin_id) FROM medicine"
        max_id = self.fetch_one(query)
        return max_id[0] if max_id[0] is not None else 0

    def map_to_object(self, row):
        if row:
            medicine_id, medicine_name, duration = row
            return medicine(medicin_id=medicine_id, medicine_name=medicine_name, duration=duration)
        return None

    def find_by_name(self, medicine_name):
        query = "SELECT * FROM medicine WHERE medicine_name = ?"
        params = (medicine_name,)
        result = self.fetch_one(query, params)
        if result:
            return self.map_to_object(result)
        return None
