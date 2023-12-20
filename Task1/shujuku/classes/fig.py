class fig:
    def __int__(self,  image_path,image_id=None,image_location=None, image_photographer=None,image_description=None,
                 created_by=None, created_at=None, updated_at=None):

        self._image_id = image_id  # 配图编号
        self._image_location = image_location  # 配图拍摄地点
        self._image_description = image_description  # 配图描述
        self._image_path=image_path#配图路径
        self._image_photographer = image_photographer  # 配图拍摄人
        self._created_by = created_by  # 创建人员
        self._created_at = created_at  # 创建时间
        self._updated_at = updated_at  # 更新时间

    @property
    def image_id(self):
        return self._image_id

    @image_id.setter
    def image_id(self, image_id):
        self._image_id = image_id

    @property
    def image_path(self):
        return self._image_path

    @image_path.setter
    def image_path(self, image_path):
        self._image_path = image_path

    @property
    def image_location(self):
        return self._image_location

    @image_location.setter
    def image_location(self, image_location):
        self._image_location = image_location

    @property
    def image_description(self):
        return self._image_description

    @image_description.setter
    def image_description(self, image_description):
        self._image_description = image_description

    @property
    def image_photographer(self):
        return self._image_photographer

    @image_photographer.setter
    def image_photographer(self, image_photographer):
        self._image_photographer = image_photographer

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