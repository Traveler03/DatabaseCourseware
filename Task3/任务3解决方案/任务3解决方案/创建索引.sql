USE GardenPlants;
-- ������id�ϴ�����������Ϊ�������Ǿ�����ѯ�����ӵ��ֶ�
CREATE INDEX idx_task_id ON Maintenance(task_id);
CREATE INDEX idx_task_id ON Maninternance_user(task_id);
CREATE INDEX idx_task_id ON plant_Maintenance(task_id);
