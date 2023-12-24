#分类的删除
#配图删除
from control import fig
import Factor
FC=Factor.dao_factory()
def delete():
    classess = FC.create("classes")
    sql = "select * from classes"
    result = classess.select(sql)
    for i in result:
        print("分类ID：%s" % i[0])
        print("父节点：%s" % i[1])
        print("等级：%s" % i[2])
        print("类名：%s" % i[3])
        print("")
    print("请输入要修改分类信息的iD:")
    print()
    class_id = -1
    judeid = 0
    while judeid == 0:
        class_id = int(input())
        for classid in result:
            if int(classid[0]) == class_id:
                judeid = 1
                break
        if judeid == 0:
            print("输入分类ID不存在，请重新输入：")
    classess.delete(class_id)
    print("植物信息删除成功")
