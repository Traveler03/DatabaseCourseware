USE GardenPlants;
GO

-- View 1: 获取任务及执行人员信息
CREATE VIEW vw_TaskWithUsers AS
SELECT
    m.task_id,
    m.task_name,
    m.time,
    m.place,
    m.task_des,
    u.user_id
FROM
    Maintenance AS m
JOIN
    Maninternance_user AS u ON m.task_id = u.task_id;
GO

-- View 2: 获取任务及关联的植物信息
CREATE VIEW vw_TaskWithPlants AS
SELECT
    m.task_id,
    m.task_name,
    m.time,
    m.place,
    m.task_des,
    p.plant_id
FROM
    Maintenance AS m
JOIN
    plant_Maintenance AS p ON m.task_id = p.task_id;
GO

-- View 3: 统计每个任务涉及的植物数量
CREATE VIEW vw_TaskPlantCount AS
SELECT
    task_id,
    COUNT(plant_id) AS plant_count
FROM
    plant_Maintenance
GROUP BY
    task_id;
GO

-- Procedure: 添加任务并分配人员
CREATE PROCEDURE sp_AddTaskWithUsers(
    @task_name NVARCHAR(50),
    @time DATE,
    @place NVARCHAR(50),
    @task_des TEXT,
    @user_id BIGINT
)
AS
BEGIN
    DECLARE @task_id BIGINT;

    -- 添加任务
    INSERT INTO Maintenance (task_name, time, place, task_des)
    VALUES (@task_name, @time, @place, @task_des);

    -- 获取新添加任务的ID
    SET @task_id = SCOPE_IDENTITY();

    -- 分配人员给任务
    INSERT INTO Maninternance_user (task_id, user_id)
    VALUES (@task_id, @user_id);
END;
GO
