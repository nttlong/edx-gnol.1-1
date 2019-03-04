CREATE SEQUENCE django_admin_log_seq;

CREATE TABLE django_admin_log (
  id int NOT NULL DEFAULT NEXTVAL ('django_admin_log_seq'),
  action_time timestamptz(6) NOT NULL,
  object_id text,
  object_repr varchar(200) NOT NULL,
  action_flag smallint check (action_flag > 0) NOT NULL,
  change_message text NOT NULL,
  content_type_id int DEFAULT NULL,
  user_id int NOT NULL,
  PRIMARY KEY (id)
 ,
  CONSTRAINT djang_content_type_id_697914295151027a_fk_django_content_type_id FOREIGN KEY (content_type_id) REFERENCES django_content_type (id),
  CONSTRAINT django_admin_log_user_id_c564eba6_fk FOREIGN KEY (user_id) REFERENCES auth_user (id)
) ;

CREATE INDEX djang_content_type_id_697914295151027a_fk_django_content_type_id ON django_admin_log (content_type_id);
CREATE INDEX django_admin_log_user_id_52fdd58701c5f563_fk_auth_user_id ON django_admin_log (user_id);


CREATE SEQUENCE api_admin_apiaccessrequest_seq;

CREATE TABLE api_admin_apiaccessrequest (
  id int NOT NULL DEFAULT NEXTVAL ('api_admin_apiaccessrequest_seq'),
  created timestamptz(6) NOT NULL,
  modified timestamptz(6) NOT NULL,
  status varchar(255) NOT NULL,
  website varchar(200) NOT NULL,
  reason text NOT NULL,
  user_id int NOT NULL,
  company_address varchar(255) NOT NULL,
  company_name varchar(255) NOT NULL,
  contacted bool NOT NULL,
  site_id int NOT NULL,
  PRIMARY KEY (id),
  CONSTRAINT api_admin_apiaccessrequest_user_id_6753e50e296cabc7_uniq UNIQUE  (user_id)
 ,
  CONSTRAINT api_admin_apiaccessre_site_id_7963330a765f8041_fk_django_site_id FOREIGN KEY (site_id) REFERENCES django_site (id),
  CONSTRAINT api_admin_apiaccessrequest_user_id_eb0cc217_fk FOREIGN KEY (user_id) REFERENCES auth_user (id)
) ;

CREATE INDEX api_admin_apiaccessrequest_9acb4454 ON api_admin_apiaccessrequest (status);
CREATE INDEX api_admin_apiaccessrequest_9365d6e7 ON api_admin_apiaccessrequest (site_id);


CREATE SEQUENCE api_admin_apiaccessconfig_seq;

CREATE TABLE api_admin_apiaccessconfig (
  id int NOT NULL DEFAULT NEXTVAL ('api_admin_apiaccessconfig_seq'),
  change_date timestamptz(6) NOT NULL,
  enabled bool NOT NULL,
  changed_by_id int DEFAULT NULL,
  PRIMARY KEY (id)
 ,
  CONSTRAINT api_admin_apiaccessconfig_changed_by_id_d2f4cd88_fk FOREIGN KEY (changed_by_id) REFERENCES auth_user (id)
) ;

CREATE INDEX api_admin_apiacce_changed_by_id_771a504ee92a076c_fk_auth_user_id ON api_admin_apiaccessconfig (changed_by_id);


CREATE SEQUENCE assessment_assessmentfeedback_seq;

CREATE TABLE assessment_assessmentfeedback (
  id int NOT NULL DEFAULT NEXTVAL ('assessment_assessmentfeedback_seq'),
  submission_uuid varchar(128) NOT NULL,
  feedback_text text NOT NULL,
  PRIMARY KEY (id),
  CONSTRAINT submission_uuid_ux UNIQUE  (submission_uuid)
) ;


CREATE SEQUENCE assessment_peerworkflow_seq;

CREATE TABLE assessment_peerworkflow (
  id int NOT NULL DEFAULT NEXTVAL ('assessment_peerworkflow_seq'),
  student_id varchar(40) NOT NULL,
  item_id varchar(128) NOT NULL,
  course_id varchar(255) NOT NULL,
  submission_uuid varchar(128) NOT NULL,
  created_at timestamptz(6) NOT NULL,
  completed_at timestamptz(6) DEFAULT NULL,
  grading_completed_at timestamptz(6) DEFAULT NULL,
  cancelled_at timestamptz(6) DEFAULT NULL,
  PRIMARY KEY (id),
  CONSTRAINT submission_uuid UNIQUE  (submission_uuid)
) ;

CREATE INDEX assessment_peerworkflow_30a811f6 ON assessment_peerworkflow (student_id);
CREATE INDEX assessment_peerworkflow_82bfda79 ON assessment_peerworkflow (item_id);
CREATE INDEX assessment_peerworkflow_ea134da7 ON assessment_peerworkflow (course_id);
CREATE INDEX assessment_peerworkflow_fde81f11 ON assessment_peerworkflow (created_at);
CREATE INDEX assessment_peerworkflow_4430a679 ON assessment_peerworkflow (completed_at);
CREATE INDEX assessment_peerworkflow_85d183d8 ON assessment_peerworkflow (grading_completed_at);
CREATE INDEX assessment_peerworkflow_740da1db ON assessment_peerworkflow (cancelled_at);

CREATE SEQUENCE celery_utils_failedtask_seq;

CREATE TABLE celery_utils_failedtask (
  id int NOT NULL DEFAULT NEXTVAL ('celery_utils_failedtask_seq'),
  created timestamptz(6) NOT NULL,
  modified timestamptz(6) NOT NULL,
  task_name varchar(255) NOT NULL,
  task_id varchar(255) NOT NULL,
  args text NOT NULL,
  kwargs text NOT NULL,
  exc varchar(255) NOT NULL,
  datetime_resolved timestamptz(6) DEFAULT NULL,
  PRIMARY KEY (id)
) ;

CREATE INDEX celery_utils_failedtask_task_name_2cb4bd734027fd4f_idx ON celery_utils_failedtask (task_name,exc);
CREATE INDEX celery_utils_failedtask_57746cc8 ON celery_utils_failedtask (task_id);
CREATE INDEX celery_utils_failedtask_499aafb6 ON celery_utils_failedtask (datetime_resolved);


CREATE SEQUENCE contentserver_cdnuseragentsconfig_seq;

CREATE TABLE contentserver_cdnuseragentsconfig (
  id int NOT NULL DEFAULT NEXTVAL ('contentserver_cdnuseragentsconfig_seq'),
  change_date timestamp(6) NOT NULL,
  enabled bool NOT NULL,
  cdn_user_agents text NOT NULL,
  changed_by_id int DEFAULT NULL,
  PRIMARY KEY (id)
 ,
  CONSTRAINT contentserver_cdnuseragentsconfig_changed_by_id_19d8cb94_fk FOREIGN KEY (changed_by_id) REFERENCES auth_user (id)
) ;

CREATE INDEX contentserver_cdn_changed_by_id_36fe2b67b2c7f0ba_fk_auth_user_id ON contentserver_cdnuseragentsconfig (changed_by_id);

CREATE SEQUENCE course_creators_coursecreator_seq;

CREATE TABLE course_creators_coursecreator (
  id int NOT NULL DEFAULT NEXTVAL ('course_creators_coursecreator_seq'),
  state_changed timestamptz(6) NOT NULL,
  state varchar(24) NOT NULL,
  note varchar(512) NOT NULL,
  user_id int NOT NULL,
  PRIMARY KEY (id),
  CONSTRAINT course_creators_coursecreator_user_id_ux UNIQUE  (user_id),
  CONSTRAINT course_creators_coursec_user_id_46ea06ad28f0be3b_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES auth_user (id)
) ;

CREATE SEQUENCE courseware_offlinecomputedgradelog_seq;

CREATE TABLE courseware_offlinecomputedgradelog (
  id int NOT NULL DEFAULT NEXTVAL ('courseware_offlinecomputedgradelog_seq'),
  course_id varchar(255) NOT NULL,
  created timestamptz(6) DEFAULT NULL,
  seconds int NOT NULL,
  nstudents int NOT NULL,
  PRIMARY KEY (id)
) ;

CREATE INDEX courseware_offlinecomputedgradelog_ea134da7 ON courseware_offlinecomputedgradelog (course_id);
CREATE INDEX courseware_offlinecomputedgradelog_e2fa5388 ON courseware_offlinecomputedgradelog (created);


CREATE SEQUENCE courseware_offlinecomputedgrade_seq;

CREATE TABLE courseware_offlinecomputedgrade (
  id int NOT NULL DEFAULT NEXTVAL ('courseware_offlinecomputedgrade_seq'),
  course_id varchar(255) NOT NULL,
  created timestamptz(6) DEFAULT NULL,
  updated timestamptz(6) NOT NULL,
  gradeset text,
  user_id int NOT NULL,
  PRIMARY KEY (id),
  CONSTRAINT courseware_offlinecomputedgrade_user_id_46133bbd0926078f_uniq UNIQUE  (user_id,course_id)
 ,
  CONSTRAINT courseware_offlinecomputedgrade_user_id_14864cea_fk FOREIGN KEY (user_id) REFERENCES auth_user (id)
) ;

CREATE INDEX courseware_offlinecomputedgrade_ea134da7 ON courseware_offlinecomputedgrade (course_id);
CREATE INDEX courseware_offlinecomputedgrade_e2fa5388 ON courseware_offlinecomputedgrade (created);
CREATE INDEX courseware_offlinecomputedgrade_0f81d52e ON courseware_offlinecomputedgrade (updated);

CREATE SEQUENCE credit_creditconfig_seq;

CREATE TABLE credit_creditconfig (
  id int NOT NULL DEFAULT NEXTVAL ('credit_creditconfig_seq'),
  change_date timestamptz(6) NOT NULL,
  enabled bool NOT NULL,
  cache_ttl int check (cache_ttl > 0) NOT NULL,
  changed_by_id int DEFAULT NULL,
  PRIMARY KEY (id)
 ,
  CONSTRAINT credit_creditconfig_changed_by_id_72e1eca9_fk FOREIGN KEY (changed_by_id) REFERENCES auth_user (id)
) ;

CREATE INDEX credit_creditconf_changed_by_id_6270a800475f6694_fk_auth_user_id ON credit_creditconfig (changed_by_id);

CREATE SEQUENCE credit_crediteligibility_seq;

CREATE TABLE credit_crediteligibility (
  id int NOT NULL DEFAULT NEXTVAL ('credit_crediteligibility_seq'),
  created timestamptz(6) NOT NULL,
  modified timestamptz(6) NOT NULL,
  username varchar(255) NOT NULL,
  deadline timestamptz(6) NOT NULL,
  course_id int NOT NULL,
  PRIMARY KEY (id),
  CONSTRAINT credit_crediteligibility_username_936cb16677e83e_uniq UNIQUE  (username,course_id)
 ,
  CONSTRAINT credit_cred_course_id_4218adeba258bf8b_fk_credit_creditcourse_id FOREIGN KEY (course_id) REFERENCES credit_creditcourse (id)
) ;

CREATE INDEX credit_cred_course_id_4218adeba258bf8b_fk_credit_creditcourse_id ON credit_crediteligibility (course_id);
CREATE INDEX credit_crediteligibility_14c4b06b ON credit_crediteligibility (username);

CREATE SEQUENCE credit_creditprovider_seq;

CREATE TABLE credit_creditprovider (
  id int NOT NULL DEFAULT NEXTVAL ('credit_creditprovider_seq'),
  created timestamptz(6) NOT NULL,
  modified timestamptz(6) NOT NULL,
  provider_id varchar(255) NOT NULL,
  active bool NOT NULL,
  display_name varchar(255) NOT NULL,
  enable_integration bool NOT NULL,
  provider_url varchar(200) NOT NULL,
  provider_status_url varchar(200) NOT NULL,
  provider_description text NOT NULL,
  fulfillment_instructions text,
  eligibility_email_message text NOT NULL,
  receipt_email_message text NOT NULL,
  thumbnail_url varchar(255) NOT NULL,
  PRIMARY KEY (id),
  CONSTRAINT provider_id UNIQUE  (provider_id)
) ;


CREATE SEQUENCE credit_creditrequest_seq;

CREATE TABLE credit_creditrequest (
  id int NOT NULL DEFAULT NEXTVAL ('credit_creditrequest_seq'),
  created timestamptz(6) NOT NULL,
  modified timestamptz(6) NOT NULL,
  uuid varchar(36) NOT NULL,
  username varchar(255) NOT NULL,
  parameters text NOT NULL,
  status varchar(255) NOT NULL,
  course_id int NOT NULL,
  provider_id int NOT NULL,
  PRIMARY KEY (id),
  CONSTRAINT credit_creditrequest_uuid_ux UNIQUE  (uuid),
  CONSTRAINT credit_creditrequest_username_4f61c10bb0d67c01_uniq UNIQUE  (username,course_id,provider_id)
 ,
  CONSTRAINT credit_c_provider_id_f2973cc3e38a483_fk_credit_creditprovider_id FOREIGN KEY (provider_id) REFERENCES credit_creditprovider (id),
  CONSTRAINT credit_cred_course_id_578c5f1124002bab_fk_credit_creditcourse_id FOREIGN KEY (course_id) REFERENCES credit_creditcourse (id)
) ;

CREATE INDEX credit_cred_course_id_578c5f1124002bab_fk_credit_creditcourse_id ON credit_creditrequest (course_id);
CREATE INDEX credit_c_provider_id_f2973cc3e38a483_fk_credit_creditprovider_id ON credit_creditrequest (provider_id);
CREATE INDEX credit_creditrequest_14c4b06b ON credit_creditrequest (username);





CREATE SEQUENCE credit_creditrequirement_seq;

CREATE TABLE credit_creditrequirement (
  id int NOT NULL DEFAULT NEXTVAL ('credit_creditrequirement_seq'),
  created timestamptz(6) NOT NULL,
  modified timestamptz(6) NOT NULL,
  namespace varchar(255) NOT NULL,
  name varchar(255) NOT NULL,
  display_name varchar(255) NOT NULL,
  "order" int check ("order" > 0) NOT NULL,
  criteria text NOT NULL,
  active bool NOT NULL,
  course_id int NOT NULL,
  PRIMARY KEY (id),
  CONSTRAINT credit_creditrequirement_namespace_33039c83b3e69b8_uniq UNIQUE  (namespace,name,course_id)
 ,
  CONSTRAINT credit_cred_course_id_1c8fb9ebd295ae19_fk_credit_creditcourse_id FOREIGN KEY (course_id) REFERENCES credit_creditcourse (id)
) ;

CREATE INDEX credit_cred_course_id_1c8fb9ebd295ae19_fk_credit_creditcourse_id ON credit_creditrequirement (course_id);


CREATE SEQUENCE credit_creditrequirementstatus_seq;

CREATE TABLE credit_creditrequirementstatus (
  id int NOT NULL DEFAULT NEXTVAL ('credit_creditrequirementstatus_seq'),
  created timestamptz(6) NOT NULL,
  modified timestamptz(6) NOT NULL,
  username varchar(255) NOT NULL,
  status varchar(36) NOT NULL,
  reason text NOT NULL,
  requirement_id int NOT NULL,
  PRIMARY KEY (id),
  CONSTRAINT credit_creditrequirementstatus_username_67dcb69ebf779e3b_uniq UNIQUE  (username,requirement_id)
 ,
  CONSTRAINT c_requirement_id_3896aa6db214f84a_fk_credit_creditrequirement_id FOREIGN KEY (requirement_id) REFERENCES credit_creditrequirement (id)
) ;

CREATE INDEX c_requirement_id_3896aa6db214f84a_fk_credit_creditrequirement_id ON credit_creditrequirementstatus (requirement_id);
CREATE INDEX credit_creditrequirementstatus_14c4b06b ON credit_creditrequirementstatus (username);






CREATE SEQUENCE oauth2_provider_application_seq;

CREATE TABLE oauth2_provider_application (
  id int NOT NULL DEFAULT NEXTVAL ('oauth2_provider_application_seq'),
  client_id varchar(100) NOT NULL,
  redirect_uris text NOT NULL,
  client_type varchar(32) NOT NULL,
  authorization_grant_type varchar(32) NOT NULL,
  client_secret varchar(255) NOT NULL,
  name varchar(255) NOT NULL,
  user_id int DEFAULT NULL,
  skip_authorization smallint NOT NULL,
  PRIMARY KEY (id),
  CONSTRAINT client_id UNIQUE  (client_id)
 ,
  CONSTRAINT oauth2_provider_application_user_id_79829054_fk FOREIGN KEY (user_id) REFERENCES auth_user (id)
) ;

CREATE INDEX oauth2_provider_application_9d667c2b ON oauth2_provider_application (client_secret);
CREATE INDEX oauth2_provider_applica_user_id_7fa13387c260b798_fk_auth_user_id ON oauth2_provider_application (user_id);


CREATE SEQUENCE oauth2_provider_accesstoken_seq;

CREATE TABLE oauth2_provider_accesstoken (
  id int NOT NULL DEFAULT NEXTVAL ('oauth2_provider_accesstoken_seq'),
  token varchar(255) NOT NULL,
  expires timestamptz(6) NOT NULL,
  scope text NOT NULL,
  application_id int NOT NULL,
  user_id int DEFAULT NULL,
  PRIMARY KEY (id),
  CONSTRAINT oauth2_provider_accesstoken_token_3f77f86fb4ecbe0f_uniq UNIQUE  (token)
 ,
  CONSTRAINT D5ac3019ee1c474fd85718b015e3d3a1 FOREIGN KEY (application_id) REFERENCES oauth2_provider_application (id),
  CONSTRAINT oauth2_provider_accesstoken_user_id_6e4c9a65_fk FOREIGN KEY (user_id) REFERENCES auth_user (id)
) ;

CREATE INDEX D5ac3019ee1c474fd85718b015e3d3a1 ON oauth2_provider_accesstoken (application_id);
CREATE INDEX oauth2_provider_accesst_user_id_5e2f004fdebea22d_fk_auth_user_id ON oauth2_provider_accesstoken (user_id);


CREATE SEQUENCE oauth2_provider_grant_seq;

CREATE TABLE oauth2_provider_grant (
  id int NOT NULL DEFAULT NEXTVAL ('oauth2_provider_grant_seq'),
  code varchar(255) NOT NULL,
  expires timestamptz(6) NOT NULL,
  redirect_uri varchar(255) NOT NULL,
  scope text NOT NULL,
  application_id int NOT NULL,
  user_id int NOT NULL,
  PRIMARY KEY (id),
  CONSTRAINT oauth2_provider_grant_code_a5c88732687483b_uniq UNIQUE  (code)
 ,
  CONSTRAINT D6b2a4f1402d4f338b690c38b795830a FOREIGN KEY (application_id) REFERENCES oauth2_provider_application (id),
  CONSTRAINT oauth2_provider_grant_user_id_e8f62af8_fk FOREIGN KEY (user_id) REFERENCES auth_user (id)
) ;

CREATE INDEX D6b2a4f1402d4f338b690c38b795830a ON oauth2_provider_grant (application_id);
CREATE INDEX oauth2_provider_grant_user_id_3111344894d452da_fk_auth_user_id ON oauth2_provider_grant (user_id);

CREATE SEQUENCE oauth2_provider_refreshtoken_seq;

CREATE TABLE oauth2_provider_refreshtoken (
  id int NOT NULL DEFAULT NEXTVAL ('oauth2_provider_refreshtoken_seq'),
  token varchar(255) NOT NULL,
  access_token_id int NOT NULL,
  application_id int NOT NULL,
  user_id int NOT NULL,
  PRIMARY KEY (id),
  CONSTRAINT access_token_id UNIQUE  (access_token_id),
  CONSTRAINT oauth2_provider_refreshtoken_token_1e4e9388e6a22527_uniq UNIQUE  (token)
 ,
  CONSTRAINT b58d9cb3b93afb36b11b7741bf1bcc1a FOREIGN KEY (access_token_id) REFERENCES oauth2_provider_accesstoken (id),
  CONSTRAINT d3e264ceec355cabed6ff9976fc42a06 FOREIGN KEY (application_id) REFERENCES oauth2_provider_application (id),
  CONSTRAINT oauth2_provider_refreshtoken_user_id_da837fce_fk FOREIGN KEY (user_id) REFERENCES auth_user (id)
) ;

CREATE INDEX d3e264ceec355cabed6ff9976fc42a06 ON oauth2_provider_refreshtoken (application_id);
CREATE INDEX oauth2_provider_refresh_user_id_3f695b639cfbc9a3_fk_auth_user_id ON oauth2_provider_refreshtoken (user_id);


CREATE SEQUENCE notify_settings_seq;

CREATE TABLE notify_settings (
  id int NOT NULL DEFAULT NEXTVAL ('notify_settings_seq'),
  interval bool NOT NULL,
  user_id int NOT NULL,
  PRIMARY KEY (id)
 ,
  CONSTRAINT notify_settings_user_id_088ebffc_fk FOREIGN KEY (user_id) REFERENCES auth_user (id)
) ;

CREATE INDEX notify_settings_user_id_14e062dc3d4345b3_fk_auth_user_id ON notify_settings (user_id);


CREATE TABLE notify_notificationtype (
  "key" varchar(128) NOT NULL,
  "label" varchar(128) DEFAULT NULL,
  content_type_id int DEFAULT NULL,
  PRIMARY KEY (key)
 ,
  CONSTRAINT notif_content_type_id_181f055892581fd8_fk_django_content_type_id FOREIGN KEY (content_type_id) REFERENCES django_content_type (id)
) ;

CREATE INDEX notif_content_type_id_181f055892581fd8_fk_django_content_type_id ON notify_notificationtype (content_type_id);


CREATE SEQUENCE notify_subscription_seq;

CREATE TABLE notify_subscription (
  subscription_id int NOT NULL DEFAULT NEXTVAL ('notify_subscription_seq'),
  object_id varchar(64) DEFAULT NULL,
  send_emails bool NOT NULL,
  notification_type_id varchar(128) NOT NULL,
  settings_id int NOT NULL,
  PRIMARY KEY (subscription_id)
 ,
  CONSTRAINT a2462650bbefc26547210b80dec61069 FOREIGN KEY (notification_type_id) REFERENCES notify_notificationtype (key),
  CONSTRAINT notify_subscr_settings_id_64d594d127e8ca95_fk_notify_settings_id FOREIGN KEY (settings_id) REFERENCES notify_settings (id)
) ;

CREATE INDEX a2462650bbefc26547210b80dec61069 ON notify_subscription (notification_type_id);
CREATE INDEX notify_subscr_settings_id_64d594d127e8ca95_fk_notify_settings_id ON notify_subscription (settings_id);

CREATE SEQUENCE notify_notification_seq;

CREATE TABLE notify_notification (
  id int NOT NULL DEFAULT NEXTVAL ('notify_notification_seq'),
  message text NOT NULL,
  url varchar(200) DEFAULT NULL,
  is_viewed bool NOT NULL,
  is_emailed bool NOT NULL,
  created timestamptz(6) NOT NULL,
  subscription_id int DEFAULT NULL,
  PRIMARY KEY (id)
 ,
  CONSTRAINT D48032390695e0699e92b8d7ccdbff7e FOREIGN KEY (subscription_id) REFERENCES notify_subscription (subscription_id)
) ;

CREATE INDEX notify_notification_ef42673f ON notify_notification (subscription_id);


CREATE SEQUENCE django_openid_auth_association_seq;

CREATE TABLE django_openid_auth_association (
  id int NOT NULL DEFAULT NEXTVAL ('django_openid_auth_association_seq'),
  server_url text NOT NULL,
  handle varchar(255) NOT NULL,
  secret text NOT NULL,
  issued int NOT NULL,
  lifetime int NOT NULL,
  assoc_type text NOT NULL,
  PRIMARY KEY (id)
) ;

CREATE SEQUENCE django_openid_auth_nonce_seq;

CREATE TABLE django_openid_auth_nonce (
  id int NOT NULL DEFAULT NEXTVAL ('django_openid_auth_nonce_seq'),
  server_url varchar(2047) NOT NULL,
  "timestamp" int NOT NULL,
  salt varchar(40) NOT NULL,
  PRIMARY KEY (id)
) ;

CREATE SEQUENCE django_openid_auth_useropenid_seq;

CREATE TABLE django_openid_auth_useropenid (
  id int NOT NULL DEFAULT NEXTVAL ('django_openid_auth_useropenid_seq'),
  claimed_id text NOT NULL,
  display_id text NOT NULL,
  user_id int NOT NULL,
  PRIMARY KEY (id)
 ,
  CONSTRAINT django_openid_auth_useropenid_user_id_707d846c_fk FOREIGN KEY (user_id) REFERENCES auth_user (id)
) ;

CREATE INDEX django_openid_auth_user_user_id_136119e72782e2cf_fk_auth_user_id ON django_openid_auth_useropenid (user_id);

CREATE SEQUENCE djcelery_crontabschedule_seq;

CREATE TABLE djcelery_crontabschedule (
  id int NOT NULL DEFAULT NEXTVAL ('djcelery_crontabschedule_seq'),
  minute varchar(64) NOT NULL,
  hour varchar(64) NOT NULL,
  day_of_week varchar(64) NOT NULL,
  day_of_month varchar(64) NOT NULL,
  month_of_year varchar(64) NOT NULL,
  PRIMARY KEY (id)
) ;

CREATE SEQUENCE djcelery_intervalschedule_seq;

CREATE TABLE djcelery_intervalschedule (
  id int NOT NULL DEFAULT NEXTVAL ('djcelery_intervalschedule_seq'),
  every int NOT NULL,
  period varchar(24) NOT NULL,
  PRIMARY KEY (id)
) ;

CREATE SEQUENCE djcelery_periodictask_seq;

CREATE TABLE djcelery_periodictask (
  id int NOT NULL DEFAULT NEXTVAL ('djcelery_periodictask_seq'),
  name varchar(200) NOT NULL,
  task varchar(200) NOT NULL,
  args text NOT NULL,
  kwargs text NOT NULL,
  queue varchar(200) DEFAULT NULL,
  exchange varchar(200) DEFAULT NULL,
  routing_key varchar(200) DEFAULT NULL,
  expires timestamptz(6) DEFAULT NULL,
  enabled bool NOT NULL,
  last_run_at timestamptz(6) DEFAULT NULL,
  total_run_count int check (total_run_count > 0) NOT NULL,
  date_changed timestamp(6) NOT NULL,
  description text NOT NULL,
  crontab_id int DEFAULT NULL,
  interval_id int DEFAULT NULL,
  PRIMARY KEY (id),
  CONSTRAINT djcelery_periodictask_name_ux UNIQUE  (name)
 ,
  CONSTRAINT djc_interval_id_20cfc1cad060dfad_fk_djcelery_intervalschedule_id FOREIGN KEY (interval_id) REFERENCES djcelery_intervalschedule (id),
  CONSTRAINT djcel_crontab_id_1d8228f5b44b680a_fk_djcelery_crontabschedule_id FOREIGN KEY (crontab_id) REFERENCES djcelery_crontabschedule (id)
) ;

CREATE INDEX djcel_crontab_id_1d8228f5b44b680a_fk_djcelery_crontabschedule_id ON djcelery_periodictask (crontab_id);
CREATE INDEX djc_interval_id_20cfc1cad060dfad_fk_djcelery_intervalschedule_id ON djcelery_periodictask (interval_id);

CREATE SEQUENCE djcelery_workerstate_seq;

CREATE TABLE djcelery_workerstate (
  id int NOT NULL DEFAULT NEXTVAL ('djcelery_workerstate_seq'),
  hostname varchar(255) NOT NULL,
  last_heartbeat timestamptz(6) DEFAULT NULL,
  PRIMARY KEY (id),
  CONSTRAINT hostname UNIQUE  (hostname)
) ;

CREATE INDEX djcelery_workerstate_f129901a ON djcelery_workerstate (last_heartbeat);

CREATE SEQUENCE djcelery_taskstate_seq;

CREATE TABLE djcelery_taskstate (
  id int NOT NULL DEFAULT NEXTVAL ('djcelery_taskstate_seq'),
  state varchar(64) NOT NULL,
  task_id varchar(36) NOT NULL,
  name varchar(200) DEFAULT NULL,
  tstamp timestamptz(6) NOT NULL,
  args text,
  kwargs text,
  eta timestamptz(6) DEFAULT NULL,
  expires timestamptz(6) DEFAULT NULL,
  result text,
  traceback text,
  runtime double precision DEFAULT NULL,
  retries int NOT NULL,
  hidden bool NOT NULL,
  worker_id int DEFAULT NULL,
  PRIMARY KEY (id),
  CONSTRAINT djcelery_taskstate_task_id UNIQUE  (task_id)
 ,
  CONSTRAINT djcelery_t_worker_id_30050731b1c3d3d9_fk_djcelery_workerstate_id FOREIGN KEY (worker_id) REFERENCES djcelery_workerstate (id)
) ;

CREATE INDEX djcelery_taskstate_9ed39e2e ON djcelery_taskstate (state);
CREATE INDEX djcelery_taskstate_b068931c ON djcelery_taskstate (name);
CREATE INDEX djcelery_taskstate_863bb2ee ON djcelery_taskstate (tstamp);
CREATE INDEX djcelery_taskstate_662f707d ON djcelery_taskstate (hidden);
CREATE INDEX djcelery_taskstate_ce77e6ef ON djcelery_taskstate (worker_id);

CREATE SEQUENCE embargo_ipfilter_seq;

CREATE TABLE embargo_ipfilter (
  id int NOT NULL DEFAULT NEXTVAL ('embargo_ipfilter_seq'),
  change_date timestamptz(6) NOT NULL,
  enabled bool NOT NULL,
  whitelist text NOT NULL,
  blacklist text NOT NULL,
  changed_by_id int DEFAULT NULL,
  PRIMARY KEY (id)
 ,
  CONSTRAINT embargo_ipfilter_changed_by_id_39e4eed2_fk FOREIGN KEY (changed_by_id) REFERENCES auth_user (id)
) ;

CREATE INDEX embargo_ipfilter_changed_by_id_5c820bfac889ea81_fk_auth_user_id ON embargo_ipfilter (changed_by_id);

CREATE SEQUENCE embargo_restrictedcourse_seq;

CREATE TABLE embargo_restrictedcourse (
  id int NOT NULL DEFAULT NEXTVAL ('embargo_restrictedcourse_seq'),
  course_key varchar(255) NOT NULL,
  enroll_msg_key varchar(255) NOT NULL,
  access_msg_key varchar(255) NOT NULL,
  disable_access_check smallint NOT NULL,
  PRIMARY KEY (id),
  CONSTRAINT embargo_restrictedcourse_course_key UNIQUE  (course_key)
) ;

CREATE SEQUENCE proctoring_proctoredexamstudentattempt_seq;

CREATE TABLE proctoring_proctoredexamstudentattempt (
  id int NOT NULL DEFAULT NEXTVAL ('proctoring_proctoredexamstudentattempt_seq'),
  created timestamptz(6) NOT NULL,
  modified timestamptz(6) NOT NULL,
  started_at timestamptz(6) DEFAULT NULL,
  completed_at timestamptz(6) DEFAULT NULL,
  last_poll_timestamp timestamptz(6) DEFAULT NULL,
  last_poll_ipaddr varchar(32) DEFAULT NULL,
  attempt_code varchar(255) DEFAULT NULL,
  external_id varchar(255) DEFAULT NULL,
  allowed_time_limit_mins int DEFAULT NULL,
  status varchar(64) NOT NULL,
  taking_as_proctored bool NOT NULL,
  is_sample_attempt bool NOT NULL,
  student_name varchar(255) NOT NULL,
  review_policy_id int DEFAULT NULL,
  proctored_exam_id int NOT NULL,
  user_id int NOT NULL,
  is_status_acknowledged smallint NOT NULL,
  PRIMARY KEY (id),
  CONSTRAINT proctoring_proctoredexamstudentatt_user_id_15d13fa8dac316a0_uniq UNIQUE  (user_id,proctored_exam_id)
 ,
  CONSTRAINT D5e0a120c32f715bfe04a0a57f399ec0 FOREIGN KEY (proctored_exam_id) REFERENCES proctoring_proctoredexam (id),
  CONSTRAINT proctoring_proctoredexamstudentattempt_user_id_2b58b7ed_fk FOREIGN KEY (user_id) REFERENCES auth_user (id)
) ;

CREATE INDEX D5e0a120c32f715bfe04a0a57f399ec0 ON proctoring_proctoredexamstudentattempt (proctored_exam_id);
CREATE INDEX proctoring_proctoredexamstudentattempt_b38e5b0e ON proctoring_proctoredexamstudentattempt (attempt_code);
CREATE INDEX proctoring_proctoredexamstudentattempt_0e684294 ON proctoring_proctoredexamstudentattempt (external_id);

CREATE SEQUENCE oauth2_client_seq;

CREATE TABLE oauth2_client (
  id int NOT NULL DEFAULT NEXTVAL ('oauth2_client_seq'),
  name varchar(255) NOT NULL,
  url varchar(200) NOT NULL,
  redirect_uri varchar(200) NOT NULL,
  client_id varchar(255) NOT NULL,
  client_secret varchar(255) NOT NULL,
  client_type int NOT NULL,
  user_id int DEFAULT NULL,
  logout_uri varchar(200) DEFAULT NULL,
  PRIMARY KEY (id)
 ,
  CONSTRAINT oauth2_client_user_id_21c89c78_fk FOREIGN KEY (user_id) REFERENCES auth_user (id)
) ;

CREATE INDEX oauth2_client_user_id_2b47284bbd512fe1_fk_auth_user_id ON oauth2_client (user_id);

CREATE SEQUENCE oauth2_provider_trustedclient_seq;

CREATE TABLE oauth2_provider_trustedclient (
  id int NOT NULL DEFAULT NEXTVAL ('oauth2_provider_trustedclient_seq'),
  client_id int NOT NULL,
  PRIMARY KEY (id)
 ,
  CONSTRAINT oauth2_provider_tr_client_id_bb96ea0be42c00a_fk_oauth2_client_id FOREIGN KEY (client_id) REFERENCES oauth2_client (id)
) ;

CREATE INDEX oauth2_provider_tr_client_id_bb96ea0be42c00a_fk_oauth2_client_id ON oauth2_provider_trustedclient (client_id);

CREATE TABLE enterprise_enterprisecustomer (
  created timestamptz(6) NOT NULL,
  modified timestamptz(6) NOT NULL,
  uuid char(32) NOT NULL,
  name varchar(255) NOT NULL,
  active bool NOT NULL,
  site_id int NOT NULL,
  catalog int check (catalog > 0) DEFAULT NULL,
  enable_data_sharing_consent bool NOT NULL,
  enforce_data_sharing_consent varchar(25) NOT NULL,
  enable_audit_enrollment bool NOT NULL,
  enable_audit_data_reporting bool NOT NULL,
  replace_sensitive_sso_username bool NOT NULL,
  hide_course_original_price bool NOT NULL,
  slug varchar(30) NOT NULL,
  PRIMARY KEY (uuid),
  CONSTRAINT enterprise_enterprisecustomer_slug_80411f46_uniq UNIQUE  (slug)
 ,
  CONSTRAINT enterprise_enterprise_site_id_41ce54c2601930cd_fk_django_site_id FOREIGN KEY (site_id) REFERENCES django_site (id)
) ;

CREATE INDEX enterprise_enterprisecustomer_9365d6e7 ON enterprise_enterprisecustomer (site_id);


CREATE SEQUENCE enterprise_pendingenterprisecustomeruser_seq;

CREATE TABLE enterprise_pendingenterprisecustomeruser (
  id int NOT NULL DEFAULT NEXTVAL ('enterprise_pendingenterprisecustomeruser_seq'),
  created timestamptz(6) NOT NULL,
  modified timestamptz(6) NOT NULL,
  user_email varchar(254) NOT NULL,
  enterprise_customer_id char(32) NOT NULL,
  PRIMARY KEY (id),
  CONSTRAINT enterprise_pendingenterprisecus_user_email_1838ab42a578cf3c_uniq UNIQUE  (user_email)
 ,
  CONSTRAINT D0f27fd26a677554e54740cfe1555271 FOREIGN KEY (enterprise_customer_id) REFERENCES enterprise_enterprisecustomer (uuid)
) ;

CREATE INDEX D0f27fd26a677554e54740cfe1555271 ON enterprise_pendingenterprisecustomeruser (enterprise_customer_id);


CREATE SEQUENCE enterprise_enrollmentnotificationemailtemplate_seq;

CREATE TABLE enterprise_enrollmentnotificationemailtemplate (
  id int NOT NULL DEFAULT NEXTVAL ('enterprise_enrollmentnotificationemailtemplate_seq'),
  created timestamptz(6) NOT NULL,
  modified timestamptz(6) NOT NULL,
  plaintext_template text NOT NULL,
  html_template text NOT NULL,
  subject_line varchar(100) NOT NULL,
  enterprise_customer_id char(32) NOT NULL,
  PRIMARY KEY (id),
  CONSTRAINT enterprise_customer_id UNIQUE  (enterprise_customer_id),
  CONSTRAINT D00946bb46f9643cebba6a818adbfd61 FOREIGN KEY (enterprise_customer_id) REFERENCES enterprise_enterprisecustomer (uuid)
) ;

CREATE TABLE enterprise_enterprisecustomercatalog (
  created timestamptz(6) NOT NULL,
  modified timestamp(6) NOT NULL,
  uuid varchar(36) NOT NULL,
  enterprise_customer_id char(32) NOT NULL,
  content_filter text,
  title varchar(255) NOT NULL,
  enabled_course_modes text NOT NULL,
  publish_audit_enrollment_urls smallint NOT NULL,
  PRIMARY KEY (uuid)
 ,
  CONSTRAINT D6b10b4c766f4d007227cae59564ac44 FOREIGN KEY (enterprise_customer_id) REFERENCES enterprise_enterprisecustomer (uuid)
) ;

CREATE INDEX D6b10b4c766f4d007227cae59564ac44 ON enterprise_enterprisecustomercatalog (enterprise_customer_id);

CREATE SEQUENCE enterprise_enterprisecustomeruser_seq;

CREATE TABLE enterprise_enterprisecustomeruser (
  id int NOT NULL DEFAULT NEXTVAL ('enterprise_enterprisecustomeruser_seq'),
  created timestamptz(6) NOT NULL,
  modified timestamptz(6) NOT NULL,
  user_id int check (user_id > 0) NOT NULL,
  enterprise_customer_id char(32) NOT NULL,
  active bool NOT NULL,
  PRIMARY KEY (id),
  CONSTRAINT enterprise_enterpri_enterprise_customer_id_257cf08ca29bc48b_uniq UNIQUE  (enterprise_customer_id,user_id),
  CONSTRAINT D38bb8d455e64dd8470b7606517efded FOREIGN KEY (enterprise_customer_id) REFERENCES enterprise_enterprisecustomer (uuid)
) ;

CREATE SEQUENCE enterprise_enterprisecourseenrollment_seq;

CREATE TABLE enterprise_enterprisecourseenrollment (
  id int NOT NULL DEFAULT NEXTVAL ('enterprise_enterprisecourseenrollment_seq'),
  created timestamptz(6) NOT NULL,
  modified timestamptz(6) NOT NULL,
  course_id varchar(255) NOT NULL,
  enterprise_customer_user_id int NOT NULL,
  PRIMARY KEY (id),
  CONSTRAINT enterprise_ente_enterprise_customer_user_id_18f302e179a5aca_uniq UNIQUE  (enterprise_customer_user_id,course_id),
  CONSTRAINT D69dbba1e57159194d7bba595f75cb24 FOREIGN KEY (enterprise_customer_user_id) REFERENCES enterprise_enterprisecustomeruser (id)
) ;

CREATE SEQUENCE enterprise_enterprisecustomerreportingconfiguration_seq;

CREATE TABLE enterprise_enterprisecustomerreportingconfiguration (
  id int NOT NULL DEFAULT NEXTVAL ('enterprise_enterprisecustomerreportingconfiguration_seq'),
  created timestamptz(6) NOT NULL,
  modified timestamptz(6) NOT NULL,
  active bool NOT NULL,
  delivery_method varchar(20) NOT NULL,
  email text NOT NULL,
  frequency varchar(20) NOT NULL,
  day_of_month smallint DEFAULT NULL,
  day_of_week smallint DEFAULT NULL,
  hour_of_day smallint NOT NULL,
  enterprise_customer_id char(32) NOT NULL,
  sftp_file_path varchar(256) DEFAULT NULL,
  sftp_hostname varchar(256) DEFAULT NULL,
  sftp_port int check (sftp_port > 0) DEFAULT NULL,
  sftp_username varchar(256) DEFAULT NULL,
  decrypted_password BYTEA,
  decrypted_sftp_password BYTEA,
  data_type varchar(20) NOT NULL,
  report_type varchar(20) NOT NULL,
  PRIMARY KEY (id)
 ,
  CONSTRAINT enterprise_enterpris_enterprise_customer__d5b55543_fk_enterpris FOREIGN KEY (enterprise_customer_id) REFERENCES enterprise_enterprisecustomer (uuid)
) ;

CREATE INDEX enterprise_enterprisecustom_enterprise_customer_id_d5b55543 ON enterprise_enterprisecustomerreportingconfiguration (enterprise_customer_id);

CREATE SEQUENCE enterprise_pendingenrollment_seq;

CREATE TABLE enterprise_pendingenrollment (
  id int NOT NULL DEFAULT NEXTVAL ('enterprise_pendingenrollment_seq'),
  created timestamptz(6) NOT NULL,
  modified timestamptz(6) NOT NULL,
  course_id varchar(255) NOT NULL,
  course_mode varchar(25) NOT NULL,
  user_id int NOT NULL,
  PRIMARY KEY (id),
  CONSTRAINT enterprise_pendingenrollment_user_id_111d29e0f8aebec5_uniq UNIQUE  (user_id,course_id),
  CONSTRAINT a9ce3c7057d5f3b27dc64261037ad37d FOREIGN KEY (user_id) REFERENCES enterprise_pendingenterprisecustomeruser (id)
) ;

CREATE SEQUENCE consent_datasharingconsent_seq;

CREATE TABLE consent_datasharingconsent (
  id int NOT NULL DEFAULT NEXTVAL ('consent_datasharingconsent_seq'),
  created timestamptz(6) NOT NULL,
  modified timestamptz(6) NOT NULL,
  username varchar(255) NOT NULL,
  granted bool DEFAULT NULL,
  course_id varchar(255) NOT NULL,
  enterprise_customer_id char(32) NOT NULL,
  PRIMARY KEY (id),
  CONSTRAINT consent_datasharing_enterprise_customer_id_667a1480f56052a2_uniq UNIQUE  (enterprise_customer_id,username,course_id),
  CONSTRAINT D030ccea2714cf8f0a2e65e948ee3d2d FOREIGN KEY (enterprise_customer_id) REFERENCES enterprise_enterprisecustomer (uuid)
) ;

CREATE SEQUENCE consent_datasharingconsenttextoverrides_seq;

CREATE TABLE consent_datasharingconsenttextoverrides (
  id int NOT NULL DEFAULT NEXTVAL ('consent_datasharingconsenttextoverrides_seq'),
  created timestamptz(6) NOT NULL,
  modified timestamptz(6) NOT NULL,
  page_title varchar(255) NOT NULL,
  left_sidebar_text text,
  top_paragraph text,
  agreement_text text,
  continue_text varchar(255) NOT NULL,
  abort_text varchar(255) NOT NULL,
  policy_dropdown_header varchar(255) DEFAULT NULL,
  policy_paragraph text,
  confirmation_modal_header varchar(255) NOT NULL,
  confirmation_modal_text text NOT NULL,
  modal_affirm_decline_text varchar(255) NOT NULL,
  modal_abort_decline_text varchar(255) NOT NULL,
  declined_notification_title text NOT NULL,
  declined_notification_message text NOT NULL,
  published smallint NOT NULL,
  enterprise_customer_id char(32) NOT NULL,
  PRIMARY KEY (id),
  CONSTRAINT consent_datasharingconsenttextoverrides_enterprise_customer_id UNIQUE  (enterprise_customer_id),
  CONSTRAINT consent_datasharingc_enterprise_customer__b979dfc1_fk_enterpris FOREIGN KEY (enterprise_customer_id) REFERENCES enterprise_enterprisecustomer (uuid)
) ;

CREATE SEQUENCE degreed_degreedenterprisecustomerconfiguration_seq;

CREATE TABLE degreed_degreedenterprisecustomerconfiguration (
  id int NOT NULL DEFAULT NEXTVAL ('degreed_degreedenterprisecustomerconfiguration_seq'),
  created timestamptz(6) NOT NULL,
  modified timestamptz(6) NOT NULL,
  active bool NOT NULL,
  key varchar(255) NOT NULL,
  secret varchar(255) NOT NULL,
  degreed_company_id varchar(255) NOT NULL,
  enterprise_customer_id char(32) NOT NULL,
  transmission_chunk_size int NOT NULL,
  PRIMARY KEY (id),
  CONSTRAINT degreed_degreedenterprisecustomerconfiguration_enterprise_customer_id UNIQUE  (enterprise_customer_id),
  CONSTRAINT D8dff51a65b4ed0c3cf73b425e343929 FOREIGN KEY (enterprise_customer_id) REFERENCES enterprise_enterprisecustomer (uuid)
) ;

CREATE SEQUENCE degreed_degreedglobalconfiguration_seq;

CREATE TABLE degreed_degreedglobalconfiguration (
  id int NOT NULL DEFAULT NEXTVAL ('degreed_degreedglobalconfiguration_seq'),
  change_date timestamptz(6) NOT NULL,
  enabled bool NOT NULL,
  degreed_base_url varchar(255) NOT NULL,
  completion_status_api_path varchar(255) NOT NULL,
  course_api_path varchar(255) NOT NULL,
  oauth_api_path varchar(255) NOT NULL,
  degreed_user_id varchar(255) NOT NULL,
  degreed_user_password varchar(255) NOT NULL,
  provider_id varchar(100) NOT NULL,
  changed_by_id int DEFAULT NULL,
  PRIMARY KEY (id)
 ,
  CONSTRAINT degreed_degreedglobalconfiguration_changed_by_id_00a8a7be_fk FOREIGN KEY (changed_by_id) REFERENCES auth_user (id)
) ;

CREATE INDEX degreed_degreedgl_changed_by_id_3af82cf8c774e820_fk_auth_user_id ON degreed_degreedglobalconfiguration (changed_by_id);






CREATE SEQUENCE enterprise_enterprisecustomerbrandingconfiguration_seq;

CREATE TABLE enterprise_enterprisecustomerbrandingconfiguration (
  id int NOT NULL DEFAULT NEXTVAL ('enterprise_enterprisecustomerbrandingconfiguration_seq'),
  created timestamptz(6) NOT NULL,
  modified timestamptz(6) NOT NULL,
  logo varchar(255) DEFAULT NULL,
  enterprise_customer_id char(32) NOT NULL,
  PRIMARY KEY (id),
  CONSTRAINT enterprise_enterprisecustomerbrandingconfiguration_enterprise_customer_id UNIQUE  (enterprise_customer_id),
  CONSTRAINT D1fbd8b8ab06c9a5efdee961a7a75e55 FOREIGN KEY (enterprise_customer_id) REFERENCES enterprise_enterprisecustomer (uuid)
) ;




CREATE SEQUENCE external_auth_externalauthmap_seq;

CREATE TABLE external_auth_externalauthmap (
  id int NOT NULL DEFAULT NEXTVAL ('external_auth_externalauthmap_seq'),
  external_id varchar(255) NOT NULL,
  external_domain varchar(255) NOT NULL,
  external_credentials text NOT NULL,
  external_email varchar(255) NOT NULL,
  external_name varchar(255) NOT NULL,
  internal_password varchar(31) NOT NULL,
  dtcreated timestamptz(6) NOT NULL,
  dtsignup timestamptz(6) DEFAULT NULL,
  user_id int DEFAULT NULL,
  PRIMARY KEY (id),
  CONSTRAINT external_auth_externalauthmap_external_id_7f035ef8bc4d313e_uniq UNIQUE  (external_id,external_domain),
  CONSTRAINT external_auth_externalauthmap_user_id UNIQUE  (user_id)
 ,
  CONSTRAINT external_auth_externalauthmap_user_id_91b3ca08_fk FOREIGN KEY (user_id) REFERENCES auth_user (id)
) ;

CREATE INDEX external_auth_externalauthmap_0e684294 ON external_auth_externalauthmap (external_id);
CREATE INDEX external_auth_externalauthmap_630a0308 ON external_auth_externalauthmap (external_domain);
CREATE INDEX external_auth_externalauthmap_e9425fc5 ON external_auth_externalauthmap (external_email);
CREATE INDEX external_auth_externalauthmap_c9555995 ON external_auth_externalauthmap (external_name);


CREATE SEQUENCE microsite_configuration_micrositehistory_seq;

CREATE TABLE microsite_configuration_micrositehistory (
  id int NOT NULL DEFAULT NEXTVAL ('microsite_configuration_micrositehistory_seq'),
  created timestamptz(6) NOT NULL,
  modified timestamptz(6) NOT NULL,
  key varchar(63) NOT NULL,
  values text NOT NULL,
  site_id int NOT NULL,
  PRIMARY KEY (id)
 ,
  CONSTRAINT microsite_configurati_site_id_6977a04d3625a533_fk_django_site_id FOREIGN KEY (site_id) REFERENCES django_site (id)
) ;

CREATE INDEX microsite_configurati_site_id_6977a04d3625a533_fk_django_site_id ON microsite_configuration_micrositehistory (site_id);


CREATE SEQUENCE microsite_configuration_microsite_seq;

CREATE TABLE microsite_configuration_microsite (
  id int NOT NULL DEFAULT NEXTVAL ('microsite_configuration_microsite_seq'),
  key varchar(63) NOT NULL,
  values text NOT NULL,
  site_id int NOT NULL,
  PRIMARY KEY (id),
  CONSTRAINT key UNIQUE  (key),
  CONSTRAINT microsite_configuration_microsite_site_id UNIQUE  (site_id),
  CONSTRAINT microsite_configuratio_site_id_3ebe20a76de5aa4_fk_django_site_id FOREIGN KEY (site_id) REFERENCES django_site (id)
) ;

CREATE SEQUENCE microsite_configuration_micrositeorganizationmapping_seq;

CREATE TABLE microsite_configuration_micrositeorganizationmapping (
  id int NOT NULL DEFAULT NEXTVAL ('microsite_configuration_micrositeorganizationmapping_seq'),
  organization varchar(63) NOT NULL,
  microsite_id int NOT NULL,
  PRIMARY KEY (id),
  CONSTRAINT organization UNIQUE  (organization)
 ,
  CONSTRAINT D1c5d7dbbb2cde12ce18b38d46f71ee0 FOREIGN KEY (microsite_id) REFERENCES microsite_configuration_microsite (id)
) ;

CREATE INDEX D1c5d7dbbb2cde12ce18b38d46f71ee0 ON microsite_configuration_micrositeorganizationmapping (microsite_id);

CREATE SEQUENCE microsite_configuration_micrositetemplate_seq;

CREATE TABLE microsite_configuration_micrositetemplate (
  id int NOT NULL DEFAULT NEXTVAL ('microsite_configuration_micrositetemplate_seq'),
  template_uri varchar(255) NOT NULL,
  template text NOT NULL,
  microsite_id int NOT NULL,
  PRIMARY KEY (id),
  CONSTRAINT microsite_configuration_micros_microsite_id_80b3f3616d2e317_uniq UNIQUE  (microsite_id,template_uri)
 ,
  CONSTRAINT D4919cbc5f1414d3de93aa9ec9aa48f3 FOREIGN KEY (microsite_id) REFERENCES microsite_configuration_microsite (id)
) ;

CREATE INDEX microsite_configuration_micrositetemplate_a8b249ec ON microsite_configuration_micrositetemplate (template_uri);

CREATE SEQUENCE milestones_usermilestone_seq;

CREATE TABLE milestones_usermilestone (
  id int NOT NULL DEFAULT NEXTVAL ('milestones_usermilestone_seq'),
  created timestamptz(6) NOT NULL,
  modified timestamptz(6) NOT NULL,
  user_id int NOT NULL,
  source text NOT NULL,
  collected timestamptz(6) DEFAULT NULL,
  active smallint NOT NULL,
  milestone_id int NOT NULL,
  PRIMARY KEY (id),
  CONSTRAINT milestones_usermilestone_user_id_10206aa452468351_uniq UNIQUE  (user_id,milestone_id)
 ,
  CONSTRAINT milesto_milestone_id_4fe38e3e9994f15c_fk_milestones_milestone_id FOREIGN KEY (milestone_id) REFERENCES milestones_milestone (id)
) ;

CREATE INDEX milesto_milestone_id_4fe38e3e9994f15c_fk_milestones_milestone_id ON milestones_usermilestone (milestone_id);
CREATE INDEX milestones_usermilestone_e8701ad4 ON milestones_usermilestone (user_id);
CREATE INDEX milestones_usermilestone_active_1827f467fe87a8ea_uniq ON milestones_usermilestone (active);

CREATE SEQUENCE oauth2_accesstoken_seq;

CREATE TABLE oauth2_accesstoken (
  id int NOT NULL DEFAULT NEXTVAL ('oauth2_accesstoken_seq'),
  token varchar(255) NOT NULL,
  expires timestamptz(6) NOT NULL,
  scope int NOT NULL,
  client_id int NOT NULL,
  user_id int NOT NULL,
  PRIMARY KEY (id)
 ,
  CONSTRAINT oauth2_accesstoke_client_id_20c73b03a7c139a2_fk_oauth2_client_id FOREIGN KEY (client_id) REFERENCES oauth2_client (id),
  CONSTRAINT oauth2_accesstoken_user_id_bcf4c395_fk FOREIGN KEY (user_id) REFERENCES auth_user (id)
) ;

CREATE INDEX oauth2_accesstoken_94a08da1 ON oauth2_accesstoken (token);
CREATE INDEX oauth2_accesstoken_2bfe9d72 ON oauth2_accesstoken (client_id);
CREATE INDEX oauth2_accesstoken_e8701ad4 ON oauth2_accesstoken (user_id);

CREATE SEQUENCE oauth2_grant_seq;

CREATE TABLE oauth2_grant (
  id int NOT NULL DEFAULT NEXTVAL ('oauth2_grant_seq'),
  code varchar(255) NOT NULL,
  expires timestamptz(6) NOT NULL,
  redirect_uri varchar(255) NOT NULL,
  scope int NOT NULL,
  client_id int NOT NULL,
  user_id int NOT NULL,
  nonce varchar(255) NOT NULL,
  PRIMARY KEY (id)
 ,
  CONSTRAINT oauth2_grant_client_id_fbfc174fbc856af_fk_oauth2_client_id FOREIGN KEY (client_id) REFERENCES oauth2_client (id),
  CONSTRAINT oauth2_grant_user_id_d8248ea3_fk FOREIGN KEY (user_id) REFERENCES auth_user (id)
) ;

CREATE INDEX oauth2_grant_user_id_3de96a461bb76819_fk_auth_user_id ON oauth2_grant (user_id);
CREATE INDEX oauth2_grant_client_id_7f83b952b3c51985_idx ON oauth2_grant (client_id,code,expires);

CREATE SEQUENCE oauth2_refreshtoken_seq;

CREATE TABLE oauth2_refreshtoken (
  id int NOT NULL DEFAULT NEXTVAL ('oauth2_refreshtoken_seq'),
  token varchar(255) NOT NULL,
  expired bool NOT NULL,
  access_token_id int NOT NULL,
  client_id int NOT NULL,
  user_id int NOT NULL,
  PRIMARY KEY (id),
  CONSTRAINT oauth2_refreshtoken_access_token_id UNIQUE  (access_token_id)
 ,
  CONSTRAINT oauth2__access_token_id_f99377d503a000b_fk_oauth2_accesstoken_id FOREIGN KEY (access_token_id) REFERENCES oauth2_accesstoken (id),
  CONSTRAINT oauth2_refreshtok_client_id_2f55036ac9aa614e_fk_oauth2_client_id FOREIGN KEY (client_id) REFERENCES oauth2_client (id),
  CONSTRAINT oauth2_refreshtoken_user_id_3d206436_fk FOREIGN KEY (user_id) REFERENCES auth_user (id)
) ;

CREATE INDEX oauth2_refreshtok_client_id_2f55036ac9aa614e_fk_oauth2_client_id ON oauth2_refreshtoken (client_id);
CREATE INDEX oauth2_refreshtoken_user_id_acecf94460b787c_fk_auth_user_id ON oauth2_refreshtoken (user_id);

CREATE SEQUENCE oauth_provider_consumer_seq;

CREATE TABLE oauth_provider_consumer (
  id int NOT NULL DEFAULT NEXTVAL ('oauth_provider_consumer_seq'),
  name varchar(255) NOT NULL,
  description text NOT NULL,
  key varchar(256) NOT NULL,
  secret varchar(16) NOT NULL,
  status bool NOT NULL,
  xauth_allowed bool NOT NULL,
  user_id int DEFAULT NULL,
  PRIMARY KEY (id)
 ,
  CONSTRAINT oauth_provider_consumer_user_id_90ce7b49_fk FOREIGN KEY (user_id) REFERENCES auth_user (id)
) ;

CREATE INDEX oauth_provider_consumer_user_id_4f22b60d2b258006_fk_auth_user_id ON oauth_provider_consumer (user_id);

CREATE SEQUENCE oauth_provider_scope_seq;

CREATE TABLE oauth_provider_scope (
  id int NOT NULL DEFAULT NEXTVAL ('oauth_provider_scope_seq'),
  name varchar(255) NOT NULL,
  url text NOT NULL,
  is_readonly bool NOT NULL,
  PRIMARY KEY (id)
) ;

CREATE SEQUENCE oauth_provider_token_seq;

CREATE TABLE oauth_provider_token (
  id int NOT NULL DEFAULT NEXTVAL ('oauth_provider_token_seq'),
  key varchar(32) DEFAULT NULL,
  secret varchar(16) DEFAULT NULL,
  token_type bool NOT NULL,
  timestamp int NOT NULL,
  is_approved bool NOT NULL,
  verifier varchar(10) NOT NULL,
  callback varchar(2083) DEFAULT NULL,
  callback_confirmed bool NOT NULL,
  consumer_id int NOT NULL,
  scope_id int DEFAULT NULL,
  user_id int DEFAULT NULL,
  PRIMARY KEY (id)
 ,
  CONSTRAINT oauth_consumer_id_1b9915b5bcf1ee5b_fk_oauth_provider_consumer_id FOREIGN KEY (consumer_id) REFERENCES oauth_provider_consumer (id),
  CONSTRAINT oauth_provi_scope_id_459821b6fecbc02a_fk_oauth_provider_scope_id FOREIGN KEY (scope_id) REFERENCES oauth_provider_scope (id),
  CONSTRAINT oauth_provider_token_user_id_6e750fab_fk FOREIGN KEY (user_id) REFERENCES auth_user (id)
) ;

CREATE INDEX oauth_consumer_id_1b9915b5bcf1ee5b_fk_oauth_provider_consumer_id ON oauth_provider_token (consumer_id);
CREATE INDEX oauth_provi_scope_id_459821b6fecbc02a_fk_oauth_provider_scope_id ON oauth_provider_token (scope_id);
CREATE INDEX oauth_provider_token_user_id_588adbcffc892186_fk_auth_user_id ON oauth_provider_token (user_id);

CREATE SEQUENCE self_paced_selfpacedconfiguration_seq;

CREATE TABLE self_paced_selfpacedconfiguration (
  id int NOT NULL DEFAULT NEXTVAL ('self_paced_selfpacedconfiguration_seq'),
  change_date timestamptz(6) NOT NULL,
  enabled bool NOT NULL,
  enable_course_home_improvements bool NOT NULL,
  changed_by_id int DEFAULT NULL,
  PRIMARY KEY (id)
 ,
  CONSTRAINT self_paced_selfpacedconfiguration_changed_by_id_02789a26_fk FOREIGN KEY (changed_by_id) REFERENCES auth_user (id)
) ;

CREATE INDEX self_paced_selfpa_changed_by_id_62c0bd4c6725fd15_fk_auth_user_id ON self_paced_selfpacedconfiguration (changed_by_id);

CREATE SEQUENCE site_configuration_siteconfigurationhistory_seq;

CREATE TABLE site_configuration_siteconfigurationhistory (
  id int NOT NULL DEFAULT NEXTVAL ('site_configuration_siteconfigurationhistory_seq'),
  created timestamptz(6) NOT NULL,
  modified timestamptz(6) NOT NULL,
  values text NOT NULL,
  site_id int NOT NULL,
  enabled bool NOT NULL,
  PRIMARY KEY (id)
 ,
  CONSTRAINT site_configuration_si_site_id_20c9c1a5f8c3358e_fk_django_site_id FOREIGN KEY (site_id) REFERENCES django_site (id)
) ;

CREATE INDEX site_configuration_si_site_id_20c9c1a5f8c3358e_fk_django_site_id ON site_configuration_siteconfigurationhistory (site_id);

CREATE SEQUENCE static_replace_assetexcludedextensionsconfig_seq;

CREATE TABLE static_replace_assetexcludedextensionsconfig (
  id int NOT NULL DEFAULT NEXTVAL ('static_replace_assetexcludedextensionsconfig_seq'),
  change_date timestamptz(6) NOT NULL,
  enabled bool NOT NULL,
  excluded_extensions text NOT NULL,
  changed_by_id int DEFAULT NULL,
  PRIMARY KEY (id)
 ,
  CONSTRAINT static_replace_assetexclu_changed_by_id_e58299b3_fk FOREIGN KEY (changed_by_id) REFERENCES auth_user (id)
) ;

CREATE INDEX static_replace_as_changed_by_id_5885827de4f271dc_fk_auth_user_id ON static_replace_assetexcludedextensionsconfig (changed_by_id);

CREATE SEQUENCE student_linkedinaddtoprofileconfiguration_seq;

CREATE TABLE student_linkedinaddtoprofileconfiguration (
  id int NOT NULL DEFAULT NEXTVAL ('student_linkedinaddtoprofileconfiguration_seq'),
  change_date timestamptz(6) NOT NULL,
  enabled bool NOT NULL,
  company_identifier text NOT NULL,
  dashboard_tracking_code text NOT NULL,
  trk_partner_name varchar(10) NOT NULL,
  changed_by_id int DEFAULT NULL,
  PRIMARY KEY (id)
 ,
  CONSTRAINT student_linkedinaddtoprof_changed_by_id_dc1c453f_fk FOREIGN KEY (changed_by_id) REFERENCES auth_user (id)
) ;

CREATE INDEX student_linkedina_changed_by_id_226a4de3af0f3296_fk_auth_user_id ON student_linkedinaddtoprofileconfiguration (changed_by_id);

CREATE SEQUENCE student_pendingnamechange_seq;

CREATE TABLE student_pendingnamechange (
  id int NOT NULL DEFAULT NEXTVAL ('student_pendingnamechange_seq'),
  new_name varchar(255) NOT NULL,
  rationale varchar(1024) NOT NULL,
  user_id int NOT NULL,
  PRIMARY KEY (id),
  CONSTRAINT student_pendingnamechange_seq_user_id UNIQUE  (user_id),
  CONSTRAINT student_pendingnamechange_user_id_e2cd8b70_fk FOREIGN KEY (user_id) REFERENCES auth_user (id)
) ;

CREATE SEQUENCE student_registrationcookieconfiguration_seq;

CREATE TABLE student_registrationcookieconfiguration (
  id int NOT NULL DEFAULT NEXTVAL ('student_registrationcookieconfiguration_seq'),
  change_date timestamptz(6) NOT NULL,
  enabled bool NOT NULL,
  utm_cookie_name varchar(255) NOT NULL,
  affiliate_cookie_name varchar(255) NOT NULL,
  changed_by_id int DEFAULT NULL,
  PRIMARY KEY (id)
 ,
  CONSTRAINT student_registrationcooki_changed_by_id_52ac88b0_fk FOREIGN KEY (changed_by_id) REFERENCES auth_user (id)
) ;

CREATE INDEX student_registrati_changed_by_id_7c813444cd41f76_fk_auth_user_id ON student_registrationcookieconfiguration (changed_by_id);


CREATE SEQUENCE auth_registration_seq;

CREATE TABLE auth_registration (
  id int NOT NULL DEFAULT NEXTVAL ('auth_registration_seq'),
  activation_key varchar(32) NOT NULL,
  user_id int NOT NULL,
  PRIMARY KEY (id),
  CONSTRAINT auth_registration_activation_key UNIQUE  (activation_key),
  CONSTRAINT auth_registration_user_id UNIQUE  (user_id),
  CONSTRAINT auth_registration_user_id_f99bc297_fk FOREIGN KEY (user_id) REFERENCES auth_user (id)
) ;

CREATE SEQUENCE student_userattribute_seq;

CREATE TABLE student_userattribute (
  id int NOT NULL DEFAULT NEXTVAL ('student_userattribute_seq'),
  created timestamptz(6) NOT NULL,
  modified timestamptz(6) NOT NULL,
  name varchar(255) NOT NULL,
  value varchar(255) NOT NULL,
  user_id int NOT NULL,
  PRIMARY KEY (id),
  CONSTRAINT student_userattribute_user_id_395f02bcb61d19c1_uniq UNIQUE  (user_id,name)
 ,
  CONSTRAINT student_userattribute_user_id_19c01f5e_fk FOREIGN KEY (user_id) REFERENCES auth_user (id)
) ;

CREATE INDEX student_userattribute_name_5fd741d8c66ce242_uniq ON student_userattribute (name);

CREATE SEQUENCE student_usertestgroup_seq;

CREATE TABLE student_usertestgroup (
  id int NOT NULL DEFAULT NEXTVAL ('student_usertestgroup_seq'),
  name varchar(32) NOT NULL,
  description text NOT NULL,
  PRIMARY KEY (id)
) ;

CREATE INDEX student_usertestgroup_b068931c ON student_usertestgroup (name);

CREATE SEQUENCE survey_surveyform_seq;

CREATE TABLE survey_surveyform (
  id int NOT NULL DEFAULT NEXTVAL ('survey_surveyform_seq'),
  created timestamptz(6) NOT NULL,
  modified timestamptz(6) NOT NULL,
  name varchar(255) NOT NULL,
  form text NOT NULL,
  PRIMARY KEY (id),
  CONSTRAINT survey_surveyform_name UNIQUE  (name)
) ;

CREATE SEQUENCE tagging_tagcategories_seq;

CREATE TABLE tagging_tagcategories (
  id int NOT NULL DEFAULT NEXTVAL ('tagging_tagcategories_seq'),
  name varchar(255) NOT NULL,
  title varchar(255) NOT NULL,
  PRIMARY KEY (id),
  CONSTRAINT tagging_tagcategories_name UNIQUE  (name)
) ;

CREATE SEQUENCE tagging_tagavailablevalues_seq;

CREATE TABLE tagging_tagavailablevalues (
  id int NOT NULL DEFAULT NEXTVAL ('tagging_tagavailablevalues_seq'),
  value varchar(255) NOT NULL,
  category_id int NOT NULL,
  PRIMARY KEY (id)
 ,
  CONSTRAINT tagging_category_id_40780d45c76e4f97_fk_tagging_tagcategories_id FOREIGN KEY (category_id) REFERENCES tagging_tagcategories (id)
) ;

CREATE INDEX tagging_tagavailablevalues_b583a629 ON tagging_tagavailablevalues (category_id);

CREATE SEQUENCE track_trackinglog_seq;

CREATE TABLE track_trackinglog (
  id int NOT NULL DEFAULT NEXTVAL ('track_trackinglog_seq'),
  dtcreated timestamptz(6) NOT NULL,
  username varchar(32) NOT NULL,
  ip varchar(32) NOT NULL,
  event_source varchar(32) NOT NULL,
  event_type varchar(512) NOT NULL,
  event text NOT NULL,
  agent varchar(256) NOT NULL,
  page varchar(512) DEFAULT NULL,
  time timestamptz(6) NOT NULL,
  host varchar(64) NOT NULL,
  PRIMARY KEY (id)
) ;

CREATE SEQUENCE user_api_userretirementrequest_seq;

CREATE TABLE user_api_userretirementrequest (
  id int NOT NULL DEFAULT NEXTVAL ('user_api_userretirementrequest_seq'),
  created timestamptz(6) NOT NULL,
  modified timestamptz(6) NOT NULL,
  user_id int NOT NULL,
  PRIMARY KEY (id),
  CONSTRAINT user_api_userretirementrequestuser_id UNIQUE  (user_id),
  CONSTRAINT user_api_userretirementrequest_user_id_7f7ca22f_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES auth_user (id)
) ;

CREATE SEQUENCE verified_track_content_migrateverifiedtrackcohortssetting_seq;

CREATE TABLE verified_track_content_migrateverifiedtrackcohortssetting (
  id int NOT NULL DEFAULT NEXTVAL ('verified_track_content_migrateverifiedtrackcohortssetting_seq'),
  change_date timestamptz(6) NOT NULL,
  enabled bool NOT NULL,
  old_course_key varchar(255) NOT NULL,
  rerun_course_key varchar(255) NOT NULL,
  audit_cohort_names text NOT NULL,
  changed_by_id int DEFAULT NULL,
  PRIMARY KEY (id)
 ,
  CONSTRAINT verified_track_content_mi_changed_by_id_29944bff_fk FOREIGN KEY (changed_by_id) REFERENCES auth_user (id)
) ;

CREATE INDEX verified_track_co_changed_by_id_3aa020546322e9ee_fk_auth_user_id ON verified_track_content_migrateverifiedtrackcohortssetting (changed_by_id);

CREATE SEQUENCE video_config_coursevideotranscriptenabledflag_seq;

CREATE TABLE video_config_coursevideotranscriptenabledflag (
  id int NOT NULL DEFAULT NEXTVAL ('video_config_coursevideotranscriptenabledflag_seq'),
  change_date timestamptz(6) NOT NULL,
  enabled bool NOT NULL,
  course_id varchar(255) NOT NULL,
  changed_by_id int DEFAULT NULL,
  PRIMARY KEY (id)
 ,
  CONSTRAINT video_config_coursevideot_changed_by_id_3bdcf2a6_fk FOREIGN KEY (changed_by_id) REFERENCES auth_user (id)
) ;

CREATE INDEX video_config_cour_changed_by_id_184a5ebdccef55f5_fk_auth_user_id ON video_config_coursevideotranscriptenabledflag (changed_by_id);
CREATE INDEX video_config_coursevideotranscriptenabledflag_ea134da7 ON video_config_coursevideotranscriptenabledflag (course_id);

CREATE SEQUENCE video_config_transcriptmigrationsetting_seq;

CREATE TABLE video_config_transcriptmigrationsetting (
  id int NOT NULL DEFAULT NEXTVAL ('video_config_transcriptmigrationsetting_seq'),
  change_date timestamptz(6) NOT NULL,
  enabled bool NOT NULL,
  force_update bool NOT NULL,
  commit bool NOT NULL,
  all_courses bool NOT NULL,
  course_ids text NOT NULL,
  changed_by_id int DEFAULT NULL,
  command_run int check (command_run > 0) NOT NULL,
  PRIMARY KEY (id)
 ,
  CONSTRAINT video_config_transcr_changed_by_id_4c7817bd_fk_auth_user FOREIGN KEY (changed_by_id) REFERENCES auth_user (id)
) ;

CREATE INDEX video_config_transcr_changed_by_id_4c7817bd_fk_auth_user ON video_config_transcriptmigrationsetting (changed_by_id);

CREATE SEQUENCE video_config_videotranscriptenabledflag_seq;

CREATE TABLE video_config_videotranscriptenabledflag (
  id int NOT NULL DEFAULT NEXTVAL ('video_config_videotranscriptenabledflag_seq'),
  change_date timestamptz(6) NOT NULL,
  enabled bool NOT NULL,
  enabled_for_all_courses bool NOT NULL,
  changed_by_id int DEFAULT NULL,
  PRIMARY KEY (id)
 ,
  CONSTRAINT video_config_videotranscr_changed_by_id_9f0afd7f_fk FOREIGN KEY (changed_by_id) REFERENCES auth_user (id)
) ;

CREATE INDEX video_config_vide_changed_by_id_3a0857ce30241112_fk_auth_user_id ON video_config_videotranscriptenabledflag (changed_by_id);

CREATE SEQUENCE video_pipeline_coursevideouploadsenabledbydefault_seq;

CREATE TABLE video_pipeline_coursevideouploadsenabledbydefault (
  id int NOT NULL DEFAULT NEXTVAL ('video_pipeline_coursevideouploadsenabledbydefault_seq'),
  change_date timestamptz(6) NOT NULL,
  enabled bool NOT NULL,
  course_id varchar(255) NOT NULL,
  changed_by_id int DEFAULT NULL,
  PRIMARY KEY (id)
 ,
  CONSTRAINT video_pipeline_coursevide_changed_by_id_84ec1a58_fk FOREIGN KEY (changed_by_id) REFERENCES auth_user (id)
) ;

CREATE INDEX video_pipeline_co_changed_by_id_6fa6d53fe11c233b_fk_auth_user_id ON video_pipeline_coursevideouploadsenabledbydefault (changed_by_id);
CREATE INDEX video_pipeline_coursevideouploadsenabledbydefault_ea134da7 ON video_pipeline_coursevideouploadsenabledbydefault (course_id);

CREATE SEQUENCE video_pipeline_videopipelineintegration_seq;

CREATE TABLE video_pipeline_videopipelineintegration (
  id int NOT NULL DEFAULT NEXTVAL ('video_pipeline_videopipelineintegration_seq'),
  change_date timestamptz(6) NOT NULL,
  enabled bool NOT NULL,
  api_url varchar(200) NOT NULL,
  service_username varchar(100) NOT NULL,
  changed_by_id int DEFAULT NULL,
  client_name varchar(100) NOT NULL,
  PRIMARY KEY (id)
 ,
  CONSTRAINT video_pipeline_videopipel_changed_by_id_b169f329_fk FOREIGN KEY (changed_by_id) REFERENCES auth_user (id)
) ;

CREATE INDEX video_pipeline_vi_changed_by_id_384bb33af13db7a5_fk_auth_user_id ON video_pipeline_videopipelineintegration (changed_by_id);


CREATE SEQUENCE waffle_sample_seq;

CREATE TABLE waffle_sample (
  id int NOT NULL DEFAULT NEXTVAL ('waffle_sample_seq'),
  name varchar(100) NOT NULL,
  percent decimal(4,1) NOT NULL,
  note text NOT NULL,
  created timestamptz(6) NOT NULL,
  modified timestamptz(6) NOT NULL,
  PRIMARY KEY (id),
  CONSTRAINT waffle_sample_name UNIQUE  (name)
) ;

CREATE INDEX waffle_sample_e2fa5388 ON waffle_sample (created);

CREATE SEQUENCE workflow_assessmentworkflow_seq;

CREATE TABLE workflow_assessmentworkflow (
  id int NOT NULL DEFAULT NEXTVAL ('workflow_assessmentworkflow_seq'),
  created timestamptz(6) NOT NULL,
  modified timestamptz(6) NOT NULL,
  status varchar(100) NOT NULL,
  status_changed timestamptz(6) NOT NULL,
  submission_uuid varchar(36) NOT NULL,
  uuid varchar(36) NOT NULL,
  course_id varchar(255) NOT NULL,
  item_id varchar(255) NOT NULL,
  PRIMARY KEY (id),
  CONSTRAINT sworkflow_assessmentworkflow_ubmission_uuid UNIQUE  (submission_uuid),
  CONSTRAINT workflow_assessmentworkflow_uuid UNIQUE  (uuid)
) ;

CREATE INDEX workflow_assessmentworkflow_ea134da7 ON workflow_assessmentworkflow (course_id);
CREATE INDEX workflow_assessmentworkflow_82bfda79 ON workflow_assessmentworkflow (item_id);

CREATE SEQUENCE xblock_config_courseeditltifieldsenabledflag_seq;

CREATE TABLE xblock_config_courseeditltifieldsenabledflag (
  id int NOT NULL DEFAULT NEXTVAL ('xblock_config_courseeditltifieldsenabledflag_seq'),
  change_date timestamptz(6) NOT NULL,
  enabled bool NOT NULL,
  course_id varchar(255) NOT NULL,
  changed_by_id int DEFAULT NULL,
  PRIMARY KEY (id)
 ,
  CONSTRAINT xblock_config_cou_changed_by_id_124d91bd160908dd_fk_auth_user_id FOREIGN KEY (changed_by_id) REFERENCES auth_user (id)
) ;

CREATE INDEX xblock_config_cou_changed_by_id_124d91bd160908dd_fk_auth_user_id ON xblock_config_courseeditltifieldsenabledflag (changed_by_id);
CREATE INDEX xblock_config_courseeditltifieldsenabledflag_ea134da7 ON xblock_config_courseeditltifieldsenabledflag (course_id);



CREATE SEQUENCE xblock_django_xblockstudioconfiguration_seq;

CREATE TABLE xblock_django_xblockstudioconfiguration (
  id int NOT NULL DEFAULT NEXTVAL ('xblock_django_xblockstudioconfiguration_seq'),
  change_date timestamptz(6) NOT NULL,
  enabled bool NOT NULL,
  name varchar(255) NOT NULL,
  template varchar(255) NOT NULL,
  support_level varchar(2) NOT NULL,
  changed_by_id int DEFAULT NULL,
  PRIMARY KEY (id)
 ,
  CONSTRAINT xblock_django_xblockstudi_changed_by_id_641b0905_fk FOREIGN KEY (changed_by_id) REFERENCES auth_user (id)
) ;

CREATE INDEX xblock_django_xblo_changed_by_id_353d5def0d11370_fk_auth_user_id ON xblock_django_xblockstudioconfiguration (changed_by_id);
CREATE INDEX xblock_django_xblockstudioconfiguration_b068931c ON xblock_django_xblockstudioconfiguration (name);

CREATE SEQUENCE auth_permission_seq;

CREATE TABLE auth_permission (
  id int NOT NULL DEFAULT NEXTVAL ('auth_permission_seq'),
  name varchar(255) NOT NULL,
  content_type_id int NOT NULL,
  codename varchar(100) NOT NULL,
  PRIMARY KEY (id),
  CONSTRAINT content_type_id UNIQUE  (content_type_id,codename),
  CONSTRAINT auth__content_type_id_508cf46651277a81_fk_django_content_type_id FOREIGN KEY (content_type_id) REFERENCES django_content_type (id)
)  ;

ALTER SEQUENCE auth_permission_seq RESTART WITH 1101;

CREATE SEQUENCE auth_user_user_permissions_seq;

CREATE TABLE auth_user_user_permissions (
  id int NOT NULL DEFAULT NEXTVAL ('auth_user_user_permissions_seq'),
  user_id int NOT NULL,
  permission_id int NOT NULL,
  PRIMARY KEY (id),
  CONSTRAINT auth_user_user_permissionsuser_id UNIQUE  (user_id,permission_id)
 ,
  CONSTRAINT auth_user_u_permission_id_384b62483d7071f0_fk_auth_permission_id FOREIGN KEY (permission_id) REFERENCES auth_permission (id),
  CONSTRAINT auth_user_user_permissi_user_id_7f0938558328534a_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES auth_user (id)
) ;

CREATE INDEX auth_user_u_permission_id_384b62483d7071f0_fk_auth_permission_id ON auth_user_user_permissions (permission_id);