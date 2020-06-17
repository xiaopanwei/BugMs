/*
 Navicat Premium Data Transfer

 Source Server         : a123456789
 Source Server Type    : MySQL
 Source Server Version : 50718
 Source Host           : cdb-q35wa9cy.cd.tencentcdb.com:10094
 Source Schema         : xpw_Ms

 Target Server Type    : MySQL
 Target Server Version : 50718
 File Encoding         : 65001

 Date: 17/06/2020 19:48:58
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for bugimage
-- ----------------------------
DROP TABLE IF EXISTS `bugimage`;
CREATE TABLE `bugimage`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `bugid` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `imageurl` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 20 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

SET FOREIGN_KEY_CHECKS = 1;
