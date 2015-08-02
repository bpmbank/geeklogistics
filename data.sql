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
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can add permission',2,'add_permission'),(5,'Can change permission',2,'change_permission'),(6,'Can delete permission',2,'delete_permission'),(7,'Can add group',3,'add_group'),(8,'Can change group',3,'change_group'),(9,'Can delete group',3,'delete_group'),(10,'Can add user',4,'add_user'),(11,'Can change user',4,'change_user'),(12,'Can delete user',4,'delete_user'),(13,'Can add content type',5,'add_contenttype'),(14,'Can change content type',5,'change_contenttype'),(15,'Can delete content type',5,'delete_contenttype'),(16,'Can add session',6,'add_session'),(17,'Can change session',6,'change_session'),(18,'Can delete session',6,'delete_session'),(19,'Can add detail',7,'add_detail'),(20,'Can change detail',7,'change_detail'),(21,'Can delete detail',7,'delete_detail'),(22,'Can add 订单',8,'add_order'),(23,'Can change 订单',8,'change_order'),(24,'Can delete 订单',8,'delete_order'),(25,'Can add 配送员',9,'add_dispatcher'),(26,'Can change 配送员',9,'change_dispatcher'),(27,'Can delete 配送员',9,'delete_dispatcher'),(28,'Can add 商家',10,'add_merchant'),(29,'Can change 商家',10,'change_merchant'),(30,'Can delete 商家',10,'delete_merchant'),(31,'Can add 展示商家',11,'add_show'),(32,'Can change 展示商家',11,'change_show'),(33,'Can delete 展示商家',11,'delete_show'),(34,'Can add 新闻',12,'add_news'),(35,'Can change 新闻',12,'change_news'),(36,'Can delete 新闻',12,'delete_news'),(37,'Can add 配送点',13,'add_station'),(38,'Can change 配送点',13,'change_station'),(39,'Can delete 配送点',13,'delete_station'),(40,'Can add status record',14,'add_statusrecord'),(41,'Can change status record',14,'change_statusrecord'),(42,'Can delete status record',14,'delete_statusrecord'),(43,'Can add 司机',15,'add_driver'),(44,'Can change 司机',15,'change_driver'),(45,'Can delete 司机',15,'delete_driver');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$12000$Umqs3bP4Cdzs$G/8+lDrTDWVr6C3c0CEo9L3puCdFLmUv6JbMlnUD4mY=','2015-07-24 11:14:44',1,'admin','','','',1,1,'2015-07-13 11:48:30');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `deliver_dispatcher`
--

LOCK TABLES `deliver_dispatcher` WRITE;
/*!40000 ALTER TABLE `deliver_dispatcher` DISABLE KEYS */;
INSERT INTO `deliver_dispatcher` VALUES (1,'001','夏茉莉','123456','0','18768119089','static/images/dispatcher/me2.jpg','2015-07-28 17:14:21','2015-07-28 17:14:21','0');
/*!40000 ALTER TABLE `deliver_dispatcher` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `deliver_driver`
--

LOCK TABLES `deliver_driver` WRITE;
/*!40000 ALTER TABLE `deliver_driver` DISABLE KEYS */;
INSERT INTO `deliver_driver` VALUES (1,'001','何小豆','123456','0','18310508575','','2015-08-01 16:46:11','2015-08-01 16:46:11','0');
/*!40000 ALTER TABLE `deliver_driver` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2015-07-13 12:10:07',1,9,'1','001',1,''),(2,'2015-07-13 12:10:33',1,8,'1','123456',2,'已修改 order_id，deliver_id 和 dispatcher 。'),(3,'2015-07-13 14:10:45',1,10,'1','星巴克',1,''),(4,'2015-07-13 14:10:51',1,11,'1','星巴克',1,''),(5,'2015-07-13 14:12:07',1,13,'1','大兴站',1,''),(6,'2015-07-13 14:13:40',1,13,'2','望京站',1,''),(7,'2015-07-13 14:14:19',1,13,'3','知春路站',1,''),(8,'2015-07-13 14:15:06',1,12,'1','极客冷链配7月20日上线啦！',1,''),(9,'2015-07-24 11:22:53',1,13,'1','化工路店',1,''),(10,'2015-07-24 11:28:56',1,10,'1','洋葱达人',1,''),(11,'2015-07-24 11:31:44',1,10,'1','洋葱达人',2,'已修改 latitude 和 longitude 。'),(12,'2015-07-24 11:33:51',1,13,'2','甜水园店',1,''),(13,'2015-07-24 11:42:26',1,13,'2','甜水园店',2,'已修改 address 。'),(14,'2015-07-24 11:42:42',1,11,'1','洋葱达人',1,''),(15,'2015-07-24 11:44:17',1,10,'2','星巴克',1,''),(16,'2015-07-24 11:44:23',1,11,'2','星巴克',1,''),(17,'2015-07-30 17:46:30',1,12,'2','新的新闻排版来咯～',1,''),(18,'2015-07-30 19:01:29',1,13,'1','化工路店',1,''),(19,'2015-07-30 19:02:07',1,13,'2','甜水园店',1,''),(20,'2015-07-30 19:02:34',1,13,'3','翠微路店',1,''),(21,'2015-07-30 19:02:59',1,13,'4','东大街店',1,''),(22,'2015-07-30 19:03:16',1,13,'5','板井店',1,''),(23,'2015-07-30 19:03:33',1,13,'6','北沙滩桥店',1,''),(24,'2015-07-30 19:03:50',1,13,'7','顺八条店',1,''),(25,'2015-07-30 19:04:06',1,13,'8','东风北桥店',1,''),(26,'2015-07-30 19:04:25',1,13,'9','新发地店',1,''),(27,'2015-07-30 19:04:40',1,13,'10','王四营店',1,''),(28,'2015-07-31 11:04:11',1,13,'3','翠微路店',2,'已修改 latitude 和 longitude 。'),(29,'2015-07-31 11:04:51',1,13,'4','东大街店',2,'已修改 latitude 和 longitude 。'),(30,'2015-07-31 11:07:00',1,13,'5','板井店',2,'已修改 latitude 和 longitude 。'),(31,'2015-07-31 11:07:33',1,13,'6','北沙滩桥店',2,'已修改 latitude 和 longitude 。'),(32,'2015-07-31 11:07:58',1,13,'7','顺八条店',2,'已修改 latitude 和 longitude 。'),(33,'2015-07-31 11:08:24',1,13,'8','东风北桥店',2,'已修改 latitude 和 longitude 。'),(34,'2015-07-31 11:09:05',1,13,'9','新发地店',2,'已修改 latitude 和 longitude 。'),(35,'2015-07-31 11:09:28',1,13,'10','王四营店',2,'已修改 latitude 和 longitude 。'),(36,'2015-07-31 22:51:18',1,8,'1','14382602715',2,'没有字段被修改。'),(37,'2015-08-01 16:47:26',1,15,'1','001',1,'');
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'log entry','admin','logentry'),(2,'permission','auth','permission'),(3,'group','auth','group'),(4,'user','auth','user'),(5,'content type','contenttypes','contenttype'),(6,'session','sessions','session'),(7,'detail','order','detail'),(8,'订单','order','order'),(9,'配送员','deliver','dispatcher'),(10,'商家','poi','merchant'),(11,'展示商家','poi','show'),(12,'新闻','news','news'),(13,'配送点','station','station'),(14,'status record','order','statusrecord'),(15,'司机','deliver','driver');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('732w3odvvjxtyljpela7nz5m5il0dzc0','YjdjMjg1MDYwNGQ0ZTkwODI0MTlmYzM3Y2I0NjJmZmMyNWI0ZmE2Mjp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9pZCI6MX0=','2015-08-07 06:52:25'),('buttnwg1xtkfqqs55fdgl5axf8jhg3p2','YjdjMjg1MDYwNGQ0ZTkwODI0MTlmYzM3Y2I0NjJmZmMyNWI0ZmE2Mjp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9pZCI6MX0=','2015-08-07 11:14:44'),('nbajv6plnclxn93zvzg1qzw893mlteg2','MGM0ZmQ0OWEzZDAwYWRjN2Y0ZmM3ZmI3MDEyMWFjMDBhYjY0ZDU5Yjp7fQ==','2015-08-03 13:51:33'),('s9x2105oabf50pft4b671e82rc08rb42','YjdjMjg1MDYwNGQ0ZTkwODI0MTlmYzM3Y2I0NjJmZmMyNWI0ZmE2Mjp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9pZCI6MX0=','2015-07-30 07:04:01'),('tisoxwx6z6ai5016j2m0z7zon07hjali','YjdjMjg1MDYwNGQ0ZTkwODI0MTlmYzM3Y2I0NjJmZmMyNWI0ZmE2Mjp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9pZCI6MX0=','2015-08-07 08:11:54'),('zwvd8wd8d82fy3rht7f7y9ybuznmuwjt','YjdjMjg1MDYwNGQ0ZTkwODI0MTlmYzM3Y2I0NjJmZmMyNWI0ZmE2Mjp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9pZCI6MX0=','2015-07-27 12:04:08');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `news_news`
--

LOCK TABLES `news_news` WRITE;
/*!40000 ALTER TABLE `news_news` DISABLE KEYS */;
INSERT INTO `news_news` VALUES (1,'极客冷链配7月20日上线啦！','<p>极客冷链啦啦啦啦</p>\r\n\r\n<p>极客冷链啦啦啦啦</p>\r\n\r\n<p>极客冷链啦啦啦啦</p>\r\n\r\n<p>极客冷链啦啦啦啦</p>\r\n\r\n<p>极客冷链啦啦啦啦</p>\r\n','2015-07-13 13:54:47','2015-07-13 13:54:47','0'),(2,'新的新闻排版来咯～','<p><img alt=\"\" src=\"/static/images/upload/20150730174541_1822847975.jpg\" style=\"height:300px; width:480px\" /></p>\r\n\r\n<p>图文混排，</p>\r\n\r\n<p>还有<span style=\"color:#FF0000\">颜色</span>，哈哈哈</p>\r\n','2015-07-30 17:45:32','2015-07-30 17:45:32','0');
/*!40000 ALTER TABLE `news_news` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `order_detail`
--

LOCK TABLES `order_detail` WRITE;
/*!40000 ALTER TABLE `order_detail` DISABLE KEYS */;
INSERT INTO `order_detail` VALUES (24,'','010-57154920','','洋葱达人','北京市大兴区黄村镇前大营村','夏梦丽','18768119089','北京市朝阳区望京花园西区127号楼2105室',0,'0'),(25,'83921748932749','010-57154920','蔬菜','洋葱达人','北京市大兴区黄村镇前大营村','夏梦丽','18768119089','北京市朝阳区望京花园西区127号楼2105室',3,'0'),(26,'632871739821','010-57154920','西瓜','洋葱达人','北京市大兴区黄村镇前大营村','夏','18768119089','望京花园西区',17,'0'),(27,'37281648127','010-57154920','大爷','洋葱达人','北京市大兴区黄村镇前大营村','夏梦丽','18768119089','望京花园西区127号楼2105室',12,'0'),(28,'5362178278','010-57154920','西瓜','洋葱达人','北京市大兴区黄村镇前大营村','何豆豆','18310509089','中关村小区322号楼1单元402室',13,'0.0'),(29,'5362178278.0','010-57154920','西瓜','洋葱达人','北京市大兴区黄村镇前大营村','何豆豆','1.83105098586e+11','中关村小区322号楼1单元402室',13,'0.0'),(30,'5362178278.0','010-57154920','西瓜','洋葱达人','北京市大兴区黄村镇前大营村','何豆豆','1.83105098586e+11','中关村小区322号楼1单元402室',13,'0.0'),(31,'5362178278.0','010-57154920','西瓜','洋葱达人','北京市大兴区黄村镇前大营村','何豆豆','183105098586','中关村小区322号楼1单元402室',13,'0.0'),(32,'5362178278.0','010-57154920','西瓜','洋葱达人','北京市大兴区黄村镇前大营村','何豆豆','183105098586','中关村小区322号楼1单元402室',13,'0.0'),(33,'5362178278','010-57154920','西瓜','洋葱达人','北京市大兴区黄村镇前大营村','何豆豆','183105098586','中关村小区322号楼1单元402室',13,'0.0'),(34,'5362178278','010-57154920','西瓜','洋葱达人','北京市大兴区黄村镇前大营村','何豆豆','183105098586','中关村小区322号楼1单元402室',13,'0.0'),(35,'5362178278','010-57154920','西瓜','洋葱达人','北京市大兴区黄村镇前大营村','何豆豆','183105098586','中关村小区322号楼1单元402室',13,'0.0'),(36,'5362178278','010-57154920','西瓜','洋葱达人','北京市大兴区黄村镇前大营村','何豆豆','183105098586','中关村小区322号楼1单元402室',13,'0');
/*!40000 ALTER TABLE `order_detail` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `order_order`
--

LOCK TABLES `order_order` WRITE;
/*!40000 ALTER TABLE `order_order` DISABLE KEYS */;
INSERT INTO `order_order` VALUES (1,'14382602715',1,NULL,NULL,'','500',1,2,0,27,'0','2015-07-30 20:44:27','2015-07-30 20:44:27','0'),(2,'14384241851',1,NULL,NULL,NULL,'100',9,6,0,28,'0','2015-08-01 18:10:03','2015-08-01 18:10:03','0'),(3,'14384257268',1,NULL,NULL,NULL,'100',9,6,0,29,'0','2015-08-01 18:40:40','2015-08-01 18:40:40','0'),(4,'14384258332',1,NULL,NULL,NULL,'100',9,6,0,30,'0','2015-08-01 18:43:39','2015-08-01 18:43:39','0'),(5,'14384258598',1,NULL,NULL,NULL,'100',9,6,0,31,'0','2015-08-01 18:43:39','2015-08-01 18:43:39','0'),(6,'14384260033',1,NULL,NULL,NULL,'100',9,6,0,32,'0','2015-08-01 18:46:34','2015-08-01 18:46:34','0'),(7,'14384262036',1,NULL,NULL,NULL,'100',9,6,0,33,'0','2015-08-01 18:49:31','2015-08-01 18:49:31','0'),(8,'14384263241',1,NULL,NULL,NULL,'100',9,6,0,34,'0','2015-08-01 18:51:56','2015-08-01 18:51:56','0'),(9,'14384263653',1,NULL,NULL,NULL,'100',9,6,0,35,'0','2015-08-01 18:52:34','2015-08-01 18:52:34','0'),(10,'14384266791',1,NULL,NULL,NULL,'100',9,6,0,36,'0','2015-08-01 18:56:13','2015-08-01 18:56:13','0');
/*!40000 ALTER TABLE `order_order` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `order_statusrecord`
--

LOCK TABLES `order_statusrecord` WRITE;
/*!40000 ALTER TABLE `order_statusrecord` DISABLE KEYS */;
INSERT INTO `order_statusrecord` VALUES (27,'200','2015-08-01 15:48:37','1',1,1),(28,'200','2015-08-01 15:48:37','1',1,1),(29,'300','2015-08-01 15:48:37','0',1,1),(30,'300','2015-08-01 15:48:37','0',1,1),(31,'300','2015-08-01 15:48:37','0',2,1),(32,'300','2015-08-01 16:46:11','2',1,1),(33,'400','2015-08-01 16:46:11','1',1,1),(34,'500','2015-08-01 16:46:11','1',1,1);
/*!40000 ALTER TABLE `order_statusrecord` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `poi_merchant`
--

LOCK TABLES `poi_merchant` WRITE;
/*!40000 ALTER TABLE `poi_merchant` DISABLE KEYS */;
INSERT INTO `poi_merchant` VALUES (1,'onion','123456','洋葱达人','北京市大兴区黄村镇前大营村',39.690534,116.377585,'010-57154920','static/images/logo/logo.png','0','2015-07-24 11:21:52','2015-07-24 11:21:52','0'),(2,'starbucks','123456','星巴克','北京市朝阳区望京花园西区',NULL,NULL,'18768119089','static/images/logo/2_AKbMl9Q.jpg','0','2015-07-24 11:25:18','2015-07-24 11:25:18','0');
/*!40000 ALTER TABLE `poi_merchant` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `poi_show`
--

LOCK TABLES `poi_show` WRITE;
/*!40000 ALTER TABLE `poi_show` DISABLE KEYS */;
INSERT INTO `poi_show` VALUES (1,1),(2,2);
/*!40000 ALTER TABLE `poi_show` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `station_station`
--

LOCK TABLES `station_station` WRITE;
/*!40000 ALTER TABLE `station_station` DISABLE KEYS */;
INSERT INTO `station_station` VALUES (1,'huagonglu','123456','化工路店','北京市朝阳区东四环南路16号','400-8870-387',39.889161,116.498999,'','2015-07-30 19:00:05','2015-07-30 19:00:05','0'),(2,'tianshuiyuan','123456','甜水园店','北京市朝阳区延静里6号楼后','400-8870-387',39.929696,116.485411,'','2015-07-30 19:00:05','2015-07-30 19:00:05','0'),(3,'cuiweilu','123456','翠微路店','北京市海淀区翠微小区4号楼附近','400-8870-387',39.920893,116.305623,'','2015-07-30 19:00:05','2015-07-30 19:00:05','0'),(4,'dongdajie','123456','东大街店','北京市丰台区东大街42号附近','400-8870-387',39.861545,116.300324,'','2015-07-30 19:00:05','2015-07-30 19:00:05','0'),(5,'banjing','123456','板井店','北京市海淀区昆明湖南路72号附近','400-8870-387',39.954959,116.297409,'','2015-07-30 19:00:05','2015-07-30 19:00:05','0'),(6,'beishatanqiao','123456','北沙滩桥店','北京市海淀区清华东路4号','400-8870-387',40.007195,116.374846,'','2015-07-30 19:00:05','2015-07-30 19:00:05','0'),(7,'shunbaqiao','123456','顺八条店','北京市丰台区东铁匠营横七条五间楼1号','400-8870-387',39.856278,116.429517,'','2015-07-30 19:00:05','2015-07-30 19:00:05','0'),(8,'dongfengbeiqiao','123456','东风北桥店','北京市朝阳区酒仙桥11街坊15号楼','400-8870-387',39.966706,116.498769,'','2015-07-30 19:00:05','2015-07-30 19:00:05','0'),(9,'xinfadi','123456','新发地店','北京市丰台区宜兰园2期','400-8870-387',39.83346,116.344347,'','2015-07-30 19:00:05','2015-07-30 19:00:05','0'),(10,'wangsiying','123456','王四营店','北京市朝阳区高碑店王四营桥北同盛轩艺术馆','400-8870-387',39.87781,116.537398,'','2015-07-30 19:00:05','2015-07-30 19:00:05','0');
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

-- Dump completed on 2015-08-02  9:53:08
