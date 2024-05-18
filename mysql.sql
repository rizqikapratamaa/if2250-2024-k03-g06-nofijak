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
INSERT INTO `finished_movies` VALUES (16,'2024-04-04'),(4,'2024-02-10'),(25,'2024-02-16'),(21,'2024-03-09'),(34,'2024-01-04'),(46,'2024-03-15'),(15,'2024-01-21'),(50,'2024-01-29'),(33,'2024-04-20'),(31,'2024-03-20'),(49,'2024-01-30'),(9,'2024-01-24'),(22,'2024-02-22'),(14,'2024-03-22'),(48,'2024-02-25'),(37,'2024-04-20');
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
INSERT INTO `finished_series` VALUES (44,'2024-04-04'),(50,'2024-02-10'),(38,'2024-02-16'),(48,'2024-03-09'),(47,'2024-01-04'),(15,'2024-03-15'),(21,'2024-01-21'),(4,'2024-01-29'),(41,'2024-04-20'),(19,'2024-03-20'),(34,'2024-01-30'),(40,'2024-02-22'),(32,'2024-03-22'),(30,'2024-02-25'),(13,'2024-04-20'),(37,'2024-01-24');
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
  `name` varchar(100) DEFAULT NULL,
  `duration` int(11) DEFAULT NULL,
  `release_year` int(11) DEFAULT NULL,
  `genre` varchar(30) DEFAULT NULL,
  `synopsis` text DEFAULT NULL,
  PRIMARY KEY (`movies_id`)
) ENGINE=InnoDB AUTO_INCREMENT=51 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `movies`
--

LOCK TABLES `movies` WRITE;
/*!40000 ALTER TABLE `movies` DISABLE KEYS */;
INSERT INTO `movies` VALUES (1,'Embrace of the Vampire',6028,1990,'Horror','anjay'),(2,'Acla, The Descent into Floristella (La discesa di Aclà a Floristella)',6797,2005,'Drama','anjay'),(3,'Lost Weekend, The',6442,1993,'Drama','anjay'),(4,'Fixed Bayonets!',5836,2005,'Drama','anjay'),(5,'Antibodies (Antikörper)',6873,2001,'Crime','anjay'),(6,'Castle in the Desert (Charlie Chan in Castle in the Desert)',6372,1996,'Comedy','anjay'),(7,'Dragon Lord (a.k.a. Dragon Strike) (Long Xiao Ye)',6861,2006,'Action','anjay'),(8,'Cold Comfort Farm',5618,2005,'Comedy','anjay'),(9,'The Burglar',6556,1987,'Crime','anjay'),(10,'Dead & Buried',5579,2004,'Horror','anjay'),(11,'Thunderheart',5896,1988,'Crime','anjay'),(12,'Mother Carey\'s Chickens',6596,2004,'Drama','anjay'),(13,'Frontière(s)',5688,1993,'Drama','anjay'),(14,'Flight of Fury',5959,1985,'Action','anjay'),(15,'Stuck',6708,2014,'Horror','anjay'),(16,'Intimate Strangers (Confidences trop intimes)',6992,2018,'Drama','anjay'),(17,'Films to Keep You Awake: The Baby\'s Room (Películas para no dormir: La habitación del niño)',6116,1990,'Horror','anjay'),(18,'Headhunter\'s Sister, The',5943,1998,'Drama','anjay'),(19,'Good Man in Africa, A',5762,2012,'Action','anjay'),(20,'Host, The',7118,1999,'Action','anjay'),(21,'Monster, The',6528,1988,'Comedy','anjay'),(22,'Ella Lola, a la Trilby',5703,2000,'(no genres listed)','anjay'),(23,'Please Vote for Me',7168,2004,'Documentary','anjay'),(24,'Blood, Guts, Bullets and Octane',5690,2001,'Action','anjay'),(25,'The Cruel Sea',6176,2000,'Drama','anjay'),(26,'Munger Road',6008,1991,'Horror','anjay'),(27,'Girl Crazy',5666,2008,'Comedy','anjay'),(28,'Sometimes They Come Back... for More',6001,2010,'Horror','anjay'),(29,'The World Forgotten',6038,1999,'Adventure','anjay'),(30,'Hunting Party, The',6915,2004,'Action','anjay'),(31,'Ink',5651,1999,'Action','anjay'),(32,'2010: The Year We Make Contact',6225,1992,'Sci-Fi','anjay'),(33,'Naked Edge, The',5652,2007,'Thriller','anjay'),(34,'Baby On Board',6182,1997,'Comedy','anjay'),(35,'After Life (Wandafuru raifu)',6955,1989,'Drama','anjay'),(36,'Backcountry',5602,2002,'Drama','anjay'),(37,'Mr. Magoo',6755,1989,'Comedy','anjay'),(38,'Street Without End (Kagirinaki hodo)',6646,1997,'Drama','anjay'),(39,'Blaze',5796,2012,'Comedy','anjay'),(40,'Sympathy for Delicious',6312,1988,'Drama','anjay'),(41,'The Message',6988,2012,'Crime','anjay'),(42,'Food Stamped',5641,2002,'Documentary','anjay'),(43,'Cat Run 2',6420,2017,'Action','anjay'),(44,'Girl in the Cadillac',7025,2020,'Drama','anjay'),(45,'The Secret of Convict Lake',6434,2005,'Western','anjay'),(46,'Lost World, The',7150,1994,'Adventure','anjay'),(47,'Why Me?',6998,1998,'Drama','anjay'),(48,'Triad Election (a.k.a. Election 2) (Hak se wui yi wo wai kwai)',6063,2002,'Crime','anjay'),(49,'Check and Double Check',6805,2004,'Comedy','anjay'),(50,'Two People',6967,1989,'Drama','anjay');
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
INSERT INTO `ongoing_movies` VALUES (38,3325),(36,3143),(18,4176),(19,3910),(13,4868),(42,4373),(40,4533),(47,4315),(45,4223),(20,3714),(6,3837),(1,4679),(10,3383),(41,4084),(26,3684),(17,4902),(2,4074),(3,3014);
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
INSERT INTO `ongoing_series` VALUES (17,1,2,3325),(33,1,2,3143),(45,1,2,4176),(11,1,2,3910),(28,1,2,4868),(46,1,2,4373),(39,1,2,4533),(26,1,2,4315),(9,1,2,4223),(31,1,2,3714),(2,1,2,3837),(36,1,2,4679),(6,1,2,3383),(42,1,3,4084),(14,1,3,3684),(16,1,3,4902),(22,2,3,4074),(23,2,3,3014);
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
INSERT INTO `review_movies` VALUES (16,7),(4,7),(25,7),(21,7),(34,8),(46,8),(15,8),(50,8),(33,8),(31,9),(49,9),(9,9),(22,9),(14,7),(48,7),(37,7);
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
INSERT INTO `review_series` VALUES (44,10,'anjay'),(50,7,'anjay'),(38,7,'anjay'),(48,7,'anjay'),(47,7,'anjay'),(15,7,'anjay'),(21,8,'anjay'),(4,8,'anjay'),(41,8,'anjay'),(19,8,'anjay'),(34,8,'anjay'),(40,8,'anjay'),(32,10,'anjay'),(30,10,'anjay'),(13,10,'anjay'),(37,10,'anjay');
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
  `name` varchar(100) DEFAULT NULL,
  `duration` int(11) DEFAULT NULL,
  `release_year` int(11) DEFAULT NULL,
  `genre` varchar(30) DEFAULT NULL,
  `synopsis` text DEFAULT NULL,
  `season` int(11) DEFAULT NULL,
  `episode` int(11) DEFAULT NULL,
  PRIMARY KEY (`series_id`)
) ENGINE=InnoDB AUTO_INCREMENT=51 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `series`
--

LOCK TABLES `series` WRITE;
/*!40000 ALTER TABLE `series` DISABLE KEYS */;
INSERT INTO `series` VALUES (1,'Embrace of the Vampire',6028,1990,'Horror','anjay',3,12),(2,'Acla, The Descent into Floristella (La discesa di Aclà a Floristella)',6797,2005,'Drama','anjay',3,12),(3,'Lost Weekend, The',6442,1993,'Drama','anjay',3,12),(4,'Fixed Bayonets!',5836,2005,'Drama','anjay',3,12),(5,'Antibodies (Antikörper)',6873,2001,'Crime','anjay',3,12),(6,'Castle in the Desert (Charlie Chan in Castle in the Desert)',6372,1996,'Comedy','anjay',3,12),(7,'Dragon Lord (a.k.a. Dragon Strike) (Long Xiao Ye)',6861,2006,'Action','anjay',3,12),(8,'Cold Comfort Farm',5618,2005,'Comedy','anjay',3,12),(9,'The Burglar',6556,1987,'Crime','anjay',3,12),(10,'Dead & Buried',5579,2004,'Horror','anjay',3,12),(11,'Thunderheart',5896,1988,'Crime','anjay',3,12),(12,'Mother Carey\'s Chickens',6596,2004,'Drama','anjay',5,12),(13,'Frontière(s)',5688,1993,'Drama','anjay',5,12),(14,'Flight of Fury',5959,1985,'Action','anjay',5,12),(15,'Stuck',6708,2014,'Horror','anjay',5,7),(16,'Intimate Strangers (Confidences trop intimes)',6992,2018,'Drama','anjay',5,7),(17,'Films to Keep You Awake: The Baby\'s Room (Películas para no dormir: La habitación del niño)',6116,1990,'Horror','anjay',5,7),(18,'Headhunter\'s Sister, The',5943,1998,'Drama','anjay',5,7),(19,'Good Man in Africa, A',5762,2012,'Action','anjay',5,7),(20,'Host, The',7118,1999,'Action','anjay',5,7),(21,'Monster, The',6528,1988,'Comedy','anjay',5,7),(22,'Ella Lola, a la Trilby',5703,2000,'(no genres listed)','anjay',5,7),(23,'Please Vote for Me',7168,2004,'Documentary','anjay',5,7),(24,'Blood, Guts, Bullets and Octane',5690,2001,'Action','anjay',5,8),(25,'The Cruel Sea',6176,2000,'Drama','anjay',5,8),(26,'Munger Road',6008,1991,'Horror','anjay',9,8),(27,'Girl Crazy',5666,2008,'Comedy','anjay',9,8),(28,'Sometimes They Come Back... for More',6001,2010,'Horror','anjay',9,8),(29,'The World Forgotten',6038,1999,'Adventure','anjay',9,8),(30,'Hunting Party, The',6915,2004,'Action','anjay',9,8),(31,'Ink',5651,1999,'Action','anjay',9,8),(32,'2010: The Year We Make Contact',6225,1992,'Sci-Fi','anjay',9,8),(33,'Naked Edge, The',5652,2007,'Thriller','anjay',9,8),(34,'Baby On Board',6182,1997,'Comedy','anjay',9,8),(35,'After Life (Wandafuru raifu)',6955,1989,'Drama','anjay',9,8),(36,'Backcountry',5602,2002,'Drama','anjay',9,8),(37,'Creep',6543,2001,'Horror','anjay',9,8),(38,'Good Bye Lenin!',6214,1994,'Comedy','anjay',9,8),(39,'Buried Alive II',6963,2008,'Horror','anjay',9,8),(40,'Outrage',6601,1986,'Drama','anjay',9,8),(41,'Philadelphia Experiment II',5744,2005,'Sci-Fi','anjay',9,8),(42,'Curse of the Pink Panther',6671,2012,'Comedy','anjay',9,8),(43,'Faster, Pussycat! Kill! Kill!',6081,2010,'Action','anjay',9,8),(44,'Music for the Movies: Bernard Herrmann',6064,2002,'Documentary','anjay',9,8),(45,'Fists in the Pocket (I Pugni in Tasca)',6155,2007,'Drama','anjay',9,8),(46,'Mindwarp',6166,1986,'Horror','anjay',9,8),(47,'Herb & Dorothy',6248,2001,'Documentary','anjay',9,8),(48,'2012',6651,2001,'Action','anjay',9,8),(49,'Diary of the Dead (a.k.a. George A. Romero\'s Diary of the Dead)',7096,2000,'Horror','anjay',9,8),(50,'Poseidon Adventure, The',6316,2000,'Action','anjay',9,8);
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
INSERT INTO `watchlist_movies` VALUES (5),(7),(8),(11),(12),(23),(24),(27),(28),(29),(30),(32),(35),(39),(43),(44);
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
INSERT INTO `watchlist_series` VALUES (1),(3),(5),(7),(8),(10),(12),(18),(20),(24),(25),(27),(29),(35),(43),(49);
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

-- Dump completed on 2024-05-18 10:26:51
