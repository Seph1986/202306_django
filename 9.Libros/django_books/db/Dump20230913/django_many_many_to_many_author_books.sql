CREATE DATABASE  IF NOT EXISTS `django_many` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `django_many`;
-- MySQL dump 10.13  Distrib 8.0.34, for Linux (x86_64)
--
-- Host: localhost    Database: django_many
-- ------------------------------------------------------
-- Server version	8.0.34-0ubuntu0.22.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `many_to_many_author_books`
--

DROP TABLE IF EXISTS `many_to_many_author_books`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `many_to_many_author_books` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `author_id` bigint NOT NULL,
  `book_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `many_to_many_athor_books_athor_id_book_id_ef1722c0_uniq` (`author_id`,`book_id`),
  KEY `many_to_many_athor_b_book_id_885bf0a5_fk_many_to_m` (`book_id`),
  CONSTRAINT `many_to_many_athor_b_book_id_885bf0a5_fk_many_to_m` FOREIGN KEY (`book_id`) REFERENCES `many_to_many_book` (`id`),
  CONSTRAINT `many_to_many_author__author_id_69a94700_fk_many_to_m` FOREIGN KEY (`author_id`) REFERENCES `many_to_many_author` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `many_to_many_author_books`
--

LOCK TABLES `many_to_many_author_books` WRITE;
/*!40000 ALTER TABLE `many_to_many_author_books` DISABLE KEYS */;
INSERT INTO `many_to_many_author_books` VALUES (1,1,1),(2,1,2),(6,2,1),(7,2,2),(8,2,3),(9,3,1),(10,3,2),(11,3,3),(12,3,4),(13,4,1),(14,4,2),(15,4,3),(16,4,4),(17,4,5),(18,5,2);
/*!40000 ALTER TABLE `many_to_many_author_books` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-09-13 16:15:52
