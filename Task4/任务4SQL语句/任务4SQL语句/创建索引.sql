USE GardenPlants;
GO

-- �ڲ��溦id�ϴ�����������Ϊ�������Ǿ�����ѯ�����ӵ��ֶ�
CREATE INDEX idx_pest_id ON pest(pest_id);
GO

CREATE INDEX idx_pest_id ON plant_pest(pest_id);
GO

CREATE INDEX idx_pest_id ON pest_medicine(pest_id);
GO
