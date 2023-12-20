from Factor import dao_factory
FC=dao_factory()
def register():
    print("=== 用户注册 ===")
    username = input("请输入用户名: ")
    password = input("请输入密码: ")
    confirm_password = input("请确认密码: ")

    if password == confirm_password:
        user = FC.create("user")

        # 在这里编写将用户名和密码存储到数据库或文件的代码
        print("注册成功！")
    else:
        print("两次输入的密码不一致，请重新注册。")

def password_is_correct(username,password):
    user=FC.create("user")
    sql="Select * from users where user_name=%s and password=%s"%(username,password)
    result=user.select(sql)
    if result:
        return True
    else
        return False
def login():
    print("=== 用户登录 ===")
    username = input("请输入用户名: ")
    password = input("请输入密码: ")

    # 在这里编写从数据库或文件中读取用户名和密码，并验证输入的用户名和密码是否匹配的代码

    if password_is_correct(username,password):
        print("登录成功！")
    else:
        print("用户名或密码错误，请重新登录。")


def main():
    while True:
        print("=== 欢迎使用用户登录系统 ===")
        print("1. 注册新用户")
        print("2. 用户登录")
        print("3. 退出程序")
        choice = input("请输入操作编号: ")

        if choice == "1":
            register()
        elif choice == "2":
            login()
        elif choice == "3":
            break
        else:
            print("无效的操作编号，请重新输入。")


if __name__ == "__main__":
    main()