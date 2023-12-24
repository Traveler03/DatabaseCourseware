#地区插入
import Factor
from classes import region as Regionn
from classes import plant,plant_region

FC=Factor.dao_factory()
def creat_region():
    plants = FC.create("plant")
    regions = FC.create("region")
    plant_regions = FC.create("plant_region")
    sql = "select plant_id,species_name from plant"
    result_name = plants.select(sql)
    judename = 0
    name = ""
    print("请输入要添加地区的植物名称：")
    for plantname in result_name:
        print(plantname[1], end=" ")
    print()
    plant_id = -1
    while judename == 0:
        name = input()
        name=name.replace(" ","")
        for plantname in result_name:
            if plantname[1] == name:
                judename = 1
                plant_id = plantname[0]
                break
        if judename == 0:
            print("输入植物名称不存在，请重新输入：")
    print("请从以下地区中输入植物省级地区（如果要增加，请输入要增加的市级名）")
    sql="select region_id,region_name from region where rank=0"
    result=regions.select(sql)
    for province in result:
        print(province[1],end=' ')
    print("")
    province_name=input("")
    judge=0
    province_id=-1
    result_city=[]
    for province in result:
        if province_name==province[1]:
            province_id=province[0]
            judge=1
            break
    if judge==1:
        sql2="select region_id,region_name from region where parent=%s"%province_id
        result_city=regions.select(sql2)
    else:
        new_region = Regionn.region()
        new_region.__int__(rank=0,region_name=province_name)
        regions.insert(new_region)
        sql_province_id="select region_id from region where region_name='%s'"%province_name
        result_province_id=regions.select(sql_province_id)
        province_id=result_province_id[0][0]
    print("请从以下市级名中输入植物所在地市级名（如果要增加，请输入要增加的市级名）")
    if result_city:
        for city in result_city:
            print(city[1],end=' ')
    print("")
    city_name=input()
    city_name=city_name.replace(" ","")
    judge2=0
    city_id=-1
    for citys in result_city:
        if city_name==citys[1]:
            city_id=citys[0]
            judge2=1
            break
    result_county=[]
    if judge2==0:
        new_region = Regionn.region()
        new_region.__int__(rank=1,parent=province_id, region_name=city_name)
        regions.insert(new_region)
        sql_city_id = "select region_id,region_name from region where region_name='%s'" % city_name
        result_city_id = regions.select(sql_city_id)
        city_id = result_city_id[0][0]
    else:
        sql2 = "select region_id,region_name from region where parent=%s" % city_id
        result_county = regions.select(sql2)
    print("请从以下县级名中输入植物所在地市级名（如果要增加，请输入要增加的县级名）")
    if result_county:
        for county in result_county:
            print(county[1], end=' ')
    print("")
    county_name = input()
    county_name=county_name.replace(" ","")
    judge3 = 0
    county_id = -1
    for countys in result_county:
        if county_name == countys[1]:
            county_id = countys[0]
            judge3 = 1
            break
    if judge3 == 0:
        new_region = Regionn.region()
        new_region.__int__(rank=2, parent=city_id, region_name=county_name)
        regions.insert(new_region)
        sql_county_id = "select region_id,region_name from region where region_name='%s'" % county_name
        result_county_id = regions.select(sql_county_id)
        county_id = result_county_id[0][0]
    new_plant_region=plant_region.plant_region()
    new_plant_region.__int__(plant_id=plant_id,region_id=county_id)
    plant_regions.insert(new_plant_region)
