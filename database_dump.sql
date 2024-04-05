CREATE DATABASE  IF NOT EXISTS `mse` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `mse`;
-- MySQL dump 10.13  Distrib 8.0.34, for Win64 (x86_64)
--
-- Host: 10.10.2.8    Database: mse
-- ------------------------------------------------------
-- Server version	8.0.36

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
-- Table structure for table `answer`
--

DROP TABLE IF EXISTS `answer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `answer` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `text` varchar(200) NOT NULL,
  `votes` int DEFAULT NULL,
  `is_right` tinyint(1) NOT NULL,
  `question_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `answer_question_id_523c1648_fk_question_id` (`question_id`),
  CONSTRAINT `answer_question_id_523c1648_fk_question_id` FOREIGN KEY (`question_id`) REFERENCES `question` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `answer`
--

LOCK TABLES `answer` WRITE;
/*!40000 ALTER TABLE `answer` DISABLE KEYS */;
/*!40000 ALTER TABLE `answer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
INSERT INTO `auth_group` VALUES (1,'administrator');
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
INSERT INTO `auth_group_permissions` VALUES (1,1,1),(2,1,2),(3,1,3),(4,1,4),(5,1,5),(6,1,6),(7,1,7),(8,1,8),(9,1,9),(10,1,10),(11,1,11),(12,1,12),(13,1,13),(14,1,14),(15,1,15),(16,1,16),(17,1,17),(18,1,18),(19,1,19),(20,1,20),(21,1,21),(22,1,22),(23,1,23),(24,1,24);
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=51 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add user',4,'add_user'),(14,'Can change user',4,'change_user'),(15,'Can delete user',4,'delete_user'),(16,'Can view user',4,'view_user'),(17,'Can add content type',5,'add_contenttype'),(18,'Can change content type',5,'change_contenttype'),(19,'Can delete content type',5,'delete_contenttype'),(20,'Can view content type',5,'view_contenttype'),(21,'Can add session',6,'add_session'),(22,'Can change session',6,'change_session'),(23,'Can delete session',6,'delete_session'),(24,'Can view session',6,'view_session'),(25,'Can add subject',7,'add_subject'),(26,'Can change subject',7,'change_subject'),(27,'Can delete subject',7,'delete_subject'),(28,'Can view subject',7,'view_subject'),(29,'Can add question',8,'add_question'),(30,'Can change question',8,'change_question'),(31,'Can delete question',8,'delete_question'),(32,'Can view question',8,'view_question'),(33,'Can add choice',9,'add_choice'),(34,'Can change choice',9,'change_choice'),(35,'Can delete choice',9,'delete_choice'),(36,'Can view choice',9,'view_choice'),(37,'Can add answer',10,'add_answer'),(38,'Can change answer',10,'change_answer'),(39,'Can delete answer',10,'delete_answer'),(40,'Can view answer',10,'view_answer'),(41,'Can add exam',11,'add_exam'),(42,'Can change exam',11,'change_exam'),(43,'Can delete exam',11,'delete_exam'),(44,'Can view exam',11,'view_exam'),(45,'Can add exam question',12,'add_examquestion'),(46,'Can change exam question',12,'change_examquestion'),(47,'Can delete exam question',12,'delete_examquestion'),(48,'Can view exam question',12,'view_examquestion'),(49,'Import question',8,'import_question'),(50,'Create exam',11,'create_exam');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$720000$8yLKcWm3wDnJVtBdjMBCCo$Mf+nVGhv20Ag7z8SCRfC+MXw1qR9VJ515AhOkJ2ZX44=','2024-04-05 12:53:26.473467',1,'tuanna','Ngô Anh','Tuấn','tuan23mse13141@fsb.edu.vn',1,1,'2024-02-06 02:23:04.000000'),(2,'pbkdf2_sha256$720000$f1IYLRnDCUPKM6AX0xTITi$68rq/Fmq1kPnb0VpucFuorB9NJ33d0C8TdZZiwzrH7M=','2024-02-23 13:28:32.292413',0,'cuongnm','','','cuongnm@gmail.com',1,1,'2024-02-23 13:17:34.000000');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2024-02-06 02:25:15.578660','1','administrator',1,'[{\"added\": {}}]',3,1),(2,'2024-02-06 07:49:28.073652','1','tuanna',2,'[{\"changed\": {\"fields\": [\"First name\", \"Last name\"]}}]',4,1),(3,'2024-02-06 07:49:44.788207','1','tuanna',2,'[{\"changed\": {\"fields\": [\"First name\"]}}]',4,1),(4,'2024-02-23 13:17:35.118458','2','cuongnm',1,'[{\"added\": {}}]',4,1),(5,'2024-02-23 13:18:18.520954','2','cuongnm',2,'[{\"changed\": {\"fields\": [\"User permissions\"]}}]',4,1),(6,'2024-02-23 13:19:12.438243','2','cuongnm',2,'[{\"changed\": {\"fields\": [\"Staff status\"]}}]',4,1),(7,'2024-02-23 13:23:39.648645','2','cuongnm',2,'[{\"changed\": {\"fields\": [\"Email address\"]}}]',4,1),(8,'2024-02-23 13:25:31.235373','2','cuongnm',2,'[{\"changed\": {\"fields\": [\"User permissions\"]}}]',4,1);
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(5,'contenttypes','contenttype'),(10,'Quiz','answer'),(9,'Quiz','choice'),(11,'Quiz','exam'),(12,'Quiz','examquestion'),(8,'Quiz','question'),(7,'Quiz','subject'),(6,'sessions','session');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=36 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2024-02-06 02:15:16.525848'),(2,'auth','0001_initial','2024-02-06 02:15:22.974423'),(3,'admin','0001_initial','2024-02-06 02:15:24.409773'),(4,'admin','0002_logentry_remove_auto_add','2024-02-06 02:15:24.508886'),(5,'admin','0003_logentry_add_action_flag_choices','2024-02-06 02:15:24.612993'),(6,'contenttypes','0002_remove_content_type_name','2024-02-06 02:15:25.686462'),(7,'auth','0002_alter_permission_name_max_length','2024-02-06 02:15:26.319659'),(8,'auth','0003_alter_user_email_max_length','2024-02-06 02:15:26.858086'),(9,'auth','0004_alter_user_username_opts','2024-02-06 02:15:26.967497'),(10,'auth','0005_alter_user_last_login_null','2024-02-06 02:15:27.435343'),(11,'auth','0006_require_contenttypes_0002','2024-02-06 02:15:27.529577'),(12,'auth','0007_alter_validators_add_error_messages','2024-02-06 02:15:27.631686'),(13,'auth','0008_alter_user_username_max_length','2024-02-06 02:15:28.185608'),(14,'auth','0009_alter_user_last_name_max_length','2024-02-06 02:15:28.732085'),(15,'auth','0010_alter_group_name_max_length','2024-02-06 02:15:29.293419'),(16,'auth','0011_update_proxy_permissions','2024-02-06 02:15:29.614050'),(17,'auth','0012_alter_user_first_name_max_length','2024-02-06 02:15:30.224310'),(18,'sessions','0001_initial','2024-02-06 02:15:30.801785'),(19,'Quiz','0001_initial','2024-02-19 01:35:45.982472'),(20,'Quiz','0002_subject_unique_appversion','2024-02-19 12:36:40.571407'),(21,'Quiz','0003_question_choice','2024-02-20 03:42:16.515932'),(22,'Quiz','0004_rename_group_question_subjects','2024-02-20 03:48:39.439305'),(23,'Quiz','0002_remove_question_subject_delete_choice_and_more','2024-02-20 06:32:26.455316'),(24,'Quiz','0002_question_choice','2024-02-20 06:35:41.174182'),(25,'Quiz','0003_alter_question_subject','2024-02-20 06:47:31.341388'),(26,'Quiz','0004_alter_subject_create_date','2024-02-20 07:45:41.097244'),(27,'Quiz','0005_question_image_url_alter_question_subject','2024-02-20 09:07:05.404336'),(28,'Quiz','0006_answer_delete_choice','2024-02-21 01:08:58.461083'),(29,'Quiz','0007_question_image_name','2024-02-21 01:11:01.602759'),(30,'Quiz','0008_answer_point','2024-02-21 01:12:14.952799'),(31,'Quiz','0009_remove_answer_is_mix_remove_answer_point_and_more','2024-02-21 01:37:48.021695'),(32,'Quiz','0010_exam_examquestion_exam_questions','2024-02-22 01:41:32.291691'),(33,'Quiz','0011_rename_create_by_exam_create_user','2024-02-22 02:19:28.541742'),(34,'Quiz','0012_exam_unique_exam_code','2024-02-22 04:39:59.641125'),(35,'Quiz','0013_alter_answer_votes_alter_question_image_name_and_more','2024-02-22 06:05:34.119386');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('4809q7nfq39ges213sqmc1kzkn07gxn1','.eJxVjMsOwiAQRf-FtSFMeBWX7v0GMsOAVA0kpV0Z_12bdKHbe865LxFxW2vcRl7izOIsQJx-N8L0yG0HfMd26zL1ti4zyV2RBx3y2jk_L4f7d1Bx1G9t0CkCUqXoAMknO4ViQZdE4DOg0VrB5CyTT5l1ZhccFwzGeaairRfvD-kGODo:1rshNA:o_M8RHG_VcUjEM7ERJu0gkKW1o_fStuKldXtOkBtBKs','2024-04-19 11:04:40.321959'),('7utnft2pvki9qzwqlyc5ol7pwgx7sdk9','.eJxVjMsOwiAQRf-FtSFMeBWX7v0GMsOAVA0kpV0Z_12bdKHbe865LxFxW2vcRl7izOIsQJx-N8L0yG0HfMd26zL1ti4zyV2RBx3y2jk_L4f7d1Bx1G9t0CkCUqXoAMknO4ViQZdE4DOg0VrB5CyTT5l1ZhccFwzGeaairRfvD-kGODo:1rsgsF:iYc3Lr4aXa9E2iykdrDxkGZt2lqGG7GWLSRnoeMkyjI','2024-04-19 10:32:43.221571'),('adjktijgat1oapk0zlgdc2mub6dbg2rs','.eJxVjMsOwiAQRf-FtSFMeBWX7v0GMsOAVA0kpV0Z_12bdKHbe865LxFxW2vcRl7izOIsQJx-N8L0yG0HfMd26zL1ti4zyV2RBx3y2jk_L4f7d1Bx1G9t0CkCUqXoAMknO4ViQZdE4DOg0VrB5CyTT5l1ZhccFwzGeaairRfvD-kGODo:1rsfnG:HbExti5R49yE2Fo9SdRuzpWAvnQe3-GI5AfAgQF48f0','2024-04-19 09:23:30.623432'),('etk7nlt641ic2relhqbxu4b3tlrqc12r','.eJxVjMsOwiAQRf-FtSFMeBWX7v0GMsOAVA0kpV0Z_12bdKHbe865LxFxW2vcRl7izOIsQJx-N8L0yG0HfMd26zL1ti4zyV2RBx3y2jk_L4f7d1Bx1G9t0CkCUqXoAMknO4ViQZdE4DOg0VrB5CyTT5l1ZhccFwzGeaairRfvD-kGODo:1rsNQb:_ChK1EB0yfuJAH8FZFLZDKiDjxxeK9LsRaDWaOFmiUY','2024-04-18 13:46:53.676825'),('h5ecu0j0e7fmf4bqpd5w1c7mkpclgfgu','.eJxVjMsOwiAQRf-FtSFMeBWX7v0GMsOAVA0kpV0Z_12bdKHbe865LxFxW2vcRl7izOIsQJx-N8L0yG0HfMd26zL1ti4zyV2RBx3y2jk_L4f7d1Bx1G9t0CkCUqXoAMknO4ViQZdE4DOg0VrB5CyTT5l1ZhccFwzGeaairRfvD-kGODo:1rsj4Q:zD7jHREzJ7c9amTKmv0vRAwWPSyB-D-v712mwsFDC7k','2024-04-19 12:53:26.475171'),('m707w1ihwiem6p9495h4xa4stdm0ri5m','.eJxVjMsOwiAQRf-FtSFMeBWX7v0GMsOAVA0kpV0Z_12bdKHbe865LxFxW2vcRl7izOIsQJx-N8L0yG0HfMd26zL1ti4zyV2RBx3y2jk_L4f7d1Bx1G9t0CkCUqXoAMknO4ViQZdE4DOg0VrB5CyTT5l1ZhccFwzGeaairRfvD-kGODo:1rcIXP:ezkHgvmV5zsxto12OWXm4IrLYCXqg0mKNuOmbUHOykE','2024-03-05 05:19:27.815712'),('okhg4zwclww47htt10rnxnqf91fpeb3t','.eJxVjMsOwiAQRf-FtSFMeBWX7v0GMsOAVA0kpV0Z_12bdKHbe865LxFxW2vcRl7izOIsQJx-N8L0yG0HfMd26zL1ti4zyV2RBx3y2jk_L4f7d1Bx1G9t0CkCUqXoAMknO4ViQZdE4DOg0VrB5CyTT5l1ZhccFwzGeaairRfvD-kGODo:1rsI4I:78hUGJJ3pitO7WiZ9jFPVfFBhjhUwRKpTVYe_IFh-0I','2024-04-18 08:03:30.655110'),('pfkqo99wb77b0jxpqpidxte2zxhe1cna','.eJxVjMsOwiAQRf-FtSFMeBWX7v0GMsOAVA0kpV0Z_12bdKHbe865LxFxW2vcRl7izOIsQJx-N8L0yG0HfMd26zL1ti4zyV2RBx3y2jk_L4f7d1Bx1G9t0CkCUqXoAMknO4ViQZdE4DOg0VrB5CyTT5l1ZhccFwzGeaairRfvD-kGODo:1rsfyX:_7NVxZ3FS5jvq3XnJzZ2SYmHNAUuAjpVVXJUdJF3z-k','2024-04-19 09:35:09.318343'),('ql07ow42ffmq6an4tgvwk2tgfi3f3dce','.eJxVjMsOwiAQRf-FtSFMeBWX7v0GMsOAVA0kpV0Z_12bdKHbe865LxFxW2vcRl7izOIsQJx-N8L0yG0HfMd26zL1ti4zyV2RBx3y2jk_L4f7d1Bx1G9t0CkCUqXoAMknO4ViQZdE4DOg0VrB5CyTT5l1ZhccFwzGeaairRfvD-kGODo:1rdVnO:7gVYGTa1eC1roTb1QvfSlHK12V4qp7w3tUJ8Tw-aAOE','2024-03-08 13:40:58.013915'),('wo15tpf2m1ynycvxgubyosx16yilck8z','.eJxVjMsOwiAQRf-FtSFMeBWX7v0GMsOAVA0kpV0Z_12bdKHbe865LxFxW2vcRl7izOIsQJx-N8L0yG0HfMd26zL1ti4zyV2RBx3y2jk_L4f7d1Bx1G9t0CkCUqXoAMknO4ViQZdE4DOg0VrB5CyTT5l1ZhccFwzGeaairRfvD-kGODo:1rsNUS:tef-_eSHVL12LMDzpfBN1I-_fU83u_btLdZ0Q0d7VSs','2024-04-18 13:50:52.953524'),('zh8cr184pxzq8h0del1nfhy8gbdeoc8h','.eJxVjMsOwiAQRf-FtSFMeBWX7v0GMsOAVA0kpV0Z_12bdKHbe865LxFxW2vcRl7izOIsQJx-N8L0yG0HfMd26zL1ti4zyV2RBx3y2jk_L4f7d1Bx1G9t0CkCUqXoAMknO4ViQZdE4DOg0VrB5CyTT5l1ZhccFwzGeaairRfvD-kGODo:1rsO0T:8NBcDLRIOB7eUY3vHeIL8ep12awrNuf-ioxjvD1pcSs','2024-04-18 14:23:57.229266'),('zzgnu9zqaf0cinnh1s4qy1rg802mve9c','.eJxVjMsOwiAQRf-FtSFMeBWX7v0GMsOAVA0kpV0Z_12bdKHbe865LxFxW2vcRl7izOIsQJx-N8L0yG0HfMd26zL1ti4zyV2RBx3y2jk_L4f7d1Bx1G9t0CkCUqXoAMknO4ViQZdE4DOg0VrB5CyTT5l1ZhccFwzGeaairRfvD-kGODo:1rsY1X:oe21hkExWAuIYFg3XOjISv3fMnkAAQrsz6DvqxT7mkQ','2024-04-19 01:05:43.917199');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `exam`
--

DROP TABLE IF EXISTS `exam`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `exam` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `code` varchar(20) NOT NULL,
  `duration` int NOT NULL,
  `num_question` int NOT NULL,
  `create_date` datetime(6) NOT NULL,
  `create_user_id` int NOT NULL,
  `subject_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `unique_exam_code` (`code`),
  KEY `exam_subject_id_3be84281_fk_subject_id` (`subject_id`),
  KEY `exam_create_user_id_5ba8a4b9_fk_auth_user_id` (`create_user_id`),
  CONSTRAINT `exam_create_user_id_5ba8a4b9_fk_auth_user_id` FOREIGN KEY (`create_user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `exam_subject_id_3be84281_fk_subject_id` FOREIGN KEY (`subject_id`) REFERENCES `subject` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `exam`
--

LOCK TABLES `exam` WRITE;
/*!40000 ALTER TABLE `exam` DISABLE KEYS */;
INSERT INTO `exam` VALUES (4,'EX4',30,4,'2024-02-22 06:47:20.477786',1,3),(5,'Ex7',30,4,'2024-02-22 06:48:48.807946',1,3),(11,'EX8',30,2,'2024-02-23 11:09:58.423059',1,3),(12,'VL001',30,3,'2024-02-23 13:22:24.070339',1,3);
/*!40000 ALTER TABLE `exam` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `exam_question`
--

DROP TABLE IF EXISTS `exam_question`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `exam_question` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `order` int NOT NULL,
  `exam_id` bigint NOT NULL,
  `question_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `exam_question_exam_id_e32fc5a5_fk_exam_id` (`exam_id`),
  KEY `exam_question_question_id_2a08bd39_fk_question_id` (`question_id`),
  CONSTRAINT `exam_question_exam_id_e32fc5a5_fk_exam_id` FOREIGN KEY (`exam_id`) REFERENCES `exam` (`id`),
  CONSTRAINT `exam_question_question_id_2a08bd39_fk_question_id` FOREIGN KEY (`question_id`) REFERENCES `question` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `exam_question`
--

LOCK TABLES `exam_question` WRITE;
/*!40000 ALTER TABLE `exam_question` DISABLE KEYS */;
INSERT INTO `exam_question` VALUES (4,1,11,6),(5,2,11,7),(6,1,12,6),(7,2,12,28),(8,3,12,27);
/*!40000 ALTER TABLE `exam_question` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `question`
--

DROP TABLE IF EXISTS `question`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `question` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `text` varchar(200) NOT NULL,
  `subject_id` bigint NOT NULL,
  `image_url` varchar(200) DEFAULT NULL,
  `image_name` varchar(200) DEFAULT NULL,
  `is_mix` tinyint(1) NOT NULL,
  `point` double NOT NULL,
  `unit` varchar(30) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `question_subject_id_100787eb_fk_subject_id` (`subject_id`),
  CONSTRAINT `question_subject_id_100787eb_fk_subject_id` FOREIGN KEY (`subject_id`) REFERENCES `subject` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=31 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `question`
--

LOCK TABLES `question` WRITE;
/*!40000 ALTER TABLE `question` DISABLE KEYS */;
INSERT INTO `question` VALUES (6,'dsfhsdkfhsd',3,'1123.jpg','1123.jpg',1,0.5,'Chapter 1'),(7,'fgghfg',3,'123.png','f',1,1,'Chapter 1'),(24,'See the figure and choose the right type of B2B E-Commerce\n[file:8435.jpg]\n',5,'','upload/23022024_195933/image/8435.jpg',1,1,'Chapter1'),(27,'See the figure and choose the right type of B2B E-Commerce\n[file:8435.jpg]\n',3,'','upload/23022024_200501/image/8435.jpg',1,1,'Chapter1'),(28,'See the figure and choose the right type of B2B E-Commerce\n[file: 2.jpg]\n',3,'','upload/23022024_200501/image/2.jpg',1,1,'Chapter1'),(29,'See the figure and choose the right type of B2B E-Commerce\n[file:8435.jpg]\n',3,'','upload/23022024_204158/image/8435.jpg',1,1,'Chapter1'),(30,'See the figure and choose the right type of B2B E-Commerce\n[file: 2.jpg]\n',3,'','upload/23022024_204158/image/2.jpg',1,1,'Chapter1');
/*!40000 ALTER TABLE `question` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `subject`
--

DROP TABLE IF EXISTS `subject`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `subject` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `code` varchar(20) NOT NULL,
  `name` varchar(100) NOT NULL,
  `create_date` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `unique appversion` (`code`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `subject`
--

LOCK TABLES `subject` WRITE;
/*!40000 ALTER TABLE `subject` DISABLE KEYS */;
INSERT INTO `subject` VALUES (3,'VL','Vật lý 1','2024-02-19 12:35:31.700657'),(5,'T','Toán','2024-02-20 14:36:58.000000'),(6,'EN','Tiếng Anh','2024-02-20 15:43:28.648855');
/*!40000 ALTER TABLE `subject` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-04-05 20:07:44
