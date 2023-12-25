-- 这里表示在哪个数据库下建
USE GardenPlants;

CREATE TABLE Maintenance (
    task_id bigint PRIMARY KEY,
    task_name nvarchar(50),
    time date,
    place nvarchar(50),
    task_des text
);

CREATE TABLE Maninternance_user (
    task_id bigint,
    user_id bigint,
    PRIMARY KEY (task_id, user_id),
    FOREIGN KEY (task_id) REFERENCES Maintenance(task_id)
);

CREATE TABLE plant_Maintenance (
    plant_id bigint,
    task_id bigint,
    PRIMARY KEY (plant_id, task_id),
    FOREIGN KEY (task_id) REFERENCES Maintenance(task_id)
);


