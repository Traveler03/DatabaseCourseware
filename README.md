## DatabaseCourseware
数据库课设小组
## 说明
- 在对应的文件夹下完成自己的任务。
- 切记不要修改除自己外的文件夹的内容，以免造成冲突！
- 记得要`commit` 后再`push`到GitHub仓库，这样有提交痕迹，用于展示使用！

## 开发规范
- 数据库的名称 `GardenPlants`
- 各个任务对应的表参考根目录下的`数据库表.txt`文件


## 课设项目结构
![image](https://github.com/Traveler03/DatabaseCourseware/assets/98093304/a5d25e7c-1696-4955-b070-057f880563c0)

## 备注
Task5_monitorData_trigger触发器详情：
当向monitorData表插入或更新数据时，如果新的数据的monitor_temp、monitor_grow或monitor_illu字段的值超过（或低于）设定的阈值，那么就向ExceptionLog_table表插入一条新的记录，记录下这个异常情况。
在sql server中运行该代码后：
① 可使用 sp_help 查看触发器的一般信息；EXEC sp_help monitorData_trigger
② 可使用 sp_depends 查看触发器的相关性；EXEC sp_depends monitorData_trigger
③ 可使用 sp_helptext 查看触发器的定义信息；EXEC sp_helptext monitorData_trigger

最新script.sql的修改情况：
为创建任务5的三个视图。
