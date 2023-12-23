import Factor
from classes import plant,plant_fig,fig
FC=Factor.dao_factory()
def creat_fig(user=None):
    plants=FC.create("plant")
    figs = FC.create("fig")
    plant_figs=FC.create("plant_fig")
    sql ="select plant_id,species_name from plant"
    result_name=plants.select(sql)
    judename = 0
    name=""
    print("请输入要配图的植物名称：")
    for plantname in result_name:
        print(plantname[1],end=" ")
    print()
    plant_id=-1
    while judename==0:
        name=input()
        for plantname in result_name:
            if plantname[1]==name:
                judename =1
                plant_id=plantname[0]
                break
        if judename==0:
            print("输入植物名称不存在，请重新输入：")
    sql = "select fig_path from fig"
    result_fig=figs.select(sql)
    judge=0
    path=""
    while judge==0:
        path = input("请输入配图的路径")
        for figpath in result_fig:
            judge=1
            if figpath[0]==path:
                print("该配图已存在")
                judge=0
                break
    people=input("请输入配图拍摄人")
    dot=input("请输入配图的地点")
    dis=input("请输入配图描述")
    new_fig=fig.fig()
    new_fig.__int__(image_path=path,image_photographer=people,image_location=dot,image_description=dis)
    figs.insert(new_fig)
    sql2="select fig_id from fig where fig_path='%s'"%path
    fig_id=figs.select(sql2)[0][0]
    new_plant_fig=plant_fig.plant_fig()
    new_plant_fig.__int__(plant_id=plant_id,image_id=fig_id)
    plant_figs.insert(new_plant_fig)
creat_fig()
