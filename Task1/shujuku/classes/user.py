class user:
    def __int__(self, user_name, password=None,
                 posts=None, Permissions=None, user_id=None):
        self._user_id = user_id # 用户编号
        self._user_name = user_name  # 用户姓名
        self._password = password  # 密码
        self._Permissions = Permissions  # 权限
        self._posts = posts  # 职位

    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        self._user_id =user_id

    @property
    def user_name(self):
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        self._user_name = user_name

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, password):
        self._password = password

    @property
    def Permissions(self):
        return self._Permissions

    @Permissions.setter
    def Permissions(self, Permissions):
        self._Permissions = Permissions

    @property
    def posts(self):
        return self._posts

    @posts.setter
    def posts(self, posts):
        self._posts = posts


