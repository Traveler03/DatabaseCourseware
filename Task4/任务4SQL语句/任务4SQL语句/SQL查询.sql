USE GardenPlants;
GO

-- 查询1: 获取指定药物的所有病虫害
SELECT P.*
FROM pest P
JOIN pest_medicine PM ON P.pest_id = PM.pest_id
WHERE PM.medicine_id = 1;
GO

-- 查询2: 获取指定病虫害的所有药物
SELECT Med.*
FROM medicine Med
JOIN pest_medicine PM ON Med.medicin_id = PM.medicine_id
WHERE PM.pest_id = 1;
GO

-- 查询3: 获取指定植物的所有病虫害
SELECT P.*
FROM pest P
JOIN plant_pest PP ON P.pest_id = PP.pest_id
WHERE PP.plant_id = 1;
GO

-- 查询4: 获取指定病虫害的所有植物
SELECT PP.*
FROM plant_pest PP
JOIN pest P ON PP.pest_id = P.pest_id
WHERE P.pest_id = 1;
GO

-- 查询5: 获取指定药物的所有植物
SELECT PP.*
FROM plant_pest PP
JOIN pest_medicine PM ON PP.pest_id = PM.pest_id
WHERE PM.medicine_id = 1;
GO
