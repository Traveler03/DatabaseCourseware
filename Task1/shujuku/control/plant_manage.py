from control import plant,plant_insert,plant_update,plant_delete,statistics,Family_nm,Fuzzy_queries,fig,fig_insert,fig_update,fig_delete
def plant_manmage():
    #植物管理
    print("*************************欢迎进入植物信息管理系统*************************")
    print("\t\t请选择您需要的业务：")
    print("\t\t1:查看所有植物的所有信息")
    print("\t\t2:查看平台中每科植物的数量")
    print("\t\t3:删除某个植物的信息")
    print("\t\t4:模糊查询")
    print("\t\t5：查看某科植物视图")
    print("\t\t6:更新某个个植物信息")
    print("\t\t7:插入某个植物新消息")
    print("\t\t8:查看植物的养护视图")
    print("\t\t9:查看某个属的植物的检测情况")
    print("\t\t10：插入植物配图")
    print("\t\t11：删除植物配图")
    print("\t\t12：更新植物配图")
    print("\t\t-1:退出植物业务服务")
    m=int(input("\t\t请输入您所需要的业务"))
    if m==1:
        plant.display()
        pass
    elif m==2:
        statistics.statis()
        pass
    elif m==3:
        plant_delete.delete()
        pass
    elif m==4:
        Fuzzy_queries.Inquire()
        pass
    elif m==5:
        Family_nm.display()
        pass
    elif m==6:
        plant_update.update_plant()
        pass
    elif m == 7:
        plant_insert.creat_plant()
        pass
    elif m == 8:

        pass
    elif m == 9:
        pass
    elif m == 10:
        fig_insert.creat_fig()
        pass
    elif m == 11:
        fig_delete.delete()
        pass
    elif m == 12:
        fig_update.fig_update()
        pass
plant_manmage()