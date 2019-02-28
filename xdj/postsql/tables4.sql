CREATE SEQUENCE courseware_xmoduleuserstatesummaryfield_seq;

CREATE TABLE courseware_xmoduleuserstatesummaryfield (
  id int NOT NULL DEFAULT NEXTVAL ('courseware_xmoduleuserstatesummaryfield_seq'),
  field_name varchar(64) NOT NULL,
  value text NOT NULL,
  created timestamptz(6) NOT NULL,
  modified timestamptz(6) NOT NULL,
  usage_id varchar(255) NOT NULL,
  PRIMARY KEY (id),
  CONSTRAINT courseware_xmoduleuserstatesummar_usage_id_5cc7ed48d6e2e021_uniq UNIQUE  (usage_id,field_name)
) ;

CREATE INDEX courseware_xmoduleuserstatesummaryfield_73f329f1 ON courseware_xmoduleuserstatesummaryfield (field_name);
CREATE INDEX courseware_xmoduleuserstatesummaryfield_e2fa5388 ON courseware_xmoduleuserstatesummaryfield (created);
CREATE INDEX courseware_xmoduleuserstatesummaryfield_9ae73c65 ON courseware_xmoduleuserstatesummaryfield (modified);
CREATE INDEX courseware_xmoduleuserstatesummaryfield_0528eb2a ON courseware_xmoduleuserstatesummaryfield (usage_id);

CREATE SEQUENCE proctoring_proctoredexamstudentallowance_seq;

CREATE TABLE proctoring_proctoredexamstudentallowance (
  id int NOT NULL DEFAULT NEXTVAL ('proctoring_proctoredexamstudentallowance_seq'),
  created timestamptz(6) NOT NULL,
  modified timestamptz(6) NOT NULL,
  key varchar(255) NOT NULL,
  value varchar(255) NOT NULL,
  proctored_exam_id int NOT NULL,
  user_id int NOT NULL,
  PRIMARY KEY (id),
  CONSTRAINT proctoring_proctoredexamstudentall_user_id_665ed945152c2f60_uniq UNIQUE  (user_id,proctored_exam_id,key)
 ,
  CONSTRAINT db55b83a7875e70b3a0ebd1f81a898d8 FOREIGN KEY (proctored_exam_id) REFERENCES proctoring_proctoredexam (id),
  CONSTRAINT proctoring_proctoredexamstudentallowance_user_id_f21ce9b6_fk FOREIGN KEY (user_id) REFERENCES auth_user (id)
) ;

CREATE INDEX db55b83a7875e70b3a0ebd1f81a898d8 ON proctoring_proctoredexamstudentallowance (proctored_exam_id);


CREATE SEQUENCE teams_courseteam_seq;

CREATE TABLE teams_courseteam (
  id int NOT NULL DEFAULT NEXTVAL ('teams_courseteam_seq'),
  team_id varchar(255) NOT NULL,
  discussion_topic_id varchar(255) NOT NULL,
  name varchar(255) NOT NULL,
  course_id varchar(255) NOT NULL,
  topic_id varchar(255) NOT NULL,
  date_created timestamptz(6) NOT NULL,
  description varchar(300) NOT NULL,
  country varchar(2) NOT NULL,
  language varchar(16) NOT NULL,
  last_activity_at timestamptz(6) NOT NULL,
  team_size int NOT NULL,
  PRIMARY KEY (id),
  CONSTRAINT team_id UNIQUE  (team_id),
  CONSTRAINT discussion_topic_id UNIQUE  (discussion_topic_id)
) ;

CREATE INDEX teams_courseteam_b068931c ON teams_courseteam (name);
CREATE INDEX teams_courseteam_ea134da7 ON teams_courseteam (course_id);
CREATE INDEX teams_courseteam_19b4d727 ON teams_courseteam (topic_id);
CREATE INDEX teams_courseteam_5ea53fcc ON teams_courseteam (last_activity_at);
CREATE INDEX teams_courseteam_181d83a1 ON teams_courseteam (team_size);


CREATE SEQUENCE grades_computegradessetting_seq;

CREATE TABLE grades_computegradessetting (
  id int NOT NULL DEFAULT NEXTVAL ('grades_computegradessetting_seq'),
  change_date timestamptz(6) NOT NULL,
  enabled bool NOT NULL,
  batch_size int NOT NULL,
  course_ids text NOT NULL,
  changed_by_id int DEFAULT NULL,
  PRIMARY KEY (id)
 ,
  CONSTRAINT grades_computegradessetting_changed_by_id_f2bf3678_fk FOREIGN KEY (changed_by_id) REFERENCES auth_user (id)
) ;

CREATE INDEX grades_computegra_changed_by_id_6599c94d3a43e583_fk_auth_user_id ON grades_computegradessetting (changed_by_id);



CREATE SEQUENCE courseware_options_seq;

CREATE TABLE courseware_options (
  id int NOT NULL DEFAULT NEXTVAL ('courseware_options_seq'),
  course_id varchar(145) NOT NULL,
  is_private bool NOT NULL,
  PRIMARY KEY (id),
  CONSTRAINT course_id_UNIQUE UNIQUE  (course_id)
) ;