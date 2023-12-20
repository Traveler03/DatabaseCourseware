from tkinter import *
from tkinter import *
from Factor import dao_factory
FC=dao_factory()
from classes import fig,plant,plant_pest,plant_fig,user
from interface.registration import open_register_window
from interface.main import open_main_window
def root_window():
    root = Tk()
    root.title("用户登录")

    # 创建用户名和密码的标签、输入框和按钮
    label_username = Label(root, text="用户名：")
    label_username.pack()
    entry_username = Entry(root)
    entry_username.pack()

    label_password = Label(root, text="密码：")
    label_password.pack()
    entry_password = Entry(root, show="*")
    entry_password.pack()

    label_result = Label(root, text="")
    label_result.pack()
    users=user.user()
    def login():
        username = entry_username.get()
        password = entry_password.get()

        # 在这里编写验证用户名和密码的逻辑
        # ...
        user = FC.create("user")
        sql = "Select * from users where user_name='%s' and password='%s'" % (username, password)
        result = user.select(sql)
        if result:
            label_result.config(text="登录成功")
            users.__int__(user_name=result[0][1],password=result[0][2],posts=result[0][3],Permissions=result[0][4])
            root.withdraw()  # 隐藏当前注册窗口
            open_main_window(root,users)
        else:
            label_result.config(text="用户名或密码错误")
    button_login = Button(root, text="登录", command=login)
    button_login.pack(side='left')
    def register_and_open_register_window():
        root.withdraw()  # 隐藏当前注册窗口
        open_register_window(root,user)  # 打开新的界面
    button_register_page = Button(root, text="注册", command=register_and_open_register_window)
    button_register_page.pack(side='right')

    label_result = Label(root, text="")
    label_result.pack()

    root.mainloop()
root_window()