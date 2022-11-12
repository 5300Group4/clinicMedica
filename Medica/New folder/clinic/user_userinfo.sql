/*
 Navicat Premium Data Transfer

 Source Server         : Mysql
 Source Server Type    : MySQL
 Source Server Version : 50740 (5.7.40-log)
 Source Host           : localhost:3306
 Source Schema         : medica

 Target Server Type    : MySQL
 Target Server Version : 50740 (5.7.40-log)
 File Encoding         : 65001

 Date: 11/11/2022 16:17:57
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for user_userinfo
-- ----------------------------
DROP TABLE IF EXISTS `user_userinfo`;
CREATE TABLE `user_userinfo`  (
  `id` int(11) NOT NULL,
  `name` varchar(32) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  `password` varchar(64) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  `age` int(11) NOT NULL,
  `email` varchar(64) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  `gender` smallint(6) NOT NULL,
  `appointment_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `user_userinfo_appointment_id_2846cbc3_fk_user_doctor_id`(`appointment_id`) USING BTREE,
  CONSTRAINT `user_userinfo_appointment_id_2846cbc3_fk_user_doctor_id` FOREIGN KEY (`appointment_id`) REFERENCES `user_doctor` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB CHARACTER SET = latin1 COLLATE = latin1_swedish_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of user_userinfo
-- ----------------------------
INSERT INTO `user_userinfo` VALUES (12, 'alex', '123456', 23, 'alex@example.com', 2, 1);

SET FOREIGN_KEY_CHECKS = 1;
