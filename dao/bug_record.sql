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

 Date: 17/06/2020 19:48:49
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for bug_record
-- ----------------------------
DROP TABLE IF EXISTS `bug_record`;
CREATE TABLE `bug_record`  (
  `bug_id` int(255) NOT NULL AUTO_INCREMENT COMMENT 'bugid',
  `product` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '所属产品',
  `bugname` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT 'bug名称',
  `feedbacktime` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '反馈时间',
  `endtime` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '关闭时间',
  `feedbackpeople` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '反馈人',
  `dealpeople` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '处理人',
  `dealstate` int(255) NULL DEFAULT NULL COMMENT '处理状态1.未处理2.处理中3.完成',
  `bugdetail` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT 'bug详情（可包含图片）',
  `dealmethod` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '处理办法',
  `bugsystem` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT 'bug属于哪一端1.pc2.Android3.ios',
  `systemversion` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '手机系统版本',
  `productsystem` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '产品版本',
  `systemmodel` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '手机型号',
  `flag` int(255) NOT NULL DEFAULT 0,
  PRIMARY KEY (`bug_id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 32 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

SET FOREIGN_KEY_CHECKS = 1;
