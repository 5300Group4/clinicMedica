/*
 Navicat Premium Data Transfer

 Source Server         : localhost
 Source Server Type    : MySQL
 Source Server Version : 50740
 Source Host           : localhost:3306
 Source Schema         : medica

 Target Server Type    : MySQL
 Target Server Version : 50740
 File Encoding         : 65001

 Date: 08/11/2022 18:53:44
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for auth_group
-- ----------------------------
DROP TABLE IF EXISTS `auth_group`;
CREATE TABLE `auth_group`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(150) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `name`(`name`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = latin1 COLLATE = latin1_swedish_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for auth_group_permissions
-- ----------------------------
DROP TABLE IF EXISTS `auth_group_permissions`;
CREATE TABLE `auth_group_permissions`  (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `auth_group_permissions_group_id_permission_id_0cd325b0_uniq`(`group_id`, `permission_id`) USING BTREE,
  INDEX `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm`(`permission_id`) USING BTREE,
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = latin1 COLLATE = latin1_swedish_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for auth_permission
-- ----------------------------
DROP TABLE IF EXISTS `auth_permission`;
CREATE TABLE `auth_permission`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `auth_permission_content_type_id_codename_01ab375a_uniq`(`content_type_id`, `codename`) USING BTREE,
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 45 CHARACTER SET = latin1 COLLATE = latin1_swedish_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of auth_permission
-- ----------------------------
INSERT INTO `auth_permission` VALUES (1, 'Can add log entry', 1, 'add_logentry');
INSERT INTO `auth_permission` VALUES (2, 'Can change log entry', 1, 'change_logentry');
INSERT INTO `auth_permission` VALUES (3, 'Can delete log entry', 1, 'delete_logentry');
INSERT INTO `auth_permission` VALUES (4, 'Can view log entry', 1, 'view_logentry');
INSERT INTO `auth_permission` VALUES (5, 'Can add permission', 2, 'add_permission');
INSERT INTO `auth_permission` VALUES (6, 'Can change permission', 2, 'change_permission');
INSERT INTO `auth_permission` VALUES (7, 'Can delete permission', 2, 'delete_permission');
INSERT INTO `auth_permission` VALUES (8, 'Can view permission', 2, 'view_permission');
INSERT INTO `auth_permission` VALUES (9, 'Can add group', 3, 'add_group');
INSERT INTO `auth_permission` VALUES (10, 'Can change group', 3, 'change_group');
INSERT INTO `auth_permission` VALUES (11, 'Can delete group', 3, 'delete_group');
INSERT INTO `auth_permission` VALUES (12, 'Can view group', 3, 'view_group');
INSERT INTO `auth_permission` VALUES (13, 'Can add user', 4, 'add_user');
INSERT INTO `auth_permission` VALUES (14, 'Can change user', 4, 'change_user');
INSERT INTO `auth_permission` VALUES (15, 'Can delete user', 4, 'delete_user');
INSERT INTO `auth_permission` VALUES (16, 'Can view user', 4, 'view_user');
INSERT INTO `auth_permission` VALUES (17, 'Can add content type', 5, 'add_contenttype');
INSERT INTO `auth_permission` VALUES (18, 'Can change content type', 5, 'change_contenttype');
INSERT INTO `auth_permission` VALUES (19, 'Can delete content type', 5, 'delete_contenttype');
INSERT INTO `auth_permission` VALUES (20, 'Can view content type', 5, 'view_contenttype');
INSERT INTO `auth_permission` VALUES (21, 'Can add session', 6, 'add_session');
INSERT INTO `auth_permission` VALUES (22, 'Can change session', 6, 'change_session');
INSERT INTO `auth_permission` VALUES (23, 'Can delete session', 6, 'delete_session');
INSERT INTO `auth_permission` VALUES (24, 'Can view session', 6, 'view_session');
INSERT INTO `auth_permission` VALUES (25, 'Can add user', 7, 'add_user');
INSERT INTO `auth_permission` VALUES (26, 'Can change user', 7, 'change_user');
INSERT INTO `auth_permission` VALUES (27, 'Can delete user', 7, 'delete_user');
INSERT INTO `auth_permission` VALUES (28, 'Can view user', 7, 'view_user');
INSERT INTO `auth_permission` VALUES (29, 'Can add appointment', 8, 'add_appointment');
INSERT INTO `auth_permission` VALUES (30, 'Can change appointment', 8, 'change_appointment');
INSERT INTO `auth_permission` VALUES (31, 'Can delete appointment', 8, 'delete_appointment');
INSERT INTO `auth_permission` VALUES (32, 'Can view appointment', 8, 'view_appointment');
INSERT INTO `auth_permission` VALUES (33, 'Can add payment', 9, 'add_payment');
INSERT INTO `auth_permission` VALUES (34, 'Can change payment', 9, 'change_payment');
INSERT INTO `auth_permission` VALUES (35, 'Can delete payment', 9, 'delete_payment');
INSERT INTO `auth_permission` VALUES (36, 'Can view payment', 9, 'view_payment');
INSERT INTO `auth_permission` VALUES (37, 'Can add doctor', 10, 'add_doctor');
INSERT INTO `auth_permission` VALUES (38, 'Can change doctor', 10, 'change_doctor');
INSERT INTO `auth_permission` VALUES (39, 'Can delete doctor', 10, 'delete_doctor');
INSERT INTO `auth_permission` VALUES (40, 'Can view doctor', 10, 'view_doctor');
INSERT INTO `auth_permission` VALUES (41, 'Can add location', 11, 'add_location');
INSERT INTO `auth_permission` VALUES (42, 'Can change location', 11, 'change_location');
INSERT INTO `auth_permission` VALUES (43, 'Can delete location', 11, 'delete_location');
INSERT INTO `auth_permission` VALUES (44, 'Can view location', 11, 'view_location');

-- ----------------------------
-- Table structure for auth_user
-- ----------------------------
DROP TABLE IF EXISTS `auth_user`;
CREATE TABLE `auth_user`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  `last_login` datetime(6) NULL DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  `first_name` varchar(150) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  `last_name` varchar(150) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  `email` varchar(254) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `username`(`username`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 2 CHARACTER SET = latin1 COLLATE = latin1_swedish_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of auth_user
-- ----------------------------
INSERT INTO `auth_user` VALUES (1, 'pbkdf2_sha256$390000$s7pIHDTnDzu4XqUN0fwMXJ$LbhRhLXsq9PhXtH9KbMjQWDIBsDwZqzSTcfgkwSzMuU=', '2022-11-01 17:33:37.443019', 1, 'medica', '', '', 'medica@example.com', 1, 1, '2022-11-01 17:32:36.719983');

-- ----------------------------
-- Table structure for auth_user_groups
-- ----------------------------
DROP TABLE IF EXISTS `auth_user_groups`;
CREATE TABLE `auth_user_groups`  (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `auth_user_groups_user_id_group_id_94350c0c_uniq`(`user_id`, `group_id`) USING BTREE,
  INDEX `auth_user_groups_group_id_97559544_fk_auth_group_id`(`group_id`) USING BTREE,
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = latin1 COLLATE = latin1_swedish_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for auth_user_user_permissions
-- ----------------------------
DROP TABLE IF EXISTS `auth_user_user_permissions`;
CREATE TABLE `auth_user_user_permissions`  (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq`(`user_id`, `permission_id`) USING BTREE,
  INDEX `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm`(`permission_id`) USING BTREE,
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = latin1 COLLATE = latin1_swedish_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for django_admin_log
-- ----------------------------
DROP TABLE IF EXISTS `django_admin_log`;
CREATE TABLE `django_admin_log`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext CHARACTER SET latin1 COLLATE latin1_swedish_ci NULL,
  `object_repr` varchar(200) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL,
  `change_message` longtext CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  `content_type_id` int(11) NULL DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `django_admin_log_content_type_id_c4bce8eb_fk_django_co`(`content_type_id`) USING BTREE,
  INDEX `django_admin_log_user_id_c564eba6_fk_auth_user_id`(`user_id`) USING BTREE,
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = latin1 COLLATE = latin1_swedish_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for django_content_type
-- ----------------------------
DROP TABLE IF EXISTS `django_content_type`;
CREATE TABLE `django_content_type`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  `model` varchar(100) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `django_content_type_app_label_model_76bd3d3b_uniq`(`app_label`, `model`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 12 CHARACTER SET = latin1 COLLATE = latin1_swedish_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of django_content_type
-- ----------------------------
INSERT INTO `django_content_type` VALUES (1, 'admin', 'logentry');
INSERT INTO `django_content_type` VALUES (3, 'auth', 'group');
INSERT INTO `django_content_type` VALUES (2, 'auth', 'permission');
INSERT INTO `django_content_type` VALUES (4, 'auth', 'user');
INSERT INTO `django_content_type` VALUES (5, 'contenttypes', 'contenttype');
INSERT INTO `django_content_type` VALUES (7, 'login', 'user');
INSERT INTO `django_content_type` VALUES (6, 'sessions', 'session');
INSERT INTO `django_content_type` VALUES (8, 'user', 'appointment');
INSERT INTO `django_content_type` VALUES (10, 'user', 'doctor');
INSERT INTO `django_content_type` VALUES (11, 'user', 'location');
INSERT INTO `django_content_type` VALUES (9, 'user', 'payment');

-- ----------------------------
-- Table structure for django_migrations
-- ----------------------------
DROP TABLE IF EXISTS `django_migrations`;
CREATE TABLE `django_migrations`  (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  `name` varchar(255) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 27 CHARACTER SET = latin1 COLLATE = latin1_swedish_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of django_migrations
-- ----------------------------
INSERT INTO `django_migrations` VALUES (1, 'contenttypes', '0001_initial', '2022-11-01 17:13:00.603628');
INSERT INTO `django_migrations` VALUES (2, 'auth', '0001_initial', '2022-11-01 17:13:01.183627');
INSERT INTO `django_migrations` VALUES (3, 'admin', '0001_initial', '2022-11-01 17:13:01.335626');
INSERT INTO `django_migrations` VALUES (4, 'admin', '0002_logentry_remove_auto_add', '2022-11-01 17:13:01.346631');
INSERT INTO `django_migrations` VALUES (5, 'admin', '0003_logentry_add_action_flag_choices', '2022-11-01 17:13:01.362628');
INSERT INTO `django_migrations` VALUES (6, 'contenttypes', '0002_remove_content_type_name', '2022-11-01 17:13:01.527626');
INSERT INTO `django_migrations` VALUES (7, 'auth', '0002_alter_permission_name_max_length', '2022-11-01 17:13:01.551628');
INSERT INTO `django_migrations` VALUES (8, 'auth', '0003_alter_user_email_max_length', '2022-11-01 17:13:01.597633');
INSERT INTO `django_migrations` VALUES (9, 'auth', '0004_alter_user_username_opts', '2022-11-01 17:13:01.611628');
INSERT INTO `django_migrations` VALUES (10, 'auth', '0005_alter_user_last_login_null', '2022-11-01 17:13:01.701635');
INSERT INTO `django_migrations` VALUES (11, 'auth', '0006_require_contenttypes_0002', '2022-11-01 17:13:01.705635');
INSERT INTO `django_migrations` VALUES (12, 'auth', '0007_alter_validators_add_error_messages', '2022-11-01 17:13:01.718628');
INSERT INTO `django_migrations` VALUES (13, 'auth', '0008_alter_user_username_max_length', '2022-11-01 17:13:01.744630');
INSERT INTO `django_migrations` VALUES (14, 'auth', '0009_alter_user_last_name_max_length', '2022-11-01 17:13:01.781631');
INSERT INTO `django_migrations` VALUES (15, 'auth', '0010_alter_group_name_max_length', '2022-11-01 17:13:01.831630');
INSERT INTO `django_migrations` VALUES (16, 'auth', '0011_update_proxy_permissions', '2022-11-01 17:13:01.856629');
INSERT INTO `django_migrations` VALUES (17, 'auth', '0012_alter_user_first_name_max_length', '2022-11-01 17:13:01.895629');
INSERT INTO `django_migrations` VALUES (18, 'login', '0001_initial', '2022-11-01 17:13:01.959630');
INSERT INTO `django_migrations` VALUES (19, 'sessions', '0001_initial', '2022-11-01 17:13:02.030629');
INSERT INTO `django_migrations` VALUES (20, 'login', '0002_alter_user_email', '2022-11-01 17:16:10.351557');
INSERT INTO `django_migrations` VALUES (21, 'user', '0001_initial', '2022-11-06 18:41:56.902735');
INSERT INTO `django_migrations` VALUES (22, 'user', '0002_appointment_doctor', '2022-11-07 05:14:53.693508');
INSERT INTO `django_migrations` VALUES (23, 'user', '0003_appointment_doctor', '2022-11-07 05:39:22.512289');
INSERT INTO `django_migrations` VALUES (24, 'user', '0004_doctor_location', '2022-11-08 20:05:46.561320');
INSERT INTO `django_migrations` VALUES (25, 'user', '0004_location', '2022-11-08 23:46:34.294896');
INSERT INTO `django_migrations` VALUES (26, 'user', '0005_merge_0004_doctor_location_0004_location', '2022-11-08 23:46:34.310449');

-- ----------------------------
-- Table structure for django_session
-- ----------------------------
DROP TABLE IF EXISTS `django_session`;
CREATE TABLE `django_session`  (
  `session_key` varchar(40) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  `session_data` longtext CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`) USING BTREE,
  INDEX `django_session_expire_date_a5c62663`(`expire_date`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = latin1 COLLATE = latin1_swedish_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of django_session
-- ----------------------------
INSERT INTO `django_session` VALUES ('gaptzjgr1fp6pm47f9d81l529efxbfex', '.eJxVjMEOwiAQBf-FsyFAYQGP3v0GssAiVQNJaU_Gf9cmPej1zcx7sYDbWsM2aAlzZmcm2el3i5ge1HaQ79hunafe1mWOfFf4QQe_9kzPy-H-HVQc9VsLqSafinbaAYAk4QgcFNLGAkaDRicXLVqkZISQkxGg0mQjeFU8asXeH7yNNuo:1opv8r:BYobjgxv21nHTWbh7RykBOR4gG9AVEdEUWHLMmFAfLE', '2022-11-15 17:33:37.447011');

-- ----------------------------
-- Table structure for login_user
-- ----------------------------
DROP TABLE IF EXISTS `login_user`;
CREATE TABLE `login_user`  (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `username` varchar(32) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  `email` varchar(32) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  `password` varchar(32) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 3 CHARACTER SET = latin1 COLLATE = latin1_swedish_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of login_user
-- ----------------------------
INSERT INTO `login_user` VALUES (1, 'alex', 'alex@example.com', 'alex');
INSERT INTO `login_user` VALUES (2, 'bob', 'bob@example.cmo', 'bob');

-- ----------------------------
-- Table structure for user_appointment
-- ----------------------------
DROP TABLE IF EXISTS `user_appointment`;
CREATE TABLE `user_appointment`  (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `email` varchar(32) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  `phone_number` varchar(32) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  `date` date NOT NULL,
  `comment` varchar(64) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  `doctor` varchar(32) CHARACTER SET latin1 COLLATE latin1_swedish_ci NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 5 CHARACTER SET = latin1 COLLATE = latin1_swedish_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of user_appointment
-- ----------------------------
INSERT INTO `user_appointment` VALUES (1, 'Fc_vac@outlook.com', '111', '2022-12-01', '', NULL);
INSERT INTO `user_appointment` VALUES (2, 'Fc_vac@outlook.com', '444', '2022-11-17', '', 'Jennifer Walker');
INSERT INTO `user_appointment` VALUES (3, 'hnan059@uottawa.ca', '111', '2022-11-25', '', 'Carl Harrise');
INSERT INTO `user_appointment` VALUES (4, 'hnan059@uottawa.ca', '111', '2022-11-25', '', 'Carl Harrise');

-- ----------------------------
-- Table structure for user_doctor
-- ----------------------------
DROP TABLE IF EXISTS `user_doctor`;
CREATE TABLE `user_doctor`  (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `name` varchar(32) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  `introduction` varchar(255) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  `picture` varchar(255) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  `location` varchar(20) CHARACTER SET latin1 COLLATE latin1_swedish_ci NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 31 CHARACTER SET = latin1 COLLATE = latin1_swedish_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of user_doctor
-- ----------------------------
INSERT INTO `user_doctor` VALUES (1, 'Rebecca Johnson', 'Cardio Thoracic Surgeon', '111', 'Ottawa');
INSERT INTO `user_doctor` VALUES (2, 'Jennifer Walker', 'Cardio Thoracic Surgeon', '222', 'Kingston');
INSERT INTO `user_doctor` VALUES (3, 'Carl Harrise', 'Oncologist', '333', 'Ottawa');
INSERT INTO `user_doctor` VALUES (4, 'Patrick Cooper', 'General Surgeon/Paediatric Surgeon', '444', 'Toronto');
INSERT INTO `user_doctor` VALUES (5, 'Akira Yamashita', 'Obstetrician and Gynaecologist', '55', 'Waterloo');
INSERT INTO `user_doctor` VALUES (6, 'Fred Swift', 'General Surgeon/Paediatric Surgeon', '6', 'Waterloo');
INSERT INTO `user_doctor` VALUES (7, 'Jessica Williams', 'Physician', '7', 'Kingston');
INSERT INTO `user_doctor` VALUES (8, 'Joy Thompson', 'General Surgeon/Paediatric Surgeon', '8', 'Windsor');
INSERT INTO `user_doctor` VALUES (9, 'Sara Lewis', 'Neurosurgeon', '9', 'Windsor');
INSERT INTO `user_doctor` VALUES (10, 'Natalie Ford', 'Oncologist', '10', 'Windsor');
INSERT INTO `user_doctor` VALUES (11, 'Jack Alexander', 'Physical Medicine', '11', 'Toronto');
INSERT INTO `user_doctor` VALUES (12, 'Alex Edwards', 'Cardio Thoracic Surgeon', '12', 'Toronto');
INSERT INTO `user_doctor` VALUES (13, 'Josh Adams', 'Neurosurgeon', '13', 'Toronto');
INSERT INTO `user_doctor` VALUES (14, 'Mary Clark', 'Urologist', '14', 'Toronto');
INSERT INTO `user_doctor` VALUES (15, 'Matthew Crowley', 'Obstetrician and Gynaecologist', '15', 'Toronto');
INSERT INTO `user_doctor` VALUES (16, 'Timmy Phillips', 'Oncologist', '16', 'Toronto');
INSERT INTO `user_doctor` VALUES (17, 'Eloise Clark', 'Oncologist', '17', 'Hamilton');
INSERT INTO `user_doctor` VALUES (18, 'Archie Anderson', 'Cardio Thoracic Surgeon', '18', 'Hamilton');
INSERT INTO `user_doctor` VALUES (19, 'Hattie Morgan', 'Neurosurgeon', '19', 'Hamilton');
INSERT INTO `user_doctor` VALUES (20, 'Rosie Davis', 'Neurosurgeon', '20', 'Ottawa');
INSERT INTO `user_doctor` VALUES (21, 'Zeke Martinez', 'Obstetrician and Gynaecologist', '21', 'Ottawa');
INSERT INTO `user_doctor` VALUES (22, 'Magnus Hernandez', 'General Surgeon/Paediatric Surgeon', '22', 'Ottawa');
INSERT INTO `user_doctor` VALUES (23, 'Titan Davis', 'Physician', '23', 'Toronto');
INSERT INTO `user_doctor` VALUES (24, 'Aurelia Hernandez', 'Physical Medicine', '24', 'Hamilton');
INSERT INTO `user_doctor` VALUES (25, 'Freya Garcia', 'Physical Medicine', '25', 'Waterloo');
INSERT INTO `user_doctor` VALUES (26, 'Maisie Morgan', 'Cardio Thoracic Surgeon', '26', 'Waterloo');
INSERT INTO `user_doctor` VALUES (27, 'Octavia Martinez', 'Physician', '27', 'Waterloo');
INSERT INTO `user_doctor` VALUES (28, 'Juniper Garcia', 'Physician', '28', 'Windsor');
INSERT INTO `user_doctor` VALUES (29, 'Cairo Anderson', 'Urologist', '29', 'Kingston');
INSERT INTO `user_doctor` VALUES (30, 'Harlem Rodriguez', 'Obstetrician and Gynaecologist', '30', 'Hamilton');

-- ----------------------------
-- Table structure for user_location
-- ----------------------------
DROP TABLE IF EXISTS `user_location`;
CREATE TABLE `user_location`  (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `address` varchar(32) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  `city` varchar(32) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  `clinic_number` varchar(255) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  `clinic_picture` varchar(255) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 7 CHARACTER SET = latin1 COLLATE = latin1_swedish_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of user_location
-- ----------------------------
INSERT INTO `user_location` VALUES (1, '245 Eglinton Ave E, Toronto, ON', 'Toronto', '111-111-1111', '111');
INSERT INTO `user_location` VALUES (2, '1300 Baseline Rd, Ottawa, ON', 'Ottawa', '222-222-2222', '222');
INSERT INTO `user_location` VALUES (3, '826 King St N, Waterloo, ON', 'Waterloo', '333-333-3333', '333');
INSERT INTO `user_location` VALUES (4, '175 Princess St, Kingston, ON', 'Kingston', '444-444-4444', '444');
INSERT INTO `user_location` VALUES (5, '541 Rideau St, Ottawa, ON', 'Windsor', '555-555-5555', '555');
INSERT INTO `user_location` VALUES (6, '340 York Blvd, Hamilton, ON', 'Hamilton', '666-666-6666', '666');

SET FOREIGN_KEY_CHECKS = 1;
