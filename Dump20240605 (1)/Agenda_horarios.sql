CREATE DATABASE  IF NOT EXISTS `Agenda` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `Agenda`;
-- MySQL dump 10.13  Distrib 8.0.36, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: Agenda
-- ------------------------------------------------------
-- Server version	8.3.0

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
-- Table structure for table `horarios`
--

DROP TABLE IF EXISTS `horarios`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `horarios` (
  `id_medico` int NOT NULL,
  `id_servico` int NOT NULL,
  `hora` datetime NOT NULL,
  `status_servico` enum('Pendente','Atendida','Cancelada','Remarcada') DEFAULT NULL,
  `id_cpf_paciente` varchar(11) NOT NULL,
  KEY `fk_id_medico_servico` (`id_medico`),
  KEY `fk_id_servico_horarios` (`id_servico`),
  KEY `fk_id_cpf_paciente` (`id_cpf_paciente`),
  CONSTRAINT `fk_id_cpf_paciente` FOREIGN KEY (`id_cpf_paciente`) REFERENCES `paciente` (`cpf`),
  CONSTRAINT `fk_id_medico_servico` FOREIGN KEY (`id_medico`) REFERENCES `medico` (`id`),
  CONSTRAINT `fk_id_servico_horarios` FOREIGN KEY (`id_servico`) REFERENCES `servico` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `horarios`
--

LOCK TABLES `horarios` WRITE;
/*!40000 ALTER TABLE `horarios` DISABLE KEYS */;
/*!40000 ALTER TABLE `horarios` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-06-05  9:41:50
