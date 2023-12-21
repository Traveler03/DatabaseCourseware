class medicine:
    def __init__(self, medicin_id, medicine_name, duration):
        self.medicin_id = medicin_id
        self.medicine_name = medicine_name
        self.duration = duration

    def get_medicin_id(self):
        return self.medicin_id

    def set_medicin_id(self, medicin_id):
        self.medicin_id = medicin_id

    def get_medicine_name(self):
        return self.medicine_name

    def set_medicine_name(self, medicine_name):
        self.medicine_name = medicine_name

    def get_duration(self):
        return self.duration

    def set_duration(self, duration):
        self.duration = duration
