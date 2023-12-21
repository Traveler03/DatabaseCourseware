from DAO import Maintenance_DAO
from DAO import Maninternance_user_DAO
from DAO import plant_Maintenance_DAO


class DAOFactory:
    def __init__(self, db):
        self.db = db

    def create_course_dao(self):
        return Maintenance_DAO(self.db)


    def create_homework_dao(self):
        return Maninternance_user_DAO(self.db)

    def create_student_dao(self):
        return plant_Maintenance_DAO(self.db)
