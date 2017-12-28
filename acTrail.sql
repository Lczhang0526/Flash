/*
 Navicat Premium Data Transfer

 Source Server         : Lczhang_LocalHost
 Source Server Type    : MySQL
 Source Server Version : 50635
 Source Host           : localhost
 Source Database       : Cisco_Aci

 Target Server Type    : MySQL
 Target Server Version : 50635
 File Encoding         : utf-8

 Date: 12/28/2017 15:36:48 PM
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
--  Table structure for `acTrail`
-- ----------------------------
DROP TABLE IF EXISTS `acTrail`;
CREATE TABLE `acTrail` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `dn` varchar(200) DEFAULT NULL,
  `dropPktPercentage` varchar(100) DEFAULT NULL,
  `dropPkt` varchar(200) DEFAULT NULL,
  `trnstNodeId` varchar(200) DEFAULT NULL,
  `totDropPkt` varchar(200) DEFAULT NULL,
  `totDropPktPercentage` varchar(100) DEFAULT NULL,
  `create` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `dstNodeId` varchar(100) DEFAULT NULL,
  `dstNodeId2` varchar(100) DEFAULT NULL,
  `excessPkt` varchar(200) DEFAULT NULL,
  `excessPktPercentage` varchar(100) DEFAULT NULL,
  `srcNodeId` varchar(100) DEFAULT NULL,
  `srcNodeId2` varchar(100) DEFAULT NULL,
  `suspect` varchar(100) DEFAULT NULL,
  `txPkt` varchar(200) DEFAULT NULL,
  `totTxPkt` varchar(200) DEFAULT NULL,
  `totRxPkt` varchar(200) DEFAULT NULL,
  `totExcessPkt` varchar(200) DEFAULT NULL,
  `totExcessPktPercentage` varchar(200) DEFAULT NULL,
  `rn` varchar(200) DEFAULT NULL,
  `pathType` varchar(200) DEFAULT NULL,
  `rxPkt` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=74110 DEFAULT CHARSET=utf8;

SET FOREIGN_KEY_CHECKS = 1;
