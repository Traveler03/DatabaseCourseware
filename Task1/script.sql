USE [master]
GO
/****** Object:  Database [Gardenplants]    Script Date: 2023/12/10 20:40:37 ******/
CREATE DATABASE [Gardenplants]
 CONTAINMENT = NONE
 ON  PRIMARY 
( NAME = N'Gardenplants', FILENAME = N'C:\Program Files\Microsoft SQL Server\MSSQL16.MSSQLSERVER\MSSQL\DATA\Gardenplants.mdf' , SIZE = 8192KB , MAXSIZE = UNLIMITED, FILEGROWTH = 65536KB )
 LOG ON 
( NAME = N'Gardenplants_log', FILENAME = N'C:\Program Files\Microsoft SQL Server\MSSQL16.MSSQLSERVER\MSSQL\DATA\Gardenplants_log.ldf' , SIZE = 8192KB , MAXSIZE = 2048GB , FILEGROWTH = 65536KB )
 WITH CATALOG_COLLATION = DATABASE_DEFAULT, LEDGER = OFF
GO
ALTER DATABASE [Gardenplants] SET COMPATIBILITY_LEVEL = 160
GO
IF (1 = FULLTEXTSERVICEPROPERTY('IsFullTextInstalled'))
begin
EXEC [Gardenplants].[dbo].[sp_fulltext_database] @action = 'enable'
end
GO
ALTER DATABASE [Gardenplants] SET ANSI_NULL_DEFAULT OFF 
GO
ALTER DATABASE [Gardenplants] SET ANSI_NULLS OFF 
GO
ALTER DATABASE [Gardenplants] SET ANSI_PADDING OFF 
GO
ALTER DATABASE [Gardenplants] SET ANSI_WARNINGS OFF 
GO
ALTER DATABASE [Gardenplants] SET ARITHABORT OFF 
GO
ALTER DATABASE [Gardenplants] SET AUTO_CLOSE OFF 
GO
ALTER DATABASE [Gardenplants] SET AUTO_SHRINK OFF 
GO
ALTER DATABASE [Gardenplants] SET AUTO_UPDATE_STATISTICS ON 
GO
ALTER DATABASE [Gardenplants] SET CURSOR_CLOSE_ON_COMMIT OFF 
GO
ALTER DATABASE [Gardenplants] SET CURSOR_DEFAULT  GLOBAL 
GO
ALTER DATABASE [Gardenplants] SET CONCAT_NULL_YIELDS_NULL OFF 
GO
ALTER DATABASE [Gardenplants] SET NUMERIC_ROUNDABORT OFF 
GO
ALTER DATABASE [Gardenplants] SET QUOTED_IDENTIFIER OFF 
GO
ALTER DATABASE [Gardenplants] SET RECURSIVE_TRIGGERS OFF 
GO
ALTER DATABASE [Gardenplants] SET  DISABLE_BROKER 
GO
ALTER DATABASE [Gardenplants] SET AUTO_UPDATE_STATISTICS_ASYNC OFF 
GO
ALTER DATABASE [Gardenplants] SET DATE_CORRELATION_OPTIMIZATION OFF 
GO
ALTER DATABASE [Gardenplants] SET TRUSTWORTHY OFF 
GO
ALTER DATABASE [Gardenplants] SET ALLOW_SNAPSHOT_ISOLATION OFF 
GO
ALTER DATABASE [Gardenplants] SET PARAMETERIZATION SIMPLE 
GO
ALTER DATABASE [Gardenplants] SET READ_COMMITTED_SNAPSHOT OFF 
GO
ALTER DATABASE [Gardenplants] SET HONOR_BROKER_PRIORITY OFF 
GO
ALTER DATABASE [Gardenplants] SET RECOVERY SIMPLE 
GO
ALTER DATABASE [Gardenplants] SET  MULTI_USER 
GO
ALTER DATABASE [Gardenplants] SET PAGE_VERIFY CHECKSUM  
GO
ALTER DATABASE [Gardenplants] SET DB_CHAINING OFF 
GO
ALTER DATABASE [Gardenplants] SET FILESTREAM( NON_TRANSACTED_ACCESS = OFF ) 
GO
ALTER DATABASE [Gardenplants] SET TARGET_RECOVERY_TIME = 60 SECONDS 
GO
ALTER DATABASE [Gardenplants] SET DELAYED_DURABILITY = DISABLED 
GO
ALTER DATABASE [Gardenplants] SET ACCELERATED_DATABASE_RECOVERY = OFF  
GO
ALTER DATABASE [Gardenplants] SET QUERY_STORE = ON
GO
ALTER DATABASE [Gardenplants] SET QUERY_STORE (OPERATION_MODE = READ_WRITE, CLEANUP_POLICY = (STALE_QUERY_THRESHOLD_DAYS = 30), DATA_FLUSH_INTERVAL_SECONDS = 900, INTERVAL_LENGTH_MINUTES = 60, MAX_STORAGE_SIZE_MB = 1000, QUERY_CAPTURE_MODE = AUTO, SIZE_BASED_CLEANUP_MODE = AUTO, MAX_PLANS_PER_QUERY = 200, WAIT_STATS_CAPTURE_MODE = ON)
GO
USE [Gardenplants]
GO
/****** Object:  Table [dbo].[alia]    Script Date: 2023/12/10 20:40:37 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[alia](
	[plant_id] [nchar](4) NOT NULL,
	[alias] [nvarchar](50) NOT NULL,
 CONSTRAINT [PK_alia] PRIMARY KEY CLUSTERED 
(
	[plant_id] ASC,
	[alias] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[fig]    Script Date: 2023/12/10 20:40:37 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[fig](
	[fig_id] [nchar](4) NOT NULL,
	[fig_path] [nvarchar](50) NOT NULL,
	[fig_place] [nvarchar](50) NULL,
	[fig_people] [nvarchar](50) NULL,
	[fig_des] [text] NULL,
	[created_by] [nvarchar](50) NULL,
	[creater_at] [date] NULL,
	[updated_at] [date] NULL,
 CONSTRAINT [PK_fig] PRIMARY KEY CLUSTERED 
(
	[fig_id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Maintenance]    Script Date: 2023/12/10 20:40:37 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Maintenance](
	[task_id] [nchar](4) NOT NULL,
	[task_name] [nvarchar](50) NOT NULL,
	[time] [date] NULL,
	[place] [nvarchar](50) NULL,
	[task_des] [text] NULL,
 CONSTRAINT [PK_Maintenance] PRIMARY KEY CLUSTERED 
(
	[task_id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Maninternance_user]    Script Date: 2023/12/10 20:40:37 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Maninternance_user](
	[task_id] [nchar](4) NOT NULL,
	[user_id] [nchar](4) NOT NULL,
 CONSTRAINT [PK_Maninternance_user] PRIMARY KEY CLUSTERED 
(
	[task_id] ASC,
	[user_id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[medicine]    Script Date: 2023/12/10 20:40:37 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[medicine](
	[medicine_id] [nchar](4) NOT NULL,
	[medicine_name] [nvarchar](50) NOT NULL,
	[duration] [nvarchar](50) NULL,
 CONSTRAINT [PK_medicine] PRIMARY KEY CLUSTERED 
(
	[medicine_id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Pest]    Script Date: 2023/12/10 20:40:37 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Pest](
	[pest_id] [nchar](4) NOT NULL,
	[pest_name] [nvarchar](50) NOT NULL,
	[cm] [text] NULL,
 CONSTRAINT [PK_Pest_manage] PRIMARY KEY CLUSTERED 
(
	[pest_id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
/****** Object:  Table [dbo].[pest_medicine]    Script Date: 2023/12/10 20:40:37 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[pest_medicine](
	[medicine_id] [nchar](4) NOT NULL,
	[pest_id] [nchar](4) NOT NULL,
	[Dosage] [nvarchar](50) NOT NULL,
 CONSTRAINT [PK_use_medicine] PRIMARY KEY CLUSTERED 
(
	[medicine_id] ASC,
	[pest_id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Plant]    Script Date: 2023/12/10 20:40:37 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Plant](
	[plant_id] [nchar](4) NOT NULL,
	[species_name] [nvarchar](50) NOT NULL,
	[morphology] [text] NULL,
	[value] [text] NULL,
	[key_tech] [text] NULL,
	[environment] [text] NULL,
	[created_by] [nvarchar](50) NULL,
	[created_at] [date] NULL,
	[updated_at] [date] NULL,
 CONSTRAINT [PK_Plant_information] PRIMARY KEY CLUSTERED 
(
	[plant_id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
/****** Object:  Table [dbo].[plant_fig]    Script Date: 2023/12/10 20:40:37 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[plant_fig](
	[plant_id] [nchar](4) NOT NULL,
	[fig_id] [nchar](4) NOT NULL,
 CONSTRAINT [PK_plant_fig] PRIMARY KEY CLUSTERED 
(
	[plant_id] ASC,
	[fig_id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[plant_Manintenance]    Script Date: 2023/12/10 20:40:37 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[plant_Manintenance](
	[plant_id] [nchar](4) NOT NULL,
	[task_id] [nchar](4) NOT NULL,
 CONSTRAINT [PK_plant_Manintenance] PRIMARY KEY CLUSTERED 
(
	[plant_id] ASC,
	[task_id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[plant_pest]    Script Date: 2023/12/10 20:40:37 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[plant_pest](
	[plant_id] [nchar](4) NOT NULL,
	[pest_id] [nchar](4) NOT NULL,
 CONSTRAINT [PK_sicken] PRIMARY KEY CLUSTERED 
(
	[plant_id] ASC,
	[pest_id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[user]    Script Date: 2023/12/10 20:40:37 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[user](
	[user_id] [nchar](4) NOT NULL,
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
INSERT [dbo].[alia] ([plant_id], [alias]) VALUES (N'k001', N'藕花')
INSERT [dbo].[alia] ([plant_id], [alias]) VALUES (N'K002', N'月季花')
GO
INSERT [dbo].[fig] ([fig_id], [fig_path], [fig_place], [fig_people], [fig_des], [created_by], [creater_at], [updated_at]) VALUES (N'N001', N'picture\ouhua1', NULL, NULL, NULL, NULL, CAST(N'2023-12-10' AS Date), CAST(N'2023-12-10' AS Date))
GO
INSERT [dbo].[Plant] ([plant_id], [species_name], [morphology], [value], [key_tech], [environment], [created_by], [created_at], [updated_at]) VALUES (N'k001', N'荷花', NULL, NULL, NULL, NULL, N'2023-12-10', NULL, CAST(N'2023-12-10' AS Date))
INSERT [dbo].[Plant] ([plant_id], [species_name], [morphology], [value], [key_tech], [environment], [created_by], [created_at], [updated_at]) VALUES (N'K002', N'月季', NULL, NULL, NULL, NULL, N'2023-12-10', NULL, CAST(N'2023-12-10' AS Date))
GO
INSERT [dbo].[plant_fig] ([plant_id], [fig_id]) VALUES (N'K001', N'N001')
GO
ALTER TABLE [dbo].[alia]  WITH CHECK ADD  CONSTRAINT [FK_alia_Plant] FOREIGN KEY([plant_id])
REFERENCES [dbo].[Plant] ([plant_id])
GO
ALTER TABLE [dbo].[alia] CHECK CONSTRAINT [FK_alia_Plant]
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
ALTER DATABASE [Gardenplants] SET  READ_WRITE 
GO
