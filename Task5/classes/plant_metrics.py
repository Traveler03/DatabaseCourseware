class plant_metrics:
    def __init__(self, plant_id, metrics_ip):
        self._plant_id = plant_id
        self._metrics_ip = metrics_ip

    @property
    def plant_id(self):
        return self._plant_id

    @plant_id.setter
    def plant_id(self, plant_id):
        self._plant_id = plant_id

    @property
    def metrics_ip(self):
        return self._metrics_ip

    @metrics_ip.setter
    def metrics_ip(self, metrics_ip):
        self._metrics_ip = metrics_ip




