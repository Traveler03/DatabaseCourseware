class plant_fig:
    def __int__(self, plant_id, image_id):
        self._image_id = image_id  # 配图编号
        self._plant_id = plant_id # 植物编号

    @property
    def image_id(self):
        return self._image_id

    @image_id.setter
    def image_id(self, image_id):
        self._image_id = image_id

    @property
    def plant_id(self):
        return self._plant_id

    @plant_id.setter
    def plant_id(self, plant_id):
        self._plant_id = plant_id
