class plant_classes:
    def __int__(self, plant_id, class_id):
        self._class_id = class_id  # 虫害编号
        self._plant_id = plant_id # 植物编号

    @property
    def class_id(self):
        return self._class_id

    @class_id.setter
    def class_id(self, class_id):
        self._class_id = class_id

    @property
    def plant_id(self):
        return self._plant_id

    @plant_id.setter
    def plant_id(self, plant_id):
        self._plant_id = plant_id
