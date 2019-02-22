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

CREATE SEQUENCE assessment_assessment_seq;

CREATE TABLE assessment_assessment (
  id int NOT NULL DEFAULT NEXTVAL ('assessment_assessment_seq'),
  submission_uuid varchar(128) NOT NULL,
  scored_at timestamptz(6) NOT NULL,
  scorer_id varchar(40) NOT NULL,
  score_type varchar(2) NOT NULL,
  feedback text NOT NULL,
  rubric_id int NOT NULL,
  PRIMARY KEY (id)
 ,
  CONSTRAINT assessment_as_rubric_id_7997f01dcbd05633_fk_assessment_rubric_id FOREIGN KEY (rubric_id) REFERENCES assessment_rubric (id)
) ;

CREATE INDEX assessment_assessment_ab5b2b73 ON assessment_assessment (submission_uuid);
CREATE INDEX assessment_assessment_ef4c53ff ON assessment_assessment (scored_at);
CREATE INDEX assessment_assessment_7b0042c0 ON assessment_assessment (scorer_id);
CREATE INDEX assessment_assessment_8980b7ae ON assessment_assessment (rubric_id);

CREATE SEQUENCE assessment_staffworkflow_seq;

CREATE TABLE assessment_staffworkflow (
  id int NOT NULL DEFAULT NEXTVAL ('assessment_staffworkflow_seq'),
  scorer_id varchar(40) NOT NULL,
  course_id varchar(255) NOT NULL,
  item_id varchar(128) NOT NULL,
  submission_uuid varchar(128) NOT NULL,
  created_at timestamptz(6) NOT NULL,
  grading_completed_at timestamptz(6) DEFAULT NULL,
  grading_started_at timestamptz(6) DEFAULT NULL,
  cancelled_at timestamptz(6) DEFAULT NULL,
  assessment varchar(128) DEFAULT NULL,
  PRIMARY KEY (id),
  CONSTRAINT assessment_staffworkflow_submission_uuid UNIQUE  (submission_uuid)
) ;

CREATE INDEX assessment_staffworkflow_7b0042c0 ON assessment_staffworkflow (scorer_id);
CREATE INDEX assessment_staffworkflow_ea134da7 ON assessment_staffworkflow (course_id);
CREATE INDEX assessment_staffworkflow_82bfda79 ON assessment_staffworkflow (item_id);
CREATE INDEX assessment_staffworkflow_fde81f11 ON assessment_staffworkflow (created_at);
CREATE INDEX assessment_staffworkflow_85d183d8 ON assessment_staffworkflow (grading_completed_at);
CREATE INDEX assessment_staffworkflow_0af9deae ON assessment_staffworkflow (grading_started_at);
CREATE INDEX assessment_staffworkflow_740da1db ON assessment_staffworkflow (cancelled_at);
CREATE INDEX assessment_staffworkflow_5096c410 ON assessment_staffworkflow (assessment);