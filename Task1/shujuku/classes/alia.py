class alia:
    def __int__(self, plant_id,alias):
        self._alias = alias  # 别名编号
        self._plant_id = plant_id # 植物编号

    @property
    def alias(self):
        return self._alias

    @alias.setter
    def alias(self, alias):
        self._alias = alias

    @property
    def plant_id(self):
        return self._plant_id

    @plant_id.setter
    def plant_id(self, plant_id):
        self._plant_id = plant_id