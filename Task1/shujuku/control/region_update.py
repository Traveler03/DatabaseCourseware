
import Factor

FC = Factor.dao_factory()


def update():
    regioness = FC.create("region")
    sql = "select * from region"
    result = regioness.select(sql)
    for i in result:
        print("分类ID：%s" % i[0])
        print("父节点：%s" % i[1])
        print("等级：%s" % i[2])
        print("类名：%s" % i[3])
        print("")
    print("请输入要修改分类信息的iD:")
    print()
    region_id = -1
    judeid = 0
    while judeid == 0:
        region_id = int(input())
        for regionid in result:
            if int(regionid[0]) == region_id:
                judeid = 1
                break
        if judeid == 0:
            print("输入分类ID不存在，请重新输入：")
    sql2 = "select * from region where region_id=%s" % region_id
    result2 = regioness.select(sql2)
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
        m = int(input())
        if m == -1:
            break
        elif m == 1:
            sql3 = "select region_id,region_name from region where rank=%s"%(result2[0][2]-1)
            result3 = regioness.select(sql3)
            for i in result3:
                print("编号%s,名称%s" % (i[0], i[1]), end=" ")
            judge = 0
            parent_id = -1
            while judge == 0:
                parent_id = int(input("请输入父节点编号"))

                for i in result3:
                    if parent_id == i[0]:
                        judge = 1
                if judge == 1:
                    break
                else:
                    print("节点输入错误，请重新输入")
            regioness.update(choose=1, id=region_id, value=parent_id)
        elif m == 2:
            name = input("请输入更新后的名字：")
            regioness.update(choose=3, id=region_id, value=name)


