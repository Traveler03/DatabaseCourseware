from DAO import medicine_DAO
from DAO import pest_DAO
from DAO import pest_medicine_DAO
from DAO import pest_DAO

class NewDAOFactory:
    def __init__(self, db):
        self.db = db

    def create_medicine_dao(self):
        return medicine_DAO(self.db)

    def create_pest_dao(self):
        return pest_DAO(self.db)

    def create_pest_medicine_dao(self):
        return pest_medicine_DAO(self.db)

    def create_plant_pest_dao(self):
        return pest_DAO(self.db)
