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
        print("植物科名：%s"%message[2])
        sql2="select c1.class_name as shuming,c2.class_name as keming  from classes c1,classes c2,plant_class,Plant \
    where plant.plant_id=plant_class.plant_id and plant_class.class_id=c1.class_id and  \
    plant.plant_id=%s and c2.class_id=(select c1.parent)"%message[0]
        result_class=plants.select(sql2)

        print("植物属名：%s"%result_class[0][0])
        print("植物别名：%s"%result_class[0][1])

        print("植物形态特征：%s"%message[3])
        print("植物栽培技术要点：%s" % message[4])
        sql3="select Pest.pest_name,Pest.cm from plant,Pest,plant_pest \
    where Plant.plant_id=plant_pest.plant_id and plant_pest.pest_id=Pest.pest_id and Plant.plant_id=%s"%message[0]
        result_pest=plants.select(sql3)
        for pest in result_pest:
            print("植物病名：%s"%pest[0])
            print("病虫害防止措施：%s"%pest[1])
        print("植物应用价值：%s" % message[5])
        print("创建人员：%s"%message[6])
        print("创建时间：%s"%message[7])
        print("更新时间：%s"%message[8])
