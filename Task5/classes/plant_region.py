class plant_region:
    def __init__(self, plant_id, region):
        self._plant_id = plant_id
        self._region = region

    @property
    def plant_id(self):
        return self._plant_id

    @plant_id.setter
    def plant_id(self, plant_id):
        self._plant_id = plant_id

    @property
    def region_id(self):
        return self._region

    @region_id.setter
    def region_id(self, region):
        self._region = region