from DAO.Maintenance_DAO import MaintenanceDAO
from DAO.Maninternance_user_DAO import ManinternanceUserDAO
from DAO.plant_Maintenance_DAO import PlantMaintenanceDAO


class DAOFactory:
    def __init__(self, db):
        self.db = db

    def create_Maintenance_DAO(self):
        return MaintenanceDAO(self.db)

    def create_Maninternance_user_DAO(self):
        return ManinternanceUserDAO(self.db)

    def create_plant_Maintenance_DAO(self):
        return PlantMaintenanceDAO(self.db)
