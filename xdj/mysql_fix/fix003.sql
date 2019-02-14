CREATE TABLE `edxval_videotranscript` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `created` datetime(6) NOT NULL,
  `modified` datetime(6) NOT NULL,
  `transcript` varchar(255) DEFAULT NULL,
  `language_code` varchar(50) NOT NULL,
  `provider` varchar(30) NOT NULL,
  `file_format` varchar(20) NOT NULL,
  `video_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `edxval_videotranscript_video_id_729fab369c0f7028_uniq` (`video_id`,`language_code`),
  KEY `edxval_videotranscript_60716c2f` (`language_code`),
  KEY `edxval_videotranscript_e1be1ad3` (`file_format`),
  KEY `edxval_videotranscript_b58b747e` (`video_id`),
  CONSTRAINT `edxval_videotranscr_video_id_2578e231c810d058_fk_edxval_video_id` FOREIGN KEY (`video_id`) REFERENCES `edxval_video` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
CREATE TABLE `edxval_videoimage` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `created` datetime(6) NOT NULL,
  `modified` datetime(6) NOT NULL,
  `image` varchar(500) DEFAULT NULL,
  `generated_images` longtext NOT NULL,
  `course_video_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `course_video_id` (`course_video_id`),
  CONSTRAINT `edxval_course_video_id_595461bc0ff739b3_fk_edxval_coursevideo_id` FOREIGN KEY (`course_video_id`) REFERENCES `edxval_coursevideo` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;