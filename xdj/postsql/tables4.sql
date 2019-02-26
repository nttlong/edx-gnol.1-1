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