class equipment_metrics:
    def __init__(self, equipment_id, metrics_ip):
        self._equipment_id = equipment_id
        self._metrics_ip = metrics_ip

    @property
    def equipment_id(self):
        return self._equipment_id

    @equipment_id.setter
    def equipment_id(self, equipment_id):
        self._equipment_id = equipment_id

    @property
    def metrics_ip(self):
        return self._metrics_ip

    @metrics_ip.setter
    def metrics_ip(self, metrics_ip):
        self._metrics_ip = metrics_ip




