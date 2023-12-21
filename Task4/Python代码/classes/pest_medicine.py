class pest_medicine:
    def __init__(self, medicine_id, pest_id, dosage):
        self.medicine_id = medicine_id
        self.pest_id = pest_id
        self.dosage = dosage

    def get_medicine_id(self):
        return self.medicine_id

    def set_medicine_id(self, medicine_id):
        self.medicine_id = medicine_id

    def get_pest_id(self):
        return self.pest_id

    def set_pest_id(self, pest_id):
        self.pest_id = pest_id

    def get_dosage(self):
        return self.dosage

    def set_dosage(self, dosage):
        self.dosage = dosage
