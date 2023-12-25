USE GardenPlants;
-- 在任务id上创建索引，因为它是我们经常查询和连接的字段
CREATE INDEX idx_task_id ON Maintenance(task_id);
CREATE INDEX idx_task_id ON Maninternance_user(task_id);
CREATE INDEX idx_task_id ON plant_Maintenance(task_id);
