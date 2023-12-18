USE [master]
GO
/****** Object:  Database [GardenPlants]    Script Date: 2023/12/18 16:50:53 ******/
CREATE DATABASE [GardenPlants]
 CONTAINMENT = NONE
 ON  PRIMARY 
( NAME = N'Gardenplants', FILENAME = N'C:\Program Files\Microsoft SQL Server\MSSQL16.MSSQLSERVER\MSSQL\DATA\Gardenplants.mdf' , SIZE = 8192KB , MAXSIZE = UNLIMITED, FILEGROWTH = 65536KB )
 LOG ON 
( NAME = N'Gardenplants_log', FILENAME = N'C:\Program Files\Microsoft SQL Server\MSSQL16.MSSQLSERVER\MSSQL\DATA\Gardenplants_log.ldf' , SIZE = 8192KB , MAXSIZE = 2048GB , FILEGROWTH = 65536KB )
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
/****** Object:  Table [dbo].[classes]    Script Date: 2023/12/18 16:50:53 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[classes](
	[class_id] [bigint] IDENTITY(1,1) NOT NULL,
	[parent] [bigint] NULL,
	[rank] [int] NULL,
	[class_name] [nchar](50) NULL,
 CONSTRAINT [PK_classes] PRIMARY KEY CLUSTERED 
(
	[class_id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[equipment]    Script Date: 2023/12/18 16:50:53 ******/
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
/****** Object:  Table [dbo].[equipment_metrics]    Script Date: 2023/12/18 16:50:53 ******/
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
/****** Object:  Table [dbo].[fig]    Script Date: 2023/12/18 16:50:53 ******/
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
/****** Object:  Table [dbo].[Maintenance]    Script Date: 2023/12/18 16:50:53 ******/
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
/****** Object:  Table [dbo].[Maninternance_user]    Script Date: 2023/12/18 16:50:53 ******/
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
/****** Object:  Table [dbo].[medicine]    Script Date: 2023/12/18 16:50:53 ******/
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
/****** Object:  Table [dbo].[metrics]    Script Date: 2023/12/18 16:50:53 ******/
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
/****** Object:  Table [dbo].[Pest]    Script Date: 2023/12/18 16:50:53 ******/
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
/****** Object:  Table [dbo].[pest_medicine]    Script Date: 2023/12/18 16:50:53 ******/
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
/****** Object:  Table [dbo].[Plant]    Script Date: 2023/12/18 16:50:53 ******/
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
/****** Object:  Table [dbo].[plant_class]    Script Date: 2023/12/18 16:50:53 ******/
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
/****** Object:  Table [dbo].[plant_fig]    Script Date: 2023/12/18 16:50:53 ******/
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
/****** Object:  Table [dbo].[plant_Manintenance]    Script Date: 2023/12/18 16:50:53 ******/
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
/****** Object:  Table [dbo].[plant_metrics]    Script Date: 2023/12/18 16:50:53 ******/
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
/****** Object:  Table [dbo].[plant_pest]    Script Date: 2023/12/18 16:50:53 ******/
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
/****** Object:  Table [dbo].[plant_region]    Script Date: 2023/12/18 16:50:53 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[plant_region](
	[plant_id] [bigint] NOT NULL,
	[region] [bigint] NOT NULL,
 CONSTRAINT [PK_plant_region] PRIMARY KEY CLUSTERED 
(
	[plant_id] ASC,
	[region] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[region]    Script Date: 2023/12/18 16:50:53 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[region](
	[region_id] [bigint] IDENTITY(1,1) NOT NULL,
	[parent] [bigint] NULL,
	[rank] [int] NULL,
	[region_name] [nchar](50) NULL,
 CONSTRAINT [PK_region] PRIMARY KEY CLUSTERED 
(
	[region_id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[users]    Script Date: 2023/12/18 16:50:53 ******/
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
SET IDENTITY_INSERT [dbo].[Plant] ON 

INSERT [dbo].[Plant] ([plant_id], [species_name], [alia], [morphology], [value], [key_tech], [environment], [created_by], [created_at], [updated_at]) VALUES (1, N'玫瑰', N'蔷薇', N'直立、蔓延或攀援灌木，多数被有皮刺、针刺或刺毛，稀无刺，有毛、无毛或有腺毛。叶互生；花单生；花托球形、坛形至杯形；花瓣5，稀4，开展，覆瓦状排列，白色、黄色，粉红色至红色；花柱顶生至侧生，外伸，离生或上部合生；花瓣倒卵形，重瓣至半重瓣，花有紫红色、黄色、粉色、白色和各种复色。枝条较为柔弱软垂且多密刺，每年花期只有一次。', N'玫瑰花中含有300多种化学成份，如芳香的醇、醛、脂肪酸、酚和含香精的油和脂，常食玫瑰制品中以柔肝醒胃，舒气活血，美容养颜，令人神爽。玫瑰初开的花朵及根可入药，有理气、活血、收敛等作用、主治月经不调，跌打损伤、肝气胃痛，乳臃肿痛等症。', N'分株繁殖和扦插繁殖。
主要价值
', N'玫瑰喜阳光充足，耐寒、耐旱，喜排水良好、疏松肥沃的壤土或轻壤土，在粘壤土中生长不良，开花不佳。宜栽植在通风良好、离墙壁较远的地方，以防日光反射，灼伤花苞，影响开花。', N'xlh', CAST(N'2023-12-16' AS Date), CAST(N'2023-12-16' AS Date))
INSERT [dbo].[Plant] ([plant_id], [species_name], [alia], [morphology], [value], [key_tech], [environment], [created_by], [created_at], [updated_at]) VALUES (2, N'莲花', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL)
INSERT [dbo].[Plant] ([plant_id], [species_name], [alia], [morphology], [value], [key_tech], [environment], [created_by], [created_at], [updated_at]) VALUES (3, N'樱花', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL)
INSERT [dbo].[Plant] ([plant_id], [species_name], [alia], [morphology], [value], [key_tech], [environment], [created_by], [created_at], [updated_at]) VALUES (4, N'梅花', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL)
INSERT [dbo].[Plant] ([plant_id], [species_name], [alia], [morphology], [value], [key_tech], [environment], [created_by], [created_at], [updated_at]) VALUES (5, N'菊花', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL)
INSERT [dbo].[Plant] ([plant_id], [species_name], [alia], [morphology], [value], [key_tech], [environment], [created_by], [created_at], [updated_at]) VALUES (6, N'杜鹃', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL)
INSERT [dbo].[Plant] ([plant_id], [species_name], [alia], [morphology], [value], [key_tech], [environment], [created_by], [created_at], [updated_at]) VALUES (7, N'紫罗兰', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL)
INSERT [dbo].[Plant] ([plant_id], [species_name], [alia], [morphology], [value], [key_tech], [environment], [created_by], [created_at], [updated_at]) VALUES (8, N'石竹', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL)
INSERT [dbo].[Plant] ([plant_id], [species_name], [alia], [morphology], [value], [key_tech], [environment], [created_by], [created_at], [updated_at]) VALUES (9, N'马蹄莲', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL)
INSERT [dbo].[Plant] ([plant_id], [species_name], [alia], [morphology], [value], [key_tech], [environment], [created_by], [created_at], [updated_at]) VALUES (10, N'牵牛花', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL)
INSERT [dbo].[Plant] ([plant_id], [species_name], [alia], [morphology], [value], [key_tech], [environment], [created_by], [created_at], [updated_at]) VALUES (11, N'茉莉', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL)
SET IDENTITY_INSERT [dbo].[Plant] OFF
GO
SET IDENTITY_INSERT [dbo].[users] ON 

INSERT [dbo].[users] ([user_id], [user_name], [password], [posts], [Permissions]) VALUES (1, N'xlh', N'123', N'管理员', 0)
INSERT [dbo].[users] ([user_id], [user_name], [password], [posts], [Permissions]) VALUES (2, N'lyh', N'456', N'游客', 4)
INSERT [dbo].[users] ([user_id], [user_name], [password], [posts], [Permissions]) VALUES (3, N'yxy', N'845', N'游客', 4)
INSERT [dbo].[users] ([user_id], [user_name], [password], [posts], [Permissions]) VALUES (4, N'czw', N'789', N'游客', 4)
INSERT [dbo].[users] ([user_id], [user_name], [password], [posts], [Permissions]) VALUES (5, N'wxm', N'485', N'游客', 4)
INSERT [dbo].[users] ([user_id], [user_name], [password], [posts], [Permissions]) VALUES (6, N'wlx', N'875', N'游客', 4)
SET IDENTITY_INSERT [dbo].[users] OFF
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
USE [master]
GO
ALTER DATABASE [GardenPlants] SET  READ_WRITE 
GO
