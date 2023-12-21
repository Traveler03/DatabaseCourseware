class metrics:
    def __init__(self, metrics_ip, illumination, temperature, grow):
        self._metrics_ip = metrics_ip
        self._illumination = illumination
        self._temperature = temperature
        self._grow = grow

    @property
    def metrics_ip(self):
        return self._metrics_ip

    @metrics_ip.setter
    def metrics_ip(self, metrics_ip):
        self._metrics_ip = metrics_ip

    @property
    def illumination(self):
        return self._illumination

    @illumination.setter
    def equipment_name(self, illumination):
        self._illumination = illumination

    @property
    def temperature(self):
        return self._temperature

    @temperature.setter
    def equipment_name(self, temperature):
        self._temperature = temperature

    @property
    def grow(self):
        return self._grow

    @grow.setter
    def equipment_name(self, grow):
        self._grow = grow

