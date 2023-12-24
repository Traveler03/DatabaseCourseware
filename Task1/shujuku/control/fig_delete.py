#配图删除
from control import fig
import Factor
FC=Factor.dao_factory()
def delete():
    fig.display()
    print("请输入要删除配图的iD:")
    print()
    figs = FC.create("fig")
    sql = "select fig_id from fig"
    result_name = figs.select(sql)
    judeid = 0
    fig_id = -1
    while judeid == 0:
        fig_id = int(input())
        for figid in result_name:
            if int(figid[0]) == fig_id:
                judeid = 1
                break
        if judeid == 0:
            print("输入配图ID不存在，请重新输入：")
    figs.delete(fig_id)
    print("植物信息删除成功")
