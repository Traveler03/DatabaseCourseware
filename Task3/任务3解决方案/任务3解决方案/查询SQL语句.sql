USE GardenPlants;

-- 查询1: 获取指定用户的所有任务
SELECT M.*
FROM Maintenance M
JOIN Maninternance_user MU ON M.task_id = MU.task_id
WHERE MU.user_id = 1;

-- 查询2: 获取指定任务的所有用户
SELECT U.*
FROM Maninternance_user U
JOIN Maintenance M ON U.task_id = M.task_id
WHERE M.task_id = 1;

-- 查询3: 获取指定植物的所有任务
SELECT M.*
FROM Maintenance M
JOIN plant_Maintenance PM ON M.task_id = PM.task_id
WHERE PM.plant_id = 1;

-- 查询4: 获取指定任务的所有植物
SELECT P.*
FROM plant_Maintenance P
JOIN Maintenance M ON P.task_id = M.task_id
WHERE M.task_id = 1;

-- 查询5: 获取指定用户的所有植物
SELECT P.*
FROM plant_Maintenance P
JOIN Maninternance_user MU ON P.task_id = MU.task_id
WHERE MU.user_id = 1;
