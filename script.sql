USE [master]
GO
/****** Object:  Database [GardenPlants]    Script Date: 2023/12/27 16:45:53 ******/
CREATE DATABASE [GardenPlants]
 CONTAINMENT = NONE
 ON  PRIMARY 
( NAME = N'GardenPlants', FILENAME = N'C:\Program Files\Microsoft SQL Server\MSSQL16.SQLEXPRESS\MSSQL\DATA\GardenPlants.mdf' , SIZE = 8192KB , MAXSIZE = UNLIMITED, FILEGROWTH = 65536KB )
 LOG ON 
( NAME = N'GardenPlants_log', FILENAME = N'C:\Program Files\Microsoft SQL Server\MSSQL16.SQLEXPRESS\MSSQL\DATA\GardenPlants_log.ldf' , SIZE = 8192KB , MAXSIZE = 2048GB , FILEGROWTH = 65536KB )
 WITH CATALOG_COLLATION = DATABASE_DEFAULT, LEDGER = OFF
GO
ALTER DATABASE [GardenPlants] SET COMPATIBILITY_LEVEL = 160
GO
IF (1 = FULLTEXTSERVICEPROPERTY('IsFullTextInstalled'))
begin
EXEC [GardenPlants].[dbo].[sp_fulltext_database] @action = 'enable'
end
GO
ALTER DATABASE [GardenPlants] SET ANSI_NULL_DEFAULT OFF 
GO
ALTER DATABASE [GardenPlants] SET ANSI_NULLS OFF 
GO
ALTER DATABASE [GardenPlants] SET ANSI_PADDING OFF 
GO
ALTER DATABASE [GardenPlants] SET ANSI_WARNINGS OFF 
GO
ALTER DATABASE [GardenPlants] SET ARITHABORT OFF 
GO
ALTER DATABASE [GardenPlants] SET AUTO_CLOSE OFF 
GO
ALTER DATABASE [GardenPlants] SET AUTO_SHRINK OFF 
GO
ALTER DATABASE [GardenPlants] SET AUTO_UPDATE_STATISTICS ON 
GO
ALTER DATABASE [GardenPlants] SET CURSOR_CLOSE_ON_COMMIT OFF 
GO
ALTER DATABASE [GardenPlants] SET CURSOR_DEFAULT  GLOBAL 
GO
ALTER DATABASE [GardenPlants] SET CONCAT_NULL_YIELDS_NULL OFF 
GO
ALTER DATABASE [GardenPlants] SET NUMERIC_ROUNDABORT OFF 
GO
ALTER DATABASE [GardenPlants] SET QUOTED_IDENTIFIER OFF 
GO
ALTER DATABASE [GardenPlants] SET RECURSIVE_TRIGGERS OFF 
GO
ALTER DATABASE [GardenPlants] SET  DISABLE_BROKER 
GO
ALTER DATABASE [GardenPlants] SET AUTO_UPDATE_STATISTICS_ASYNC OFF 
GO
ALTER DATABASE [GardenPlants] SET DATE_CORRELATION_OPTIMIZATION OFF 
GO
ALTER DATABASE [GardenPlants] SET TRUSTWORTHY OFF 
GO
ALTER DATABASE [GardenPlants] SET ALLOW_SNAPSHOT_ISOLATION OFF 
GO
ALTER DATABASE [GardenPlants] SET PARAMETERIZATION SIMPLE 
GO
ALTER DATABASE [GardenPlants] SET READ_COMMITTED_SNAPSHOT OFF 
GO
ALTER DATABASE [GardenPlants] SET HONOR_BROKER_PRIORITY OFF 
GO
ALTER DATABASE [GardenPlants] SET RECOVERY SIMPLE 
GO
ALTER DATABASE [GardenPlants] SET  MULTI_USER 
GO
ALTER DATABASE [GardenPlants] SET PAGE_VERIFY CHECKSUM  
GO
ALTER DATABASE [GardenPlants] SET DB_CHAINING OFF 
GO
ALTER DATABASE [GardenPlants] SET FILESTREAM( NON_TRANSACTED_ACCESS = OFF ) 
GO
ALTER DATABASE [GardenPlants] SET TARGET_RECOVERY_TIME = 60 SECONDS 
GO
ALTER DATABASE [GardenPlants] SET DELAYED_DURABILITY = DISABLED 
GO
ALTER DATABASE [GardenPlants] SET ACCELERATED_DATABASE_RECOVERY = OFF  
GO
ALTER DATABASE [GardenPlants] SET QUERY_STORE = ON
GO
ALTER DATABASE [GardenPlants] SET QUERY_STORE (OPERATION_MODE = READ_WRITE, CLEANUP_POLICY = (STALE_QUERY_THRESHOLD_DAYS = 30), DATA_FLUSH_INTERVAL_SECONDS = 900, INTERVAL_LENGTH_MINUTES = 60, MAX_STORAGE_SIZE_MB = 1000, QUERY_CAPTURE_MODE = AUTO, SIZE_BASED_CLEANUP_MODE = AUTO, MAX_PLANS_PER_QUERY = 200, WAIT_STATS_CAPTURE_MODE = ON)
GO
USE [GardenPlants]
GO
/****** Object:  Table [dbo].[Maintenance]    Script Date: 2023/12/27 16:45:53 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Maintenance](
	[task_id] [bigint] IDENTITY(1,1) NOT NULL,
	[task_name] [nvarchar](50) NOT NULL,
	[time] [date] NULL,
	[place] [nvarchar](50) NULL,
	[task_des] [nvarchar](max) NULL,
 CONSTRAINT [PK_Maintenance] PRIMARY KEY CLUSTERED 
(
	[task_id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Maninternance_user]    Script Date: 2023/12/27 16:45:53 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Maninternance_user](
	[task_id] [bigint] NOT NULL,
	[user_id] [bigint] NOT NULL,
 CONSTRAINT [PK_Maninternance_user] PRIMARY KEY CLUSTERED 
(
	[task_id] ASC,
	[user_id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  View [dbo].[vw_TaskWithUsers]    Script Date: 2023/12/27 16:45:53 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO

-- View 1: 获取任务及执行人员信息
CREATE VIEW [dbo].[vw_TaskWithUsers] AS
SELECT
    m.task_id,
    m.task_name,
    m.time,
    m.place,
    m.task_des,
    u.user_id
FROM
    Maintenance AS m
JOIN
    Maninternance_user AS u ON m.task_id = u.task_id;

GO
/****** Object:  Table [dbo].[plant_Manintenance]    Script Date: 2023/12/27 16:45:53 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[plant_Manintenance](
	[plant_id] [bigint] NOT NULL,
	[task_id] [bigint] NOT NULL,
 CONSTRAINT [PK_plant_Manintenance] PRIMARY KEY CLUSTERED 
(
	[plant_id] ASC,
	[task_id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  View [dbo].[vw_TaskWithPlants]    Script Date: 2023/12/27 16:45:53 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO

-- View 2: 获取任务及关联的植物信息
CREATE VIEW [dbo].[vw_TaskWithPlants] AS
SELECT
    m.task_id,
    m.task_name,
    m.time,
    m.place,
    m.task_des,
    p.plant_id
FROM
    Maintenance AS m
JOIN
    plant_Manintenance AS p ON m.task_id = p.task_id;

GO
/****** Object:  View [dbo].[vw_TaskPlantCount]    Script Date: 2023/12/27 16:45:53 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO

-- View 3: 统计每个任务涉及的植物数量
CREATE VIEW [dbo].[vw_TaskPlantCount] AS
SELECT
    task_id,
    COUNT(plant_id) AS plant_count
FROM
    plant_Manintenance
GROUP BY
    task_id;

GO
/****** Object:  Table [dbo].[Pest]    Script Date: 2023/12/27 16:45:53 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Pest](
	[pest_id] [bigint] IDENTITY(1,1) NOT NULL,
	[pest_name] [nvarchar](50) NOT NULL,
	[cm] [nvarchar](max) NULL,
 CONSTRAINT [PK_Pest_manage] PRIMARY KEY CLUSTERED 
(
	[pest_id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
/****** Object:  Table [dbo].[medicine]    Script Date: 2023/12/27 16:45:53 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[medicine](
	[medicine_id] [bigint] IDENTITY(1,1) NOT NULL,
	[medicine_name] [nvarchar](50) NOT NULL,
	[duration] [nvarchar](50) NULL,
 CONSTRAINT [PK_medicine] PRIMARY KEY CLUSTERED 
(
	[medicine_id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[pest_medicine]    Script Date: 2023/12/27 16:45:53 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[pest_medicine](
	[medicine_id] [bigint] NOT NULL,
	[pest_id] [bigint] NOT NULL,
	[Dosage] [nvarchar](50) NOT NULL,
 CONSTRAINT [PK_use_medicine] PRIMARY KEY CLUSTERED 
(
	[medicine_id] ASC,
	[pest_id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  View [dbo].[MedicinePests]    Script Date: 2023/12/27 16:45:53 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO

-- 视图1: 查看每种药物对应的病虫害
CREATE VIEW [dbo].[MedicinePests] AS
SELECT Med.medicine_id, Med.medicine_name, P.pest_id, P.pest_name
FROM medicine Med
JOIN pest_medicine PM ON Med.medicine_id = PM.medicine_id
JOIN pest P ON PM.pest_id = P.pest_id;

GO
/****** Object:  Table [dbo].[plant_pest]    Script Date: 2023/12/27 16:45:53 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[plant_pest](
	[plant_id] [bigint] NOT NULL,
	[pest_id] [bigint] NOT NULL,
 CONSTRAINT [PK_sicken] PRIMARY KEY CLUSTERED 
(
	[plant_id] ASC,
	[pest_id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  View [dbo].[PlantPests]    Script Date: 2023/12/27 16:45:53 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO

-- 视图2: 查看每种植物的病虫害
CREATE VIEW [dbo].[PlantPests] AS
SELECT PP.plant_id, P.pest_id, P.pest_name
FROM plant_pest PP
JOIN pest P ON PP.pest_id = P.pest_id;

GO
/****** Object:  View [dbo].[PestMedicines]    Script Date: 2023/12/27 16:45:53 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO

-- 视图3: 查看每种病虫害的药物
CREATE VIEW [dbo].[PestMedicines] AS
SELECT P.pest_id, P.pest_name, Med.medicine_id, Med.medicine_name
FROM pest P
JOIN pest_medicine PM ON P.pest_id = PM.pest_id
JOIN medicine Med ON PM.medicine_id = Med.medicine_id;

GO
/****** Object:  Table [dbo].[Plant]    Script Date: 2023/12/27 16:45:53 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Plant](
	[plant_id] [bigint] IDENTITY(1,1) NOT NULL,
	[species_name] [nvarchar](50) NOT NULL,
	[alia] [nvarchar](max) NULL,
	[morphology] [nvarchar](max) NULL,
	[value] [nvarchar](max) NULL,
	[key_tech] [nvarchar](max) NULL,
	[environment] [nvarchar](max) NULL,
	[created_by] [nvarchar](50) NULL,
	[created_at] [date] NULL,
	[updated_at] [date] NULL,
 CONSTRAINT [PK_Plant_information] PRIMARY KEY CLUSTERED 
(
	[plant_id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
/****** Object:  Table [dbo].[plant_class]    Script Date: 2023/12/27 16:45:53 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[plant_class](
	[plant_id] [bigint] NOT NULL,
	[class_id] [bigint] NOT NULL,
 CONSTRAINT [PK_plant_class] PRIMARY KEY CLUSTERED 
(
	[plant_id] ASC,
	[class_id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[classes]    Script Date: 2023/12/27 16:45:53 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[classes](
	[class_id] [bigint] IDENTITY(1,1) NOT NULL,
	[parent] [bigint] NULL,
	[rank] [int] NULL,
	[class_name] [nvarchar](50) NULL,
 CONSTRAINT [PK_classes] PRIMARY KEY CLUSTERED 
(
	[class_id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[plant_region]    Script Date: 2023/12/27 16:45:53 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[plant_region](
	[plant_id] [bigint] NOT NULL,
	[region_id] [bigint] NOT NULL,
 CONSTRAINT [PK_plant_region] PRIMARY KEY CLUSTERED 
(
	[plant_id] ASC,
	[region_id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[region]    Script Date: 2023/12/27 16:45:53 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[region](
	[region_id] [bigint] IDENTITY(1,1) NOT NULL,
	[parent] [bigint] NULL,
	[rank] [int] NULL,
	[region_name] [nvarchar](50) NULL,
 CONSTRAINT [PK_region] PRIMARY KEY CLUSTERED 
(
	[region_id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  View [dbo].[plant_view]    Script Date: 2023/12/27 16:45:53 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE VIEW [dbo].[plant_view] AS
SELECT 
    plant.plant_id,
    c1.class_name AS shuming,
    c2.class_name AS keming,
    plant.species_name,
    Plant.environment,
    r1.region_name AS province,
    r2.region_name AS city,
    r3.region_name AS county
FROM 
    classes c1
JOIN 
    plant_class ON (c1.class_id = plant_class.class_id)
JOIN 
    Plant ON (plant.plant_id = plant_class.plant_id)
JOIN 
    classes c2 ON (c1.parent = c2.class_id)
LEFT JOIN 
    plant_region ON (plant.plant_id = plant_region.plant_id)
LEFT JOIN 
    region r3 ON (plant_region.region_id = r3.region_id)
LEFT JOIN 
    region r2 ON (r3.parent = r2.region_id)
LEFT JOIN 
    region r1 ON (r2.parent = r1.region_id)
GO
/****** Object:  View [dbo].[View_60]    Script Date: 2023/12/27 16:45:53 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE VIEW [dbo].[View_60] AS 
        SELECT DISTINCT 
            plant.plant_id,
            species_name,
            c1.class_name AS keming,
            c2.class_name AS shuming,
            Plant.alia, 
            plant.key_tech,
            plant.morphology,
            plant.value,
            plant.created_by,
            plant.created_at,
            plant.updated_at 
        FROM 
            classes c1,
            classes c2,
            plant_class,
            Plant,
            Pest,
            plant_pest 
        WHERE 
            plant.plant_id=plant_class.plant_id 
            AND plant_class.class_id=c2.class_id 
            AND c1.class_id=(SELECT c2.parent) 
            AND c1.class_id= 60
GO
/****** Object:  View [dbo].[View_61]    Script Date: 2023/12/27 16:45:53 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE VIEW [dbo].[View_61] AS 
        SELECT DISTINCT 
            plant.plant_id,
            species_name,
            c1.class_name AS keming,
            c2.class_name AS shuming,
            Plant.alia, 
            plant.key_tech,
            plant.morphology,
            plant.value,
            plant.created_by,
            plant.created_at,
            plant.updated_at 
        FROM 
            classes c1,
            classes c2,
            plant_class,
            Plant,
            Pest,
            plant_pest 
        WHERE 
            plant.plant_id=plant_class.plant_id 
            AND plant_class.class_id=c2.class_id 
            AND c1.class_id=(SELECT c2.parent) 
            AND c1.class_id= 61
GO
/****** Object:  View [dbo].[View_62]    Script Date: 2023/12/27 16:45:53 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE VIEW [dbo].[View_62] AS 
        SELECT DISTINCT 
            plant.plant_id,
            species_name,
            c1.class_name AS keming,
            c2.class_name AS shuming,
            Plant.alia, 
            plant.key_tech,
            plant.morphology,
            plant.value,
            plant.created_by,
            plant.created_at,
            plant.updated_at 
        FROM 
            classes c1,
            classes c2,
            plant_class,
            Plant,
            Pest,
            plant_pest 
        WHERE 
            plant.plant_id=plant_class.plant_id 
            AND plant_class.class_id=c2.class_id 
            AND c1.class_id=(SELECT c2.parent) 
            AND c1.class_id= 62
GO
/****** Object:  View [dbo].[View_1]    Script Date: 2023/12/27 16:45:53 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
create view [dbo].[View_1] as select DISTINCT plant.plant_id,species_name,c1.class_name as keming,c2.class_name as shuming,Plant.alia,
        plant.key_tech,plant.morphology,plant.value,plant.created_by,plant.created_at,
        plant.updated_at from classes c1,classes c2,plant_class,Plant,Pest,plant_pest
        where plant.plant_id=plant_class.plant_id and plant_class.class_id=c2.class_id
        and c1.class_id=(select c2.parent ) and c1.class_id=1
GO
/****** Object:  Table [dbo].[monitorData]    Script Date: 2023/12/27 16:45:53 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[monitorData](
	[monitor_id] [bigint] NOT NULL,
	[monitor_region] [nvarchar](50) NOT NULL,
	[monitor_time] [date] NOT NULL,
	[plant_id] [bigint] NOT NULL,
	[monitor_temp] [float] NULL,
	[monitor_grow] [nvarchar](50) NULL,
	[monitor_illu] [nvarchar](50) NULL,
 CONSTRAINT [PK_monitorData] PRIMARY KEY CLUSTERED 
(
	[monitor_id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  View [dbo].[monitorData_plant]    Script Date: 2023/12/27 16:45:53 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE VIEW [dbo].[monitorData_plant] AS
SELECT monitorData.*, plant.species_name, plant.alia
FROM monitorData
JOIN plant ON monitorData.plant_id = plant.plant_id;
GO
/****** Object:  Table [dbo].[equipment]    Script Date: 2023/12/27 16:45:53 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[equipment](
	[equipment_id] [bigint] IDENTITY(1,1) NOT NULL,
	[equipment_name] [nchar](50) NOT NULL,
 CONSTRAINT [PK_equipment] PRIMARY KEY CLUSTERED 
(
	[equipment_id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[equipment_metrics]    Script Date: 2023/12/27 16:45:53 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[equipment_metrics](
	[equipment_id] [bigint] NOT NULL,
	[metrics_ip] [bigint] NOT NULL,
 CONSTRAINT [PK_equipment_metrics_1] PRIMARY KEY CLUSTERED 
(
	[equipment_id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  View [dbo].[metrics_equipment]    Script Date: 2023/12/27 16:45:53 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE VIEW [dbo].[metrics_equipment] AS
SELECT equipment_metrics.*, equipment.equipment_name
FROM equipment_metrics
JOIN equipment ON equipment_metrics.equipment_id = equipment.equipment_id;
GO
/****** Object:  Table [dbo].[metrics]    Script Date: 2023/12/27 16:45:53 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[metrics](
	[metrics_ip] [bigint] IDENTITY(1,1) NOT NULL,
	[illumination] [int] NULL,
	[temperature] [int] NULL,
	[grow] [int] NULL,
 CONSTRAINT [PK_metrics] PRIMARY KEY CLUSTERED 
(
	[metrics_ip] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[plant_metrics]    Script Date: 2023/12/27 16:45:53 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[plant_metrics](
	[plant_id] [bigint] NOT NULL,
	[metrics_ip] [bigint] NOT NULL,
 CONSTRAINT [PK_plant_metrics_1] PRIMARY KEY CLUSTERED 
(
	[plant_id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  View [dbo].[metrics_plant]    Script Date: 2023/12/27 16:45:53 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE VIEW [dbo].[metrics_plant] AS
SELECT plant.plant_id, plant.species_name, plant.alia, metrics.*
FROM plant
JOIN dbo.plant_metrics ON plant.plant_id = dbo.plant_metrics.plant_id
JOIN metrics ON dbo.plant_metrics.metrics_ip = metrics.metrics_ip;
GO
/****** Object:  Table [dbo].[equipment_plant]    Script Date: 2023/12/27 16:45:53 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[equipment_plant](
	[equipment_id] [bigint] NOT NULL,
	[plant_id] [bigint] NOT NULL,
 CONSTRAINT [PK_equipment_plant_1] PRIMARY KEY CLUSTERED 
(
	[plant_id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[ExceptionLog]    Script Date: 2023/12/27 16:45:53 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[ExceptionLog](
	[monitor_id] [bigint] NOT NULL,
	[exception_detail] [nvarchar](255) NOT NULL,
 CONSTRAINT [PK_ExceptionLog] PRIMARY KEY CLUSTERED 
(
	[monitor_id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[fig]    Script Date: 2023/12/27 16:45:53 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[fig](
	[fig_id] [bigint] IDENTITY(1,1) NOT NULL,
	[fig_path] [nvarchar](50) NOT NULL,
	[fig_place] [nvarchar](50) NULL,
	[fig_people] [nvarchar](50) NULL,
	[fig_des] [nvarchar](max) NULL,
	[created_by] [nvarchar](50) NULL,
	[creater_at] [date] NULL,
	[updated_at] [date] NULL,
 CONSTRAINT [PK_fig] PRIMARY KEY CLUSTERED 
(
	[fig_id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
/****** Object:  Table [dbo].[plant_fig]    Script Date: 2023/12/27 16:45:53 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[plant_fig](
	[plant_id] [bigint] NOT NULL,
	[fig_id] [bigint] NOT NULL,
 CONSTRAINT [PK_plant_fig] PRIMARY KEY CLUSTERED 
(
	[plant_id] ASC,
	[fig_id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[plantThreshold]    Script Date: 2023/12/27 16:45:53 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[plantThreshold](
	[plant_id] [bigint] NOT NULL,
	[maxtemp] [float] NOT NULL,
	[mintemp] [float] NOT NULL,
	[maxgrow] [nvarchar](50) NOT NULL,
	[mingrow] [nvarchar](50) NOT NULL,
	[maxillu] [nvarchar](50) NOT NULL,
	[minillu] [nvarchar](50) NOT NULL,
 CONSTRAINT [PK_plantThreshold] PRIMARY KEY CLUSTERED 
(
	[plant_id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[users]    Script Date: 2023/12/27 16:45:53 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[users](
	[user_id] [bigint] IDENTITY(1,1) NOT NULL,
	[user_name] [nvarchar](50) NOT NULL,
	[password] [nvarchar](50) NOT NULL,
	[posts] [nvarchar](50) NOT NULL,
 CONSTRAINT [PK_user] PRIMARY KEY CLUSTERED 
(
	[user_id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
SET ANSI_PADDING ON
GO
/****** Object:  Index [index_class]    Script Date: 2023/12/27 16:45:54 ******/
CREATE NONCLUSTERED INDEX [index_class] ON [dbo].[classes]
(
	[class_name] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, DROP_EXISTING = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
GO
/****** Object:  Index [idx_task_id]    Script Date: 2023/12/27 16:45:54 ******/
CREATE NONCLUSTERED INDEX [idx_task_id] ON [dbo].[Maintenance]
(
	[task_id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, DROP_EXISTING = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
GO
/****** Object:  Index [idx_task_id]    Script Date: 2023/12/27 16:45:54 ******/
CREATE NONCLUSTERED INDEX [idx_task_id] ON [dbo].[Maninternance_user]
(
	[task_id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, DROP_EXISTING = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
GO
/****** Object:  Index [idx_pest_id]    Script Date: 2023/12/27 16:45:54 ******/
CREATE NONCLUSTERED INDEX [idx_pest_id] ON [dbo].[Pest]
(
	[pest_id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, DROP_EXISTING = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
GO
/****** Object:  Index [idx_pest_id]    Script Date: 2023/12/27 16:45:54 ******/
CREATE NONCLUSTERED INDEX [idx_pest_id] ON [dbo].[pest_medicine]
(
	[pest_id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, DROP_EXISTING = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
GO
SET ANSI_PADDING ON
GO
/****** Object:  Index [index_plant]    Script Date: 2023/12/27 16:45:54 ******/
CREATE NONCLUSTERED INDEX [index_plant] ON [dbo].[Plant]
(
	[species_name] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, DROP_EXISTING = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
GO
/****** Object:  Index [idx_task_id]    Script Date: 2023/12/27 16:45:54 ******/
CREATE NONCLUSTERED INDEX [idx_task_id] ON [dbo].[plant_Manintenance]
(
	[task_id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, DROP_EXISTING = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
GO
/****** Object:  Index [idx_pest_id]    Script Date: 2023/12/27 16:45:54 ******/
CREATE NONCLUSTERED INDEX [idx_pest_id] ON [dbo].[plant_pest]
(
	[pest_id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, DROP_EXISTING = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
GO
ALTER TABLE [dbo].[monitorData]  WITH CHECK ADD  CONSTRAINT [FK_monitorData_Plant] FOREIGN KEY([monitor_id])
REFERENCES [dbo].[Plant] ([plant_id])
GO
ALTER TABLE [dbo].[monitorData] CHECK CONSTRAINT [FK_monitorData_Plant]
GO
ALTER TABLE [dbo].[plant_class]  WITH CHECK ADD  CONSTRAINT [FK_plant_class_classes] FOREIGN KEY([class_id])
REFERENCES [dbo].[classes] ([class_id])
GO
ALTER TABLE [dbo].[plant_class] CHECK CONSTRAINT [FK_plant_class_classes]
GO
ALTER TABLE [dbo].[plant_class]  WITH CHECK ADD  CONSTRAINT [FK_plant_class_Plant] FOREIGN KEY([plant_id])
REFERENCES [dbo].[Plant] ([plant_id])
GO
ALTER TABLE [dbo].[plant_class] CHECK CONSTRAINT [FK_plant_class_Plant]
GO
ALTER TABLE [dbo].[plant_fig]  WITH CHECK ADD  CONSTRAINT [FK_plant_fig_fig] FOREIGN KEY([fig_id])
REFERENCES [dbo].[fig] ([fig_id])
GO
ALTER TABLE [dbo].[plant_fig] CHECK CONSTRAINT [FK_plant_fig_fig]
GO
ALTER TABLE [dbo].[plant_fig]  WITH CHECK ADD  CONSTRAINT [FK_plant_fig_Plant] FOREIGN KEY([plant_id])
REFERENCES [dbo].[Plant] ([plant_id])
GO
ALTER TABLE [dbo].[plant_fig] CHECK CONSTRAINT [FK_plant_fig_Plant]
GO
ALTER TABLE [dbo].[plant_pest]  WITH CHECK ADD  CONSTRAINT [FK_plant_pest_Pest] FOREIGN KEY([pest_id])
REFERENCES [dbo].[Pest] ([pest_id])
GO
ALTER TABLE [dbo].[plant_pest] CHECK CONSTRAINT [FK_plant_pest_Pest]
GO
ALTER TABLE [dbo].[plant_pest]  WITH CHECK ADD  CONSTRAINT [FK_plant_pest_Plant] FOREIGN KEY([plant_id])
REFERENCES [dbo].[Plant] ([plant_id])
GO
ALTER TABLE [dbo].[plant_pest] CHECK CONSTRAINT [FK_plant_pest_Plant]
GO
ALTER TABLE [dbo].[plant_region]  WITH CHECK ADD  CONSTRAINT [FK_plant_region_Plant] FOREIGN KEY([plant_id])
REFERENCES [dbo].[Plant] ([plant_id])
GO
ALTER TABLE [dbo].[plant_region] CHECK CONSTRAINT [FK_plant_region_Plant]
GO
ALTER TABLE [dbo].[plant_region]  WITH CHECK ADD  CONSTRAINT [FK_plant_region_region] FOREIGN KEY([region_id])
REFERENCES [dbo].[region] ([region_id])
GO
ALTER TABLE [dbo].[plant_region] CHECK CONSTRAINT [FK_plant_region_region]
GO
/****** Object:  StoredProcedure [dbo].[InsertMaintenance]    Script Date: 2023/12/27 16:45:54 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO

-- 存储过程: 插入新的养护任务，并分配给指定的人员和植物
CREATE PROCEDURE [dbo].[InsertMaintenance]
    @task_id bigint, 
    @task_name nvarchar(50), 
    @time date, 
    @place nvarchar(50), 
    @task_des text, 
    @user_id bigint, 
    @plant_id bigint
AS
BEGIN
    INSERT INTO Maintenance(task_id, task_name, time, place, task_des) VALUES(@task_id, @task_name, @time, @place, @task_des);
    INSERT INTO Maninternance_user(task_id, user_id) VALUES(@task_id, @user_id);
    INSERT INTO plant_Manintenance(plant_id, task_id) VALUES(@plant_id, @task_id);
END;

GO
/****** Object:  StoredProcedure [dbo].[InsertPest]    Script Date: 2023/12/27 16:45:54 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO

-- 存储过程: 插入新的病虫害，并分配给指定的药物和植物
CREATE PROCEDURE [dbo].[InsertPest]
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
/****** Object:  StoredProcedure [dbo].[sp_AddTaskWithUsers]    Script Date: 2023/12/27 16:45:54 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO

-- Procedure: 添加任务并分配人员
CREATE PROCEDURE [dbo].[sp_AddTaskWithUsers](
    @task_name NVARCHAR(50),
    @time DATE,
    @place NVARCHAR(50),
    @task_des TEXT,
    @user_id BIGINT
)
AS
BEGIN
    DECLARE @task_id BIGINT;

    -- 添加任务
    INSERT INTO Maintenance (task_name, time, place, task_des)
    VALUES (@task_name, @time, @place, @task_des);

    -- 获取新添加任务的ID
    SET @task_id = SCOPE_IDENTITY();

    -- 分配人员给任务
    INSERT INTO Maninternance_user (task_id, user_id)
    VALUES (@task_id, @user_id);
END;

GO
USE [master]
GO
ALTER DATABASE [GardenPlants] SET  READ_WRITE 
GO
