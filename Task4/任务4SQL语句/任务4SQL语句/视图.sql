USE GardenPlants;
GO

-- ��ͼ1: �鿴ÿ��ҩ���Ӧ�Ĳ��溦
CREATE VIEW MedicinePests AS
SELECT Med.medicin_id, Med.medicine_name, P.pest_id, P.pest_name
FROM medicine Med
JOIN pest_medicine PM ON Med.medicin_id = PM.medicine_id
JOIN pest P ON PM.pest_id = P.pest_id;
GO

-- ��ͼ2: �鿴ÿ��ֲ��Ĳ��溦
CREATE VIEW PlantPests AS
SELECT PP.plant_id, P.pest_id, P.pest_name
FROM plant_pest PP
JOIN pest P ON PP.pest_id = P.pest_id;
GO

-- ��ͼ3: �鿴ÿ�ֲ��溦��ҩ��
CREATE VIEW PestMedicines AS
SELECT P.pest_id, P.pest_name, Med.medicin_id, Med.medicine_name
FROM pest P
JOIN pest_medicine PM ON P.pest_id = PM.pest_id
JOIN medicine Med ON PM.medicine_id = Med.medicin_id;
GO
