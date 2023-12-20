class plant_region:
    def __int__(self, plant_id, region_id):
        self._region_id = region_id  # 虫害编号
        self._plant_id = plant_id # 植物编号

    @property
    def region_id(self):
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        self._region_id = region_id

    @property
    def plant_id(self):
        return self._plant_id

    @plant_id.setter
    def plant_id(self, plant_id):
        self._plant_id = plant_id
