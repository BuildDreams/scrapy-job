/*
Navicat MySQL Data Transfer

Source Server         : zq
Source Server Version : 50724
Source Host           : localhost:3306
Source Database       : test

Target Server Type    : MYSQL
Target Server Version : 50724
File Encoding         : 65001

Date: 2018-12-30 15:19:11
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for job51
-- ----------------------------
DROP TABLE IF EXISTS `job51`;
CREATE TABLE `job51` (
  `name` varchar(255) DEFAULT NULL,
  `provinces` varchar(255) DEFAULT NULL,
  `area` varchar(255) DEFAULT NULL,
  `workyear` varchar(255) DEFAULT NULL,
  `edu` varchar(255) DEFAULT NULL,
  `datatime` datetime DEFAULT NULL,
  `min_salary` decimal(10,0) DEFAULT NULL,
  `high_salary` decimal(10,0) DEFAULT NULL,
  `welfare` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
