#不同科视图
import Factor
FC=Factor.dao_factory()
def display():
    plants=FC.create("plant")
    print("所有植物的科名：")
    classess = FC.create("classes")
    sql = "select class_id,class_name from classes where rank=0"
    result = classess.select(sql)
    for name in result:
        print(name[1],end=" ")
    print("")
    judename = 0
    name = ""
    class_id=-1;
    while judename == 0:
        name=input("请输入要查询的植物科名：")
        for classname in result:
            if classname[1] == name:
                class_id=classname[0]
                judename = 1
                break
        if judename!=1:
            print("植物名重复，请重新输入：")
    viewname = "View_" + str(class_id)
    sql2 = "select * from %s" % viewname
    result2 = classess.select(sql2)
    for message in result2:
        print("植物编号：%s" % message[0])
        print("植物名称：%s" % message[1])
        print("植物科名：%s" % message[2])
        print("植物属名：%s" % message[3])
        print("植物别名：%s" % message[4])
        print("植物形态特征：%s" % message[6])
        print("植物栽培技术要点：%s" % message[5])
        sql3 = "select Pest.pest_name,Pest.cm from plant,Pest,plant_pest \
            where Plant.plant_id=plant_pest.plant_id and plant_pest.pest_id=Pest.pest_id and Plant.plant_id=%s" % \
               message[0]
        result_pest = plants.select(sql3)
        for pest in result_pest:
            print("植物病名：%s" % pest[0])
            print("病虫害防止措施：%s" % pest[1])
        print("植物应用价值：%s" % message[7])
        sql = "select fig.fig_id,species_name,fig_path,fig_place,fig_people,fig_des from fig, \
                         plant,plant_fig where fig.fig_id=plant_fig.fig_id and Plant.plant_id=plant_fig.plant_id and plant.plant_id=%d" % \
              message[0]
        result_fig = plants.select(sql)
        for fig_m in result_fig:
            print("配图编号：%s" % fig_m[0])
            print("图片路径：%s" % fig_m[2])
            print("拍摄地点：%s" % fig_m[3])
            print("配图人员：%s" % fig_m[4])
            print("配图描述：%s" % fig_m[5])
        print("创建人员：%s" % message[8])
        print("创建时间：%s" % message[9])
        print("更新时间：%s" % message[10])
        print("")
