USE GardenPlants;

CREATE TABLE plant (
    plant_id BIGINT PRIMARY KEY,
    alia NVARCHAR(MAX),
    species_name NVARCHAR(50),
    morphology NVARCHAR(MAX),
    value NVARCHAR(MAX),
    key_tech NVARCHAR(MAX),
    environment NVARCHAR(MAX),
    created_by NVARCHAR(50),
    created_at DATE,
    updated_at DATE
);

CREATE TABLE pest (
    pest_id BIGINT PRIMARY KEY,
    pest_name NVARCHAR(50),
    cm NVARCHAR(MAX)
);

CREATE TABLE medicine (
    medicin_id BIGINT PRIMARY KEY,
    medicine_name NVARCHAR(50),
    duration NVARCHAR(50)
);

CREATE TABLE plant_pest (
    plant_id BIGINT,
    pest_id BIGINT,
    PRIMARY KEY (plant_id, pest_id),
    FOREIGN KEY (plant_id) REFERENCES plant(plant_id),
    FOREIGN KEY (pest_id) REFERENCES pest(pest_id)
);

CREATE TABLE pest_medicine (
    medicine_id BIGINT,
    pest_id BIGINT,
    Dosage NVARCHAR(50),
    PRIMARY KEY (medicine_id, pest_id),
    FOREIGN KEY (medicine_id) REFERENCES medicine(medicin_id),
    FOREIGN KEY (pest_id) REFERENCES pest(pest_id)
);