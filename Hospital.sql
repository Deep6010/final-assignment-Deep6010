-- MySQL dump 10.13  Distrib 8.0.20, for Win64 (x86_64)
--
-- Host: localhost    Database: hospital_management
-- ------------------------------------------------------
-- Server version	8.0.20

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
-- Dumping data for table `appointment_detail`
--

LOCK TABLES `appointment_detail` WRITE;
/*!40000 ALTER TABLE `appointment_detail` DISABLE KEYS */;
INSERT INTO `appointment_detail` VALUES (1,'101',1,'Raju chaudary',1,'Abnish','2020-09-30','3 p.m.'),(2,'102',3,'Sikha Jha',2,'Abnish','2020-09-14','11 am');
/*!40000 ALTER TABLE `appointment_detail` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `doctor_detail`
--

LOCK TABLES `doctor_detail` WRITE;
/*!40000 ALTER TABLE `doctor_detail` DISABLE KEYS */;
INSERT INTO `doctor_detail` VALUES (1,'Raju Chaudhary ','8am-2pm','gastroenterology','MBBS','9876563367','Janakpur'),(2,'Hari Bahadur','10am-4pm','gynecologist','PHD','986625562','Kathmandu'),(3,'Sikha Jha','9am-3pm','physician consultant','MBBS','9817786653','Pepsicola,Ktm');
/*!40000 ALTER TABLE `doctor_detail` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `login`
--

LOCK TABLES `login` WRITE;
/*!40000 ALTER TABLE `login` DISABLE KEYS */;
INSERT INTO `login` VALUES ('deep','1234');
/*!40000 ALTER TABLE `login` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `patient_detail`
--

LOCK TABLES `patient_detail` WRITE;
/*!40000 ALTER TABLE `patient_detail` DISABLE KEYS */;
INSERT INTO `patient_detail` VALUES (1,'Rohit','25','male','9817640005','Janakpur','Apandix'),(2,'Abnish','20','male','9819882546','Bhamarpura','lungs problem '),(3,'Rahul','26','male','9819882545','Madan','Skin problem');
/*!40000 ALTER TABLE `patient_detail` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-09-30 14:14:43
