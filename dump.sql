-- MariaDB dump 10.19  Distrib 10.6.16-MariaDB, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database: repel
-- ------------------------------------------------------
-- Server version	10.6.16-MariaDB-0ubuntu0.22.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `finished_movies`
--

DROP TABLE IF EXISTS `finished_movies`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `finished_movies` (
  `movies_id` int(11) DEFAULT NULL,
  `finished_date` date DEFAULT NULL,
  KEY `movies_id` (`movies_id`),
  CONSTRAINT `finished_movies_ibfk_1` FOREIGN KEY (`movies_id`) REFERENCES `movies` (`movies_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `finished_movies`
--

LOCK TABLES `finished_movies` WRITE;
/*!40000 ALTER TABLE `finished_movies` DISABLE KEYS */;
INSERT INTO `finished_movies` VALUES (52,'2024-04-04'),(91,'2024-02-10'),(56,'2024-02-16'),(79,'2024-03-09'),(35,'2024-01-04'),(16,'2024-03-15'),(95,'2024-01-21'),(28,'2024-01-29'),(90,'2024-04-20'),(3,'2024-03-20'),(19,'2024-01-30'),(83,'2024-02-22'),(45,'2024-03-22'),(89,'2024-02-25'),(46,'2024-04-20'),(72,'2024-01-24'),(81,'2024-02-22'),(53,'2024-04-26'),(71,'2024-01-18'),(67,'2024-04-06'),(74,'2024-02-23'),(27,'2024-02-14'),(38,'2024-01-10'),(26,'2024-02-11'),(51,'2024-02-07'),(88,'2024-03-14'),(29,'2024-04-20'),(8,'2024-03-25'),(42,'2024-02-01');
/*!40000 ALTER TABLE `finished_movies` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `finished_series`
--

DROP TABLE IF EXISTS `finished_series`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `finished_series` (
  `series_id` int(11) DEFAULT NULL,
  `finished_date` date DEFAULT NULL,
  KEY `series_id` (`series_id`),
  CONSTRAINT `finished_series_ibfk_1` FOREIGN KEY (`series_id`) REFERENCES `series` (`series_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `finished_series`
--

LOCK TABLES `finished_series` WRITE;
/*!40000 ALTER TABLE `finished_series` DISABLE KEYS */;
INSERT INTO `finished_series` VALUES (52,'2024-04-04'),(91,'2024-02-10'),(56,'2024-02-16'),(79,'2024-03-09'),(35,'2024-01-04'),(16,'2024-03-15'),(95,'2024-01-21'),(28,'2024-01-29'),(90,'2024-04-20'),(3,'2024-03-20'),(19,'2024-01-30'),(83,'2024-02-22'),(45,'2024-03-22'),(89,'2024-02-25'),(46,'2024-04-20'),(72,'2024-01-24'),(81,'2024-02-22'),(53,'2024-04-26'),(71,'2024-01-18'),(67,'2024-04-06'),(74,'2024-02-23'),(27,'2024-02-14'),(38,'2024-01-10'),(26,'2024-02-11'),(51,'2024-02-07'),(88,'2024-03-14'),(29,'2024-04-20'),(8,'2024-03-25'),(42,'2024-02-01');
/*!40000 ALTER TABLE `finished_series` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `movies`
--

DROP TABLE IF EXISTS `movies`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `movies` (
  `movies_id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) DEFAULT NULL,
  `duration` int(11) DEFAULT NULL,
  `release_year` int(11) DEFAULT NULL,
  `genre` varchar(30) DEFAULT NULL,
  `synopsis` text DEFAULT NULL,
  PRIMARY KEY (`movies_id`)
) ENGINE=InnoDB AUTO_INCREMENT=100 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `movies`
--

LOCK TABLES `movies` WRITE;
/*!40000 ALTER TABLE `movies` DISABLE KEYS */;
INSERT INTO `movies` VALUES (1,'Embrace of the Vampire',6028,1990,'Horror|Thriller',NULL),(3,'Lost Weekend, The',6442,1993,'Drama',NULL),(4,'Fixed Bayonets!',5836,2005,'Drama|War',NULL),(5,'Antibodies (Antikörper)',6873,2001,'Crime|Drama|Horror|Thriller',NULL),(7,'Dragon Lord (a.k.a. Dragon Strike) (Long Xiao Ye)',6861,2006,'Action',NULL),(8,'Cold Comfort Farm',5618,2005,'Comedy',NULL),(9,'The Burglar',6556,1987,'Crime|Drama',NULL),(10,'Dead & Buried',5579,2004,'Horror',NULL),(11,'Thunderheart',5896,1988,'Crime|Mystery|Thriller',NULL),(12,'Mother Carey\'s Chickens',6596,2004,'Drama|Romance',NULL),(13,'Frontière(s)',5688,1993,'Drama|Horror|Thriller',NULL),(14,'Flight of Fury',5959,1985,'Action',NULL),(15,'Stuck',6708,2014,'Horror|Thriller',NULL),(16,'Intimate Strangers (Confidences trop intimes)',6992,2018,'Drama',NULL),(18,'Headhunter\'s Sister, The',5943,1998,'Drama',NULL),(19,'Good Man in Africa, A',5762,2012,'Action|Adventure',NULL),(20,'Host, The',7118,1999,'Action|Adventure|Romance',NULL),(21,'Monster, The',6528,1988,'Comedy|Horror|Mystery|Sci-Fi',NULL),(22,'Ella Lola, a la Trilby',5703,2000,'(no genres listed)',NULL),(23,'Please Vote for Me',7168,2004,'Documentary',NULL),(24,'Blood, Guts, Bullets and Octane',5690,2001,'Action|Comedy',NULL),(25,'The Cruel Sea',6176,2000,'Drama|War',NULL),(26,'Munger Road',6008,1991,'Horror|Mystery|Thriller',NULL),(27,'Girl Crazy',5666,2008,'Comedy|Musical|Romance',NULL),(28,'Sometimes They Come Back... for More',6001,2010,'Horror',NULL),(29,'The World Forgotten',6038,1999,'Adventure|Documentary',NULL),(31,'Ink',5651,1999,'Action|Fantasy|Sci-Fi',NULL),(32,'2010: The Year We Make Contact',6225,1992,'Sci-Fi',NULL),(33,'Naked Edge, The',5652,2007,'Thriller',NULL),(34,'Baby On Board',6182,1997,'Comedy',NULL),(35,'After Life (Wandafuru raifu)',6955,1989,'Drama|Fantasy',NULL),(36,'Backcountry',5602,2002,'Drama|Horror|Thriller',NULL),(37,'Mr. Magoo',6755,1989,'Comedy',NULL),(38,'Street Without End (Kagirinaki hodo)',6646,1997,'Drama',NULL),(39,'Blaze',5796,2012,'Comedy|Drama',NULL),(40,'Sympathy for Delicious',6312,1988,'Drama',NULL),(41,'The Message',6988,2012,'Crime|Drama|Thriller|War',NULL),(42,'Food Stamped',5641,2002,'Documentary',NULL),(43,'Cat Run 2',6420,2017,'Action',NULL),(44,'Girl in the Cadillac',7025,2020,'Drama',NULL),(45,'The Secret of Convict Lake',6434,2005,'Western',NULL),(46,'Lost World, The',7150,1994,'Adventure',NULL),(47,'Blue Bird, The',6756,1999,'Fantasy',NULL),(48,'Young People',6192,1988,'Drama',NULL),(49,'Shoppen ',6540,2007,'Comedy|Romance',NULL),(50,'Nana',7092,2010,'Drama',NULL),(51,'Kiss for Corliss, A (Almost a Bride)',6471,1991,'Comedy',NULL),(52,'Salome\'s Last Dance',5484,2009,'Comedy|Drama',NULL),(53,'Contagion',6917,1985,'Sci-Fi|Thriller|IMAX',NULL),(54,'Staggered',6190,1997,'Comedy',NULL),(55,'Honeymoon Killers, The',6526,1988,'Crime|Thriller',NULL),(56,'Livid (Livide)',7199,1993,'Fantasy|Horror',NULL),(57,'Space Odyssey: Voyage to the Planets',6120,1998,'Documentary|Drama|Sci-Fi',NULL),(58,'Camp de Thiaroye',7166,2012,'Drama|War',NULL),(59,'I Spit on Your Grave (Day of the Woman)',6064,1988,'Horror|Thriller',NULL),(62,'Year My Voice Broke, The',6519,2001,'Drama',NULL),(64,'Voyage to the Bottom of the Sea',6353,2012,'Adventure|Sci-Fi',NULL),(65,'Armed and Dangerous',5472,2000,'Comedy|Crime',NULL),(66,'Tim and Eric\'s Billion Dollar Movie',7172,2007,'Comedy',NULL),(67,'Harlem Nights',6422,1987,'Comedy|Crime|Romance',NULL),(68,'Genevieve',6126,2005,'Comedy',NULL),(69,'Wayne\'s World 2',6576,2003,'Comedy',NULL),(70,'Nancy Drew: Detective',6446,2011,'Comedy|Mystery',NULL),(71,'Armless',5588,2007,'Comedy',NULL),(72,'Bio-Dome',5663,2002,'Comedy',NULL),(73,'Cheaper by the Dozen',6016,2017,'Comedy|Drama',NULL),(74,'Letter Never Sent (Neotpravlennoye pismo)',6379,2007,'Drama|Romance',NULL),(75,'Cool World',5644,1988,'Animation|Comedy|Fantasy',NULL),(76,'Details, The',6516,2015,'Comedy',NULL),(77,'French Film',6753,2004,'Comedy|Romance',NULL),(78,'Gasoline (Benzina)',6832,1995,'Crime',NULL),(79,'Hanging Up',5481,1990,'Comedy|Drama',NULL),(80,'Stand-In',6487,2008,'Comedy',NULL),(81,'Mummy\'s Ghost, The',6923,1985,'Horror',NULL),(82,'Brown Sugar',6522,1992,'Romance',NULL),(83,'Baxter, The',7034,2010,'Comedy|Drama|Romance',NULL),(84,'Ned Kelly',6812,2023,'Drama',NULL),(85,'Burning Bright',5754,2014,'Drama|Horror|Thriller',NULL),(86,'Mom and Dad Save the World',5924,2007,'Comedy|Sci-Fi',NULL),(87,'Gunga Din',5815,1986,'Adventure|Comedy|War',NULL),(88,'Spanish Fly',6178,2007,'Drama',NULL),(89,'Petrified Forest, The',5961,1988,'Crime|Drama|Romance',NULL),(90,'Bad Medicine',6170,2006,'Comedy',NULL),(91,'And Then There Was You',5943,1993,'Drama',NULL),(92,'That Guy... Who Was in That Thing',6508,2022,'Documentary',NULL),(93,'Mission, The',5514,1987,'Drama',NULL),(94,'Critters 2: The Main Course',6595,1995,'Comedy|Horror|Sci-Fi',NULL),(95,'Your Friend the Rat',6959,2024,'Animation',NULL),(96,'Faces of Death 4',6039,2023,'Documentary|Horror',NULL),(97,'Kamchatka',5806,1990,'Drama',NULL),(98,'Golden Boy',6770,1998,'Drama',NULL),(99,'WUSA',6769,1985,'Drama',NULL);
/*!40000 ALTER TABLE `movies` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ongoing_movies`
--

DROP TABLE IF EXISTS `ongoing_movies`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ongoing_movies` (
  `movies_id` int(11) DEFAULT NULL,
  `watched_duration` int(11) DEFAULT NULL,
  KEY `movies_id` (`movies_id`),
  CONSTRAINT `ongoing_movies_ibfk_1` FOREIGN KEY (`movies_id`) REFERENCES `movies` (`movies_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ongoing_movies`
--

LOCK TABLES `ongoing_movies` WRITE;
/*!40000 ALTER TABLE `ongoing_movies` DISABLE KEYS */;
INSERT INTO `ongoing_movies` VALUES (75,3325),(1,3143),(66,4176),(40,3910),(68,4868),(93,4533),(85,4315),(49,4223),(50,3714),(86,3837),(48,4679),(87,3383),(39,4084),(22,3684),(94,4074),(80,3014),(33,3033),(76,4896),(12,4916),(58,3410),(69,4899),(15,4952),(64,3846),(9,4769),(78,4913),(25,4548),(62,3001),(24,3908),(97,4081),(4,3901);
/*!40000 ALTER TABLE `ongoing_movies` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ongoing_series`
--

DROP TABLE IF EXISTS `ongoing_series`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ongoing_series` (
  `series_id` int(11) DEFAULT NULL,
  `season_progress` int(11) DEFAULT NULL,
  `episode_progress` int(11) DEFAULT NULL,
  `watched_duration` int(11) DEFAULT NULL,
  KEY `series_id` (`series_id`),
  CONSTRAINT `ongoing_series_ibfk_1` FOREIGN KEY (`series_id`) REFERENCES `series` (`series_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ongoing_series`
--

LOCK TABLES `ongoing_series` WRITE;
/*!40000 ALTER TABLE `ongoing_series` DISABLE KEYS */;
INSERT INTO `ongoing_series` VALUES (75,1,2,3325),(1,1,2,3143),(66,1,2,4176),(40,1,2,3910),(68,1,2,4868),(93,1,2,4533),(85,1,2,4315),(49,1,2,4223),(50,1,2,3714),(86,1,2,3837),(48,1,2,4679),(87,1,2,3383),(39,1,3,4084),(22,1,3,3684),(94,2,3,4074),(80,2,3,3014),(33,2,3,3033),(76,2,3,4896),(12,2,3,4916),(58,2,3,3410),(69,2,3,4899),(15,2,3,4952),(64,2,4,3846),(9,2,4,4769),(78,2,4,4913),(25,2,4,4548),(62,2,4,3001),(24,2,4,3908),(97,2,4,4081),(4,2,4,3901);
/*!40000 ALTER TABLE `ongoing_series` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `review_movies`
--

DROP TABLE IF EXISTS `review_movies`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `review_movies` (
  `movies_id` int(11) DEFAULT NULL,
  `rating` int(11) DEFAULT NULL,
  KEY `movies_id` (`movies_id`),
  CONSTRAINT `review_movies_ibfk_1` FOREIGN KEY (`movies_id`) REFERENCES `finished_movies` (`movies_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `review_movies`
--

LOCK TABLES `review_movies` WRITE;
/*!40000 ALTER TABLE `review_movies` DISABLE KEYS */;
INSERT INTO `review_movies` VALUES (52,7),(91,7),(56,7),(79,7),(35,7),(16,9),(95,9),(3,9),(19,9),(83,9),(45,6),(89,6),(81,6),(67,10),(74,10),(51,10),(88,10),(29,8),(8,8),(42,8);
/*!40000 ALTER TABLE `review_movies` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `review_series`
--

DROP TABLE IF EXISTS `review_series`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `review_series` (
  `series_id` int(11) DEFAULT NULL,
  `rating` int(11) DEFAULT NULL,
  `review` text DEFAULT NULL,
  KEY `series_id` (`series_id`),
  CONSTRAINT `review_series_ibfk_1` FOREIGN KEY (`series_id`) REFERENCES `finished_series` (`series_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `review_series`
--

LOCK TABLES `review_series` WRITE;
/*!40000 ALTER TABLE `review_series` DISABLE KEYS */;
INSERT INTO `review_series` VALUES (52,7,NULL),(91,7,NULL),(56,7,NULL),(79,7,NULL),(35,7,NULL),(16,9,NULL),(95,9,NULL),(3,9,NULL),(19,9,NULL),(83,9,NULL),(45,6,NULL),(89,6,NULL),(81,6,NULL),(67,10,NULL),(74,10,NULL),(51,10,NULL),(88,10,NULL),(29,8,NULL),(8,8,NULL),(42,8,NULL);
/*!40000 ALTER TABLE `review_series` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `series`
--

DROP TABLE IF EXISTS `series`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `series` (
  `series_id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) DEFAULT NULL,
  `duration` int(11) DEFAULT NULL,
  `release_year` int(11) DEFAULT NULL,
  `genre` varchar(30) DEFAULT NULL,
  `synopsis` text DEFAULT NULL,
  `season` int(11) DEFAULT NULL,
  `episode` int(11) DEFAULT NULL,
  PRIMARY KEY (`series_id`)
) ENGINE=InnoDB AUTO_INCREMENT=100 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `series`
--

LOCK TABLES `series` WRITE;
/*!40000 ALTER TABLE `series` DISABLE KEYS */;
INSERT INTO `series` VALUES (1,'Embrace of the Vampire',6028,1990,'Horror|Thriller',NULL,3,12),(3,'Lost Weekend, The',6442,1993,'Drama',NULL,3,12),(4,'Fixed Bayonets!',5836,2005,'Drama|War',NULL,3,12),(5,'Antibodies (Antikörper)',6873,2001,'Crime|Drama|Horror|Thriller',NULL,3,12),(7,'Dragon Lord (a.k.a. Dragon Strike) (Long Xiao Ye)',6861,2006,'Action',NULL,3,12),(8,'Cold Comfort Farm',5618,2005,'Comedy',NULL,3,12),(9,'The Burglar',6556,1987,'Crime|Drama',NULL,3,12),(10,'Dead & Buried',5579,2004,'Horror',NULL,3,12),(11,'Thunderheart',5896,1988,'Crime|Mystery|Thriller',NULL,3,12),(12,'Mother Carey\'s Chickens',6596,2004,'Drama|Romance',NULL,5,12),(13,'Frontière(s)',5688,1993,'Drama|Horror|Thriller',NULL,5,12),(14,'Flight of Fury',5959,1985,'Action',NULL,5,12),(15,'Stuck',6708,2014,'Horror|Thriller',NULL,5,7),(16,'Intimate Strangers (Confidences trop intimes)',6992,2018,'Drama',NULL,5,7),(18,'Headhunter\'s Sister, The',5943,1998,'Drama',NULL,5,7),(19,'Good Man in Africa, A',5762,2012,'Action|Adventure',NULL,5,7),(20,'Host, The',7118,1999,'Action|Adventure|Romance',NULL,5,7),(21,'Monster, The',6528,1988,'Comedy|Horror|Mystery|Sci-Fi',NULL,5,7),(22,'Ella Lola, a la Trilby',5703,2000,'(no genres listed)',NULL,5,7),(23,'Please Vote for Me',7168,2004,'Documentary',NULL,5,7),(24,'Blood, Guts, Bullets and Octane',5690,2001,'Action|Comedy',NULL,5,8),(25,'The Cruel Sea',6176,2000,'Drama|War',NULL,5,8),(26,'Munger Road',6008,1991,'Horror|Mystery|Thriller',NULL,9,8),(27,'Girl Crazy',5666,2008,'Comedy|Musical|Romance',NULL,9,8),(28,'Sometimes They Come Back... for More',6001,2010,'Horror',NULL,9,8),(29,'The World Forgotten',6038,1999,'Adventure|Documentary',NULL,9,8),(31,'Ink',5651,1999,'Action|Fantasy|Sci-Fi',NULL,9,8),(32,'2010: The Year We Make Contact',6225,1992,'Sci-Fi',NULL,9,8),(33,'Naked Edge, The',5652,2007,'Thriller',NULL,9,8),(34,'Baby On Board',6182,1997,'Comedy',NULL,9,8),(35,'After Life (Wandafuru raifu)',6955,1989,'Drama|Fantasy',NULL,9,8),(36,'Backcountry',5602,2002,'Drama|Horror|Thriller',NULL,9,8),(37,'Mr. Magoo',6755,1989,'Comedy',NULL,9,8),(38,'Street Without End (Kagirinaki hodo)',6646,1997,'Drama',NULL,9,8),(39,'Blaze',5796,2012,'Comedy|Drama',NULL,9,8),(40,'Sympathy for Delicious',6312,1988,'Drama',NULL,9,8),(41,'The Message',6988,2012,'Crime|Drama|Thriller|War',NULL,9,8),(42,'Food Stamped',5641,2002,'Documentary',NULL,9,8),(43,'Cat Run 2',6420,2017,'Action',NULL,9,8),(44,'Girl in the Cadillac',7025,2020,'Drama',NULL,2,6),(45,'The Secret of Convict Lake',6434,2005,'Western',NULL,2,6),(46,'Lost World, The',7150,1994,'Adventure',NULL,2,6),(47,'Blue Bird, The',6756,1999,'Fantasy',NULL,2,6),(48,'Young People',6192,1988,'Drama',NULL,2,6),(49,'Shoppen ',6540,2007,'Comedy|Romance',NULL,2,6),(50,'Nana',7092,2010,'Drama',NULL,2,6),(51,'Kiss for Corliss, A (Almost a Bride)',6471,1991,'Comedy',NULL,2,6),(52,'Salome\'s Last Dance',5484,2009,'Comedy|Drama',NULL,2,6),(53,'Contagion',6917,1985,'Sci-Fi|Thriller|IMAX',NULL,2,6),(54,'Staggered',6190,1997,'Comedy',NULL,8,6),(55,'Honeymoon Killers, The',6526,1988,'Crime|Thriller',NULL,8,6),(56,'Livid (Livide)',7199,1993,'Fantasy|Horror',NULL,8,10),(57,'Space Odyssey: Voyage to the Planets',6120,1998,'Documentary|Drama|Sci-Fi',NULL,8,10),(58,'Camp de Thiaroye',7166,2012,'Drama|War',NULL,8,10),(59,'I Spit on Your Grave (Day of the Woman)',6064,1988,'Horror|Thriller',NULL,8,10),(62,'Year My Voice Broke, The',6519,2001,'Drama',NULL,8,10),(64,'Voyage to the Bottom of the Sea',6353,2012,'Adventure|Sci-Fi',NULL,8,10),(65,'Armed and Dangerous',5472,2000,'Comedy|Crime',NULL,8,10),(66,'Tim and Eric\'s Billion Dollar Movie',7172,2007,'Comedy',NULL,8,10),(67,'Harlem Nights',6422,1987,'Comedy|Crime|Romance',NULL,8,10),(68,'Genevieve',6126,2005,'Comedy',NULL,8,10),(69,'Wayne\'s World 2',6576,2003,'Comedy',NULL,8,10),(70,'Nancy Drew: Detective',6446,2011,'Comedy|Mystery',NULL,8,10),(71,'Armless',5588,2007,'Comedy',NULL,12,10),(72,'Bio-Dome',5663,2002,'Comedy',NULL,12,10),(73,'Cheaper by the Dozen',6016,2017,'Comedy|Drama',NULL,12,10),(74,'Letter Never Sent (Neotpravlennoye pismo)',6379,2007,'Drama|Romance',NULL,12,10),(75,'Cool World',5644,1988,'Animation|Comedy|Fantasy',NULL,12,16),(76,'Details, The',6516,2015,'Comedy',NULL,12,16),(77,'French Film',6753,2004,'Comedy|Romance',NULL,12,16),(78,'Gasoline (Benzina)',6832,1995,'Crime',NULL,12,16),(79,'Hanging Up',5481,1990,'Comedy|Drama',NULL,12,16),(80,'Stand-In',6487,2008,'Comedy',NULL,12,16),(81,'Mummy\'s Ghost, The',6923,1985,'Horror',NULL,12,16),(82,'Brown Sugar',6522,1992,'Romance',NULL,12,16),(83,'Baxter, The',7034,2010,'Comedy|Drama|Romance',NULL,12,16),(84,'Ned Kelly',6812,2023,'Drama',NULL,12,16),(85,'Burning Bright',5754,2014,'Drama|Horror|Thriller',NULL,12,5),(86,'Mom and Dad Save the World',5924,2007,'Comedy|Sci-Fi',NULL,12,5),(87,'Gunga Din',5815,1986,'Adventure|Comedy|War',NULL,6,5),(88,'Spanish Fly',6178,2007,'Drama',NULL,6,5),(89,'Petrified Forest, The',5961,1988,'Crime|Drama|Romance',NULL,6,5),(90,'Bad Medicine',6170,2006,'Comedy',NULL,6,5),(91,'And Then There Was You',5943,1993,'Drama',NULL,6,5),(92,'That Guy... Who Was in That Thing',6508,2022,'Documentary',NULL,6,5),(93,'Mission, The',5514,1987,'Drama',NULL,6,5),(94,'Critters 2: The Main Course',6595,1995,'Comedy|Horror|Sci-Fi',NULL,6,5),(95,'Your Friend the Rat',6959,2024,'Animation',NULL,6,5),(96,'Faces of Death 4',6039,2023,'Documentary|Horror',NULL,6,5),(97,'Kamchatka',5806,1990,'Drama',NULL,6,5),(98,'Golden Boy',6770,1998,'Drama',NULL,5,5),(99,'WUSA',6769,1985,'Drama',NULL,5,5);
/*!40000 ALTER TABLE `series` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `watchlist_movies`
--

DROP TABLE IF EXISTS `watchlist_movies`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `watchlist_movies` (
  `movies_id` int(11) DEFAULT NULL,
  KEY `movies_id` (`movies_id`),
  CONSTRAINT `watchlist_movies_ibfk_1` FOREIGN KEY (`movies_id`) REFERENCES `movies` (`movies_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `watchlist_movies`
--

LOCK TABLES `watchlist_movies` WRITE;
/*!40000 ALTER TABLE `watchlist_movies` DISABLE KEYS */;
INSERT INTO `watchlist_movies` VALUES (5),(7),(10),(11),(13),(14),(18),(20),(21),(23),(31),(32),(34),(36),(37),(41),(43),(44),(47),(54),(55),(57),(59),(65),(70),(73),(77),(82),(84),(92),(96),(98),(99);
/*!40000 ALTER TABLE `watchlist_movies` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `watchlist_series`
--

DROP TABLE IF EXISTS `watchlist_series`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `watchlist_series` (
  `series_id` int(11) DEFAULT NULL,
  KEY `series_id` (`series_id`),
  CONSTRAINT `watchlist_series_ibfk_1` FOREIGN KEY (`series_id`) REFERENCES `series` (`series_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `watchlist_series`
--

LOCK TABLES `watchlist_series` WRITE;
/*!40000 ALTER TABLE `watchlist_series` DISABLE KEYS */;
INSERT INTO `watchlist_series` VALUES (5),(7),(10),(11),(13),(14),(18),(20),(21),(23),(31),(32),(34),(36),(37),(41),(43),(44),(47),(54),(55),(57),(59),(65),(70),(73),(77),(82),(84),(92),(96),(98),(99);
/*!40000 ALTER TABLE `watchlist_series` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-05-13 20:47:53
