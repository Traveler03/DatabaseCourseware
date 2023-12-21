class monitorData:
    def __init__(self, monitor_id, monitor_region, monitor_time, plant_id, monitor_temp, monitor_grow, monitor_illu):
        self._monitor_id = monitor_id
        self._monitor_region = monitor_region
        self._monitor_time = monitor_time
        self._plant_id = plant_id
        self._monitor_temp = monitor_temp
        self._monitor_grow = monitor_grow
        self._monitor_illu = monitor_illu

    @property
    def monitor_id(self):
        return self._monitor_id

    @monitor_id.setter
    def equipment_id(self, monitor_id):
        self._monitor_id = monitor_id

    @property
    def monitor_region(self):
        return self._monitor_region

    @monitor_region.setter
    def equipment_name(self, monitor_region):
        self._monitor_region = monitor_region

    @property
    def monitor_time(self):
        return self._monitor_time

    @monitor_time.setter
    def equipment_name(self, monitor_time):
        self._monitor_time = monitor_time

    @property
    def plant_id(self):
        return self._plant_id

    @plant_id.setter
    def equipment_name(self, plant_id):
        self._plant_id = plant_id

    @property
    def monitor_temp(self):
        return self._monitor_temp

    @monitor_temp.setter
    def monitor_temp(self, monitor_temp):
        self._monitor_temp = monitor_temp

    @property
    def monitor_grow(self):
        return self._monitor_grow

    @monitor_grow.setter
    def monitor_grow(self, monitor_grow):
        self._monitor_grow = monitor_grow

    @property
    def monitor_illu(self):
        return self._monitor_illu

    @monitor_illu.setter
    def monitor_illu(self, monitor_illu):
        self._monitor_illu = monitor_illu

