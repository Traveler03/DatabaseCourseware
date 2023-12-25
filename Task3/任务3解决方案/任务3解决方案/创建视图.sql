USE GardenPlants;
GO

-- View 1: ��ȡ����ִ����Ա��Ϣ
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

-- View 2: ��ȡ���񼰹�����ֲ����Ϣ
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

-- View 3: ͳ��ÿ�������漰��ֲ������
CREATE VIEW vw_TaskPlantCount AS
SELECT
    task_id,
    COUNT(plant_id) AS plant_count
FROM
    plant_Maintenance
GROUP BY
    task_id;
GO

-- Procedure: ������񲢷�����Ա
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

    -- �������
    INSERT INTO Maintenance (task_name, time, place, task_des)
    VALUES (@task_name, @time, @place, @task_des);

    -- ��ȡ����������ID
    SET @task_id = SCOPE_IDENTITY();

    -- ������Ա������
    INSERT INTO Maninternance_user (task_id, user_id)
    VALUES (@task_id, @user_id);
END;
GO
