class equipment:
    def __init__(self, equipment_id, equipment_name):
        self._equipment_id = equipment_id
        self._equipment_name = equipment_name

    @property
    def equipment_id(self):
        return self._equipment_id

    @equipment_id.setter
    def equipment_id(self, equipment_id):
        self._equipment_id = equipment_id

    @property
    def equipment_name(self):
        return self._equipment_name

    @equipment_name.setter
    def equipment_name(self, equipment_name):
        self._equipment_name = equipment_name




