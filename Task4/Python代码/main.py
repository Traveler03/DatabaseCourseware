from factory import *
from database import *

from classes.medicine import medicine
from classes.pest import pest
from classes.pest_medicine import pest_medicine
from classes.plant_pest import plant_pest

# 创建数据库连接
db = Database('127.0.0.1', 'GardenPlants', 'sa', '123456')

# 创建 DAOFactory 实例，并传入数据库连接对象，并实例化各个DAO
dao_factory = DaoFactory(db)
medicine_DAO = dao_factory.create_medicine_dao()
pest_DAO = dao_factory.create_pest_dao()
pest_medicine_DAO = dao_factory.create_pest_medicine_dao()
plant_pest_DAO = dao_factory.create_plant_pest_dao()


def print_menu_4():
    print("========== 药物-病虫害管理系统 ==========")
    print("1. 查询病虫害对应的药物信息")
    print("2. 增加药物、病虫害及关联信息")
    print("3. 删除病虫害及关联信息")
    print("4. 修改病虫害及关联信息")
    print("5. 展示所有药物、病虫害及关联信息")
    print("0. 退出程序")


def display_all_info():
    # 展示所有药物信息
    print("\n所有药物信息：")
    all_medicines = medicine_DAO.fetch_all("SELECT * FROM medicine")
    for medicine_info in all_medicines:
        print(
            f"药物ID: {medicine_info.medicin_id}, 药物名称: {medicine_info.medicine_name}, 作用期限: {medicine_info.duration}")

    # 展示所有病虫害信息
    print("\n所有病虫害信息：")
    all_pests = pest_DAO.fetch_all("SELECT * FROM pest")
    for pest_info in all_pests:
        print(
            f"病虫害ID: {pest_info.pest_id}, 病虫害名称: {pest_info.pest_name}, 防治方法: {pest_info.cm}")

    # 展示所有植物-病虫害关联信息
    print("\n所有植物-病虫害关联信息：")
    all_plant_pests = plant_pest_DAO.fetch_all("SELECT * FROM plant_pest")
    for plant_pest_info in all_plant_pests:
        print(
            f"植物ID: {plant_pest_info.plant_id}, 病虫害ID: {plant_pest_info.pest_id}")

    # 展示所有病虫害-药物关联信息
    print("\n所有病虫害-药物关联信息：")
    all_pest_medicines = pest_medicine_DAO.fetch_all("SELECT * FROM pest_medicine")
    for pest_medicine_info in all_pest_medicines:
        print(
            f"药物ID: {pest_medicine_info.medicine_id}, 病虫害ID: {pest_medicine_info.pest_id}, 药物用量: {pest_medicine_info.dosage}")


while True:
    print_menu_4()
    choice = int(input("请输入选项："))

    if choice == 1:  # 查询
        pest_id = int(input("请输入病虫害ID："))
        pest_medicine_info = pest_medicine_DAO.find_by_pest_id(pest_id)
        if pest_medicine_info is not None:
            medicine_id = pest_medicine_info.get_medicine_id()
            medicine_info = medicine_DAO.find(medicine_id)
            print(f"病虫害ID为{pest_id}的药物信息：")
            print(
                f"药物ID: {medicine_info.get_medicin_id()}, 药物名称: {medicine_info.get_medicine_name()}, 作用期限: {medicine_info.get_duration()}")
        else:
            print(f"未找到病虫害ID为{pest_id}的相关信息.")

    elif choice == 2:  # 增加
        sub_choice = int(input(
            "请选择要添加的信息：\n1. 药物信息\n2. 病虫害信息\n3. 病虫害-药物关联\n4. 植物-病虫害关联\n请输入选项："))

        if sub_choice == 1:  # 增加药物信息
            medicine_name = input("请输入药物名称：")
            duration = input("请输入药物作用期限：")
            new_medicine = medicine(medicin_id=None, medicine_name=medicine_name, duration=duration)
            medicine_DAO.insert(new_medicine)
            print("药物信息添加成功！")

        elif sub_choice == 2:  # 增加病虫害信息
            pest_name = input("请输入病虫害名称：")
            cm = input("请输入防治方法：")
            new_pest = pest(pest_id=None, pest_name=pest_name, cm=cm)
            pest_DAO.insert(new_pest)
            print("病虫害信息添加成功！")

        elif sub_choice == 3:  # 建立病虫害-药物关联
            # 查询已存在的药物信息
            medicine_name = input("请输入已存在的药物名称：")
            existing_medicine = medicine_DAO.find_by_name(medicine_name)

            if existing_medicine is None:
                print(f"未找到药物名称为 {medicine_name} 的药物信息，请先添加该药物信息。")
                continue

            # 查询已存在的病虫害信息
            pest_name = input("请输入已存在的病虫害名称：")
            existing_pest = pest_DAO.find_by_name(pest_name)

            if existing_pest is None:
                print(f"未找到病虫害名称为 {pest_name} 的病虫害信息，请先添加该病虫害信息。")
                continue

            # 建立病虫害-药物关联
            existing_pest_medicine = pest_medicine_DAO.find(existing_medicine.get_medicin_id(),
                                                            existing_pest.get_pest_id())

            if existing_pest_medicine is None:
                dosage = input("请输入药物用量：")
                new_pest_medicine = pest_medicine(medicine_id=existing_medicine.get_medicin_id(),
                                                  pest_id=existing_pest.get_pest_id(),
                                                  dosage=dosage)
                pest_medicine_DAO.insert(new_pest_medicine)
                print("病虫害-药物关联建立成功！")
            else:
                print(f"病虫害 {pest_name} 已关联到药物 {medicine_name}，无需重复关联.")

        elif sub_choice == 4:  # 添加植物-病虫害关联信息
            # 查询已存在的植物信息
            plant_id = int(input("请输入已存在的植物ID："))

            # 查询已存在的病虫害信息
            pest_name = input("请输入已存在的病虫害名称：")
            existing_pest = pest_DAO.find_by_name(pest_name)

            if existing_pest is None:
                print(f"未找到病虫害名称为 {pest_name} 的病虫害信息，请先添加该病虫害信息。")
                continue

            # 建立植物-病虫害关联
            existing_pest_medicine = plant_pest_DAO.find(plant_id, existing_pest.get_pest_id())

            if existing_pest_medicine is None:
                existing_pest_medicine = plant_pest(plant_id=plant_id, pest_id=existing_pest.get_pest_id())
                plant_pest_DAO.insert(existing_pest_medicine)

            print("植物-病虫害关联建立成功！")

    elif choice == 3:  # 删除
        pest_id = int(input("请输入要删除的病虫害ID："))

        # 查找与病虫害关联的植物-病虫害关联信息
        plant_pest_list = plant_pest_DAO.find_by_pest_id(pest_id)

        # 遍历并逐个删除植物-病虫害关联信息
        for plant_pest_info in plant_pest_list:
            plant_pest_DAO.delete(plant_pest_info)

        # 查找与病虫害关联的病虫害-药物关联信息
        pest_medicine_list = pest_medicine_DAO.find_by_pest_id(pest_id)

        # 遍历并逐个删除病虫害-药物关联信息
        for pest_medicine_info in pest_medicine_list:
            pest_medicine_DAO.delete(pest_medicine_info)

        # 删除病虫害
        pest_DAO.delete(pest_DAO.find(pest_id))
        print("数据删除成功！")


    elif choice == 4:  # 修改

        sub_choice = int(input(

            "请选择要修改的信息：\n1. 修改药物有效期\n2. 修改病虫害-药物关联信息\n请输入选项："))

        if sub_choice == 1:  # 修改药物有效期

            medicine_id = int(input("请输入要修改的药物ID："))

            new_duration = input("请输入新的药物作用期限：")

            medicine_info = medicine_DAO.find(medicine_id)

            if medicine_info is not None:

                medicine_info.set_duration(new_duration)

                medicine_DAO.update(medicine_info)

                print("药物有效期修改成功！")

            else:

                print(f"未找到药物ID为 {medicine_id} 的药物信息。")


        elif sub_choice == 2:  # 修改病虫害-药物关联信息

            pest_id = int(input("请输入要修改的病虫害ID："))

            medicine_name = input("请输入已存在的药物名称：")

            existing_medicine = medicine_DAO.find_by_name(medicine_name)

            if existing_medicine is not None:

                existing_pest_medicine = pest_medicine_DAO.find(existing_medicine.get_medicin_id(), pest_id)

                if existing_pest_medicine is not None:

                    new_dosage = input("请输入新的药物用量：")

                    existing_pest_medicine.set_dosage(new_dosage)

                    pest_medicine_DAO.update(existing_pest_medicine)

                    print("病虫害-药物关联信息修改成功！")

                else:

                    print(f"未找到病虫害ID为 {pest_id} 与药物 {medicine_name} 关联的信息。")

            else:

                print(f"未找到药物名称为 {medicine_name} 的药物信息。")


        else:

            print("无效的选项，请重新输入。")



    elif choice == 5:  # 展示所有药物、病虫害及关联信息
        display_all_info()

    elif choice == 0:  #
        print("程序已退出。")
        break

    else:
        print("无效的选项，请重新输入。")
