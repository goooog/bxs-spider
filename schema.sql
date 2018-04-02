CREATE DATABASE `bxs` /*!40100 DEFAULT CHARACTER SET utf8 */;


CREATE TABLE `insurance_rate` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `insurance_id` int(11) NOT NULL,
  `insurance_name` varchar(45) NOT NULL,
  `sex` tinyint(4) NOT NULL,
  `age` int(11) NOT NULL,
  `years` tinyint(4) DEFAULT NULL COMMENT '缴费年限',
  `baoe` decimal(20,2) NOT NULL,
  `baof` decimal(20,2) NOT NULL,
  `lingqu` int(11) DEFAULT NULL COMMENT '养老金领取年龄',
  `duration` int(11) DEFAULT NULL COMMENT '保障期限',
  `lingqu_type` tinyint(4) DEFAULT NULL COMMENT '是否保证领取： 0/1',
  `smoke` tinyint(4) DEFAULT NULL COMMENT '是否抽烟',
  `social` tinyint(4) DEFAULT NULL COMMENT '是否有社保',
  `plan` tinyint(4) DEFAULT NULL,
  `create_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `baof_total` decimal(20,2) NOT NULL DEFAULT '0.00',
  `baoe1` decimal(20,2) DEFAULT NULL,
  `baof1` decimal(20,2) DEFAULT NULL,
  `baoe2` decimal(20,2) DEFAULT NULL,
  `baof2` decimal(20,2) DEFAULT NULL,
  `baoe3` decimal(20,2) DEFAULT NULL,
  `baof3` decimal(20,2) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8;


CREATE TABLE `insurance_profit_variable` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `insurance_id` int(11) NOT NULL,
  `insurance_name` varchar(45) NOT NULL,
  `sex` tinyint(4) NOT NULL,
  `age` int(11) NOT NULL,
  `years` tinyint(4) DEFAULT NULL COMMENT '缴费年限',
  `baoe` decimal(20,2) NOT NULL,
  `baof` decimal(20,2) NOT NULL,
  `lingqu` int(11) DEFAULT NULL COMMENT '养老金领取年龄',
  `duration` int(11) DEFAULT NULL COMMENT '保障期限',
  `lingqu_type` tinyint(4) DEFAULT NULL COMMENT '是否保证领取： 0/1',
  `smoke` tinyint(4) DEFAULT NULL COMMENT '是否抽烟',
  `social` tinyint(4) DEFAULT NULL COMMENT '是否有社保',
  `plan` tinyint(4) DEFAULT NULL,
  `create_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `baof_total` decimal(20,2) NOT NULL DEFAULT '0.00',
  `baoe1` decimal(20,2) DEFAULT NULL,
  `baof1` decimal(20,2) DEFAULT NULL,
  `baoe2` decimal(20,2) DEFAULT NULL,
  `baof2` decimal(20,2) DEFAULT NULL,
  `baoe3` decimal(20,2) DEFAULT NULL,
  `baof3` decimal(20,2) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8;


CREATE TABLE `insurance_profit_value` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `profit_id` int(11) NOT NULL,
  `insurance_id` int(11) NOT NULL,
  `name` varchar(45) NOT NULL,
  `policy_year` int(11) NOT NULL,
  `profit_grade` enum('L','M','H') NOT NULL,
  `wanneng_grade` enum('L','M','H') NOT NULL,
  `money` decimal(20,2) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
