-- MySQL dump 10.13  Distrib 5.7.17, for Linux (i686)
--
-- Host: localhost    Database: projectx
-- ------------------------------------------------------
-- Server version	5.7.17-0ubuntu0.16.04.2

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `co_filetable`
--

DROP TABLE IF EXISTS `co_filetable`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `co_filetable` (
  `cid` int(11) NOT NULL AUTO_INCREMENT,
  `co_name` varchar(30) NOT NULL,
  `nameoffile` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`cid`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `co_filetable`
--

LOCK TABLES `co_filetable` WRITE;
/*!40000 ALTER TABLE `co_filetable` DISABLE KEYS */;
INSERT INTO `co_filetable` VALUES (1,'comte','co_files/comte.txt'),(2,'comtest','co_files/comtest.txt'),(3,'new_co','co_files/new_co.txt'),(4,'ano_new_stu','co_files/ano_new_stu.txt'),(5,'co1','co_files/co1.txt'),(6,'newcoo','co_files/newcoo.txt'),(7,'elecom','co_files/elecom.txt'),(8,'djasld','co_files/djasld.txt'),(9,'neco','co_files/neco.txt'),(10,'fincom1','co_files/fincom1.txt'),(11,'fincom2','co_files/fincom2.txt');
/*!40000 ALTER TABLE `co_filetable` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `company`
--

DROP TABLE IF EXISTS `company`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `company` (
  `cid` int(11) NOT NULL AUTO_INCREMENT,
  `co_name` varchar(30) DEFAULT NULL,
  `link` varchar(70) DEFAULT NULL,
  `num` int(11) DEFAULT NULL,
  `field` varchar(30) DEFAULT NULL,
  `email` varchar(40) DEFAULT NULL,
  `password` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`cid`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `company`
--

LOCK TABLES `company` WRITE;
/*!40000 ALTER TABLE `company` DISABLE KEYS */;
INSERT INTO `company` VALUES (1,'here again','http://127.0.0.1:5000/register_stu/',4,'field','sljdlsa@som','pass'),(2,'newone','http://127.0.0.1:5000/register_stu/',6,'new','newon@lj','pass'),(3,'com','panyhttp://127.0.0.1:5000/register/',3,'dub','hub@d','pass'),(6,'comte','http://127.0.0.1:5000/register/',2,'dsla','slak@sad','pass'),(9,'comtest','http://127.0.0.1:5000/register/',3,'ldfs;','fldja@ldjs','pass'),(10,'new_co','http://127.0.0.1:5000/register/',3,'cs','lsjd@ldsjl','pass'),(11,'ano_new_stu','http://127.0.0.1:5000/register/',3,'cs','sldj@ljs','pass'),(12,'co1','http://127.0.0.1:5000/register/',-5,'elec','lsjfld@lksd','pass'),(13,'newcoo','http://127.0.0.1:5000/register/',2,'cs','lsdjf@lslds','pass'),(14,'elecom','http://127.0.0.1:5000/register/',3,'ele','lsjlsd@lskjas','pass'),(15,'djasld','http://127.0.0.1:5000/register/',2,'elec','ldjasl@jas','pass'),(16,'neco','http://127.0.0.1:5000/register/',1,'elec','ldjllds@ldsjladkjlasj','pass'),(17,'fincom1','https://fmovies.se/',2,'final','fincom1@none','pass'),(18,'fincom2','https://fmovies.se/',2,'final','fincom2@none','pass');
/*!40000 ALTER TABLE `company` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `stu_filetable`
--

DROP TABLE IF EXISTS `stu_filetable`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `stu_filetable` (
  `userid` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(30) NOT NULL,
  `nameoffile` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`userid`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `stu_filetable`
--

LOCK TABLES `stu_filetable` WRITE;
/*!40000 ALTER TABLE `stu_filetable` DISABLE KEYS */;
INSERT INTO `stu_filetable` VALUES (1,'teststu','stu_files/teststu.txt'),(2,'stud','stu_files/stud.txt'),(3,'newstu','stu_files/newstu.txt'),(4,'stu1','stu_files/stu1.txt'),(5,'newwala','stu_files/newwala.txt'),(6,'psfs','stu_files/psfs.txt'),(7,'dsfkd','stu_files/dsfkd.txt'),(8,'fdlkjas','stu_files/fdlkjas.txt'),(9,'finstu1','stu_files/finstu1.txt'),(10,'finstu2','stu_files/finstu2.txt');
/*!40000 ALTER TABLE `stu_filetable` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `users` (
  `uid` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(30) NOT NULL,
  `preference` varchar(30) DEFAULT NULL,
  `dob` varchar(30) DEFAULT NULL,
  `email` varchar(30) DEFAULT NULL,
  `password` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`uid`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'rel','pel','07/9/2017','relpel','rel'),(2,'','','','',''),(3,'hey','pee','09/04/1997','ldi@ye','see'),(4,'hy','lsjd','hjlj','lsj@laj','kok'),(5,'neo','matrix','deo','new@s','pass'),(6,'stu','ai','ent ','hun@m','pass'),(8,'teststu','test','ldjs','dslj@ljsl','pass'),(9,'stud','pre','lakjd','jlasa@lds','pass'),(10,'newstu','cs','lsjslk','alkdsj@lsajd','pass'),(11,'stu1','elec','lkajsd','lasdj@lasdf','pass'),(12,'newwala','ele','lkjsdl','ladsjf@ldsls','pass'),(15,'psfs','elec','ldjf','ldjf@kldsj','pass'),(16,'dsfkd','elec','djlal','lfldsk@ldsf','pass'),(17,'fdlkjas','elec','jfldsdasl','ldsjlsdlal@lds','pass'),(18,'finstu1','final','09/05/1919','fin@stu1','pass'),(19,'finstu2','final','09/03/1882','finstu@hun','pass');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2017-04-27 22:02:33
