#植物
import Factor
FC=Factor.dao_factory()
plants=FC.create("plant")
def display():
    sql ="select plant_id,species_name,alia,\
    morphology,key_tech,value,created_by,created_at,updated_at\
     from Plant"
    result = plants.select(sql)
    for message in result:
        print("植物编号：%s"%message[0])
        print("植物名称：%s" % message[1])
        print("植物别名：%s"%message[2])
        sql2="SELECT c1.class_name AS shuming, c2.class_name AS keming\
        FROM plant\
        LEFT JOIN plant_class ON plant.plant_id = plant_class.plant_id\
        LEFT JOIN classes c1 ON plant_class.class_id = c1.class_id\
        LEFT JOIN classes c2 ON c1.parent = c2.class_id\
        WHERE plant.plant_id = %s;"%message[0]
        result_class=plants.select(sql2)
        print("植物科名：%s"%result_class[0][1])
        print("植物属名：%s"%result_class[0][0])

        print("植物形态特征：%s"%message[3])
        print("植物栽培技术要点：%s" % message[4])
        sql3="select Pest.pest_name,Pest.cm from plant,Pest,plant_pest \
    where Plant.plant_id=plant_pest.plant_id and plant_pest.pest_id=Pest.pest_id and Plant.plant_id=%s"%message[0]
        result_pest=plants.select(sql3)
        for pest in result_pest:
            print("植物病名：%s"%pest[0])
            print("病虫害防止措施：%s"%pest[1])
        print("植物应用价值：%s" % message[5])
        sql = "select fig.fig_id,species_name,fig_path,fig_place,fig_people,fig_des from fig, \
                 plant,plant_fig where fig.fig_id=plant_fig.fig_id and Plant.plant_id=plant_fig.plant_id and plant.plant_id=%d"%message[0]
        result_fig = plants.select(sql)
        for fig_m in result_fig:
            print("配图编号：%s"%fig_m[0])
            print("图片路径：%s"%fig_m[2])
            print("拍摄地点：%s"%fig_m[3])
            print("配图人员：%s"%fig_m[4])
            print("配图描述：%s"%fig_m[5])
        print("创建人员：%s"%message[6])
        print("创建时间：%s"%message[7])
        print("更新时间：%s"%message[8])
        print("")
