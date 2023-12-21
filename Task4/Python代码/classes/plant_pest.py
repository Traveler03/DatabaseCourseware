class plant_pest:
    def __init__(self, plant_id, pest_id):
        self.plant_id = plant_id
        self.pest_id = pest_id

    def get_plant_id(self):
        return self.plant_id

    def set_plant_id(self, plant_id):
        self.plant_id = plant_id

    def get_pest_id(self):
        return self.pest_id

    def set_pest_id(self, pest_id):
        self.pest_id = pest_id
