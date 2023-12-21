class equipment_plant:
    def __init__(self, equipment_id, plant_id):
        self._equipment_id = equipment_id
        self._plant_id = plant_id

    @property
    def equipment_id(self):
        return self._equipment_id

    @equipment_id.setter
    def equipment_id(self, equipment_id):
        self._equipment_id = equipment_id

    @property
    def plant_id(self):
        return self._plant_id

    @plant_id.setter
    def plant_id(self, plant_id):
        self._plant_id = plant_id




