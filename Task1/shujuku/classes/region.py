class region:
    def __int__(self, region_name, parent=None,
                 rank=None,region_id=None):
        self._region_id = region_id # 地区编号
        self._region_name = region_name  # 地区名
        self._parent = parent  # 父节点
        self._rank = rank  # 等级

    @property
    def region_id(self):
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        self._region_id =region_id

    @property
    def region_name(self):
        return self._region_name

    @region_name.setter
    def region_name(self, region_name):
        self._region_name = region_name

    @property
    def parent(self):
        return self._parent

    @parent.setter
    def parent(self, parent):
        self._parent = parent

    @property
    def rank(self):
        return self._rank

    @rank.setter
    def rank(self, rank):
        self._rank = rank


