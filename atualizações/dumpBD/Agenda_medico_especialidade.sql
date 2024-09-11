-- MySQL dump 10.13  Distrib 8.0.28, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: Agenda
-- ------------------------------------------------------
-- Server version	8.1.0

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
-- Table structure for table `medico_especialidade`
--

DROP TABLE IF EXISTS `medico_especialidade`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `medico_especialidade` (
  `id` int NOT NULL AUTO_INCREMENT,
  `FK_medico` int NOT NULL,
  `FK_especialidade` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `FK_medico` (`FK_medico`),
  KEY `FK_especialidade` (`FK_especialidade`),
  CONSTRAINT `medico_especialidade_ibfk_1` FOREIGN KEY (`FK_medico`) REFERENCES `medico` (`id`),
  CONSTRAINT `medico_especialidade_ibfk_2` FOREIGN KEY (`FK_especialidade`) REFERENCES `especialidade` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `medico_especialidade`
--

LOCK TABLES `medico_especialidade` WRITE;
/*!40000 ALTER TABLE `medico_especialidade` DISABLE KEYS */;
INSERT INTO `medico_especialidade` VALUES (1,2,2),(2,2,3),(3,3,2),(4,3,4),(5,14,1),(8,18,1),(9,18,4),(10,19,2),(11,19,4),(12,15,1),(18,17,1),(19,20,1),(20,20,2),(21,20,9);
/*!40000 ALTER TABLE `medico_especialidade` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-08-21 11:49:20
