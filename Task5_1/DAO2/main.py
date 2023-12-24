import abc
import pymssql
from monitorData_DAO import *
from monitorData import *
from equipment_DAO import *
from metrics_DAO import *
from plant_region_DAO import *
from plant_region import plant_region
from plant_metrics import plant_metrics
from plant_metrics_DAO import *
from equipment_metrics import *
from equipment_metrics_DAO import *
from ExceptionLog import *
from ExceptionLog_DAO import *
from plantThreshold import *
from plantThreshold_DAO import *
def xiugaimulu():
    while True:
        print("1、监测设备\n2、监测信息\n3、监测指标\n4、植物-地区表\n5、植物-监测指标表\n6、设备-监测指标表\n7、异常信息日志表\n8、植物监测阈值表\n0、退出")
        choice2 = input("请输入数字:")
        if choice2=="1":
            jianceshebei()
        elif choice2=="2":
            jiancexinxi()
        elif choice2=="3":
            jiancezhibiao()
        elif choice2=="4":
            zhiwudiqu()
        elif choice2=="5":
            zhiwujiancezhibiao()
        elif choice2=="6":
            shebeijiancebiao()
        elif choice2 == "7":
            yichangxinxi()
        elif choice2 == "8":
            zhiwuyuzhi()
        elif choice2=="0":
            break

        else:
            print("无效的数字")
def zhiwuyuzhi():
    dao = plantThreshold_dao_Impl()

    while True:
        print("请选择操作：")
        print("1. 增加植物阈值信息")
        print("2. 更新植物阈值信息")
        print("3. 删除植物阈值信息")
        print("4. 查询植物阈值信息")
        print("0. 退出程序")

        choice = input("请输入操作编号：")

        if choice == "1":
            plant_id = input("请输入植物ID：")
            maxtemp = input("请输入最大温度：")
            mintemp = input("请输入最小温度：")
            maxgrow = input("请输入最大生长值：")
            mingrow = input("请输入最小生长值：")
            maxillu = input("请输入最大光照：")
            minillu = input("请输入最小光照：")
            pt = plantThreshold(plant_id, maxtemp, mintemp, maxgrow, mingrow, maxillu, minillu)
            dao.insert(pt)
            print("植物阈值信息已添加")

        elif choice == "2":
            plant_id = input("请输入植物ID：")
            maxtemp = input("请输入新的最大温度：")
            mintemp = input("请输入新的最小温度：")
            maxgrow = input("请输入新的最大生长值：")
            mingrow = input("请输入新的最小生长值：")
            maxillu = input("请输入新的最大光照：")
            minillu = input("请输入新的最小光照：")
            pt = plantThreshold(plant_id, maxtemp, mintemp, maxgrow, mingrow, maxillu, minillu)
            dao.update(pt)
            print("植物阈值信息已更新")

        elif choice == "3":
            plant_id = input("请输入植物ID：")
            dao.delete(plant_id)
            print("植物阈值信息已删除")

        elif choice == "4":
            plant_id = input("请输入植物ID：")
            result = dao.select(plant_id)
            for item in result:
                print(item)

        elif choice == "0":
            break

        else:
            print("无效的操作编号，请重新输入")

def yichangxinxi():
    dao = ExceptionLog_dao_Impl()

    while True:
        print("请选择操作：")
        print("1. 增加异常日志信息")
        print("2. 更新异常日志信息")
        print("3. 删除异常日志信息")
        print("4. 查询异常日志信息")
        print("0. 退出程序")

        choice = input("请输入操作编号：")

        if choice == "1":
            monitor_id = input("请输入监控ID：")
            exception_detail = input("请输入异常详情：")
            el = ExceptionLog(monitor_id, exception_detail)
            dao.insert(el)
            print("异常日志信息已添加")

        elif choice == "2":
            monitor_id = input("请输入监控ID：")
            new_exception_detail = input("请输入新的异常详情：")
            el = ExceptionLog(monitor_id, new_exception_detail)
            dao.update(el)
            print("异常日志信息已更新")

        elif choice == "3":
            monitor_id = input("请输入监控ID：")
            dao.delete(monitor_id)
            print("异常日志信息已删除")

        elif choice == "4":
            monitor_id = input("请输入监控ID：")
            result = dao.select(monitor_id)
            for item in result:
                print(item)

        elif choice == "0":
            break

        else:
            print("无效的操作编号，请重新输入")
def shebeijiancebiao():
    dao = equipment_metrics_dao_Impl()

    while True:
        print("1. 添加设备指标信息")
        print("2. 更新设备指标信息")
        print("3. 删除设备指标信息")
        print("4. 查询设备指标信息")
        print("5. 退出程序")

        choice = input("请选择操作：")

        if choice == "1":
            equipment_id = input("请输入设备ID：")
            metrics_ip = input("请输入指标IP：")

            data = equipment_metrics(equipment_id, metrics_ip)  # 创建设备指标对象
            dao.insert(data)  # 插入到数据库

            print("设备指标信息添加成功！")

        elif choice == "2":
            equipment_id = input("请输入要更新的设备ID：")
            metrics_ip = input("请输入新的指标IP：")

            data = equipment_metrics(equipment_id, metrics_ip)  # 创建设备指标对象
            dao.update(data)  # 更新数据库

            print("设备指标信息更新成功！")

        elif choice == "3":
            equipment_id = input("请输入要删除的设备ID：")

            dao.delete(equipment_id)  # 删除数据库中对应的记录

            print("设备指标信息删除成功！")

        elif choice == "4":
            equipment_id = input("请输入要查询的设备ID：")

            result = dao.select(equipment_id)  # 查询数据库中对应的记录

            if result:
                print("查询结果：")
                for record in result:
                    print(record)  # 打印查询结果
            else:
                print("未找到对应的设备指标信息！")

        elif choice == "5":
            break

        else:
            print("无效的选择，请重新输入！")
def zhiwujiancezhibiao():
    dao = plant_metrics_dao_Impl()

    while True:
        print("1. 添加植物指标信息")
        print("2. 更新植物指标信息")
        print("3. 删除植物指标信息")
        print("4. 查询植物指标信息")
        print("0. 退出程序")

        choice = input("请选择操作：")

        if choice == "1":
            plant_id = input("请输入植物ID：")
            metrics_ip = input("请输入指标IP：")
            pm = plant_metrics(plant_id, metrics_ip)
            dao.insert(pm)
            print("植物指标信息已添加")

        elif choice == "2":
            plant_id = input("请输入植物ID：")
            new_metrics_ip = input("请输入新的指标IP：")
            pm = plant_metrics(plant_id, new_metrics_ip)
            dao.update(pm)
            print("植物指标信息已更新")


        elif choice == "3":
            plant_id = input("请输入要删除的植物ID：")

            dao.delete(plant_id)  # 删除数据库中对应的记录

            print("植物指标信息删除成功！")

        elif choice == "4":
            plant_id = input("请输入要查询的植物ID：")

            result = dao.select(plant_id)  # 查询数据库中对应的记录

            if result:
                print("查询结果：")
                for record in result:
                    print(record)  # 打印查询结果
            else:
                print("未找到对应的植物指标信息！")

        elif choice == "0":
            break

        else:
            print("无效的选择，请重新输入！")
def zhiwudiqu():
    dao = plant_region_dao_Impl()

    while True:
        print("请选择操作：")
        print("1. 增加植物地区信息")
        print("2. 删除植物地区信息")
        print("3. 更新植物地区信息")
        print("4. 查询植物地区信息")
        print("0. 退出程序")

        choice = input("请输入选项：")

        if choice == "1":
            plant_id = input("请输入植物ID：")
            region = input("请输入地区ID：")
            data = plant_region(plant_id, region)
            dao.insert(data)
            print("植物地区信息已添加")

        elif choice == "2":
            plant_id = input("请输入要删除的植物ID：")
            dao.delete(plant_id)
            print("植物地区信息已删除")

        elif choice == "3":
            plant_id = input("请输入要更新的植物ID：")
            new_region_id = input("请输入新的地区ID：")
            data = plant_region(plant_id, new_region_id)
            dao.update(data)
            print("植物地区信息已更新")

        elif choice == "4":
            plant_id = input("请输入要查询的植物ID：")
            result = dao.select(plant_id)
            if result:
                print("查询结果：")
                for row in result:
                    print(row)
            else:
                print("植物地区信息不存在")

        elif choice == "0":
            print("程序已退出")
            break

        else:
            print("无效的选项，请重新输入")
def jiancezhibiao():
    dao = metrics_dao_Impl()

    while True:
        print("请选择操作:")
        print("1. 添加信息")
        print("2. 更新信息")
        print("3. 删除信息")
        print("4. 查询信息")
        print("0. 退出程序")

        choice = input("请输入选项: ")

        if choice == "1":
           # metrics_ip = input("请输入IP地址: ")
            illumination = float(input("请输入光照强度: "))
            temperature = float(input("请输入温度: "))
            grow = input("请输入生长状态: ")

           # new_metrics = metrics(metrics_ip=metrics_ip, illumination=illumination, temperature=temperature, grow=grow)
            dao.insert(illumination,temperature,grow)
            print("信息添加成功！")

        elif choice == "2":
            metrics_ip = input("请输入要更新信息的IP地址: ")
            illumination = float(input("请输入新的光照强度: "))
            temperature = float(input("请输入新的温度: "))
            grow = input("请输入新的生长状态: ")

            updated_metrics = metrics(metrics_ip=metrics_ip, illumination=illumination, temperature=temperature,
                                      grow=grow)
            dao.update(updated_metrics)
            print("信息更新成功！")

        elif choice == "3":
            metrics_ip = input("请输入要删除信息的IP地址: ")
            dao.delete(metrics_ip)
            print("信息删除成功！")

        elif choice == "4":
            metrics_ip = input("请输入要查询信息的IP地址: ")
            result = dao.select(metrics_ip)
            if result:
                print("查询结果:")
                for row in result:
                    print(row)
            else:
                print("未找到匹配的信息！")

        elif choice == "0":
            print("程序已退出。")
            break

        else:
            print("无效选项，请重新输入！")
def jianceshebei():
    equipment_dao_impl = equipment_dao_Impl()
    while True:
        print("请选择操作：")
        print("1. 增加信息")
        print("2. 删除信息")
        print("3. 更新信息")
        print("4. 查询信息")
        print("0. 退出")
        choice = input("请输入选择的操作编号：")

        if choice== "1":
            new_name = input("请输入设备名称：")
            equipment_dao_impl.insert(new_name)
            print("插入成功！")

        if choice=="2":
            to_be_deleted_id = input("请输入要删除的设备ID：")
            equipment_dao_impl.delete(to_be_deleted_id)
            print("删除成功！")

        if choice=="3":
            existing_id = input("请输入要更新的设备ID：")
            new_updated_name = input("请输入更新后的设备名称：")
            updated_equipment = equipment(existing_id, new_updated_name)
            equipment_dao_impl.update(updated_equipment)
            print("更新成功！")

        if choice=="4":
            desired_id = input("请输入要查询的设备ID：")
            result = equipment_dao_impl.select(desired_id)
            if result:
                print("查询结果：", result)
            else:
                print("未找到匹配信息。")

        if choice =="0":
            break;

def jiancexinxi():
    dao_impl = monitorData_dao_Impl()

    while True:
        print("请选择操作：")
        print("1. 增加信息")
        print("2. 删除信息")
        print("3. 更新信息")
        print("4. 查询信息")
        print("0. 退出")
        choice = input("请输入选择的操作编号：")

        if choice == "1":
            # 增加信息
            monitor_id = input("请输入监测数据的 ID：")
            monitor_region = input("请输入监测区域：")
            monitor_time = input("请输入监测时间：")
            plant_id = input("请输入植物 ID：")
            monitor_temp = input("请输入监测温度：")
            monitor_grow = input("请输入监测生长情况：")
            monitor_illu = input("请输入监测光照强度：")

            data = monitorData(monitor_id, monitor_region, monitor_time, plant_id, monitor_temp, monitor_grow,
                               monitor_illu)
            dao_impl.insert(data)
            print("已成功添加监测数据！")

        elif choice == "2":
            # 删除信息
            id = input("请输入要删除的监测数据的 ID：")
            dao_impl.delete(id)
            print("已成功删除监测数据！")

        elif choice == "3":
            # 更新信息
            monitor_id = input("请输入要更新的监测数据的 ID：")
            monitor_region = input("请输入新的监测区域：")
            monitor_time = input("请输入新的监测时间：")
            plant_id = input("请输入新的植物 ID：")
            monitor_temp = input("请输入新的监测温度：")
            monitor_grow = input("请输入新的监测生长情况：")
            monitor_illu = input("请输入新的监测光照强度：")

            data = monitorData(monitor_id, monitor_region, monitor_time, plant_id, monitor_temp, monitor_grow,
                               monitor_illu)
            dao_impl.update(data)
            print("已成功更新监测数据！")

        elif choice == "4":
            # 查询信息
            id = input("请输入查询植物id：")
            result = dao_impl.select(id)
            print("查询结果：")
            for row in result:
                print(row)

        elif choice == "0":
            # 退出程序
            break

        else:
            print("无效的选择，请重新输入！")


def average():
    pass



def max():
    pass


if __name__ == '__main__':
    while True:
        print("1、增、删、改、查信息")
        print("2、平均值查询")
        print("3、最大值查询")
        choice = input("请输入数字:")

        if choice == "1":
            xiugaimulu()
        elif choice == "2":
            average()
        elif choice == "3":
            max()
        else:
            print("无效的选择\n")









