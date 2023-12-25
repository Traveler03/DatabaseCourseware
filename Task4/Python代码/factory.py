from DAO.medicine_DAO import MedicineDAO
from DAO.pest_DAO import PestDAO
from DAO.pest_medicine_DAO import PestMedicineDAO
from DAO.plan_pest_DAO import PlantPestDAO


class DaoFactory:
    def __init__(self, db):
        self.db = db

    def create_medicine_dao(self):
        return MedicineDAO(self.db)

    def create_pest_dao(self):
        return PestDAO(self.db)

    def create_pest_medicine_dao(self):
        return PestMedicineDAO(self.db)

    def create_plant_pest_dao(self):
        return PlantPestDAO(self.db)
