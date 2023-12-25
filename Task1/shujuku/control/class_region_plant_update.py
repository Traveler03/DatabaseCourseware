from control import class_region_plant
import Factor
from classes import region as Regionn
from classes import plant,plant_region
FC=Factor.dao_factory()
plants=FC.create("plant")
def update():
    class_region_plant.display()
    regions=FC.create("region")
    plant_regions=FC.create("plant_region")
    sql2 = "SELECT \
            plant.plant_id,\
            c1.class_name AS shuming,\
            c2.class_name AS keming,\
            plant.species_name,\
            Plant.environment,\
            r1.region_name AS province,\
            r2.region_name AS city,\
            r3.region_name AS county\
            FROM \
            classes c1 \
            JOIN plant_class ON (c1.class_id = plant_class.class_id)\
            JOIN Plant ON (plant.plant_id = plant_class.plant_id)\
            JOIN classes c2 ON (c1.parent = c2.class_id)\
            LEFT JOIN plant_region ON (plant.plant_id = plant_region.plant_id)\
            LEFT JOIN region r3 ON (plant_region.region_id = r3.region_id)\
            LEFT JOIN region r2 ON (r3.parent = r2.region_id)\
            LEFT JOIN region r1 ON (r2.parent = r1.region_id)"
    plants = FC.create("plant")
    sql = "select plant_id from Plant"
    resul = plants.select(sql)
    judeid = 0
    print("请输入要修改植物信息的iD:")
    print()
    plant_id = -1
    while judeid == 0:
        plant_id = int(input())
        for plantid in resul:
            if int(plantid[0]) == plant_id:
                judeid = 1
                break
        if judeid == 0:
            print("输入植物ID不存在，请重新输入：")
    sql=sql2+" where plant.plant_id=%s"%plant_id
    print(sql)
    result = plants.select(sql)
    print("植物编号：%s" % result[0][0])
    print("科名：%s" % result[0][1])
    print("属名：%s" % result[0][2])
    print("种名：%s" % result[0][3])
    print("生长环境：%s" % result[0][4])
    print("省：%s" % result[0][5])
    print("市：%s" % result[0][6])
    print("县：%s" % result[0][7])
    while 1:
        print("生长环境、科名、属名、种名请于植物信息进行更新")
        print("1:修改植物的省：请输入1")
        print("2:修改植物科市：请输入2")
        print("3:修改植物属县：请输入3")
        print("4:退出请输入-1")
        m=int(input())
        if m==-1:
            break
        elif m==1:
            new_plant_reigon = plant_region.plant_region()
            new_plant_reigon.__int__(plant_id=plant_id, region_id=result[0][7])
            plant_regions.delete(new_plant_reigon)
            print("请从以下地区中输入植物省级地区（如果要增加，请输入要增加的市级名）")
            sql = "select region_id,region_name from region where rank=0"
            result = regions.select(sql)
            for province in result:
                print(province[1], end=' ')
            print("")
            province_name = input("")
            judge = 0
            province_id = -1
            result_city = []
            for province in result:
                if province_name == province[1]:
                    province_id = province[0]
                    judge = 1
                    break
            if judge == 1:
                sql2 = "select region_id,region_name from region where parent=%s" % province_id
                result_city = regions.select(sql2)
            else:
                new_region = Regionn.region()
                new_region.__int__(rank=0, region_name=province_name)
                regions.insert(new_region)
                sql_province_id = "select region_id from region where region_name='%s'" % province_name
                result_province_id = regions.select(sql_province_id)
                province_id = result_province_id[0][0]
            print("请从以下市级名中输入植物所在地市级名（如果要增加，请输入要增加的市级名）")
            if result_city:
                for city in result_city:
                    print(city[1], end=' ')
            print("")
            city_name = input()
            city_name = city_name.replace(" ", "")
            judge2 = 0
            city_id = -1
            for citys in result_city:
                if city_name == citys[1]:
                    city_id = citys[0]
                    judge2 = 1
                    break
            result_county = []
            if judge2 == 0:
                new_region = Regionn.region()
                new_region.__int__(rank=1, parent=province_id, region_name=city_name)
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
            county_name = county_name.replace(" ", "")
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
            new_plant_region = plant_region.plant_region()
            new_plant_region.__int__(plant_id=plant_id, region_id=county_id)
            plant_regions.insert(new_plant_region)
            pass
        elif m==2:
            new_plant_reigon = plant_region.plant_region()
            new_plant_reigon.__int__(plant_id=plant_id, region_id=result[0][7])
            plant_regions.delete(new_plant_reigon)
            print("请从以下地区中输入植物省级地区（如果要增加，请输入要增加的市级名）")
            sql = "select region_id,region_name from region where rank=1"
            result_city = regions.select(sql)
            if result_city:
                for city in result_city:
                    print(city[1], end=' ')
            print("")
            city_name = input()
            city_name = city_name.replace(" ", "")
            judge2 = 0
            city_id = -1
            for citys in result_city:
                if city_name == citys[1]:
                    city_id = citys[0]
                    judge2 = 1
                    break
            result_county = []
            if judge2 == 0:
                new_region = Regionn.region()
                new_region.__int__(rank=1, parent=result[0][5], region_name=city_name)
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
            county_name = county_name.replace(" ", "")
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
            new_plant_region = plant_region.plant_region()
            new_plant_region.__int__(plant_id=plant_id, region_id=county_id)
            plant_regions.insert(new_plant_region)
            pass
        elif m==3:
            new_plant_reigon = plant_region.plant_region()
            new_plant_reigon.__int__(plant_id=plant_id, region_id=result[0][7])
            plant_regions.delete(new_plant_reigon)
            print("请从以下县级名中输入植物所在地市级名（如果要增加，请输入要增加的县级名）")
            sql = "select region_id,region_name from region where rank=2"
            result_county = regions.select(sql)
            if result_county:
                for county in result_county:
                    print(county[1], end=' ')
            print("")
            county_name = input()
            county_name = county_name.replace(" ", "")
            judge3 = 0
            county_id = -1
            for countys in result_county:
                if county_name == countys[1]:
                    county_id = countys[0]
                    judge3 = 1
                    break
            if judge3 == 0:
                new_region = Regionn.region()
                new_region.__int__(rank=2, parent=result[0][6], region_name=county_name)
                regions.insert(new_region)
                sql_county_id = "select region_id,region_name from region where region_name='%s'" % county_name
                result_county_id = regions.select(sql_county_id)
                county_id = result_county_id[0][0]
            new_plant_region = plant_region.plant_region()
            new_plant_region.__int__(plant_id=plant_id, region_id=county_id)
            plant_regions.insert(new_plant_region)
            pass
