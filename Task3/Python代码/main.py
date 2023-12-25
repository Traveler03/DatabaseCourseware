from classes.Maninternance_user import Maninternance_user
from classes.plant_Maintenance import plant_Maintenance
from classes.Maintenance import Maintenance

from factory import *
from database import *
from datetime import datetime

db = Database('127.0.0.1', 'GardenPlants', 'sa', '123456')

# 创建 DAOFactory 实例，并传入数据库连接对象 并且实例化各个DAO
dao_factory = DAOFactory(db)

Maintenance_DAO = dao_factory.create_Maintenance_DAO()

plant_Maintenance_DAO = dao_factory.create_plant_Maintenance_DAO()

Maintenance_user_DAO = dao_factory.create_Maninternance_user_DAO()


def print_menu_3():
    print("0: 退出业务")
    print("1: 查看所有的养护任务信息")
    print("2: 增加养护任务信息")
    print("3: 删除养护任务信息")
    print("4: 修改养护任务信息")
    print("5: 查找养护任务信息")
    print("\n")


def input_maintenance_details():
    task_name = input("请输入任务名称: ")

    while True:
        time_str = input("请输入执行时间 (YYYY-MM-DD): ")

        try:
            time = datetime.strptime(time_str, "%Y-%m-%d").date()
            break  # Break the loop if the date is valid
        except ValueError:
            print("日期格式无效，请使用YYYY-MM-DD格式。请重新输入。")

    place = input("请输入执行地点: ")
    task_des = input("请输入任务描述: ")

    # 获取表中最后一个数据项的ID并加一
    last_task_id = Maintenance_DAO.get_last_task_id()
    new_task_id = last_task_id + 1 if last_task_id is not None else 1

    return Maintenance(task_id=new_task_id, task_name=task_name, time=time, place=place, task_des=task_des)


def input_task_id():
    return int(input("输入任务ID: "))


while True:
    print_menu_3()
    a = int(input("请输入选项："))

    if a == 0:
        break
    elif a == 1:
        # 查看所有养护任务信息
        all_maintenance_tasks = Maintenance_DAO.get_all()
        for task in all_maintenance_tasks:
            print(f"任务id: {task.get_task_id()}, 任务名称: {task.get_task_name()}, "
                  f"执行时间: {task.get_time()}, 执行地点: {task.get_place()}, 任务描述: {task.get_task_des()}")

            # 打印关联的养护人员信息
            maintenance_users = Maintenance_DAO.get_maintenance_users(task.get_task_id(), Maintenance_user_DAO)
            print("Maintenance Users:")
            for user in maintenance_users:
                print(f"用户id: {user.get_user_id()}")

            # 打印关联的养护任务植物信息
            maintenance_plants = Maintenance_DAO.get_maintenance_plants(task.get_task_id(), plant_Maintenance_DAO)
            print("Maintenance Plants:")
            for plant in maintenance_plants:
                print(f"植物id: {plant.get_plant_id()}")
            print("\n")

    elif a == 2:
        # 增加养护任务信息
        new_maintenance = input_maintenance_details()
        Maintenance_DAO.insert(new_maintenance)

        # 更新 Maninternance_user 表
        user_id = int(input("输入人员ID："))
        Maintenance_user_DAO.insert(Maninternance_user(task_id=new_maintenance.get_task_id(), user_id=user_id))

        # 更新 plant_Maintenance 表
        plant_id = int(input("输入植物ID："))
        plant_Maintenance_DAO.insert(plant_Maintenance(plant_id=plant_id, task_id=new_maintenance.get_task_id()))

        print("养护任务成功添加！")
    elif a == 3:
        # 删除养护任务信息
        task_id_to_delete = input_task_id()
        task_to_delete = Maintenance_DAO.find(task_id_to_delete)
        if task_to_delete:
            # 同步删除 Maninternance_user 表中的记录
            user_to_delete = Maintenance_user_DAO.find(task_id_to_delete)
            if user_to_delete:
                Maintenance_user_DAO.delete(user_to_delete)
                print("养护人员信息成功删除！")
            else:
                print("未找到养护人员信息！")

            # 同步删除 plant_Maintenance 表中的记录
            plant_to_delete = plant_Maintenance_DAO.find(task_id_to_delete)
            if plant_to_delete:
                plant_Maintenance_DAO.delete(plant_to_delete)
                print("植物养护信息成功删除！")
            else:
                print("未找到植物养护信息！")

            Maintenance_DAO.delete(task_to_delete)

            print("养护任务成功删除！")
        else:
            print("未找到任务！")

    elif a == 4:
        # 修改养护任务信息
        task_id_to_update = input_task_id()
        task_to_update = Maintenance_DAO.find(task_id_to_update)
        if task_to_update:
            new_maintenance = input_maintenance_details()
            new_maintenance.set_task_id(task_id_to_update)
            Maintenance_DAO.update(new_maintenance)

            # 同步更新 Maintenance_user 表
            user_id = int(input("输入新的人员ID："))
            Maintenance_user_DAO.update(Maninternance_user(user_id=user_id, task_id=task_id_to_update))

            # 同步更新 plant_Maintenance 表
            plant_id = int(input("输入新的植物ID："))
            plant_Maintenance_DAO.update(plant_Maintenance(plant_id=plant_id, task_id=task_id_to_update))

            print("养护任务成功更新！")
        else:
            print("未找到任务！")

    elif a == 5:
        # 查找养护任务信息
        task_id_to_find = input_task_id()
        found_task = Maintenance_DAO.find(task_id_to_find)
        if found_task:
            print(f"任务id: {found_task.get_task_id()}, 任务名: {found_task.get_task_name()}, "
                  f"执行时间: {found_task.get_time()}, 执行地点: {found_task.get_place()}, 任务描述: {found_task.get_task_des()}")

            # 打印关联的养护人员信息
            maintenance_users = Maintenance_DAO.get_maintenance_users(found_task.get_task_id(),
                                                                      Maintenance_user_DAO)
            print("关联养护人员:")
            for user in maintenance_users:
                print(f"用户id: {user.get_user_id()}")

            # 打印关联的养护任务植物信息
            maintenance_plants = Maintenance_DAO.get_maintenance_plants(found_task.get_task_id(),
                                                                        plant_Maintenance_DAO)
            print("关联养护植物:")
            for plant in maintenance_plants:
                print(f"植物id: {plant.get_plant_id()}")

        else:
            print("未找到任务！")

    else:
        print("无效的选项，请重新输入！")
