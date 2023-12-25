from control import class_region_plant,class_update,class_delete,class_region_plant_update,region_update,region_insert,region_delete

def class_manage():
    # 植物管理
    print("*************************欢迎进入植物信分类管理系统*************************")
    print("\t\t请选择您需要的业务：")
    print("\t\t1:查看植物的分类信息")
    print("\t\t2:改正分类信息")
    print("\t\t3:删除某个分类信息")
    print("\t\t4:插入植物地区信息")
    print("\t\t5:更新植物及地区信息")
    print("\t\t6:改正地区信息")
    print("\t\t7:删除地区信息")
    print("\t\t-1:退出植物业务服务")
    m = int(input("\t\t请输入您所需要的业务"))
    if m == 1:
        class_region_plant.display()
        pass
    elif m == 2:
        class_update.update()
        pass
    elif m == 3:
        class_delete.delete()
        pass
    elif m == 4:
        region_insert.creat_region()
        pass
    elif m == 5:
        class_region_plant_update.update()
        pass
    elif m == 6:
        region_update.update()
        pass
    elif m == 7:
        region_delete.delete()
        pass
    elif m==-1:
        return
