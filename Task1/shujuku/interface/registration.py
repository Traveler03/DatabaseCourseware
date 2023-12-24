from tkinter import *
from Factor import dao_factory
FC=dao_factory()
from classes import fig,plant,plant_pest,plant_fig,user
def user_insert(username,password,Permissions):
    new_users = FC.create("user")
    new_user = user.user()
    if Permissions==0:
        new_user.__int__(user_name=username, password=password, posts="上级主管部门", Permissions=0)
        pass
    elif Permissions==1:
        new_user.__int__(user_name=username, password=password, posts="系统管理员", Permissions=1)
        pass
    elif Permissions==2:
        new_user.__int__(user_name=username, password=password, posts="养护人员", Permissions=2)
        pass
    elif Permissions==3:
        new_user.__int__(user_name=username, password=password, posts="监测人员", Permissions=3)
        pass
    elif Permissions==4:
        new_user.__int__(user_name=username, password=password, posts="游客", Permissions=4)
        pass
    new_users.insert(new_user)

def open_register_window(root):
    register_window = Toplevel(root)
    register_window.title("用户注册")

    # 在注册页面上创建用户名、密码的输入框和注册按钮
    label_register_username = Label(register_window, text="新用户名：")
    label_register_username.pack()
    entry_register_username = Entry(register_window)
    entry_register_username.pack()

    label_register_password = Label(register_window, text="新密码：")
    label_register_password.pack()
    entry_register_password = Entry(register_window, show="*")
    entry_register_password.pack()

    label_result = Label(root, text="")
    label_result.pack()

    def register_and_open_new_window():
        user_insert(entry_register_username.get(), entry_register_password.get(), 4)
        register_window.destroy()  # 关闭当前注册窗口
        root.deiconify()  # 打开新的界面
    button_register = Button(register_window, text="注册",command=register_and_open_new_window)
    button_register.pack()