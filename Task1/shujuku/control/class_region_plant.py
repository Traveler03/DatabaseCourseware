import Factor
FC=Factor.dao_factory()
plants=FC.create("plant")
def display():
        sql="select plant.plant_id,c1.class_name as shuming,c2.class_name as keming,plant.species_name,Plant.environment,r1.region_name as province,r2.region_name as city,r3.region_name as county \
from classes c1,classes c2,plant_class,Plant ,region r1,region r2,region r3,plant_region\
    where plant.plant_id=plant_class.plant_id and plant_class.class_id=c1.class_id and  \
     c2.class_id=(select c1.parent) and plant.plant_id=plant_region.plant_id \
	and plant_region.region_id=r3.region_id and r2.region_id=(select r3.parent) and r1.region_id=(select r2.parent)"
        result = plants.select(sql)
        for message in result:
            print("植物编号：%s"%message[0])
            print("科名：%s" % message[1])
            print("属名：%s" % message[2])
            print("种名：%s" % message[3])
            print("生长环境：%s" % message[4])
            print("省：%s" % message[5])
            print("市：%s" % message[6])
            print("县：%s" % message[7])
            print()
display()