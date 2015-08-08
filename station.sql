-- MySQL dump 10.13  Distrib 5.6.14, for osx10.7 (x86_64)
--
-- Host: localhost    Database: geeklogistics
-- ------------------------------------------------------
-- Server version	5.6.14

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
-- Table structure for table `station_station`
--

DROP TABLE IF EXISTS `station_station`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `station_station` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(30) NOT NULL,
  `password` varchar(30) NOT NULL,
  `name` varchar(30) NOT NULL,
  `address` varchar(50) NOT NULL,
  `phone` varchar(30) DEFAULT NULL,
  `latitude` double NOT NULL,
  `longitude` double NOT NULL,
  `image` varchar(100) DEFAULT NULL,
  `ctime` datetime NOT NULL,
  `utime` datetime NOT NULL,
  `status` varchar(3) NOT NULL,
  `station_type` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `station_station`
--

LOCK TABLES `station_station` WRITE;
/*!40000 ALTER TABLE `station_station` DISABLE KEYS */;
INSERT INTO `station_station` VALUES (1,'huagonglu','123456','化工路店','北京市朝阳区东四环南路16号','400-8870-387',39.889161,116.498999,'','2015-07-30 19:00:05','2015-07-30 19:00:05','0',0),(2,'tianshuiyuan','123456','甜水园店','北京市朝阳区延静里6号楼后','400-8870-387',39.929696,116.485411,'','2015-07-30 19:00:05','2015-07-30 19:00:05','0',0),(3,'cuiweilu','123456','翠微路店','北京市海淀区翠微小区4号楼附近','400-8870-387',39.920893,116.305623,'','2015-07-30 19:00:05','2015-07-30 19:00:05','0',0),(4,'dongdajie','123456','东大街店','北京市丰台区东大街42号附近','400-8870-387',39.861545,116.300324,'','2015-07-30 19:00:05','2015-07-30 19:00:05','0',0),(5,'banjing','123456','板井店','北京市海淀区昆明湖南路72号附近','400-8870-387',39.954959,116.297409,'','2015-07-30 19:00:05','2015-07-30 19:00:05','0',0),(6,'beishatanqiao','123456','北沙滩桥店','北京市海淀区清华东路4号','400-8870-387',40.007195,116.374846,'','2015-07-30 19:00:05','2015-07-30 19:00:05','0',0),(7,'songjiazhuang','123456','宋家庄店','北京市丰台区东铁匠营横七条五间楼1号','400-8870-387',39.856278,116.429517,'','2015-07-30 19:00:05','2015-07-30 19:00:05','0',0),(8,'dongfengbeiqiao','123456','东风北桥店','北京市朝阳区酒仙桥11街坊15号楼','400-8870-387',39.966706,116.498769,'','2015-07-30 19:00:05','2015-07-30 19:00:05','0',0),(9,'xinfadi','123456','新发地店','北京市丰台区宜兰园2期','400-8870-387',39.83346,116.344347,'','2015-07-30 19:00:05','2015-07-30 19:00:05','0',0),(10,'wangsiying','123456','王四营店','北京市朝阳区高碑店王四营桥北同盛轩艺术馆','400-8870-387',39.87781,116.537398,'','2015-07-30 19:00:05','2015-07-30 19:00:05','0',0),(11,'daxing','123456','极客总部-北京极客罗杰斯特有限公司','北京市大兴区黄村镇前大营村','400-8870-387',39.691099,116.373053,'','2015-08-01 20:59:18','2015-08-01 20:59:18','0',1),(12,'liyuan','123456','梨园店','北京市通州区云景南大街144号','400-8870-387',39.884509,116.653036,'','2015-08-07 18:44:33','2015-08-07 18:44:33','0',0),(13,'shijingshan','123456','石景山店','北京市石景山区古城南大街52号','400-8870-387',39.908277,116.194133,'','2015-08-07 18:44:33','2015-08-07 18:44:33','0',0),(14,'lishuiqiqao','123456','立水桥店','北京市昌平区陈营村卫生院旁','400-8870-387',40.052294,116.41828,'','2015-08-07 18:44:33','2015-08-07 18:44:33','0',0),(15,'shungqiao','123456','双桥店','北京市朝阳区双桥第一小学分校 ','400-8870-387',39.907945,116.588187,'','2015-08-07 18:44:33','2015-08-07 18:44:33','0',0);
/*!40000 ALTER TABLE `station_station` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2015-08-08 23:23:31
