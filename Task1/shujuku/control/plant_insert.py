import Factor
from classes.classes import classes as classs
from classes import plant,plant_classes
FC=Factor.dao_factory()
def creat_plant(user=None):
    plants=FC.create("plant")
    sql ="select species_name from plant"
    result_name=plants.select(sql)
    judename = 0
    name=""
    while judename==0:
        name=input("请输入植物名：")
        for plantname in result_name:
            judename =1
            if plantname[0]==name:
                print("植物名重复，请重新输入：")
                judename =0
                continue

    print("请从以下科名中输入植物科名（如果要增加，请输入要增加的科名）")
    sql="select class_id,class_name from classes where rank=0"
    result=plants.select(sql)
    for Family in result:
        print(Family[1],end=' ')
    print("")
    Family_name=input("")
    judge=0
    Family_id=-1
    result_genus=[]
    for Family in result:
        if Family_name==Family[1]:
            Family_id=Family[0]
            judge=1
            break
    if judge==1:
        sql2="select class_id,class_name from classes where parent=%s"%Family_id
        result_genus=plants.select(sql2)
    else:
        classess=FC.create("classes")
        new_class=classs()
        new_class.__int__(rank=0,class_name=Family_name)
        classess.insert(new_class)
        sql_Family_id="select class_id from classes where class_name='%s'"%Family_name
        result_famil_id=classess.select(sql_Family_id)
        Family_id=result_famil_id[0][0]
    print("请从以下科名中输入植物属名（如果要增加，请输入要增加的属名）")
    if result_genus:
        for Genus in result_genus:
            print(Genus[1],end=' ')
    print("")
    Genus_name=input()
    judge2=0
    Genus_id=-1
    for Genuss in result_genus:
        if Genus_name==Genuss[1]:
            Genus_id=Genuss[0]
            judge2=1
            break
    if judge2==0:
        classess = FC.create("classes")
        new_class = classs()
        new_class.__int__(rank=1,parent=Family_id, class_name=Family_name)
        classess.insert(new_class)
        sql_Genus_id = "select class_id from classes where class_name='%s'" % Family_name
        result_Genus_id = classess.select(sql_Genus_id)
        Genus_id = result_Genus_id[0][0]
    alies=input("请输入植物别名：")
    morphology=input("请输入植物形态特征：")
    key_tech=input("请输入植物栽培技术")
    value=input("请输入植物价值")
    envirment=input("请输入植物的生长环境")
    new_plant=plant.plant()
    new_plant.__int__(species_name=name,alies=alies,morphology=morphology,value=value,key_tech=key_tech,environment=envirment)
    plants.insert(new_plant)
    sql3="select plant_id from plant where species_name='%s'"%name
    result_id=plants.select(sql3)
    FC_plant_classes=FC.create("plant_classes")
    new_plant_classes=plant_classes.plant_classes()
    new_plant_classes.__int__(plant_id=result_id[0][0],class_id=Genus_id)
    FC_plant_classes.insert(new_plant_classes)
creat_plant()