class plantThreshold:
    def __init__(self, plant_id, maxtemp=None,
                 mintemp=None, maxgrow=None, mingrow=None, maxillu=None, minillu=None):
        self._mingrow = mingrow
        self._plant_id = plant_id
        self._maxtemp = maxtemp
        self._maxgrow = maxgrow
        self._mintemp = mintemp
        self._maxillu = maxillu
        self._minillu = minillu

    @property
    def mingrow(self):
        return self._mingrow

    @mingrow.setter
    def mingrow(self, mingrow):
        self._mingrow = mingrow

    @property
    def plant_id(self):
        return self._plant_id

    @plant_id.setter
    def plant_id(self, plant_id):
        self._plant_id = plant_id

    @property
    def maxtemp(self):
        return self._maxtemp

    @maxtemp.setter
    def maxtemp(self, maxtemp):
        self._maxtemp = maxtemp

    @property
    def maxgrow(self):
        return self._maxgrow

    @maxgrow.setter
    def maxgrow(self, maxgrow):
        self._maxgrow = maxgrow

    @property
    def mintemp(self):
        return self._mintemp

    @mintemp.setter
    def mintemp(self, mintemp):
        self._mintemp = mintemp

    @property
    def maxillu(self):
        return self._maxillu

    @maxillu.setter
    def maxillu(self, maxillu):
        self._maxillu = maxillu

    @property
    def minillu(self):
        return self._minillu

    @minillu.setter
    def minillu(self, minillu):
        self._minillu = minillu