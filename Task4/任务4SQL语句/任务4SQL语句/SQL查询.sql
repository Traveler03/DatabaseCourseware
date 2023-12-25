USE GardenPlants;
GO

-- ��ѯ1: ��ȡָ��ҩ������в��溦
SELECT P.*
FROM pest P
JOIN pest_medicine PM ON P.pest_id = PM.pest_id
WHERE PM.medicine_id = 1;
GO

-- ��ѯ2: ��ȡָ�����溦������ҩ��
SELECT Med.*
FROM medicine Med
JOIN pest_medicine PM ON Med.medicin_id = PM.medicine_id
WHERE PM.pest_id = 1;
GO

-- ��ѯ3: ��ȡָ��ֲ������в��溦
SELECT P.*
FROM pest P
JOIN plant_pest PP ON P.pest_id = PP.pest_id
WHERE PP.plant_id = 1;
GO

-- ��ѯ4: ��ȡָ�����溦������ֲ��
SELECT PP.*
FROM plant_pest PP
JOIN pest P ON PP.pest_id = P.pest_id
WHERE P.pest_id = 1;
GO

-- ��ѯ5: ��ȡָ��ҩ�������ֲ��
SELECT PP.*
FROM plant_pest PP
JOIN pest_medicine PM ON PP.pest_id = PM.pest_id
WHERE PM.medicine_id = 1;
GO
