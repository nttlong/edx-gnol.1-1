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

CREATE SEQUENCE courseware_xmodulestudentprefsfield_seq;

CREATE TABLE courseware_xmodulestudentprefsfield (
  id int NOT NULL DEFAULT NEXTVAL ('courseware_xmodulestudentprefsfield_seq'),
  field_name varchar(64) NOT NULL,
  value text NOT NULL,
  created timestamptz(6) NOT NULL,
  modified timestamptz(6) NOT NULL,
  module_type varchar(64) NOT NULL,
  student_id int NOT NULL,
  PRIMARY KEY (id),
  CONSTRAINT courseware_xmodulestudentprefsf_student_id_2a5d275498b7a407_uniq UNIQUE  (student_id,module_type,field_name)
 ,
  CONSTRAINT courseware_xmodulestudentprefsfield_student_id_3c60ec8a_fk FOREIGN KEY (student_id) REFERENCES auth_user (id)
) ;

CREATE INDEX courseware_xmodulestudentprefsfield_73f329f1 ON courseware_xmodulestudentprefsfield (field_name);
CREATE INDEX courseware_xmodulestudentprefsfield_e2fa5388 ON courseware_xmodulestudentprefsfield (created);
CREATE INDEX courseware_xmodulestudentprefsfield_9ae73c65 ON courseware_xmodulestudentprefsfield (modified);
CREATE INDEX courseware_xmodulestudentprefsfield_82bd5515 ON courseware_xmodulestudentprefsfield (module_type);

CREATE SEQUENCE coursewarehistoryextended_studentmodulehistoryextended_seq;

CREATE TABLE coursewarehistoryextended_studentmodulehistoryextended (
  version varchar(255) DEFAULT NULL,
  created timestamptz(6) NOT NULL,
  state text,
  grade double precision DEFAULT NULL,
  max_grade double precision DEFAULT NULL,
  id bigint check (id > 0) NOT NULL DEFAULT NEXTVAL ('coursewarehistoryextended_studentmodulehistoryextended_seq'),
  student_module_id int NOT NULL,
  PRIMARY KEY (id)
) ;

CREATE INDEX coursewarehistoryextended_studentmodulehistoryextended_2af72f10 ON coursewarehistoryextended_studentmodulehistoryextended (version);
CREATE INDEX coursewarehistoryextended_studentmodulehistoryextended_e2fa5388 ON coursewarehistoryextended_studentmodulehistoryextended (created);
CREATE INDEX coursewarehistoryextended_student_module_id_61b23a7a1dd27fe4_idx ON coursewarehistoryextended_studentmodulehistoryextended (student_module_id);