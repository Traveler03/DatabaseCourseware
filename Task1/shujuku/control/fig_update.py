#配图更新
from control import fig
from classes import plant as plant2
from classes import fig,plant_fig
import Factor
FC=Factor.dao_factory()
def fig_update():
    fig.display()
    figs = FC.create("fig")
    sql = "select fig_id from fig"
    result=figs.select(sql)
    judeid = 0
    print("请输入要修改植物信息的iD:")
    print()
    fig_id = -1
    while judeid == 0:
        fig_id = int(input())
        for figid in result:
            if int(figid[0]) == fig_id:
                judeid = 1
                break
        if judeid == 0:
            print("输入配图ID不存在，请重新输入：")
    sql_id = "select * from fig where fig_id=%d" % fig_id
    result_id = figs.select(sql_id)
    print("配图编号：%s" % result_id[0][0])
    print("配图路径：%s" % result_id[0][1])
    print("拍摄地点：%s" % result_id[0][2])
    print("拍摄人员：%s" % result_id[0][3])
    print("配图描述：%s" % result_id[0][4])
    print("创建人员：%s" % result_id[0][5])
    print("创建时间：%s" % result_id[0][6])
    print("更新时间：%s" % result_id[0][7])
    while 1:
        print("1:修改配图路径：请输入1")
        print("2:修改拍摄地点：请输入2")
        print("3:修改拍摄人员：请输入3")
        print("4:修改配图描述：请输入4")
        print("5:退出：请输入-1")
        m=int(input())
        if m==-1:

            break
        elif m==1:
            fig_path = input("请输入要更新的配图路径")
            figs.update(choose=1,value=fig_path,id=fig_id)
            pass
        elif m==2:
            fig_dot = input("请输入要更新的拍摄地点")
            figs.update(choose=2, value=fig_dot, id=fig_id)
            pass
        elif m==3:
            fig_people = input("请输入要更新的拍摄地点")
            figs.update(choose=3, value=fig_people, id=fig_id)
            pass
        elif m==4:
            fig_dis = input("请输入要更新的拍摄地点")
            figs.update(choose=3, value=fig_dis, id=fig_id)
            pass