#分类
import Factor
FC=Factor.dao_factory()
plants=FC.create("plant")
def display():
        sql="SELECT \
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
        result = plants.select(sql)
        for message in result:
            print("植物编号：%s"%message[0])
            print("科名：%s" % message[1])
            print("属名：%s" % message[2])
            print("种名：%s" % message[3])
            print("生长环境：%s" % message[4])

            print("分布地区有：")
            sql2 = "SELECT \
    r1.region_name AS province,\
    r2.region_name AS city,\
    r3.region_name AS county \
FROM \
	plant \
    LEFT JOIN plant_region ON (plant.plant_id = plant_region.plant_id)\
    LEFT JOIN region r3 ON (plant_region.region_id = r3.region_id)\
    LEFT JOIN region r2 ON (r3.parent = r2.region_id)\
    LEFT JOIN region r1 ON (r2.parent = r1.region_id)\
    where plant.plant_id=%s"%message[0]
            result2=plants.select(sql2)
            for i in result2:
                print("省：%s" % i[0])
                print("市：%s" % i[1])
                print("县：%s" % i[2])
            print()
