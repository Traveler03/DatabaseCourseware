-- 使用 GardenPlants 数据库
USE GardenPlants;
GO

-- 存储过程: 插入新的养护任务，并分配给指定的人员和植物
CREATE PROCEDURE InsertMaintenance
    @task_id bigint, 
    @task_name nvarchar(50), 
    @time date, 
    @place nvarchar(50), 
    @task_des text, 
    @user_id bigint, 
    @plant_id bigint
AS
BEGIN
    INSERT INTO Maintenance(task_id, task_name, time, place, task_des) VALUES(@task_id, @task_name, @time, @place, @task_des);
    INSERT INTO Maninternance_user(task_id, user_id) VALUES(@task_id, @user_id);
    INSERT INTO plant_Maintenance(plant_id, task_id) VALUES(@plant_id, @task_id);
END;
GO

/*
-- 插入具体的条目
EXEC InsertMaintenance 1, 'Watering', '2023-12-26', 'Greenhouse', 'Water the plants', 1, 1;
EXEC InsertMaintenance 2, 'Pruning', '2023-12-27', 'Outdoor', 'Prune the plants', 2, 2;
EXEC InsertMaintenance 3, 'Fertilizing', '2023-12-28', 'Indoor', 'Fertilize the plants', 3, 3;
*/