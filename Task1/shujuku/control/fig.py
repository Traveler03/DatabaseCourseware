#配图
import Factor
FC=Factor.dao_factory()
figs=FC.create("fig")
def display():
    sql ="select fig.fig_id,species_name,fig_path,fig_place,fig_people,fig_des,fig.created_by,fig.creater_at,fig.updated_at from fig, \
         plant,plant_fig where fig.fig_id=plant_fig.fig_id and Plant.plant_id=plant_fig.plant_id"
    result = figs.select(sql)
    for message in result:
        print("配图编号：%s"%message[0])
        print("植物名称：%s" % message[1])
        print("配图路径：%s"%message[2])
        print("拍摄地点：%s"%message[3])
        print("拍摄人员：%s" % message[4])
        print("配图描述：%s" % message[5])
        print("创建人员：%s"%message[6])
        print("创建时间：%s"%message[7])
        print("更新时间：%s"%message[8])
        print()

