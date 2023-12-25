USE GardenPlants;
GO

-- 存储过程: 插入新的病虫害，并分配给指定的药物和植物
CREATE PROCEDURE InsertPest
    @pest_id bigint, 
    @pest_name nvarchar(50), 
    @cm nvarchar(MAX), 
    @medicine_id bigint, 
    @plant_id bigint
AS
BEGIN
    INSERT INTO pest(pest_id, pest_name, cm) VALUES(@pest_id, @pest_name, @cm);
    INSERT INTO pest_medicine(medicine_id, pest_id) VALUES(@medicine_id, @pest_id);
    INSERT INTO plant_pest(plant_id, pest_id) VALUES(@plant_id, @pest_id);
END;
GO
