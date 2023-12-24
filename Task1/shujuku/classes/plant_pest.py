class plant_pest:
    def __int__(self, plant_id, pest_id):
        self._pest_id = pest_id  # 虫害编号
        self._plant_id = plant_id # 植物编号

    @property
    def pest_id(self):
        return self._pest_id

    @pest_id.setter
    def pest_id(self, pest_id):
        self._pest_id = pest_id

    @property
    def plant_id(self):
        return self._plant_id

    @plant_id.setter
    def plant_id(self, plant_id):
        self._plant_id = plant_id
