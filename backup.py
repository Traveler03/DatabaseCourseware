# to backup database
# 主要实现备份GardenPlants数据库,到当前目录下面的database_backup目录下面，备份文件为GardenPlants.bak
# 关键性数据库备份命令：Backup Database GardenPlants　

import configparser
import pymssql
import os
import datetime
import time

# 配置当前时间
# 由于这个脚本只是其一，单单的进行本地备份，
# 脚本为后期超过30天自动删除和用python实现跨网络的windows server服务器之间的文件传输做准备

time1 = str(datetime.datetime.now())
time2 = time1.split('.')[0]
time3 = time2.split(' ')[0]

# 该脚本所需要的配置文件、日志和备份目录的路径，方便创建
# 这个脚本有自己的配置文件和日志展示
current_path = os.getcwd()
current_config_path = current_path + '\\' + 'config.ini'
current_log_path = current_path + '\\' + 'log.txt'
current_database_backup_path = current_path + '\\' + 'database_backup'


# 判断配置文件.ini和日志文件是否存在，没有则创建
def path_txt_judge(txt):
    if os.path.exists(txt):
        print(time2, '    ' + txt + '已存在，不需要创建')
        file = open(current_log_path, 'a', encoding='utf-8')
        #    file.write('hello\nword')
        a = str(time2 + "    " + txt + "文件存在")
        # print(a)
        file.write(a + "\n")
        file.close()
    else:
        file = open(txt, 'a', encoding='utf-8')  # a 的话是追加写入，不覆盖之前的内容
        a1 = str(time2 + '    创建' + txt + '文件' + current_log_path + '成功')
        file.write(a1 + "\n")
        file.close()


# 判断backup目录是否存在，不存在则创建
# 为什么要指定目录呢，因为后期咱上传到别的服务的时候能第一时间找到备份文件
def path_dir_judge(dir):
    if os.path.exists(dir):
        print(time2, '    文件目录存在，不需要创建')
        file = open(current_log_path, 'a', encoding='utf-8')  # w 的含义为可进行读写
        #    file.write('hello\nword')
        d = str(time2 + '    备份目录' + current_database_backup_path + '存在')
        file.write(d + "\n")
        file.close()
    else:
        os.makedirs(dir)
        file = open(current_log_path, 'a', encoding='utf-8')  # w 的含义为可进行读写
        #    file.write('hello\nword')
        d1 = str(time2 + '    备份目录' + current_database_backup_path + '创建成功')
        file.write(d1 + "\n")
        file.close()


# 主要实现了一个对日志文件的写，非常清晰明了的告诉自己都干了些什么
def log_write(log):
    file = open(current_log_path, 'a', encoding='utf-8')  # w 的含义为可进行读写
    file.write(log + "\n")
    file.close()


def backup_db():
    # 调用相应的函数
    path_txt_judge(current_log_path)
    path_txt_judge(current_config_path)
    path_dir_judge(current_database_backup_path)

    # 对配置文件config.ini进行读取，获取所需要的数据
    cf = configparser.ConfigParser()
    cf.read(current_config_path)
    database_host = cf.get('sql_server', 'host')  # 得到hose
    database_port = cf.get('sql_server', 'port')  # 得到端口号
    database_user = cf.get('sql_server', 'user')  # 得到登录数据的用户名
    database_password = cf.get('sql_server', 'password')  # 得到登录数据库的密码
    backup_database = cf.get('database_name', 'database_name')  # 得到你想要备份的数据库名称

    # 连接数据库，执行备份操作
    conn = pymssql.connect(host=database_host, port=database_port, user=database_user, password=database_password)
    if conn:
        print(time2, "    连接数据库", database_host, "成功!")
        e = str(time2 + '    连接数据库' + database_host + '成功')
        log_write(e)
    else:
        print(time2, "    连接数据库", database_host,
              "没有成功! 请仔细检查防火墙、数据库tcp/ip动态端口是否开启或者配置文件配置是否正确")
        e1 = str(
            time2 + '    连接数据库' + database_host + '出现问题，请仔细检查防火墙、数据库tcp/ip动态端口是否开启或者配置文件配置是否正确')
        log_write(e1)
        time.sleep(5)

    conn.autocommit(True)
    cursor = conn.cursor()
    backup_sql_path = current_database_backup_path + "\\" + time3 + "_" + backup_database + ".bak"

    sql = "Backup Database " + backup_database + "　To disk=" + '\'' + backup_sql_path + '\''
    cursor.execute(sql)
    sql1 = str("Backup Database " + backup_database + "　To disk=" + '\'' + backup_sql_path + '\'')
    f2 = str(time2 + '    对数据库执行备份操作' + '备份语句为:' + sql1)
    print(time2, '    正在对数据库进行备份操作，请稍等...')
    log_write(f2)
    conn.commit()  # 这个提交动作比较重要
    time.sleep(10)

    # 断开与数据库的连接
    conn.close()
    print(time2, "    已断开与数据库", database_host, "的连接!")
    time.sleep(10)
    f1 = str(time2 + "    已断开" + database_host + '数据库的连接!')
    log_write(f1)

