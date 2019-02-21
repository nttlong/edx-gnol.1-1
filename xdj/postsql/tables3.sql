CREATE SEQUENCE edxval_videoimage_seq;

CREATE TABLE edxval_videoimage (
  id int NOT NULL DEFAULT NEXTVAL ('edxval_videoimage_seq'),
  created timestamptz(6) NOT NULL,
  modified timestamptz(6) NOT NULL,
  image varchar(500) DEFAULT NULL,
  generated_images text NOT NULL,
  course_video_id int NOT NULL,
  PRIMARY KEY (id),
  CONSTRAINT course_video_id UNIQUE  (course_video_id),
  CONSTRAINT edxval_course_video_id_595461bc0ff739b3_fk_edxval_coursevideo_id FOREIGN KEY (course_video_id) REFERENCES edxval_coursevideo (id)
) ;