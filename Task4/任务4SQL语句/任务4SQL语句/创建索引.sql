USE GardenPlants;
GO

-- 在病虫害id上创建索引，因为它是我们经常查询和连接的字段
CREATE INDEX idx_pest_id ON pest(pest_id);
GO

CREATE INDEX idx_pest_id ON plant_pest(pest_id);
GO

CREATE INDEX idx_pest_id ON pest_medicine(pest_id);
GO
