#模糊查询
import Factor
from classes import plant as plant2
FC=Factor.dao_factory()
def Inquire():
    print("请输入想要模糊查询的信息：")
    print("1：植物编号")
    print("2：植物名称")
    print("3：植物科名")
    print("4：植物属名")
    print("5：植物别名")
    print("6：植物形态特征")
    print("7：植物栽培技术")
    print("8：植物防治措施")
    print("9：植物应用价值")
    print("10：植物病名")
    print("11：创建人员")
    print("12：创建时间")
    print("13：更新时间")
    print("请输入想要查询的字段序号，输入0，退出")
    m=[]
    while 1:
        n=int(input())
        if n==0:
            break
        elif n<1 or n>13:
            print("输入错误,请重新输入")
        else:
            m.append(n)
    sql="select DISTINCT plant.plant_id from classes c1,classes c2,plant_class,Plant \
       ,pest,plant_pest,region r1,region r2,region r3,plant_region where plant.plant_id=plant_class.plant_id "
    for i in m:
        if i==1:
            id=input("请输入要查询的id号：")
            sql+=" and plant_id like '%{}%' ".format(id)
            pass
        elif i==2:
            name = input("请输入要查询的名称：")
            sql += " and species_name like '%{}%' ".format(name)
            pass
        elif i==3:
            keming = input("请输入要查询的科名：")
            sql += " and c2.class_name like '%{}%' and c1.parent=c2.class_id and plant.plant_id=plant_class.plant_id and plant_class.class_id=c1.class_id ".format(keming)
            pass
        elif i==4:
            shuming=input("请输入要查询的属名：")
            sql+=" and c1.class_name like '%{}%' and plant.plant_id=plant_class.plant_id and plant_class.class_id=c1.class_id ".format(shuming)
            pass
        elif i==5:
            alia = input("请输入要查询的别名：")
            sql += " and alia like '%{}%' ".format(alia)
            pass
        elif i==6:
            morphology = input("请输入要查询的植物形态特征：")
            sql += " and morphology like '%{}%' ".format(morphology)
            pass
        elif i==7:
            key_tech = input("请输入要查询的植物栽培技术：")
            sql += " and key_tech like '%{}%' ".format(key_tech)
            pass
        elif i==8:
            cm = input("请输入要查询的防治措施：")
            sql += " and pest.cm like '%{}%' and Pest.pest_id=plant_pest.pest_id and Plant.plant_id=plant_pest.plant_id ".format(cm)
            pass
        elif i==9:
            value = input("请输入要查询的植物栽培技术：")
            sql += " and key_tech like '%{}%' ".format(value)
            pass
        elif i==10:
            pest_name = input("请输入要查询的病名：")
            sql += " and pest.pest_name like '%{}%' and Pest.pest_id=plant_pest.pest_id and Plant.plant_id=plant_pest.plant_id ".format(
                pest_name)
            pass
        elif i==11:
            created_by = input("请输入要查询的植物栽培技术：")
            sql += " and creat_by like '%{}%' ".format(created_by)
            pass
        elif i==12:
            created_at = input("请输入要查询的植物栽培技术：")
            sql += " and created_at like '%{}%' ".format(created_at)
            pass
        elif i==13:
            updated_at = input("请输入要查询的植物栽培技术：")
            sql += " and updated_at like '%{}%' ".format(updated_at)
            pass
    plants = FC.create("plant")
    result=plants.select(sql)
    for i in result:
        plant_id=i[0]
        sql_id = "select plant_id,species_name,alia,\
                    morphology,key_tech,environment,value,created_by,created_at,updated_at\
                     from Plant where plant_id=%d" % plant_id
        result_id = plants.select(sql_id)
        print("植物编号：%s" % result_id[0][0])
        print("植物名称：%s" % result_id[0][1])
        print("植物别名：%s" % result_id[0][2])
        sql2 = "select c1.class_id,c1.class_name as shuming,c2.class_id,c2.class_name as keming  from classes c1,classes c2,plant_class,Plant \
               where plant.plant_id=plant_class.plant_id and plant_class.class_id=c1.class_id and  \
               plant.plant_id=%s and c2.class_id=(select c1.parent)" % result_id[0][0]
        result_class = plants.select(sql2)

        print("植物科名：%s" % result_class[0][3])
        print("植物属名：%s" % result_class[0][1])
        print("植物形态特征：%s" % result_id[0][3])
        print("植物栽培技术要点：%s" % result_id[0][4])
        print("植物生长环境：%s" % result_id[0][5])
        sql3 = "select Pest.pest_name,Pest.cm from plant,Pest,plant_pest \
               where Plant.plant_id=plant_pest.plant_id and plant_pest.pest_id=Pest.pest_id and Plant.plant_id=%s" % \
               result_id[0][0]
        result_pest = plants.select(sql3)
        for pest in result_pest:
            print("植物病名：%s" % pest[0])
            print("病虫害防止措施：%s" % pest[1])
        print("植物应用价值：%s" % result_id[0][6])
        sql = "select fig.fig_id,species_name,fig_path,fig_place,fig_people,fig_des from fig, \
                            plant,plant_fig where fig.fig_id=plant_fig.fig_id and Plant.plant_id=plant_fig.plant_id and plant.plant_id=%d" % \
              result_id[0][0]
        result_fig = plants.select(sql)
        for fig_m in result_fig:
            print("配图编号：%s" % fig_m[0])
            print("图片路径：%s" % fig_m[2])
            print("拍摄地点：%s" % fig_m[3])
            print("配图人员：%s" % fig_m[4])
            print("配图描述：%s" % fig_m[5])
        print("创建人员：%s" % result_id[0][7])
        print("创建时间：%s" % result_id[0][8])
        print("更新时间：%s" % result_id[0][9])
        print("")
