class classes:
    def __int__(self, class_name, parent=None,
                 rank=None,class_id=None):
        self._class_id = class_id # 分类编号
        self._class_name = class_name  # 分类名
        self._parent = parent  # 父节点
        self._rank = rank  # 等级

    @property
    def class_id(self):
        return self._class_id

    @class_id.setter
    def class_id(self, class_id):
        self._class_id =class_id

    @property
    def class_name(self):
        return self._class_name

    @class_name.setter
    def class_name(self, class_name):
        self._class_name = class_name

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


