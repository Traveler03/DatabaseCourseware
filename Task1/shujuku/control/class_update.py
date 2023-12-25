
import Factor
FC=Factor.dao_factory()
def update():
    classess = FC.create("classes")
    sql="select * from classes"
    result=classess.select(sql)
    for i in result:
        print("分类ID：%s"%i[0])
        print("父节点：%s" % i[1])
        print("等级：%s" % i[2])
        print("类名：%s" % i[3])
        print("")
    print("请输入要修改分类信息的iD:")
    print()
    class_id = -1
    judeid=0
    while judeid == 0:
        class_id = int(input())
        for classid in result:
            if int(classid[0]) == class_id:
                judeid = 1
                break
        if judeid == 0:
            print("输入分类ID不存在，请重新输入：")
    sql2 = "select * from classes where class_id=%s"%class_id
    result2=classess.select(sql2)
    print("该分类信息为：")
    for i in result2:
        print("分类ID：%s" % i[0])
        print("父节点：%s" % i[1])
        print("等级：%s" % i[2])
        print("类名：%s" % i[3])
    while 1:
        print("修改父节点请输入1")
        print("修改类名请输入2")
        print("退出请输入-1")
        m=int(input())
        if m==-1:
            break
        elif m==1:
            sql3="select class_id,class_name from classes where rank=0"
            result3 = classess.select(sql3)
            for i in result3:
                print("编号%s,名称%s"%(i[0],i[1]),end=" ")
            judge = 0
            parent_id=-1
            while judge==0:
                parent_id=int(input("请输入父节点编号"))

                for i in result3:
                    if parent_id==i[0]:
                        judge=1
                if judge==1:
                    break
                else:
                    print("节点输入错误，请重新输入")
            classess.update(choose=1,id=class_id,value=parent_id)
        elif m==2:
            name=input("请输入更新后的名字：")
            classess.update(choose=3, id=class_id, value=name)


