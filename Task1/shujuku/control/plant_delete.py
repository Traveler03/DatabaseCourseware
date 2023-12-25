#植物删除
from classes import plant as plant2
from control import plant
import Factor
FC=Factor.dao_factory()
def delete():
    plant.display()
    print("请输入要删除植物信息的iD:")
    print()
    plants = FC.create("plant")
    sql = "select plant_id from Plant"
    result_name = plants.select(sql)
    judeid = 0
    plant_id = -1
    while judeid == 0:
        plant_id = int(input())
        for plantid in result_name:
            if int(plantid[0]) == plant_id:
                judeid = 1
                break
        if judeid == 0:
            print("输入植物ID不存在，请重新输入：")
    plants.delete(plant_id)
    print("植物信息删除成功")
