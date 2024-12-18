/*
SQLyog Community Edition- MySQL GUI v7.01 
MySQL - 5.0.27-community-nt : Database - ecommerce
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;

CREATE DATABASE /*!32312 IF NOT EXISTS*/`ecommerce` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `ecommerce`;

/*Table structure for table `cartdata` */

DROP TABLE IF EXISTS `cartdata`;

CREATE TABLE `cartdata` (
  `id` varchar(255) default NULL,
  `uploader` varchar(255) default NULL,
  `filename` varchar(255) default NULL,
  `pname` varchar(255) default NULL,
  `pcat` varchar(255) default NULL,
  `pdate` varchar(255) default NULL,
  `pprize` varchar(255) default NULL,
  `quantity` varchar(255) default NULL,
  `buyer` varchar(255) default NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `cartdata` */

/*Table structure for table `payment` */

DROP TABLE IF EXISTS `payment`;

CREATE TABLE `payment` (
  `pid` varchar(255) default NULL,
  `img` varchar(255) default NULL,
  `title` varchar(255) default NULL,
  `prize` varchar(255) default NULL,
  `quantity` varchar(255) default NULL,
  `date` varchar(255) default NULL,
  `buyer` varchar(255) default NULL,
  `shipaddress` varchar(255) default NULL,
  `status` varchar(255) default 'Order Placed'
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `payment` */

insert  into `payment`(`pid`,`img`,`title`,`prize`,`quantity`,`date`,`buyer`,`shipaddress`,`status`) values ('7','static/files/admin/team-3.jpg','xxvxcv','333','2','2024-03-26','d','vikhroli park site','Order Placed'),('1','static/files/admin/farm_background_1.jpg','Product67','2566','3','2024-03-26','d','indira nagar','Packed'),('8','static/files/admin/team-1.jpg','ssas cascasc','1200','4','2024-03-25','d','indira nagar','Out for delivery'),('1','static/files/admin/farm_background_1.jpg','Product67','2566','3','2024-03-24','a','Nerul','Order Placed'),('4','static/files/admin/marie.jpg','marrie','5200','5','2024-03-24','a','Nerul','Order Placed');

/*Table structure for table `productdetails` */

DROP TABLE IF EXISTS `productdetails`;

CREATE TABLE `productdetails` (
  `id` int(255) NOT NULL auto_increment,
  `uploader` varchar(255) default NULL,
  `filename` varchar(255) default NULL,
  `pname` varchar(255) default NULL,
  `pcat` varchar(255) default NULL,
  `pdate` varchar(255) default NULL,
  `pprize` varchar(255) default NULL,
  `description` longtext,
  `instruction` longtext,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `productdetails` */

insert  into `productdetails`(`id`,`uploader`,`filename`,`pname`,`pcat`,`pdate`,`pprize`,`description`,`instruction`) values (1,'admin','static/files/admin/farm_background_1.jpg','Product67','random','2023-02-16','2566','xzcxzczxczxccxc','zxczxczxcxczx'),(3,'admin','static/files/admin/ivana-square.jpg','Long hair','fff','2023-02-05','6700','zxczxzxczxcxczx','xzczxczxczxczxcx xnvjndnnkdkd kdjkjsd dkdjds ds'),(4,'admin','static/files/admin/marie.jpg','marrie','Machine','2023-02-10','5200','ffsdfsdfsdfsf','cxzczxczxczczc   zczxcxxxxxxxxxxxxxxxxxccccccccccc '),(5,'admin','static/files/admin/2.jpg','Product34','Beans','2023-02-16','1254','Nice grass','Green grass'),(7,'admin','static/files/admin/team-3.jpg','xxvxcv','ghghg','2023-03-07','333','xcvxcvxcv  vxcv          vxc v xvxv vxv xvxv','cxvxcvxcvcvc v v v cx xvc xcvvxcv '),(8,'admin','static/files/admin/team-1.jpg','ssas cascasc','csajc','0004-04-05','1200','Forener product','Kahi nahi'),(9,'admin','static/files/admin/new_test_2.jpg','dsasd','asdasdasd','2024-03-27','2131','dsfsdf s fsd fsd f',' sdf sdfds fsd sdf  ');

/*Table structure for table `users` */

DROP TABLE IF EXISTS `users`;

CREATE TABLE `users` (
  `id` int(255) NOT NULL auto_increment,
  `username` varchar(255) default NULL,
  `email` varchar(255) default NULL,
  `mobile` varchar(255) default NULL,
  `password` varchar(255) default NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `users` */

insert  into `users`(`id`,`username`,`email`,`mobile`,`password`) values (3,'a','yash@gmail.com','9372914050','a'),(4,'d','dasdas99@gmail.com','9930090886','d');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
