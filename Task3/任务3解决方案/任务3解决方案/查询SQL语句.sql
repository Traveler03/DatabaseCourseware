USE GardenPlants;

-- ��ѯ1: ��ȡָ���û�����������
SELECT M.*
FROM Maintenance M
JOIN Maninternance_user MU ON M.task_id = MU.task_id
WHERE MU.user_id = 1;

-- ��ѯ2: ��ȡָ������������û�
SELECT U.*
FROM Maninternance_user U
JOIN Maintenance M ON U.task_id = M.task_id
WHERE M.task_id = 1;

-- ��ѯ3: ��ȡָ��ֲ�����������
SELECT M.*
FROM Maintenance M
JOIN plant_Maintenance PM ON M.task_id = PM.task_id
WHERE PM.plant_id = 1;

-- ��ѯ4: ��ȡָ�����������ֲ��
SELECT P.*
FROM plant_Maintenance P
JOIN Maintenance M ON P.task_id = M.task_id
WHERE M.task_id = 1;

-- ��ѯ5: ��ȡָ���û�������ֲ��
SELECT P.*
FROM plant_Maintenance P
JOIN Maninternance_user MU ON P.task_id = MU.task_id
WHERE MU.user_id = 1;
