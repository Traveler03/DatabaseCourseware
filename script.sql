USE [master]
GO
/****** Object:  Database [GardenPlants]    Script Date: 2023/12/24 19:57:44 ******/
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
/****** Object:  Table [dbo].[Plant]    Script Date: 2023/12/24 19:57:44 ******/
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
/****** Object:  Table [dbo].[Pest]    Script Date: 2023/12/24 19:57:44 ******/
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
/****** Object:  Table [dbo].[plant_class]    Script Date: 2023/12/24 19:57:44 ******/
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
/****** Object:  Table [dbo].[plant_pest]    Script Date: 2023/12/24 19:57:44 ******/
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
/****** Object:  Table [dbo].[classes]    Script Date: 2023/12/24 19:57:44 ******/
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
/****** Object:  View [dbo].[View_60]    Script Date: 2023/12/24 19:57:44 ******/
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
/****** Object:  View [dbo].[View_61]    Script Date: 2023/12/24 19:57:44 ******/
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
/****** Object:  View [dbo].[View_62]    Script Date: 2023/12/24 19:57:44 ******/
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
/****** Object:  View [dbo].[View_1]    Script Date: 2023/12/24 19:57:44 ******/
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
/****** Object:  Table [dbo].[equipment]    Script Date: 2023/12/24 19:57:44 ******/
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
/****** Object:  Table [dbo].[equipment_metrics]    Script Date: 2023/12/24 19:57:44 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[equipment_metrics](
	[equipment_id] [bigint] NOT NULL,
	[metrics_ip] [bigint] NOT NULL,
 CONSTRAINT [PK_equipment_metrics] PRIMARY KEY CLUSTERED 
(
	[equipment_id] ASC,
	[metrics_ip] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[equipment_plant]    Script Date: 2023/12/24 19:57:44 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[equipment_plant](
	[equipment_id] [bigint] NOT NULL,
	[plant_id] [bigint] NOT NULL,
 CONSTRAINT [PK_equipment_plant] PRIMARY KEY CLUSTERED 
(
	[equipment_id] ASC,
	[plant_id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[ExceptionLog]    Script Date: 2023/12/24 19:57:44 ******/
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
/****** Object:  Table [dbo].[fig]    Script Date: 2023/12/24 19:57:44 ******/
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
/****** Object:  Table [dbo].[Maintenance]    Script Date: 2023/12/24 19:57:44 ******/
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
/****** Object:  Table [dbo].[Maninternance_user]    Script Date: 2023/12/24 19:57:44 ******/
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
/****** Object:  Table [dbo].[medicine]    Script Date: 2023/12/24 19:57:44 ******/
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
/****** Object:  Table [dbo].[metrics]    Script Date: 2023/12/24 19:57:44 ******/
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
/****** Object:  Table [dbo].[monitorData]    Script Date: 2023/12/24 19:57:44 ******/
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
/****** Object:  Table [dbo].[pest_medicine]    Script Date: 2023/12/24 19:57:44 ******/
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
/****** Object:  Table [dbo].[plant_fig]    Script Date: 2023/12/24 19:57:44 ******/
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
/****** Object:  Table [dbo].[plant_Manintenance]    Script Date: 2023/12/24 19:57:44 ******/
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
/****** Object:  Table [dbo].[plant_metrics]    Script Date: 2023/12/24 19:57:44 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[plant_metrics](
	[plant_id] [bigint] NOT NULL,
	[metrics_ip] [bigint] NOT NULL,
 CONSTRAINT [PK_plant_metrics] PRIMARY KEY CLUSTERED 
(
	[plant_id] ASC,
	[metrics_ip] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[plant_region]    Script Date: 2023/12/24 19:57:44 ******/
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
/****** Object:  Table [dbo].[plantThreshold]    Script Date: 2023/12/24 19:57:44 ******/
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
/****** Object:  Table [dbo].[region]    Script Date: 2023/12/24 19:57:44 ******/
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
/****** Object:  Table [dbo].[users]    Script Date: 2023/12/24 19:57:44 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[users](
	[user_id] [bigint] IDENTITY(1,1) NOT NULL,
	[user_name] [nvarchar](50) NOT NULL,
	[password] [nvarchar](50) NOT NULL,
	[posts] [nvarchar](50) NOT NULL,
	[Permissions] [int] NOT NULL,
 CONSTRAINT [PK_user] PRIMARY KEY CLUSTERED 
(
	[user_id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
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
USE [master]
GO
ALTER DATABASE [GardenPlants] SET  READ_WRITE 
GO
