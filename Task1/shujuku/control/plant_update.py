#植物更新
from control import plant
from classes import plant as plant2
from classes import classes as class2
from classes import plant_classes
import Factor
FC=Factor.dao_factory()

def update_plant():
    plant.display()
    figs = FC.create("fig")
    classess=FC.create("classes")
    plant_classess=FC.create("plant_classes")
    plants=FC.create("plant")
    sql = "select plant_id from Plant"
    result_name = plants.select(sql)
    judeid = 0
    print("请输入要修改植物信息的iD:")
    print()
    plant_id=-1
    while judeid == 0:
        plant_id = int(input())
        for plantid in result_name:
            if int(plantid[0]) == plant_id:
                judeid = 1
                break
        if judeid == 0:
            print("输入植物ID不存在，请重新输入：")
    sql_id = "select plant_id,species_name,alia,\
            morphology,key_tech,environment,value,created_by,created_at,updated_at\
             from Plant where plant_id=%d"%plant_id
    result_id = plants.select(sql_id)
    print("植物编号：%s" % result_id[0][0])
    print("植物名称：%s" % result_id[0][1])
    print("植物别名：%s" % result_id[0][2])
    sql2 = "select c1.class_id,c1.class_name as shuming,c2.class_id,c2.class_name as keming  FROM plant\
        LEFT JOIN plant_class ON plant.plant_id = plant_class.plant_id\
        LEFT JOIN classes c1 ON plant_class.class_id = c1.class_id\
        LEFT JOIN classes c2 ON c1.parent = c2.class_id\
        WHERE plant.plant_id = %s" % result_id[0][0]
    result_class = plants.select(sql2)

    print("植物科名：%s" % result_class[0][3])
    print("植物属名：%s" % result_class[0][1])
    print("植物形态特征：%s" % result_id[0][3])
    print("植物栽培技术要点：%s" % result_id[0][4])
    print("植物生长环境：%s"%result_id[0][5])
    sql3 = "select Pest.pest_name,Pest.cm from plant,Pest,plant_pest \
       where Plant.plant_id=plant_pest.plant_id and plant_pest.pest_id=Pest.pest_id and Plant.plant_id=%s" % result_id[0][0]
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
    while 1:
        print("1:修改植物名称：请输入1")
        print("2:修改植物科名：请输入2")
        print("3:修改植物属名：请输入3")
        print("4:修改植物别名：请输入4")
        print("5:修改植物形态特征：请输入5")
        print("6:修改植物栽培技术要点：请输入6")
        print("7:修改植物生活环境：请输入7")
        print("8:修改植物应用价值：请输入8")
        print("9:修改配图：请输入9")
        print("10:退出：请输入-1")
        m=int(input())
        if m==1:
            sql3 = "select species_name from plant"
            result_name = plants.select(sql3)
            judename = 0
            name = ""
            while judename == 0:
                name = input("请输入要更新的植物名：")
                for plantname in result_name:
                    judename = 1
                    if plantname[0] == name:
                        print("植物名重复，请重新输入：")
                        judename = 0
                        break
            plants.update(choose=1,id=result_id[0][0],value=name)
            pass
        elif m==2:
            new_plant_class=plant_classes.plant_classes()
            new_plant_class.__int__(plant_id=result_id[0][0],class_id=result_class[0][0])
            plant_classess.delete(new_plant_class)
            print("请从以下科名中输入植物科名（如果要增加，请输入要增加的科名）")
            sql = "select class_id,class_name from classes where rank=0"
            result = plants.select(sql)
            for Family in result:
                print(Family[1], end=' ')
            print("")
            Family_name = input("")
            Family_name = Family_name.replace(" ", "")
            judge = 0
            Family_id = -1
            result_genus = []
            for Family in result:
                if Family_name == Family[1]:
                    Family_id = Family[0]
                    judge = 1
                    break
            if judge == 1:
                sql2 = "select class_id,class_name from classes where parent=%s" % Family_id
                result_genus = plants.select(sql2)
            else:
                classess = FC.create("classes")
                new_class = class2.classes()
                new_class.__int__(rank=0, class_name=Family_name)
                classess.insert(new_class)
                sql_Family_id = "select class_id from classes where class_name='%s'" % Family_name
                result_famil_id = classess.select(sql_Family_id)
                Family_id = result_famil_id[0][0]
            print("请从以下科名中输入植物属名（如果要增加，请输入要增加的属名）")
            if result_genus:
                for Genus in result_genus:
                    print(Genus[1], end=' ')
            print("")
            Genus_name = input()
            Genus_name = Genus_name.replace(" ", "")
            judge2 = 0
            Genus_id = -1
            for Genuss in result_genus:
                if Genus_name == Genuss[1]:
                    Genus_id = Genuss[0]
                    judge2 = 1
                    break
            if judge2 == 0:
                classess = FC.create("classes")
                new_class = class2.classes()
                new_class.__int__(rank=1, parent=Family_id, class_name=Genus_name)
                classess.insert(new_class)
                sql_Genus_id = "select class_id from classes where class_name='%s'" % Genus_name
                result_Genus_id = classess.select(sql_Genus_id)
                Genus_id = result_Genus_id[0][0]
            new_plant_classes = plant_classes.plant_classes()
            new_plant_classes.__int__(plant_id=result_id[0][0], class_id=Genus_id)
            plant_classess.insert(new_plant_classes)
            pass
        elif m==3:
            new_plant_class = plant_classes.plant_classes()
            new_plant_class.__int__(plant_id=result_id[0][0], class_id=result_class[0][0])
            plant_classess.delete(new_plant_class)
            print("请输入要更新的属名：")
            sql4="select class_id,class_name from classes where parent=%s" % result_class[0][2]
            result_genus= plants.select(sql4)
            if result_genus:
                for Genus in result_genus:
                    print(Genus[1], end=' ')
            print("")
            Genus_name = input()
            Genus_name = Genus_name.replace(" ", "")
            judge2 = 0
            Genus_id = -1
            for Genuss in result_genus:
                if Genus_name == Genuss[1]:
                    Genus_id = Genuss[0]
                    judge2 = 1
                    break
            if judge2 == 0:
                classess = FC.create("classes")
                new_class = class2.classes()
                new_class.__int__(rank=1, parent=result_class[0][2],class_name=Genus_name)
                classess.insert(new_class)
                sql_Genus_id = "select class_id from classes where class_name='%s'" % Genus_name
                result_Genus_id = classess.select(sql_Genus_id)
                Genus_id = result_Genus_id[0][0]
            new_plant_classes = plant_classes.plant_classes()
            new_plant_classes.__int__(plant_id=result_id[0][0], class_id=Genus_id)
            plant_classess.insert(new_plant_classes)
            pass
        elif m==4:
            alies = input("请输入要更新的别名")
            plants.update(choose=2,id=result_id[0][0],value=alies)
            pass
        elif m==5:
            morphology = input("请输入要更新的植物形态特征：")
            plants.update(choose=3,id=result_id[0][0],value=morphology)
            pass
        elif m==6:
            key_tech=input("请输入要更新的植物栽培技术要点：")
            plants.update(choose=5,id=result_id[0][0],value=key_tech)
            pass
        elif m==7:
            envionment=input("请输入要更新的植物生活环境")
            plants.update(choose=6,id=result_id[0][0],value=envionment)
            pass
        elif m==8:
            value=input("请输入要更新的植物应用价值：")
            plants.update(choose=4,id=result_id[0][0],value=value)
            pass
        elif m==9:
            fig_id=-1
            while 1:
                fig_id=int(input("请输入要更新的配图ID"))
                judge=-1
                for fig_m in result_fig:
                    if fig_m[0]==fig_id:
                        judge=1
                        break
                if judge!=1:
                    print("输入错误，该植物没有这个配图,请重新输入")
                else:
                    break
            sql_id = "select * from fig where fig_id=%d" % fig_id
            result_figid = figs.select(sql_id)
            print("配图编号：%s" % result_figid[0][0])
            print("配图路径：%s" % result_figid[0][1])
            print("拍摄地点：%s" % result_figid[0][2])
            print("拍摄人员：%s" % result_figid[0][3])
            print("配图描述：%s" % result_figid[0][4])
            print("创建人员：%s" % result_figid[0][5])
            print("创建时间：%s" % result_figid[0][6])
            print("更新时间：%s" % result_figid[0][7])
            while 1:
                print("1:修改配图路径：请输入1")
                print("2:修改拍摄地点：请输入2")
                print("3:修改拍摄人员：请输入3")
                print("4:修改配图描述：请输入4")
                print("5:退出：请输入-1")
                m = int(input())
                if m == -1:
                    break
                elif m == 1:
                    fig_path = input("请输入要更新的配图路径")
                    figs.update(choose=1, value=fig_path, id=fig_id)
                    pass
                elif m == 2:
                    fig_dot = input("请输入要更新的拍摄地点")
                    figs.update(choose=2, value=fig_dot, id=fig_id)
                    pass
                elif m == 3:
                    fig_people = input("请输入要更新的拍摄人员")
                    figs.update(choose=3, value=fig_people, id=fig_id)
                    pass
                elif m == 4:
                    fig_dis = input("请输入要更新的配图描述")
                    figs.update(choose=3, value=fig_dis, id=fig_id)
                    pass
            pass
        elif m==-1:
            return
update_plant()