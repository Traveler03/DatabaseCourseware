class pest:
    def __init__(self, pest_id, pest_name, cm):
        self.pest_id = pest_id
        self.pest_name = pest_name
        self.cm = cm

    def get_pest_id(self):
        return self.pest_id

    def set_pest_id(self, pest_id):
        self.pest_id = pest_id

    def get_pest_name(self):
        return self.pest_name

    def set_pest_name(self, pest_name):
        self.pest_name = pest_name

    def get_cm(self):
        return self.cm

    def set_cm(self, cm):
        self.cm = cm
