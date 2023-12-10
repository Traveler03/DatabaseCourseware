class plant:
    def __int__(self, id, species_name, morphology=None,
                 value=None, key_tech=None,environment=None, created_by=None, created_at=None, updated_at=None):
        self._plant_id = id  # 编号
        self._species_name = species_name  # 种名
        self._morphology = morphology  # 形态特征
        self._key_tech = key_tech  # 栽培技术要点
        self._value = value  # 应用价值
        self._environment=environment#生长环境
        self._created_by = created_by  # 创建人员
        self._created_at = created_at  # 创建时间
        self._updated_at = updated_at  # 更新时间
    @property
    def plant_id(self):
        return self._plant_id

    @plant_id.setter
    def plant_id(self, plant_id):
        self._plant_id =plant_id

    @property
    def species_name(self):
        return self._species_name

    @species_name.setter
    def species_name(self, species_name):
        self._species_name = species_name

    @property
    def morphology(self):
        return self._morphology

    @morphology.setter
    def morphology(self, morphology):
        self._morphology = morphology

    @property
    def key_tech(self):
        return self._key_tech

    @key_tech.setter
    def key_tech(self, key_tech):
        self._key_tech = key_tech

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value

    @property
    def environment(self):
        return self._environment

    @environment.setter
    def environment(self, environment):
        self._environment = environment
    @property
    def created_by(self):
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        self._created_by = created_by

    @property
    def created_at(self):
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        self._created_at = created_at

    @property
    def updated_at(self):
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        self._updated_at = updated_at
