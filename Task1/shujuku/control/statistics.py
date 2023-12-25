#统计科下面种的数量
import Factor
FC=Factor.dao_factory()
def statis():
    classess=FC.create("classes")
    sql="select class_id,class_name from classes where rank=0"
    result=classess.select(sql)
    for view in result:
        viewname="View_"+str(view[0])
        sql2="select count(*) from %s"%viewname
        result2=classess.select(sql2)
        print("%s:%s"%(view[1],result2[0][0]))
