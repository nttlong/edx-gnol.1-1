

CREATE SEQUENCE django_site_seq;

CREATE TABLE django_site (
  id int NOT NULL DEFAULT NEXTVAL ('django_site_seq'),
  domain varchar(100) NOT NULL,
  name varchar(50) NOT NULL,
  PRIMARY KEY (id),
  CONSTRAINT django_site_domain_a2e37b91_uniq UNIQUE  (domain)
)  ;
CREATE SEQUENCE auth_user_seq;

CREATE TABLE auth_user (
  id int NOT NULL DEFAULT NEXTVAL ('auth_user_seq'),
  password varchar(128) NOT NULL,
  last_login timestamptz(6) DEFAULT NULL,
  is_superuser bool NOT NULL,
  username varchar(150) NOT NULL,
  first_name varchar(30) NOT NULL,
  last_name varchar(30) NOT NULL,
  email varchar(254) NOT NULL,
  is_staff bool NOT NULL,
  is_active bool NOT NULL,
  date_joined timestamptz(6) NOT NULL,
  PRIMARY KEY (id),
  CONSTRAINT username UNIQUE  (username),
  CONSTRAINT email UNIQUE  (email)
);

ALTER SEQUENCE auth_user_seq RESTART WITH 2;

ALTER SEQUENCE django_site_seq RESTART WITH 2;


CREATE SEQUENCE auth_group_seq;

CREATE TABLE auth_group (
  id int NOT NULL DEFAULT NEXTVAL ('auth_group_seq'),
  name varchar(80) NOT NULL,
  PRIMARY KEY (id),
  CONSTRAINT auth_group_name_ux UNIQUE  (name)
)  ;

ALTER SEQUENCE auth_group_seq RESTART WITH 2;


CREATE SEQUENCE auth_user_groups_seq;

CREATE TABLE auth_user_groups (
  id int NOT NULL DEFAULT NEXTVAL ('auth_user_groups_seq'),
  user_id int NOT NULL,
  group_id int NOT NULL,
  PRIMARY KEY (id),
  CONSTRAINT auth_user_groups_user_id UNIQUE  (user_id,group_id)
 ,
  CONSTRAINT auth_user_groups_group_id_33ac548dcf5f8e37_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES auth_group (id),
  CONSTRAINT auth_user_groups_user_id_4b5ed4ffdb8fd9b0_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES auth_user (id)
) ;

CREATE INDEX auth_user_groups_group_id_33ac548dcf5f8e37_fk_auth_group_id ON auth_user_groups (group_id);

CREATE SEQUENCE django_content_type_seq;

CREATE TABLE django_content_type (
  id int NOT NULL DEFAULT NEXTVAL ('django_content_type_seq'),
  app_label varchar(100) NOT NULL,
  model varchar(100) NOT NULL,
  PRIMARY KEY (id),
  CONSTRAINT django_content_type_app_label_45f3b1d93ec8c61c_uniq UNIQUE  (app_label,model)
)  ;

ALTER SEQUENCE django_content_type_seq RESTART WITH 366;

CREATE SEQUENCE site_configuration_siteconfiguration_seq;
CREATE TABLE site_configuration_siteconfiguration (
  id int NOT NULL DEFAULT NEXTVAL ('site_configuration_siteconfiguration_seq'),
  values text NOT NULL,
  site_id int NOT NULL,
  enabled bool NOT NULL,
  PRIMARY KEY (id),
  CONSTRAINT site_id UNIQUE  (site_id),
  CONSTRAINT site_configuration_si_site_id_51c4aa24ab9238cb_fk_django_site_id FOREIGN KEY (site_id) REFERENCES django_site (id)
) ;

CREATE SEQUENCE django_redirect_seq;


CREATE TABLE django_redirect (
  id int NOT NULL DEFAULT NEXTVAL ('django_redirect_seq'),
  site_id int NOT NULL,
  old_path varchar(200) NOT NULL,
  new_path varchar(200) NOT NULL,
  PRIMARY KEY (id),
  CONSTRAINT site_id_ux UNIQUE  (site_id,old_path)
 ,
  CONSTRAINT django_redirect_site_id_121a4403f653e524_fk_django_site_id FOREIGN KEY (site_id) REFERENCES django_site (id)
) ;

CREATE INDEX django_redirect_91a0b591 ON django_redirect (old_path);

CREATE SEQUENCE student_userstanding_seq;

CREATE TABLE student_userstanding (
  id int NOT NULL DEFAULT NEXTVAL ('student_userstanding_seq'),
  account_status varchar(31) NOT NULL,
  standing_last_changed_at timestamptz(6) NOT NULL,
  changed_by_id int NOT NULL,
  user_id int NOT NULL,
  PRIMARY KEY (id),
  CONSTRAINT user_id UNIQUE  (user_id)
 ,
  CONSTRAINT student_userstanding_changed_by_id_469252b4_fk FOREIGN KEY (changed_by_id) REFERENCES auth_user (id),
  CONSTRAINT student_userstanding_user_id_00b147e5_fk FOREIGN KEY (user_id) REFERENCES auth_user (id)
) ;

CREATE INDEX student_userstand_changed_by_id_23784b83f2849aff_fk_auth_user_id ON student_userstanding (changed_by_id);

CREATE SEQUENCE splash_splashconfig_seq;

CREATE TABLE splash_splashconfig (
  id int NOT NULL DEFAULT NEXTVAL ('splash_splashconfig_seq'),
  change_date timestamptz(6) NOT NULL,
  enabled smallint NOT NULL,
  cookie_name text NOT NULL,
  cookie_allowed_values text NOT NULL,
  unaffected_usernames text NOT NULL,
  unaffected_url_paths text NOT NULL,
  redirect_url varchar(200) NOT NULL,
  changed_by_id int DEFAULT NULL,
  PRIMARY KEY (id)
 ,
  CONSTRAINT splash_splashconfig_changed_by_id_883b17ba_fk FOREIGN KEY (changed_by_id) REFERENCES auth_user (id)
) ;

CREATE INDEX splash_splashconf_changed_by_id_735b38ad8ed19270_fk_auth_user_id ON splash_splashconfig (changed_by_id);

CREATE SEQUENCE dark_lang_darklangconfig_seq;

CREATE TABLE dark_lang_darklangconfig (
  id int NOT NULL DEFAULT NEXTVAL ('dark_lang_darklangconfig_seq'),
  change_date timestamptz(6) NOT NULL,
  enabled smallint NOT NULL,
  released_languages text NOT NULL,
  changed_by_id int DEFAULT NULL,
  PRIMARY KEY (id)
 ,
  CONSTRAINT dark_lang_darklangconfig_changed_by_id_9a7df899_fk FOREIGN KEY (changed_by_id) REFERENCES auth_user (id)
)  ;

ALTER SEQUENCE dark_lang_darklangconfig_seq RESTART WITH 2;

CREATE INDEX dark_lang_darklan_changed_by_id_7e1defb1121d58b8_fk_auth_user_id ON dark_lang_darklangconfig (changed_by_id);

CREATE SEQUENCE theming_sitetheme_seq;

CREATE TABLE theming_sitetheme (
  id int NOT NULL DEFAULT NEXTVAL ('theming_sitetheme_seq'),
  theme_dir_name varchar(255) NOT NULL,
  site_id int NOT NULL,
  PRIMARY KEY (id)
 ,
  CONSTRAINT theming_sitetheme_site_id_4fccdacaebfeb01f_fk_django_site_id FOREIGN KEY (site_id) REFERENCES django_site (id)
) ;

CREATE INDEX theming_sitetheme_site_id_4fccdacaebfeb01f_fk_django_site_id ON theming_sitetheme (site_id);

CREATE TABLE course_overviews_courseoverview (
  created timestamptz(6) NOT NULL,
  modified timestamptz(6) NOT NULL,
  version int NOT NULL,
  id varchar(255) NOT NULL,
  _location varchar(255) NOT NULL,
  display_name text,
  display_number_with_default text NOT NULL,
  display_org_with_default text NOT NULL,
  start timestamptz(6) DEFAULT NULL,
  "end" timestamptz(6) DEFAULT NULL,
  advertised_start text,
  course_image_url text NOT NULL,
  social_sharing_url text,
  end_of_course_survey_url text,
  certificates_display_behavior text,
  certificates_show_before_end bool NOT NULL,
  cert_html_view_enabled bool NOT NULL,
  has_any_active_web_certificate bool NOT NULL,
  cert_name_short text NOT NULL,
  cert_name_long text NOT NULL,
  lowest_passing_grade decimal(5,2) DEFAULT NULL,
  days_early_for_beta double precision DEFAULT NULL,
  mobile_available bool NOT NULL,
  visible_to_staff_only bool NOT NULL,
  _pre_requisite_courses_json text NOT NULL,
  enrollment_start timestamptz(6) DEFAULT NULL,
  enrollment_end timestamptz(6) DEFAULT NULL,
  enrollment_domain text,
  invitation_only bool NOT NULL,
  max_student_enrollments_allowed int DEFAULT NULL,
  announcement timestamptz(6) DEFAULT NULL,
  catalog_visibility text,
  course_video_url text,
  effort text,
  short_description text,
  org text NOT NULL,
  self_paced bool NOT NULL,
  marketing_url text,
  eligible_for_financial_aid bool NOT NULL,
  language text,
  certificate_available_date timestamptz(6) DEFAULT NULL,
  PRIMARY KEY (id));


  CREATE SEQUENCE courseware_subjects_seq;

CREATE TABLE courseware_subjects (
  "id" INT NOT NULL DEFAULT NEXTVAL ('courseware_subjects_seq'),
  "SubjectCode" VARCHAR(45) NOT NULL,
  "SubjectName" VARCHAR(300) NOT NULL,
  "SubjectFName" VARCHAR(300) NULL,
  "SubjectDescription" VARCHAR(2000) NULL,
  "CreatedBy" VARCHAR(45) NULL,
  "CreatedOn" timestamptz(0) NULL,
  "ModifiedBy" VARCHAR(45) NULL,
  "ModifiedOn" timestamptz(0) NULL,
  PRIMARY KEY ("id"),
  CONSTRAINT SubjectCode_UNIQUE UNIQUE  ("SubjectCode"));


  CREATE SEQUENCE status_globalstatusmessage_seq;

CREATE TABLE status_globalstatusmessage (
  id int NOT NULL DEFAULT NEXTVAL ('status_globalstatusmessage_seq'),
  change_date timestamptz(6) NOT NULL,
  enabled smallint NOT NULL,
  message text,
  changed_by_id int DEFAULT NULL,
  PRIMARY KEY (id)
 ,
  CONSTRAINT status_globalstatusmessage_changed_by_id_3c627848_fk FOREIGN KEY (changed_by_id) REFERENCES auth_user (id)
) ;

CREATE INDEX status_globalstat_changed_by_id_76ab1cf17be5644d_fk_auth_user_id ON status_globalstatusmessage (changed_by_id);


CREATE SEQUENCE user_api_retirementstate_seq;

CREATE TABLE user_api_retirementstate (
  id int NOT NULL DEFAULT NEXTVAL ('user_api_retirementstate_seq'),
  state_name varchar(30) NOT NULL,
  state_execution_order smallint NOT NULL,
  is_dead_end_state smallint NOT NULL,
  required smallint NOT NULL,
  PRIMARY KEY (id),
  CONSTRAINT state_name UNIQUE  (state_name),
  CONSTRAINT state_execution_order UNIQUE  (state_execution_order)
) ;

CREATE INDEX user_api_retirementstate_is_dead_end_state_62eaf9b7 ON user_api_retirementstate (is_dead_end_state);



CREATE SEQUENCE user_api_userretirementstatus_seq;

CREATE TABLE user_api_userretirementstatus (
  id int NOT NULL DEFAULT NEXTVAL ('user_api_userretirementstatus_seq'),
  created timestamptz(6) NOT NULL,
  modified timestamptz(6) NOT NULL,
  original_username varchar(150) NOT NULL,
  original_email varchar(254) NOT NULL,
  original_name varchar(255) NOT NULL,
  retired_username varchar(150) NOT NULL,
  retired_email varchar(254) NOT NULL,
  responses text NOT NULL,
  current_state_id int NOT NULL,
  last_state_id int NOT NULL,
  user_id int NOT NULL,
  PRIMARY KEY (id),
  CONSTRAINT user_id_ux UNIQUE  (user_id)
 ,
  CONSTRAINT user_api_userretirem_current_state_id_e37bb094_fk_user_api_ FOREIGN KEY (current_state_id) REFERENCES user_api_retirementstate (id),
  CONSTRAINT user_api_userretirem_last_state_id_359e74cd_fk_user_api_ FOREIGN KEY (last_state_id) REFERENCES user_api_retirementstate (id),
  CONSTRAINT user_api_userretirementstatus_user_id_aca4dc7b_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES auth_user (id)
) ;

CREATE INDEX user_api_userretirem_current_state_id_e37bb094_fk_user_api_ ON user_api_userretirementstatus (current_state_id);
CREATE INDEX user_api_userretirem_last_state_id_359e74cd_fk_user_api_ ON user_api_userretirementstatus (last_state_id);
CREATE INDEX user_api_userretirementstatus_original_username_fa5d4a21 ON user_api_userretirementstatus (original_username);
CREATE INDEX user_api_userretirementstatus_original_email_a7203bff ON user_api_userretirementstatus (original_email);
CREATE INDEX user_api_userretirementstatus_original_name_17c2846b ON user_api_userretirementstatus (original_name);
CREATE INDEX user_api_userretirementstatus_retired_username_52067a53 ON user_api_userretirementstatus (retired_username);
CREATE INDEX user_api_userretirementstatus_retired_email_ee7c1579 ON user_api_userretirementstatus (retired_email);









CREATE SEQUENCE waffle_switch_seq;

CREATE TABLE waffle_switch (
  id int NOT NULL DEFAULT NEXTVAL ('waffle_switch_seq'),
  "name" varchar(100) NOT NULL,
  active smallint NOT NULL,
  note text NOT NULL,
  created timestamptz(6) NOT NULL,
  modified timestamptz(6) NOT NULL,
  PRIMARY KEY (id),
  CONSTRAINT name UNIQUE  (name)
)  ;

ALTER SEQUENCE waffle_switch_seq RESTART WITH 2;

CREATE INDEX waffle_switch_e2fa5388 ON waffle_switch (created);

CREATE SEQUENCE user_api_userpreference_seq;

CREATE TABLE user_api_userpreference (
  id int NOT NULL DEFAULT NEXTVAL ('user_api_userpreference_seq'),
  key varchar(255) NOT NULL,
  value text NOT NULL,
  user_id int NOT NULL,
  PRIMARY KEY (id),
  CONSTRAINT user_api_userpreference_user_id_4e4942d73f760072_uniq UNIQUE  (user_id,key)
 ,
  CONSTRAINT user_api_userpreference_user_id_68f8a34b_fk FOREIGN KEY (user_id) REFERENCES auth_user (id)
) ;

CREATE INDEX user_api_userpreference_3c6e0b8a ON user_api_userpreference (key);


CREATE SEQUENCE email_marketing_emailmarketingconfiguration_seq;

CREATE TABLE email_marketing_emailmarketingconfiguration (
  id int NOT NULL DEFAULT NEXTVAL ('email_marketing_emailmarketingconfiguration_seq'),
  change_date timestamptz(6) NOT NULL,
  enabled smallint NOT NULL,
  sailthru_key varchar(32) NOT NULL,
  sailthru_secret varchar(32) NOT NULL,
  sailthru_new_user_list varchar(48) NOT NULL,
  sailthru_retry_interval int NOT NULL,
  sailthru_max_retries int NOT NULL,
  changed_by_id int DEFAULT NULL,
  sailthru_abandoned_cart_delay int NOT NULL,
  sailthru_abandoned_cart_template varchar(20) NOT NULL,
  sailthru_content_cache_age int NOT NULL,
  sailthru_enroll_cost int NOT NULL,
  sailthru_enroll_template varchar(20) NOT NULL,
  sailthru_get_tags_from_sailthru smallint NOT NULL,
  sailthru_purchase_template varchar(20) NOT NULL,
  sailthru_upgrade_template varchar(20) NOT NULL,
  sailthru_lms_url_override varchar(80) NOT NULL,
  welcome_email_send_delay int NOT NULL,
  user_registration_cookie_timeout_delay double precision NOT NULL,
  sailthru_welcome_template varchar(20) NOT NULL,
  sailthru_verification_failed_template varchar(20) NOT NULL,
  sailthru_verification_passed_template varchar(20) NOT NULL,
  PRIMARY KEY (id)
 ,
  CONSTRAINT email_marketing_emailmark_changed_by_id_15ce753b_fk FOREIGN KEY (changed_by_id) REFERENCES auth_user (id)
) ;

CREATE INDEX email_marketing_e_changed_by_id_1c6968b921f23b0b_fk_auth_user_id ON email_marketing_emailmarketingconfiguration (changed_by_id);


CREATE SEQUENCE shoppingcart_order_seq;

CREATE TABLE shoppingcart_order (
  id int NOT NULL DEFAULT NEXTVAL ('shoppingcart_order_seq'),
  currency varchar(8) NOT NULL,
  status varchar(32) NOT NULL,
  purchase_time timestamptz(6) DEFAULT NULL,
  refunded_time timestamptz(6) DEFAULT NULL,
  bill_to_first varchar(64) NOT NULL,
  bill_to_last varchar(64) NOT NULL,
  bill_to_street1 varchar(128) NOT NULL,
  bill_to_street2 varchar(128) NOT NULL,
  bill_to_city varchar(64) NOT NULL,
  bill_to_state varchar(8) NOT NULL,
  bill_to_postalcode varchar(16) NOT NULL,
  bill_to_country varchar(64) NOT NULL,
  bill_to_ccnum varchar(8) NOT NULL,
  bill_to_cardtype varchar(32) NOT NULL,
  processor_reply_dump text NOT NULL,
  company_name varchar(255) DEFAULT NULL,
  company_contact_name varchar(255) DEFAULT NULL,
  company_contact_email varchar(255) DEFAULT NULL,
  recipient_name varchar(255) DEFAULT NULL,
  recipient_email varchar(255) DEFAULT NULL,
  customer_reference_number varchar(63) DEFAULT NULL,
  order_type varchar(32) NOT NULL,
  user_id int NOT NULL,
  PRIMARY KEY (id)
 ,
  CONSTRAINT shoppingcart_order_user_id_ca2398bc_fk FOREIGN KEY (user_id) REFERENCES auth_user (id)
) ;

CREATE INDEX shoppingcart_order_user_id_4e1f3e3b06ee22a6_fk_auth_user_id ON shoppingcart_order (user_id);


CREATE SEQUENCE auth_userprofile_seq;

CREATE TABLE auth_userprofile (
  id int NOT NULL DEFAULT NEXTVAL ('auth_userprofile_seq'),
  name varchar(255) NOT NULL,
  meta text NOT NULL,
  courseware varchar(255) NOT NULL,
  language varchar(255) NOT NULL,
  location varchar(255) NOT NULL,
  year_of_birth int DEFAULT NULL,
  gender varchar(6) DEFAULT NULL,
  level_of_education varchar(6) DEFAULT NULL,
  mailing_address text,
  city text,
  country varchar(2) DEFAULT NULL,
  goals text,
  allow_certificate bool NOT NULL,
  bio varchar(3000) DEFAULT NULL,
  profile_image_uploaded_at timestamptz(6) DEFAULT NULL,
  user_id int NOT NULL,
  PRIMARY KEY (id),
  CONSTRAINT auth_userprofile_user_id_ux UNIQUE  (user_id)
 ,
  CONSTRAINT auth_userprofile_user_id_62634b27_fk FOREIGN KEY (user_id) REFERENCES auth_user (id)
) ;

CREATE INDEX auth_userprofile_b068931c ON auth_userprofile (name);
CREATE INDEX auth_userprofile_8512ae7d ON auth_userprofile (language);
CREATE INDEX auth_userprofile_d5189de0 ON auth_userprofile (location);
CREATE INDEX auth_userprofile_8939d49d ON auth_userprofile (year_of_birth);
CREATE INDEX auth_userprofile_cc90f191 ON auth_userprofile (gender);
CREATE INDEX auth_userprofile_a895faa8 ON auth_userprofile (level_of_education);


CREATE SEQUENCE courseware_orgs_seq;

CREATE TABLE courseware_orgs (
  "id" INT NOT NULL DEFAULT NEXTVAL ('courseware_orgs_seq'),
  "OrgCode" VARCHAR(45) NOT NULL,
  "OrgName" VARCHAR(200) NULL ,
  "OrgFName" VARCHAR(200) NULL,
  "OrgAddress" VARCHAR(200) NULL,
  "OrgWebSite" VARCHAR(2000) NULL,
  "OrgDescription" VARCHAR(2000) NULL,
  "RegisteredBy" INT,
  "RegisteredOn" timestamptz(0) NULL,
  "CreatedOn" timestamptz(0) NULL,
  "CreatedBy" VARCHAR(45) NULL,
  "ModifiedOn" timestamptz(0) NULL,
  "ModifiedBy" VARCHAR(45) NULL,
  PRIMARY KEY (id),
  CONSTRAINT OrgCode_UNIQUE UNIQUE  ("OrgCode"));

  CREATE SEQUENCE course_action_state_coursererunstate_seq;

CREATE TABLE course_action_state_coursererunstate (
  id int NOT NULL DEFAULT NEXTVAL ('course_action_state_coursererunstate_seq'),
  created_time timestamptz(6) NOT NULL,
  updated_time timestamptz(6) NOT NULL,
  course_key varchar(255) NOT NULL,
  action varchar(100) NOT NULL,
  state varchar(50) NOT NULL,
  should_display bool NOT NULL,
  message varchar(1000) NOT NULL,
  source_course_key varchar(255) NOT NULL,
  display_name varchar(255) NOT NULL,
  created_user_id int DEFAULT NULL,
  updated_user_id int DEFAULT NULL,
  PRIMARY KEY (id),
  CONSTRAINT course_action_state_coursereruns_course_key_cf5da77ed3032d6_uniq UNIQUE  (course_key,action)
 ,
  CONSTRAINT course_action_s_created_user_id_7f53088ef8dccd0b_fk_auth_user_id FOREIGN KEY (created_user_id) REFERENCES auth_user (id),
  CONSTRAINT course_action_s_updated_user_id_4fab18012332c9a4_fk_auth_user_id FOREIGN KEY (updated_user_id) REFERENCES auth_user (id)
) ;
CREATE INDEX course_action_s_created_user_id_7f53088ef8dccd0b_fk_auth_user_id ON course_action_state_coursererunstate (created_user_id);
CREATE INDEX course_action_s_updated_user_id_4fab18012332c9a4_fk_auth_user_id ON course_action_state_coursererunstate (updated_user_id);
CREATE INDEX course_action_state_coursererunstate_c8235886 ON course_action_state_coursererunstate (course_key);
CREATE INDEX course_action_state_coursererunstate_418c5509 ON course_action_state_coursererunstate (action);
CREATE INDEX course_action_state_coursererunstate_a9bd7343 ON course_action_state_coursererunstate (source_course_key);

CREATE SEQUENCE courseware_user_orgs_seq;

CREATE TABLE courseware_user_orgs (
  id INT NOT NULL DEFAULT NEXTVAL ('courseware_user_orgs_seq'),
  "Org_id" INT NULL,
  "User_id" INT NULL,
  PRIMARY KEY (id));

CREATE SEQUENCE xblock_django_xblockconfiguration_seq;

CREATE TABLE xblock_django_xblockconfiguration (
  id int NOT NULL DEFAULT NEXTVAL ('xblock_django_xblockconfiguration_seq'),
  change_date timestamptz(6) NOT NULL,
  enabled bool NOT NULL,
  name varchar(255) NOT NULL,
  deprecated bool NOT NULL,
  changed_by_id int DEFAULT NULL,
  PRIMARY KEY (id)
 ,
  CONSTRAINT xblock_django_xblockconfiguration_changed_by_id_221b9d0e_fk FOREIGN KEY (changed_by_id) REFERENCES auth_user (id)
) ;

CREATE INDEX xblock_django_xbl_changed_by_id_61068ae9f50d6490_fk_auth_user_id ON xblock_django_xblockconfiguration (changed_by_id);
CREATE INDEX xblock_django_xblockconfiguration_b068931c ON xblock_django_xblockconfiguration (name);

CREATE SEQUENCE credit_creditcourse_seq;

CREATE TABLE credit_creditcourse (
  id int NOT NULL DEFAULT NEXTVAL ('credit_creditcourse_seq'),
  course_key varchar(255) NOT NULL,
  enabled bool NOT NULL,
  PRIMARY KEY (id),
  CONSTRAINT course_key UNIQUE  (course_key)
) ;

CREATE SEQUENCE student_courseaccessrole_seq;

CREATE TABLE student_courseaccessrole (
  id int NOT NULL DEFAULT NEXTVAL ('student_courseaccessrole_seq'),
  org varchar(64) NOT NULL,
  course_id varchar(255) NOT NULL,
  "role" varchar(64) NOT NULL,
  user_id int NOT NULL,
  PRIMARY KEY (id),
  CONSTRAINT student_courseaccessrole_user_id_3203176c4f474414_uniq UNIQUE  (user_id,org,course_id,role)
 ,
  CONSTRAINT student_courseaccessrole_user_id_90cf21fe_fk FOREIGN KEY (user_id) REFERENCES auth_user (id)
) ;

CREATE INDEX student_courseaccessrole_5a445d71 ON student_courseaccessrole (org);
CREATE INDEX student_courseaccessrole_ea134da7 ON student_courseaccessrole (course_id);
CREATE INDEX student_courseaccessrole_29a7e964 ON student_courseaccessrole (role);

CREATE SEQUENCE course_overviews_courseoverviewimageset_seq;

CREATE TABLE course_overviews_courseoverviewimageset (
  id int NOT NULL DEFAULT NEXTVAL ('course_overviews_courseoverviewimageset_seq'),
  created timestamptz(6) NOT NULL,
  modified timestamptz(6) NOT NULL,
  small_url text NOT NULL,
  large_url text NOT NULL,
  course_overview_id varchar(255) NOT NULL,
  PRIMARY KEY (id),
  CONSTRAINT course_overview_id UNIQUE  (course_overview_id),
  CONSTRAINT D47baf904f8952eb0e1fafefd558a718 FOREIGN KEY (course_overview_id) REFERENCES course_overviews_courseoverview (id)
) ;

CREATE SEQUENCE course_structures_coursestructure_seq;

CREATE TABLE course_structures_coursestructure (
  id int NOT NULL DEFAULT NEXTVAL ('course_structures_coursestructure_seq'),
  created timestamptz(6) NOT NULL,
  modified timestamptz(6) NOT NULL,
  course_id varchar(255) NOT NULL,
  structure_json text,
  discussion_id_map_json text,
  PRIMARY KEY (id),
  CONSTRAINT course_id UNIQUE  (course_id)
) ;

CREATE SEQUENCE verify_student_verificationdeadline_seq;

CREATE TABLE verify_student_verificationdeadline (
  id int NOT NULL DEFAULT NEXTVAL ('verify_student_verificationdeadline_seq'),
  created timestamptz(6) NOT NULL,
  modified timestamptz(6) NOT NULL,
  course_key varchar(255) NOT NULL,
  deadline timestamptz(6) NOT NULL,
  deadline_is_explicit smallint NOT NULL,
  PRIMARY KEY (id),
  CONSTRAINT verify_student_verificationdeadline_course_key UNIQUE  (course_key)
) ;

CREATE SEQUENCE course_overviews_courseoverviewtab_seq;

CREATE TABLE course_overviews_courseoverviewtab (
  id int NOT NULL DEFAULT NEXTVAL ('course_overviews_courseoverviewtab_seq'),
  tab_id varchar(50) NOT NULL,
  course_overview_id varchar(255) NOT NULL,
  PRIMARY KEY (id)
 ,
  CONSTRAINT D298658de1d4c8777e046eed658fc94e FOREIGN KEY (course_overview_id) REFERENCES course_overviews_courseoverview (id)
) ;

CREATE INDEX D298658de1d4c8777e046eed658fc94e ON course_overviews_courseoverviewtab (course_overview_id);

CREATE SEQUENCE course_overviews_courseoverviewimageconfig_seq;

CREATE TABLE course_overviews_courseoverviewimageconfig (
  id int NOT NULL DEFAULT NEXTVAL ('course_overviews_courseoverviewimageconfig_seq'),
  change_date timestamptz(6) NOT NULL,
  enabled bool NOT NULL,
  small_width int NOT NULL,
  small_height int NOT NULL,
  large_width int NOT NULL,
  large_height int NOT NULL,
  changed_by_id int DEFAULT NULL,
  PRIMARY KEY (id)
 ,
  CONSTRAINT course_overviews_courseov_changed_by_id_b60ae39a_fk FOREIGN KEY (changed_by_id) REFERENCES auth_user (id)
) ;

CREATE INDEX course_overviews__changed_by_id_54b19ba1c134af6a_fk_auth_user_id ON course_overviews_courseoverviewimageconfig (changed_by_id);

CREATE TABLE django_comment_common_discussionsidmapping (
  course_id varchar(255) NOT NULL,
  mapping text NOT NULL,
  PRIMARY KEY (course_id)
) ;

CREATE SEQUENCE django_comment_client_role_seq;

CREATE TABLE django_comment_client_role (
  id int NOT NULL DEFAULT NEXTVAL ('django_comment_client_role_seq'),
  name varchar(30) NOT NULL,
  course_id varchar(255) NOT NULL,
  PRIMARY KEY (id)
) ;

CREATE INDEX django_comment_client_role_ea134da7 ON django_comment_client_role (course_id);


CREATE TABLE django_comment_client_permission (
  name varchar(30) NOT NULL,
  PRIMARY KEY (name)
) ;


CREATE SEQUENCE django_comment_client_permission_roles_seq;

CREATE TABLE django_comment_client_permission_roles (
  id int NOT NULL DEFAULT NEXTVAL ('django_comment_client_permission_roles_seq'),
  permission_id varchar(30) NOT NULL,
  role_id int NOT NULL,
  PRIMARY KEY (id),
  CONSTRAINT permission_id UNIQUE  (permission_id,role_id)
 ,
  CONSTRAINT D4e9a4067c1db9041491363f5e032121 FOREIGN KEY (permission_id) REFERENCES django_comment_client_permission (name),
  CONSTRAINT django_role_id_558412c96ef7ba87_fk_django_comment_client_role_id FOREIGN KEY (role_id) REFERENCES django_comment_client_role (id)
) ;

CREATE INDEX django_role_id_558412c96ef7ba87_fk_django_comment_client_role_id ON django_comment_client_permission_roles (role_id);

CREATE SEQUENCE student_courseenrollment_seq;

CREATE TABLE student_courseenrollment (
  id int NOT NULL DEFAULT NEXTVAL ('student_courseenrollment_seq'),
  course_id varchar(255) NOT NULL,
  created timestamptz(6) DEFAULT NULL,
  is_active bool NOT NULL,
  mode varchar(100) NOT NULL,
  user_id int NOT NULL,
  PRIMARY KEY (id),
  CONSTRAINT student_courseenrollment_user_id_2d2a572f07dd8e37_uniq UNIQUE  (user_id,course_id)
 ,
  CONSTRAINT student_courseenrollment_user_id_4263a8e2_fk FOREIGN KEY (user_id) REFERENCES auth_user (id)
) ;

CREATE INDEX student_courseenrollment_ea134da7 ON student_courseenrollment (course_id);
CREATE INDEX student_courseenrollment_e2fa5388 ON student_courseenrollment (created);

CREATE SEQUENCE django_comment_client_role_users_seq;

CREATE TABLE django_comment_client_role_users (
  id int NOT NULL DEFAULT NEXTVAL ('django_comment_client_role_users_seq'),
  role_id int NOT NULL,
  user_id int NOT NULL,
  PRIMARY KEY (id),
  CONSTRAINT role_id UNIQUE  (role_id,user_id) ,
  CONSTRAINT django_comment_client_r_user_id__fk_auth_user_id FOREIGN KEY (user_id) REFERENCES auth_user (id),
  CONSTRAINT django_role_id_fk_django_comment_client_role_id FOREIGN KEY (role_id) REFERENCES django_comment_client_role (id)
) ;

CREATE INDEX django_comment_client_r_user_id__fk_auth_user_id ON django_comment_client_role_users (user_id);

CREATE SEQUENCE verified_track_content_verifiedtrackcohortedcourse_seq;

CREATE TABLE verified_track_content_verifiedtrackcohortedcourse (
  id int NOT NULL DEFAULT NEXTVAL ('verified_track_content_verifiedtrackcohortedcourse_seq'),
  course_key varchar(255) NOT NULL,
  enabled bool NOT NULL,
  verified_cohort_name varchar(100) NOT NULL,
  PRIMARY KEY (id),
  CONSTRAINT course_key_ux UNIQUE  (course_key)
) ;

CREATE SEQUENCE schedules_scheduleconfig_seq;

CREATE TABLE schedules_scheduleconfig (
  id int NOT NULL DEFAULT NEXTVAL ('schedules_scheduleconfig_seq'),
  change_date timestamptz(6) NOT NULL,
  enabled bool NOT NULL,
  create_schedules smallint NOT NULL,
  enqueue_recurring_nudge bool NOT NULL,
  deliver_recurring_nudge bool NOT NULL,
  changed_by_id int DEFAULT NULL,
  site_id int NOT NULL,
  deliver_upgrade_reminder bool NOT NULL,
  enqueue_upgrade_reminder bool NOT NULL,
  deliver_course_update bool NOT NULL,
  enqueue_course_update bool NOT NULL,
  hold_back_ratio double precision NOT NULL,
  PRIMARY KEY (id)
 ,
  CONSTRAINT schedules_schedulecon_site_id_5c0875f7e76f2d1f_fk_django_site_id FOREIGN KEY (site_id) REFERENCES django_site (id),
  CONSTRAINT schedules_scheduleconfig_changed_by_id_38ef599b_fk FOREIGN KEY (changed_by_id) REFERENCES auth_user (id)
) ;

CREATE SEQUENCE schedules_schedule_seq;

CREATE TABLE schedules_schedule (
  id int NOT NULL DEFAULT NEXTVAL ('schedules_schedule_seq'),
  created timestamptz(6) NOT NULL,
  modified timestamptz(6) NOT NULL,
  active bool NOT NULL,
  "start" timestamptz(6) NOT NULL,
  upgrade_deadline timestamptz(6) DEFAULT NULL,
  enrollment_id int NOT NULL,
  PRIMARY KEY (id),
  CONSTRAINT enrollment_id UNIQUE  (enrollment_id)
 ,
  CONSTRAINT sc_enrollment_id_73757e1116f677ec_fk_student_courseenrollment_id FOREIGN KEY (enrollment_id) REFERENCES student_courseenrollment (id)
) ;

CREATE INDEX schedules_schedule_start_796b08534b0ea8a8_uniq ON schedules_schedule (start);
CREATE INDEX schedules_schedule_upgrade_deadline_29b3e0a021034e_uniq ON schedules_schedule (upgrade_deadline);

CREATE INDEX schedules_schedul_changed_by_id_5f7d8004127c3aac_fk_auth_user_id ON schedules_scheduleconfig (changed_by_id);
CREATE INDEX schedules_schedulecon_site_id_5c0875f7e76f2d1f_fk_django_site_id ON schedules_scheduleconfig (site_id);

CREATE SEQUENCE waffle_utils_waffleflagcourseoverridemodel_seq;

CREATE TABLE waffle_utils_waffleflagcourseoverridemodel (
  id int NOT NULL DEFAULT NEXTVAL ('waffle_utils_waffleflagcourseoverridemodel_seq'),
  change_date timestamptz(6) NOT NULL,
  enabled bool NOT NULL,
  waffle_flag varchar(255) NOT NULL,
  course_id varchar(255) NOT NULL,
  override_choice varchar(3) NOT NULL,
  changed_by_id int DEFAULT NULL,
  PRIMARY KEY (id)
 ,
  CONSTRAINT waffle_utils_waffleflagco_changed_by_id_28429bf5_fk FOREIGN KEY (changed_by_id) REFERENCES auth_user (id)
) ;

CREATE INDEX waffle_utils_waff_changed_by_id_3b230839b4c20581_fk_auth_user_id ON waffle_utils_waffleflagcourseoverridemodel (changed_by_id);
CREATE INDEX waffle_utils_waffleflagcourseoverridemodel_6690e26e ON waffle_utils_waffleflagcourseoverridemodel (waffle_flag);
CREATE INDEX waffle_utils_waffleflagcourseoverridemodel_ea134da7 ON waffle_utils_waffleflagcourseoverridemodel (course_id);


CREATE SEQUENCE waffle_flag_seq;

CREATE TABLE waffle_flag (
  id int NOT NULL DEFAULT NEXTVAL ('waffle_flag_seq'),
  name varchar(100) NOT NULL,
  everyone bool DEFAULT NULL,
  percent decimal(3,1) DEFAULT NULL,
  testing bool NOT NULL,
  superusers bool NOT NULL,
  staff bool NOT NULL,
  authenticated bool NOT NULL,
  languages text NOT NULL,
  rollout bool NOT NULL,
  note text NOT NULL,
  created timestamptz(6) NOT NULL,
  modified timestamptz(6) NOT NULL,
  PRIMARY KEY (id),
  CONSTRAINT name_ux UNIQUE  (name)
) ;

CREATE INDEX waffle_flag_e2fa5388 ON waffle_flag (created);

CREATE SEQUENCE student_courseenrollmentallowed_seq;

CREATE TABLE student_courseenrollmentallowed (
  id int NOT NULL DEFAULT NEXTVAL ('student_courseenrollmentallowed_seq'),
  email varchar(255) NOT NULL,
  course_id varchar(255) NOT NULL,
  auto_enroll bool NOT NULL,
  created timestamptz(6) DEFAULT NULL,
  user_id int DEFAULT NULL,
  PRIMARY KEY (id),
  CONSTRAINT student_courseenrollmentallowed_email_6f3eafd4a6c58591_uniq UNIQUE  (email,course_id)
 ,
  CONSTRAINT student_courseenrollmentallowed_user_id_5875cce6_fk FOREIGN KEY (user_id) REFERENCES auth_user (id)
) ;

CREATE INDEX student_courseenrollmentallowed_0c83f57c ON student_courseenrollmentallowed (email);
CREATE INDEX student_courseenrollmentallowed_ea134da7 ON student_courseenrollmentallowed (course_id);
CREATE INDEX student_courseenrollmentallowed_e2fa5388 ON student_courseenrollmentallowed (created);
CREATE INDEX student_courseenrollmentallowed_e8701ad4 ON student_courseenrollmentallowed (user_id);
CREATE SEQUENCE courseware_subjects_links_seq;

CREATE TABLE courseware_subjects_links (
  id INT NOT NULL DEFAULT NEXTVAL ('courseware_subjects_links_seq'),
  subject_id VARCHAR(145) NULL,
  course_id VARCHAR(145) NULL,
  PRIMARY KEY (id));

CREATE SEQUENCE video_pipeline_videouploadsenabledbydefault_seq;

CREATE TABLE video_pipeline_videouploadsenabledbydefault (
  id int NOT NULL DEFAULT NEXTVAL ('video_pipeline_videouploadsenabledbydefault_seq'),
  change_date timestamptz(6) NOT NULL,
  enabled bool NOT NULL,
  enabled_for_all_courses smallint NOT NULL,
  changed_by_id int DEFAULT NULL,
  PRIMARY KEY (id)
 ,
  CONSTRAINT video_pipeline_videouploa_changed_by_id_3d066822_fk FOREIGN KEY (changed_by_id) REFERENCES auth_user (id)
) ;

CREATE INDEX video_pipeline_vi_changed_by_id_4fff17e91cce415c_fk_auth_user_id ON video_pipeline_videouploadsenabledbydefault (changed_by_id);

CREATE TABLE courseware_chapters (
  course_id VARCHAR(255) NULL,
  display_name VARCHAR(245) NULL,
  chapter_id VARCHAR(255) NULL,
  created_on timestamptz(0) NULL,
  creator_id VARCHAR(150) NULL,
  modified_on timestamptz(0) NULL,
  modifier_id VARCHAR(150) NULL,
  PRIMARY KEY (chapter_id))
;


CREATE TABLE courseware_sequential (
  sequential_id VARCHAR(255) NULL,
  chapter_id VARCHAR(255) NULL,
  course_id VARCHAR(255) NULL,
  display_name VARCHAR(245) NULL,
  created_on timestamptz(0) NULL,
  creator_id VARCHAR(150) NULL,
  modified_on timestamptz(0) NULL,
  modifier_id VARCHAR(150) NULL,
  PRIMARY KEY (sequential_id))
;

CREATE TABLE courseware_vertical (
	vertical_id VARCHAR(255) NULL,
  sequential_id VARCHAR(255) NULL,
  chapter_id VARCHAR(255) NULL,
  course_id VARCHAR(255) NULL,
  display_name VARCHAR(245) NULL,
  created_on timestamptz(0) NULL,
  creator_id VARCHAR(150) NULL,
  modified_on timestamptz(0) NULL,
  modifier_id VARCHAR(150) NULL,
  PRIMARY KEY (vertical_id))
;

CREATE SEQUENCE xblock_django_xblockstudioconfigurationflag_seq;

CREATE TABLE xblock_django_xblockstudioconfigurationflag (
  id int NOT NULL DEFAULT NEXTVAL ('xblock_django_xblockstudioconfigurationflag_seq'),
  change_date timestamptz(6) NOT NULL,
  enabled bool NOT NULL,
  changed_by_id int DEFAULT NULL,
  PRIMARY KEY (id)
 ,
  CONSTRAINT xblock_django_xblockstudi_changed_by_id_fdf047b8_fk FOREIGN KEY (changed_by_id) REFERENCES auth_user (id)
) ;

CREATE INDEX xblock_django_xbl_changed_by_id_11457ce96bbbfbf6_fk_auth_user_id ON xblock_django_xblockstudioconfigurationflag (changed_by_id);

CREATE TABLE courseware_xblocks (
  xblock_id VARCHAR(255) NULL,
  xblock_type VARCHAR(255) NULL,
  vertical_id VARCHAR(255) NULL,
  course_id VARCHAR(255) NULL,
  display_name VARCHAR(245) NULL,
  created_on timestamptz(0) NULL,
  creator_id VARCHAR(150) NULL,
  modified_on timestamptz(0) NULL,
  modifier_id VARCHAR(150) NULL,
  PRIMARY KEY (xblock_id))
;

CREATE SEQUENCE static_replace_assetbaseurlconfig_seq;
CREATE TABLE static_replace_assetbaseurlconfig (
  id int NOT NULL DEFAULT NEXTVAL ('static_replace_assetbaseurlconfig_seq'),
  change_date timestamptz(6) NOT NULL,
  enabled bool NOT NULL,
  base_url text NOT NULL,
  changed_by_id int DEFAULT NULL,
  PRIMARY KEY (id)
 ,
  CONSTRAINT static_replace_assetbaseurlconfig_changed_by_id_f592e050_fk FOREIGN KEY (changed_by_id) REFERENCES auth_user (id)
) ;

CREATE INDEX static_replace_as_changed_by_id_796c2e5b1bee7027_fk_auth_user_id ON static_replace_assetbaseurlconfig (changed_by_id);

CREATE SEQUENCE courseware_studentmodule_seq;

CREATE TABLE courseware_studentmodule (
  id int NOT NULL DEFAULT NEXTVAL ('courseware_studentmodule_seq'),
  module_type varchar(32) NOT NULL,
  module_id varchar(255) NOT NULL,
  course_id varchar(255) NOT NULL,
  state text,
  grade double precision DEFAULT NULL,
  max_grade double precision DEFAULT NULL,
  done varchar(8) NOT NULL,
  created timestamptz(6) NOT NULL,
  modified timestamptz(6) NOT NULL,
  student_id int NOT NULL,
  PRIMARY KEY (id),
  CONSTRAINT courseware_studentmodule_student_id_635d77aea1256de5_uniq UNIQUE  (student_id,module_id,course_id)
 ,
  CONSTRAINT courseware_studentmodule_student_id_c7ed88a0_fk FOREIGN KEY (student_id) REFERENCES auth_user (id)
) ;

CREATE INDEX courseware_studentmodule_82bd5515 ON courseware_studentmodule (module_type);
CREATE INDEX courseware_studentmodule_ea134da7 ON courseware_studentmodule (course_id);
CREATE INDEX courseware_studentmodule_de6a20aa ON courseware_studentmodule (grade);
CREATE INDEX courseware_studentmodule_e2fa5388 ON courseware_studentmodule (created);
CREATE INDEX courseware_studentmodule_9ae73c65 ON courseware_studentmodule (modified);


CREATE SEQUENCE user_api_usercoursetag_seq;

CREATE TABLE user_api_usercoursetag (
  id int NOT NULL DEFAULT NEXTVAL ('user_api_usercoursetag_seq'),
  key varchar(255) NOT NULL,
  course_id varchar(255) NOT NULL,
  value text NOT NULL,
  user_id int NOT NULL,
  PRIMARY KEY (id),
  CONSTRAINT user_api_usercoursetag_user_id_64d9a32c9890f610_uniq UNIQUE  (user_id,course_id,key)
 ,
  CONSTRAINT user_api_usercoursetag_user_id_2692245bbb861fc2_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES auth_user (id)
) ;

CREATE INDEX user_api_usercoursetag_3c6e0b8a ON user_api_usercoursetag (key);
CREATE INDEX user_api_usercoursetag_ea134da7 ON user_api_usercoursetag (course_id);

CREATE SEQUENCE shoppingcart_orderitem_seq;

CREATE TABLE shoppingcart_orderitem (
  id int NOT NULL DEFAULT NEXTVAL ('shoppingcart_orderitem_seq'),
  created timestamptz(6) NOT NULL,
  modified timestamptz(6) NOT NULL,
  status varchar(32) NOT NULL,
  qty int NOT NULL,
  unit_cost decimal(30,2) NOT NULL,
  list_price decimal(30,2) DEFAULT NULL,
  line_desc varchar(1024) NOT NULL,
  currency varchar(8) NOT NULL,
  fulfilled_time timestamptz(6) DEFAULT NULL,
  refund_requested_time timestamptz(6) DEFAULT NULL,
  service_fee decimal(30,2) NOT NULL,
  report_comments text NOT NULL,
  order_id int NOT NULL,
  user_id int NOT NULL,
  PRIMARY KEY (id)
 ,
  CONSTRAINT shoppingcart__order_id_325e5347f18743e3_fk_shoppingcart_order_id FOREIGN KEY (order_id) REFERENCES shoppingcart_order (id),
  CONSTRAINT shoppingcart_orderitem_user_id_93073a67_fk FOREIGN KEY (user_id) REFERENCES auth_user (id)
) ;

CREATE INDEX shoppingcart_orderitem_9acb4454 ON shoppingcart_orderitem (status);
CREATE INDEX shoppingcart_orderitem_3b927c91 ON shoppingcart_orderitem (fulfilled_time);
CREATE INDEX shoppingcart_orderitem_76ed2946 ON shoppingcart_orderitem (refund_requested_time);
CREATE INDEX shoppingcart_orderitem_69dfcb07 ON shoppingcart_orderitem (order_id);
CREATE INDEX shoppingcart_orderitem_e8701ad4 ON shoppingcart_orderitem (user_id);


CREATE TABLE shoppingcart_paidcourseregistration (
  orderitem_ptr_id int NOT NULL,
  course_id varchar(128) NOT NULL,
  mode varchar(50) NOT NULL,
  course_enrollment_id int DEFAULT NULL,
  PRIMARY KEY (orderitem_ptr_id)
 ,
  CONSTRAINT D8d681d7e59c2dcf2ea55e7e5e06553d FOREIGN KEY (course_enrollment_id) REFERENCES student_courseenrollment (id),
  CONSTRAINT s_orderitem_ptr_id_3c991acc5d644f13_fk_shoppingcart_orderitem_id FOREIGN KEY (orderitem_ptr_id) REFERENCES shoppingcart_orderitem (id)
) ;

CREATE INDEX D8d681d7e59c2dcf2ea55e7e5e06553d ON shoppingcart_paidcourseregistration (course_enrollment_id);
CREATE INDEX shoppingcart_paidcourseregistration_ea134da7 ON shoppingcart_paidcourseregistration (course_id);
CREATE INDEX shoppingcart_paidcourseregistration_15d61712 ON shoppingcart_paidcourseregistration (mode);


CREATE TABLE shoppingcart_courseregcodeitem (
  orderitem_ptr_id int NOT NULL,
  course_id varchar(128) NOT NULL,
  mode varchar(50) NOT NULL,
  PRIMARY KEY (orderitem_ptr_id)
 ,
  CONSTRAINT s_orderitem_ptr_id_7ca6c1b9c7df7905_fk_shoppingcart_orderitem_id FOREIGN KEY (orderitem_ptr_id) REFERENCES shoppingcart_orderitem (id)
) ;

CREATE INDEX shoppingcart_courseregcodeitem_ea134da7 ON shoppingcart_courseregcodeitem (course_id);
CREATE INDEX shoppingcart_courseregcodeitem_15d61712 ON shoppingcart_courseregcodeitem (mode);

CREATE SEQUENCE commerce_commerceconfiguration_seq;

CREATE TABLE commerce_commerceconfiguration (
  id int NOT NULL DEFAULT NEXTVAL ('commerce_commerceconfiguration_seq'),
  change_date timestamptz(6) NOT NULL,
  enabled bool NOT NULL,
  checkout_on_ecommerce_service bool NOT NULL,
  changed_by_id int DEFAULT NULL,
  cache_ttl int check (cache_ttl > 0) NOT NULL,
  receipt_page varchar(255) NOT NULL,
  enable_automatic_refund_approval bool NOT NULL,
  basket_checkout_page varchar(255) NOT NULL,
  PRIMARY KEY (id)
 ,
  CONSTRAINT commerce_commerceconfiguration_changed_by_id_2c9a6f14_fk FOREIGN KEY (changed_by_id) REFERENCES auth_user (id)
) ;

CREATE INDEX commerce_commerce_changed_by_id_7441951d1c97c1d7_fk_auth_user_id ON commerce_commerceconfiguration (changed_by_id);

CREATE TABLE shoppingcart_certificateitem (
  orderitem_ptr_id int NOT NULL,
  course_id varchar(128) NOT NULL,
  mode varchar(50) NOT NULL,
  course_enrollment_id int NOT NULL,
  PRIMARY KEY (orderitem_ptr_id)
 ,
  CONSTRAINT D231cb871868cb92e6ed1ee8e53a1bee FOREIGN KEY (course_enrollment_id) REFERENCES student_courseenrollment (id),
  CONSTRAINT s_orderitem_ptr_id_5127313bc5a09762_fk_shoppingcart_orderitem_id FOREIGN KEY (orderitem_ptr_id) REFERENCES shoppingcart_orderitem (id)
) ;

CREATE INDEX D231cb871868cb92e6ed1ee8e53a1bee ON shoppingcart_certificateitem (course_enrollment_id);
CREATE INDEX shoppingcart_certificateitem_ea134da7 ON shoppingcart_certificateitem (course_id);
CREATE INDEX shoppingcart_certificateitem_15d61712 ON shoppingcart_certificateitem (mode);

CREATE TABLE shoppingcart_donation (
  orderitem_ptr_id int NOT NULL,
  donation_type varchar(32) NOT NULL,
  course_id varchar(255) NOT NULL,
  PRIMARY KEY (orderitem_ptr_id)
 ,
  CONSTRAINT s_orderitem_ptr_id_18caefe119e0bd2f_fk_shoppingcart_orderitem_id FOREIGN KEY (orderitem_ptr_id) REFERENCES shoppingcart_orderitem (id)
) ;

CREATE INDEX shoppingcart_donation_ea134da7 ON shoppingcart_donation (course_id);

CREATE SEQUENCE student_anonymoususerid_seq;

CREATE TABLE student_anonymoususerid (
  id int NOT NULL DEFAULT NEXTVAL ('student_anonymoususerid_seq'),
  anonymous_user_id varchar(32) NOT NULL,
  course_id varchar(255) NOT NULL,
  user_id int NOT NULL,
  PRIMARY KEY (id),
  CONSTRAINT anonymous_user_id UNIQUE  (anonymous_user_id)
 ,
  CONSTRAINT student_anonymoususerid_user_id_0fb2ad5c_fk FOREIGN KEY (user_id) REFERENCES auth_user (id)
) ;

CREATE INDEX student_anonymoususerid_user_id_1a18af72cf6b95f7_fk_auth_user_id ON student_anonymoususerid (user_id);
CREATE INDEX student_anonymoususerid_ea134da7 ON student_anonymoususerid (course_id);

CREATE SEQUENCE student_entranceexamconfiguration_seq;

CREATE TABLE student_entranceexamconfiguration (
  id int NOT NULL DEFAULT NEXTVAL ('student_entranceexamconfiguration_seq'),
  course_id varchar(255) NOT NULL,
  created timestamptz(6) DEFAULT NULL,
  updated timestamptz(6) NOT NULL,
  skip_entrance_exam smallint NOT NULL,
  user_id int NOT NULL,
  PRIMARY KEY (id),
  CONSTRAINT student_entranceexamconfiguration_user_id_714c2ef6a88504f0_uniq UNIQUE  (user_id,course_id)
 ,
  CONSTRAINT student_entranceexamconfiguration_user_id_387a35d6_fk FOREIGN KEY (user_id) REFERENCES auth_user (id)
) ;

CREATE INDEX student_entranceexamconfiguration_ea134da7 ON student_entranceexamconfiguration (course_id);
CREATE INDEX student_entranceexamconfiguration_e2fa5388 ON student_entranceexamconfiguration (created);
CREATE INDEX student_entranceexamconfiguration_0f81d52e ON student_entranceexamconfiguration (updated);

CREATE SEQUENCE milestones_milestonerelationshiptype_seq;

CREATE TABLE milestones_milestonerelationshiptype (
  id int NOT NULL DEFAULT NEXTVAL ('milestones_milestonerelationshiptype_seq'),
  created timestamptz(6) NOT NULL,
  modified timestamptz(6) NOT NULL,
  name varchar(25) NOT NULL,
  description text NOT NULL,
  active bool NOT NULL,
  PRIMARY KEY (id),
  CONSTRAINT milestones_milestonerelationshiptype_name_ux UNIQUE  (name));

  CREATE SEQUENCE milestones_milestone_seq;

CREATE TABLE milestones_milestone (
  id int NOT NULL DEFAULT NEXTVAL ('milestones_milestone_seq'),
  created timestamptz(6) NOT NULL,
  modified timestamptz(6) NOT NULL,
  namespace varchar(255) NOT NULL,
  name varchar(255) NOT NULL,
  display_name varchar(255) NOT NULL,
  description text NOT NULL,
  active bool NOT NULL,
  PRIMARY KEY (id),
  CONSTRAINT milestones_milestone_namespace_460a2f6943016c0b_uniq UNIQUE  (namespace,name)
) ;

CREATE INDEX milestones_milestone_89801e9e ON milestones_milestone (namespace);
CREATE INDEX milestones_milestone_b068931c ON milestones_milestone (name);
CREATE INDEX milestones_milestone_active_1182ba3c09d42c35_uniq ON milestones_milestone (active);


CREATE SEQUENCE milestones_coursemilestone_seq;

CREATE TABLE milestones_coursemilestone (
  id int NOT NULL DEFAULT NEXTVAL ('milestones_coursemilestone_seq'),
  created timestamptz(6) NOT NULL,
  modified timestamptz(6) NOT NULL,
  course_id varchar(255) NOT NULL,
  active bool NOT NULL,
  milestone_id int NOT NULL,
  milestone_relationship_type_id int NOT NULL,
  PRIMARY KEY (id),
  CONSTRAINT milestones_coursemilestone_course_id_5a06e10579eab3b7_uniq UNIQUE  (course_id,milestone_id)
 ,
  CONSTRAINT D69536d0d313008147c5daf5341090e1 FOREIGN KEY (milestone_relationship_type_id) REFERENCES milestones_milestonerelationshiptype (id),
  CONSTRAINT milesto_milestone_id_284153799c54d7d8_fk_milestones_milestone_id FOREIGN KEY (milestone_id) REFERENCES milestones_milestone (id)
) ;

CREATE INDEX milestones_coursemilestone_ea134da7 ON milestones_coursemilestone (course_id);
CREATE INDEX milestones_coursemilestone_dbb5cd1e ON milestones_coursemilestone (milestone_id);
CREATE INDEX milestones_coursemilestone_db6866e3 ON milestones_coursemilestone (milestone_relationship_type_id);
CREATE INDEX milestones_coursemilestone_active_5c3a925f8cc4bde2_uniq ON milestones_coursemilestone (active);

CREATE SEQUENCE completion_blockcompletion_seq;

CREATE TABLE completion_blockcompletion (
  created timestamptz(6) NOT NULL,
  modified timestamptz(6) NOT NULL,
  id bigint NOT NULL DEFAULT NEXTVAL ('completion_blockcompletion_seq'),
  course_key varchar(255) NOT NULL,
  block_key varchar(255) NOT NULL,
  block_type varchar(64) NOT NULL,
  completion double precision NOT NULL,
  user_id int NOT NULL,
  PRIMARY KEY (id),
  CONSTRAINT completion_blockcompletion_course_key_54aa5e002d4e74a2_uniq UNIQUE  (course_key,block_key,user_id)
 ,
  CONSTRAINT completion_blockcompletion_user_id_20994c23_fk FOREIGN KEY (user_id) REFERENCES auth_user (id)
) ;

CREATE INDEX completion_blockcompletion_course_key_4e99db81ed8510f4_idx ON completion_blockcompletion (course_key,block_type,user_id);
CREATE INDEX completion_blockcompletion_user_id_1d63de3a4a8ef1e5_idx ON completion_blockcompletion (user_id,course_key,modified);

CREATE SEQUENCE course_goals_coursegoal_seq;

CREATE TABLE course_goals_coursegoal (
  id int NOT NULL DEFAULT NEXTVAL ('course_goals_coursegoal_seq'),
  course_key varchar(255) NOT NULL,
  goal_key varchar(100) NOT NULL,
  user_id int NOT NULL,
  PRIMARY KEY (id),
  CONSTRAINT course_goals_coursegoal_user_id_7b4ac74987215807_uniq UNIQUE  (user_id,course_key)
 ,
  CONSTRAINT course_goals_coursegoal_user_id_0a07e3db_fk FOREIGN KEY (user_id) REFERENCES auth_user (id)
) ;

CREATE INDEX course_goals_coursegoal_c8235886 ON course_goals_coursegoal (course_key);

CREATE SEQUENCE shoppingcart_invoice_seq;

CREATE TABLE shoppingcart_invoice (
  id int NOT NULL DEFAULT NEXTVAL ('shoppingcart_invoice_seq'),
  created timestamptz(6) NOT NULL,
  modified timestamptz(6) NOT NULL,
  company_name varchar(255) NOT NULL,
  company_contact_name varchar(255) NOT NULL,
  company_contact_email varchar(255) NOT NULL,
  recipient_name varchar(255) NOT NULL,
  recipient_email varchar(255) NOT NULL,
  address_line_1 varchar(255) NOT NULL,
  address_line_2 varchar(255) DEFAULT NULL,
  address_line_3 varchar(255) DEFAULT NULL,
  city varchar(255) DEFAULT NULL,
  state varchar(255) DEFAULT NULL,
  zip varchar(15) DEFAULT NULL,
  country varchar(64) DEFAULT NULL,
  total_amount double precision NOT NULL,
  course_id varchar(255) NOT NULL,
  internal_reference varchar(255) DEFAULT NULL,
  customer_reference_number varchar(63) DEFAULT NULL,
  is_valid smallint NOT NULL,
  PRIMARY KEY (id)
) ;

CREATE INDEX shoppingcart_invoice_c1007e8a ON shoppingcart_invoice (company_name);
CREATE INDEX shoppingcart_invoice_ea134da7 ON shoppingcart_invoice (course_id);


CREATE SEQUENCE shoppingcart_invoiceitem_seq;

CREATE TABLE shoppingcart_invoiceitem (
  id int NOT NULL DEFAULT NEXTVAL ('shoppingcart_invoiceitem_seq'),
  created timestamptz(6) NOT NULL,
  modified timestamptz(6) NOT NULL,
  qty int NOT NULL,
  unit_price decimal(30,2) NOT NULL,
  currency varchar(8) NOT NULL,
  invoice_id int NOT NULL,
  PRIMARY KEY (id)
 ,
  CONSTRAINT shoppingc_invoice_id_35828791c8405d01_fk_shoppingcart_invoice_id FOREIGN KEY (invoice_id) REFERENCES shoppingcart_invoice (id)
) ;

CREATE INDEX shoppingcart_invoiceitem_f1f5d967 ON shoppingcart_invoiceitem (invoice_id);

CREATE TABLE shoppingcart_courseregistrationcodeinvoiceitem (
  invoiceitem_ptr_id int NOT NULL,
  course_id varchar(128) NOT NULL,
  PRIMARY KEY (invoiceitem_ptr_id)
 ,
  CONSTRAINT D75797188300cb2dc6a7b16353295aaf FOREIGN KEY (invoiceitem_ptr_id) REFERENCES shoppingcart_invoiceitem (id)
) ;

CREATE INDEX shoppingcart_courseregistrationcodeinvoiceitem_ea134da7 ON shoppingcart_courseregistrationcodeinvoiceitem (course_id);

CREATE SEQUENCE shoppingcart_courseregistrationcode_seq;

CREATE TABLE shoppingcart_courseregistrationcode (
  id int NOT NULL DEFAULT NEXTVAL ('shoppingcart_courseregistrationcode_seq'),
  code varchar(32) NOT NULL,
  course_id varchar(255) NOT NULL,
  created_at timestamptz(6) NOT NULL,
  mode_slug varchar(100) DEFAULT NULL,
  is_valid bool NOT NULL,
  created_by_id int NOT NULL,
  invoice_id int DEFAULT NULL,
  order_id int DEFAULT NULL,
  invoice_item_id int DEFAULT NULL,
  PRIMARY KEY (id),
  CONSTRAINT code UNIQUE  (code)
 ,
  CONSTRAINT f040030b6361304bd87eb40c09a82094 FOREIGN KEY (invoice_item_id) REFERENCES shoppingcart_courseregistrationcodeinvoiceitem (invoiceitem_ptr_id),
  CONSTRAINT shoppingc_invoice_id_422f26bdc7c5cb99_fk_shoppingcart_invoice_id FOREIGN KEY (invoice_id) REFERENCES shoppingcart_invoice (id),
  CONSTRAINT shoppingcart__order_id_279d7e2df3fe6b6a_fk_shoppingcart_order_id FOREIGN KEY (order_id) REFERENCES shoppingcart_order (id),
  CONSTRAINT shoppingcart_courseregistrationcode_created_by_id_4a0a3481_fk FOREIGN KEY (created_by_id) REFERENCES auth_user (id)
) ;

CREATE INDEX shoppingcart_cour_created_by_id_11125a9667aa01c9_fk_auth_user_id ON shoppingcart_courseregistrationcode (created_by_id);
CREATE INDEX shoppingcart_courseregistrationcode_ea134da7 ON shoppingcart_courseregistrationcode (course_id);
CREATE INDEX shoppingcart_courseregistrationcode_f1f5d967 ON shoppingcart_courseregistrationcode (invoice_id);
CREATE INDEX shoppingcart_courseregistrationcode_69dfcb07 ON shoppingcart_courseregistrationcode (order_id);
CREATE INDEX shoppingcart_courseregistrationcode_7a471658 ON shoppingcart_courseregistrationcode (invoice_item_id);

CREATE SEQUENCE shoppingcart_registrationcoderedemption_seq;

CREATE TABLE shoppingcart_registrationcoderedemption (
  id int NOT NULL DEFAULT NEXTVAL ('shoppingcart_registrationcoderedemption_seq'),
  redeemed_at timestamptz(6) DEFAULT NULL,
  course_enrollment_id int DEFAULT NULL,
  order_id int DEFAULT NULL,
  redeemed_by_id int NOT NULL,
  registration_code_id int NOT NULL,
  PRIMARY KEY (id)
 ,
  CONSTRAINT D1ed44c4be114e424571929bce972f54 FOREIGN KEY (registration_code_id) REFERENCES shoppingcart_courseregistrationcode (id),
  CONSTRAINT D6654a8efe686d45804b6116dfc6bee1 FOREIGN KEY (course_enrollment_id) REFERENCES student_courseenrollment (id),
  CONSTRAINT shoppingcart_r_order_id_752ddc3003afe96_fk_shoppingcart_order_id FOREIGN KEY (order_id) REFERENCES shoppingcart_order (id),
  CONSTRAINT shoppingcart_registration_redeemed_by_id_95c54187_fk FOREIGN KEY (redeemed_by_id) REFERENCES auth_user (id)
) ;

CREATE INDEX D6654a8efe686d45804b6116dfc6bee1 ON shoppingcart_registrationcoderedemption (course_enrollment_id);
CREATE INDEX shoppingcart_r_order_id_752ddc3003afe96_fk_shoppingcart_order_id ON shoppingcart_registrationcoderedemption (order_id);
CREATE INDEX shoppingcart_reg_redeemed_by_id_455df2dd74004fff_fk_auth_user_id ON shoppingcart_registrationcoderedemption (redeemed_by_id);
CREATE INDEX D1ed44c4be114e424571929bce972f54 ON shoppingcart_registrationcoderedemption (registration_code_id);


CREATE SEQUENCE crawlers_crawlersconfig_seq;

CREATE TABLE crawlers_crawlersconfig (
  id int NOT NULL DEFAULT NEXTVAL ('crawlers_crawlersconfig_seq'),
  change_date timestamptz(6) NOT NULL,
  enabled bool NOT NULL,
  known_user_agents text NOT NULL,
  changed_by_id int DEFAULT NULL,
  PRIMARY KEY (id)
 ,
  CONSTRAINT crawlers_crawlersconfig_changed_by_id_544af924_fk FOREIGN KEY (changed_by_id) REFERENCES auth_user (id)
) ;

CREATE INDEX crawlers_crawlers_changed_by_id_7014349920284aa4_fk_auth_user_id ON crawlers_crawlersconfig (changed_by_id);

CREATE SEQUENCE courseware_xmodulestudentinfofield_seq;

CREATE TABLE courseware_xmodulestudentinfofield (
  id int NOT NULL DEFAULT NEXTVAL ('courseware_xmodulestudentinfofield_seq'),
  field_name varchar(64) NOT NULL,
  value text NOT NULL,
  created timestamptz(6) NOT NULL,
  modified timestamptz(6) NOT NULL,
  student_id int NOT NULL,
  PRIMARY KEY (id),
  CONSTRAINT courseware_xmodulestudentinfofi_student_id_33f2f772c49db067_uniq UNIQUE  (student_id,field_name)
 ,
  CONSTRAINT courseware_xmodulestudentinfofield_student_id_b78d39b4_fk FOREIGN KEY (student_id) REFERENCES auth_user (id)
) ;

CREATE INDEX courseware_xmodulestudentinfofield_73f329f1 ON courseware_xmodulestudentinfofield (field_name);
CREATE INDEX courseware_xmodulestudentinfofield_e2fa5388 ON courseware_xmodulestudentinfofield (created);
CREATE INDEX courseware_xmodulestudentinfofield_9ae73c65 ON courseware_xmodulestudentinfofield (modified);

CREATE SEQUENCE wiki_articlerevision_seq;

CREATE TABLE wiki_articlerevision (
  id int NOT NULL DEFAULT NEXTVAL ('wiki_articlerevision_seq'),
  revision_number int NOT NULL,
  user_message text NOT NULL,
  automatic_log text NOT NULL,
  ip_address char(39) DEFAULT NULL,
  modified timestamptz(6) NOT NULL,
  created timestamptz(6) NOT NULL,
  deleted bool NOT NULL,
  locked bool NOT NULL,
  content text NOT NULL,
  title varchar(512) NOT NULL,
  article_id int NOT NULL,
  previous_revision_id int DEFAULT NULL,
  user_id int DEFAULT NULL,
  PRIMARY KEY (id),
  CONSTRAINT wiki_articlerevision_article_id_4b4e7910c8e7b2d0_uniq UNIQUE  (article_id,revision_number) ,
  CONSTRAINT fae2b1c6e892c699844d5dda69aeb89e FOREIGN KEY (previous_revision_id) REFERENCES wiki_articlerevision (id),
  CONSTRAINT wiki_articlerevision_user_id_c687e4de_fk FOREIGN KEY (user_id) REFERENCES auth_user (id)
) ;

CREATE INDEX fae2b1c6e892c699844d5dda69aeb89e ON wiki_articlerevision (previous_revision_id);
CREATE INDEX wiki_articlerevision_user_id_183520686b6ead55_fk_auth_user_id ON wiki_articlerevision (user_id);


CREATE SEQUENCE wiki_article_seq;

CREATE TABLE wiki_article (
  id int NOT NULL DEFAULT NEXTVAL ('wiki_article_seq'),
  created timestamptz(6) NOT NULL,
  modified timestamptz(6) NOT NULL,
  group_read bool NOT NULL,
  group_write bool NOT NULL,
  other_read bool NOT NULL,
  other_write bool NOT NULL,
  current_revision_id int DEFAULT NULL,
  group_id int DEFAULT NULL,
  owner_id int DEFAULT NULL,
  PRIMARY KEY (id),
  CONSTRAINT current_revision_id UNIQUE  (current_revision_id),
  CONSTRAINT current_revision_id_42a9dbec1e0dd15c_fk_wiki_articlerevision_id FOREIGN KEY (current_revision_id) REFERENCES wiki_articlerevision (id),
  CONSTRAINT wiki_article_group_id_2b38601b6aa39f3d_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES auth_group (id),
  CONSTRAINT wiki_article_owner_id_956bc94a_fk FOREIGN KEY (owner_id) REFERENCES auth_user (id)
);

CREATE INDEX wiki_article_0e939a4f ON wiki_article (group_id);
CREATE INDEX wiki_article_5e7b1936 ON wiki_article (owner_id);



CREATE SEQUENCE wiki_urlpath_seq;

CREATE TABLE wiki_urlpath (
  id int NOT NULL DEFAULT NEXTVAL ('wiki_urlpath_seq'),
  slug varchar(255) DEFAULT NULL,
  lft int check (lft > 0) NOT NULL,
  rght int check (rght > 0) NOT NULL,
  tree_id int check (tree_id > 0) NOT NULL,
  level int check (level > 0) NOT NULL,
  article_id int NOT NULL,
  parent_id int DEFAULT NULL,
  site_id int NOT NULL,
  PRIMARY KEY (id),
  CONSTRAINT wiki_urlpath_site_id_124f6aa7b2cc9b82_uniq UNIQUE  (site_id,parent_id,slug)
 ,
  CONSTRAINT wiki_urlpath_article_id_1d1c5eb9a64e1390_fk_wiki_article_id FOREIGN KEY (article_id) REFERENCES wiki_article (id),
  CONSTRAINT wiki_urlpath_parent_id_24eab80cd168595f_fk_wiki_urlpath_id FOREIGN KEY (parent_id) REFERENCES wiki_urlpath (id),
  CONSTRAINT wiki_urlpath_site_id_4f30e731b0464e80_fk_django_site_id FOREIGN KEY (site_id) REFERENCES django_site (id)
) ;

CREATE INDEX wiki_urlpath_article_id_1d1c5eb9a64e1390_fk_wiki_article_id ON wiki_urlpath (article_id);
CREATE INDEX wiki_urlpath_2dbcba41 ON wiki_urlpath (slug);
CREATE INDEX wiki_urlpath_caf7cc51 ON wiki_urlpath (lft);
CREATE INDEX wiki_urlpath_3cfbd988 ON wiki_urlpath (rght);
CREATE INDEX wiki_urlpath_656442a0 ON wiki_urlpath (tree_id);
CREATE INDEX wiki_urlpath_c9e9a848 ON wiki_urlpath (level);
CREATE INDEX wiki_urlpath_6be37982 ON wiki_urlpath (parent_id);
alter table wiki_articlerevision add  CONSTRAINT wiki_articlerevis_article_id_1f2c587981af1463_fk_wiki_article_id FOREIGN KEY (article_id) REFERENCES wiki_article (id);

CREATE SEQUENCE wiki_articleplugin_seq;

CREATE TABLE wiki_articleplugin (
  id int NOT NULL DEFAULT NEXTVAL ('wiki_articleplugin_seq'),
  deleted bool NOT NULL,
  created timestamptz(6) NOT NULL,
  article_id int NOT NULL,
  PRIMARY KEY (id) ,
  CONSTRAINT wiki_articleplugi_article_id_2d2c794af030d9dd_fk_wiki_article_id FOREIGN KEY (article_id) REFERENCES wiki_article (id)
) ;

CREATE INDEX wiki_articleplugin_a00c1b00 ON wiki_articleplugin (article_id);

CREATE TABLE wiki_simpleplugin (
  articleplugin_ptr_id int NOT NULL,
  article_revision_id int NOT NULL,
  PRIMARY KEY (articleplugin_ptr_id)
 ,
  CONSTRAINT w_article_revision_id_8be41c856aa0285_fk_wiki_articlerevision_id FOREIGN KEY (article_revision_id) REFERENCES wiki_articlerevision (id),
  CONSTRAINT w_articleplugin_ptr_id_36e661324cc27ff2_fk_wiki_articleplugin_id FOREIGN KEY (articleplugin_ptr_id) REFERENCES wiki_articleplugin (id)
) ;

CREATE INDEX w_article_revision_id_8be41c856aa0285_fk_wiki_articlerevision_id ON wiki_simpleplugin (article_revision_id);


CREATE SEQUENCE wiki_articleforobject_seq;

CREATE TABLE wiki_articleforobject (
  id int NOT NULL DEFAULT NEXTVAL ('wiki_articleforobject_seq'),
  object_id int check (object_id > 0) NOT NULL,
  is_mptt bool NOT NULL,
  article_id int NOT NULL,
  content_type_id int NOT NULL,
  PRIMARY KEY (id),
  CONSTRAINT wiki_articleforobject_content_type_id_27c4cce189b3bcab_uniq UNIQUE  (content_type_id,object_id)
 ,
  CONSTRAINT wiki__content_type_id_6a39c68b7a20c3c4_fk_django_content_type_id FOREIGN KEY (content_type_id) REFERENCES django_content_type (id),
  CONSTRAINT wiki_articleforobj_article_id_6effcfadf020e71_fk_wiki_article_id FOREIGN KEY (article_id) REFERENCES wiki_article (id)
) ;

CREATE INDEX wiki_articleforobj_article_id_6effcfadf020e71_fk_wiki_article_id ON wiki_articleforobject (article_id);

CREATE SEQUENCE grades_persistentgradesenabledflag_seq;

CREATE TABLE grades_persistentgradesenabledflag (
  id int NOT NULL DEFAULT NEXTVAL ('grades_persistentgradesenabledflag_seq'),
  change_date timestamptz(6) NOT NULL,
  enabled bool NOT NULL,
  enabled_for_all_courses bool NOT NULL,
  changed_by_id int DEFAULT NULL,
  PRIMARY KEY (id)
 ,
  CONSTRAINT grades_persistentgradesenabledflag_changed_by_id_f80cdad1_fk FOREIGN KEY (changed_by_id) REFERENCES auth_user (id)
) ;

CREATE INDEX grades_persistent_changed_by_id_2350d66400243149_fk_auth_user_id ON grades_persistentgradesenabledflag (changed_by_id);

CREATE SEQUENCE submissions_studentitem_seq;

CREATE TABLE submissions_studentitem (
  id int NOT NULL DEFAULT NEXTVAL ('submissions_studentitem_seq'),
  student_id varchar(255) NOT NULL,
  course_id varchar(255) NOT NULL,
  item_id varchar(255) NOT NULL,
  item_type varchar(100) NOT NULL,
  PRIMARY KEY (id),
  CONSTRAINT submissions_studentitem_course_id_6a6eccbdec6ffd0b_uniq UNIQUE  (course_id,student_id,item_id)
) ;

CREATE INDEX submissions_studentitem_30a811f6 ON submissions_studentitem (student_id);
CREATE INDEX submissions_studentitem_ea134da7 ON submissions_studentitem (course_id);
CREATE INDEX submissions_studentitem_82bfda79 ON submissions_studentitem (item_id);



CREATE SEQUENCE submissions_submission_seq;

CREATE TABLE submissions_submission (
  id int NOT NULL DEFAULT NEXTVAL ('submissions_submission_seq'),
  uuid char(32) NOT NULL,
  attempt_number int check (attempt_number > 0) NOT NULL,
  submitted_at timestamptz(6) NOT NULL,
  created_at timestamptz(6) NOT NULL,
  raw_answer text NOT NULL,
  student_item_id int NOT NULL,
  status varchar(1) NOT NULL,
  PRIMARY KEY (id)
 ,
  CONSTRAINT su_student_item_id_d3801ff833d05b1_fk_submissions_studentitem_id FOREIGN KEY (student_item_id) REFERENCES submissions_studentitem (id)
) ;

CREATE INDEX su_student_item_id_d3801ff833d05b1_fk_submissions_studentitem_id ON submissions_submission (student_item_id);
CREATE INDEX submissions_submission_ef7c876f ON submissions_submission (uuid);
CREATE INDEX submissions_submission_22bb6ff9 ON submissions_submission (submitted_at);
CREATE INDEX submissions_submission_fde81f11 ON submissions_submission (created_at);

CREATE SEQUENCE submissions_score_seq;

CREATE TABLE submissions_score (
  id int NOT NULL DEFAULT NEXTVAL ('submissions_score_seq'),
  points_earned int check (points_earned > 0) NOT NULL,
  points_possible int check (points_possible > 0) NOT NULL,
  created_at timestamptz(6) NOT NULL,
  reset bool NOT NULL,
  student_item_id int NOT NULL,
  submission_id int DEFAULT NULL,
  PRIMARY KEY (id)
 ,
  CONSTRAINT s_student_item_id_7d4d4bb6a7dd0642_fk_submissions_studentitem_id FOREIGN KEY (student_item_id) REFERENCES submissions_studentitem (id),
  CONSTRAINT subm_submission_id_3fc975fe88442ff7_fk_submissions_submission_id FOREIGN KEY (submission_id) REFERENCES submissions_submission (id)
) ;

CREATE INDEX submissions_score_fde81f11 ON submissions_score (created_at);
CREATE INDEX submissions_score_02d5e83e ON submissions_score (student_item_id);
CREATE INDEX submissions_score_1dd9cfcc ON submissions_score (submission_id);
CREATE SEQUENCE submissions_scoresummary_seq;

CREATE TABLE submissions_scoresummary (
  id int NOT NULL DEFAULT NEXTVAL ('submissions_scoresummary_seq'),
  highest_id int NOT NULL,
  latest_id int NOT NULL,
  student_item_id int NOT NULL,
  PRIMARY KEY (id),
  CONSTRAINT student_item_id UNIQUE  (student_item_id)
 ,
  CONSTRAINT s_student_item_id_32fa0a425a149b1b_fk_submissions_studentitem_id FOREIGN KEY (student_item_id) REFERENCES submissions_studentitem (id),
  CONSTRAINT submissions__highest_id_7fd91b8eb312c175_fk_submissions_score_id FOREIGN KEY (highest_id) REFERENCES submissions_score (id),
  CONSTRAINT submissions_s_latest_id_2b352506a35fd569_fk_submissions_score_id FOREIGN KEY (latest_id) REFERENCES submissions_score (id)
) ;

CREATE INDEX submissions__highest_id_7fd91b8eb312c175_fk_submissions_score_id ON submissions_scoresummary (highest_id);
CREATE INDEX submissions_s_latest_id_2b352506a35fd569_fk_submissions_score_id ON submissions_scoresummary (latest_id);

CREATE SEQUENCE programs_programsapiconfig_seq;

CREATE TABLE programs_programsapiconfig (
  id int NOT NULL DEFAULT NEXTVAL ('programs_programsapiconfig_seq'),
  change_date timestamptz(6) NOT NULL,
  enabled bool NOT NULL,
  changed_by_id int DEFAULT NULL,
  marketing_path varchar(255) NOT NULL,
  PRIMARY KEY (id)
 ,
  CONSTRAINT programs_programsapiconfig_changed_by_id_93e09d74_fk FOREIGN KEY (changed_by_id) REFERENCES auth_user (id)
) ;

CREATE INDEX programs_programsa_changed_by_id_b7c3b49d5c0dcd3_fk_auth_user_id ON programs_programsapiconfig (changed_by_id);



CREATE SEQUENCE credentials_credentialsapiconfig_seq;

CREATE TABLE credentials_credentialsapiconfig (
  id int NOT NULL DEFAULT NEXTVAL ('credentials_credentialsapiconfig_seq'),
  change_date timestamptz(6) NOT NULL,
  enabled bool NOT NULL,
  internal_service_url varchar(200) NOT NULL,
  public_service_url varchar(200) NOT NULL,
  enable_learner_issuance smallint NOT NULL,
  enable_studio_authoring smallint NOT NULL,
  cache_ttl int check (cache_ttl > 0) NOT NULL,
  changed_by_id int DEFAULT NULL,
  PRIMARY KEY (id)
 ,
  CONSTRAINT credentials_credentialsapiconfig_changed_by_id_9e145a81_fk FOREIGN KEY (changed_by_id) REFERENCES auth_user (id)
) ;

CREATE INDEX credentials_crede_changed_by_id_273a2e6b0649c861_fk_auth_user_id ON credentials_credentialsapiconfig (changed_by_id);


CREATE SEQUENCE student_languageproficiency_seq;

CREATE TABLE student_languageproficiency (
  id int NOT NULL DEFAULT NEXTVAL ('student_languageproficiency_seq'),
  code varchar(16) NOT NULL,
  user_profile_id int NOT NULL,
  PRIMARY KEY (id),
  CONSTRAINT student_languageproficiency_code_68e76171684c62e5_uniq UNIQUE  (code,user_profile_id)
 ,
  CONSTRAINT student__user_profile_id_283edb437b102619_fk_auth_userprofile_id FOREIGN KEY (user_profile_id) REFERENCES auth_userprofile (id)
) ;

CREATE INDEX student_languageproficiency_06037614 ON student_languageproficiency (user_profile_id);


CREATE SEQUENCE student_sociallink_seq;

CREATE TABLE student_sociallink (
  id int NOT NULL DEFAULT NEXTVAL ('student_sociallink_seq'),
  platform varchar(30) NOT NULL,
  social_link varchar(100) NOT NULL,
  user_profile_id int NOT NULL,
  PRIMARY KEY (id)
 ,
  CONSTRAINT student_s_user_profile_id_7c5a1bfd4e58b3a_fk_auth_userprofile_id FOREIGN KEY (user_profile_id) REFERENCES auth_userprofile (id)
) ;

CREATE INDEX student_s_user_profile_id_7c5a1bfd4e58b3a_fk_auth_userprofile_id ON student_sociallink (user_profile_id);



CREATE SEQUENCE entitlements_courseentitlementpolicy_seq;

CREATE TABLE entitlements_courseentitlementpolicy (
  id int NOT NULL DEFAULT NEXTVAL ('entitlements_courseentitlementpolicy_seq'),
  expiration_period bigint NOT NULL,
  refund_period bigint NOT NULL,
  regain_period bigint NOT NULL,
  site_id int DEFAULT NULL,
  mode varchar(32) DEFAULT NULL,
  PRIMARY KEY (id)
 ,
  CONSTRAINT entitlements_coursee_site_id_c7a9e107_fk_django_si FOREIGN KEY (site_id) REFERENCES django_site (id)
) ;

CREATE INDEX entitlements_courseen_site_id_5256b0e7f6e039cc_fk_django_site_id ON entitlements_courseentitlementpolicy (site_id);

CREATE SEQUENCE entitlements_courseentitlement_seq;

CREATE TABLE entitlements_courseentitlement (
  id int NOT NULL DEFAULT NEXTVAL ('entitlements_courseentitlement_seq'),
  created timestamptz(6) NOT NULL,
  modified timestamptz(6) NOT NULL,
  uuid char(32) NOT NULL,
  course_uuid char(32) NOT NULL,
  expired_at timestamptz(6) DEFAULT NULL,
  mode varchar(100) NOT NULL,
  order_number varchar(128) DEFAULT NULL,
  enrollment_course_run_id int DEFAULT NULL,
  user_id int NOT NULL,
  _policy_id int DEFAULT NULL,
  refund_locked smallint NOT NULL,
  PRIMARY KEY (id),
  CONSTRAINT entitlements_courseentitlement_uuid_a690dd005d0695b_uniq UNIQUE  (uuid)
 ,
  CONSTRAINT D2cebc0610e28b9b3a821c839e2fe01c FOREIGN KEY (_policy_id) REFERENCES entitlements_courseentitlementpolicy (id),
  CONSTRAINT entitlements_courseentitlement_user_id_a518a225_fk FOREIGN KEY (user_id) REFERENCES auth_user (id),
  CONSTRAINT fda6bce9129c5afc395658f36b9d444e FOREIGN KEY (enrollment_course_run_id) REFERENCES student_courseenrollment (id)
) ;

CREATE INDEX entitlements_courseentit_user_id_a8df050144d72f8_fk_auth_user_id ON entitlements_courseentitlement (user_id);
CREATE INDEX fda6bce9129c5afc395658f36b9d444e ON entitlements_courseentitlement (enrollment_course_run_id);
CREATE INDEX entitlements_courseentitlement_36cddc86 ON entitlements_courseentitlement (_policy_id);

CREATE SEQUENCE student_dashboardconfiguration_seq;

CREATE TABLE student_dashboardconfiguration (
  id int NOT NULL DEFAULT NEXTVAL ('student_dashboardconfiguration_seq'),
  change_date timestamptz(6) NOT NULL,
  enabled bool NOT NULL,
  recent_enrollment_time_delta int check (recent_enrollment_time_delta > 0) NOT NULL,
  changed_by_id int DEFAULT NULL,
  PRIMARY KEY (id)
 ,
  CONSTRAINT student_dashboardconfiguration_changed_by_id_1960484b_fk FOREIGN KEY (changed_by_id) REFERENCES auth_user (id)
) ;

CREATE INDEX student_dashboard_changed_by_id_4db1e1194c4ae32c_fk_auth_user_id ON student_dashboardconfiguration (changed_by_id);


CREATE SEQUENCE verify_student_softwaresecurephotoverification_seq;

CREATE TABLE verify_student_softwaresecurephotoverification (
  id int NOT NULL DEFAULT NEXTVAL ('verify_student_softwaresecurephotoverification_seq'),
  status varchar(100) NOT NULL,
  status_changed timestamptz(6) NOT NULL,
  name varchar(255) NOT NULL,
  face_image_url varchar(255) NOT NULL,
  photo_id_image_url varchar(255) NOT NULL,
  receipt_id varchar(255) NOT NULL,
  created_at timestamptz(6) NOT NULL,
  updated_at timestamptz(6) NOT NULL,
  display bool NOT NULL,
  submitted_at timestamptz(6) DEFAULT NULL,
  reviewing_service varchar(255) NOT NULL,
  error_msg text NOT NULL,
  error_code varchar(50) NOT NULL,
  photo_id_key text NOT NULL,
  copy_id_photo_from_id int DEFAULT NULL,
  reviewing_user_id int DEFAULT NULL,
  user_id int NOT NULL,
  PRIMARY KEY (id)
 ,
  CONSTRAINT D01dce17b91c9382bd80d4be23a3e0cf FOREIGN KEY (copy_id_photo_from_id) REFERENCES verify_student_softwaresecurephotoverification (id),
  CONSTRAINT verify_student_softwarese_reviewing_user_id_55fd003a_fk FOREIGN KEY (reviewing_user_id) REFERENCES auth_user (id),
  CONSTRAINT verify_student_softwarese_user_id_66ca4f6d_fk FOREIGN KEY (user_id) REFERENCES auth_user (id)
) ;

CREATE INDEX D01dce17b91c9382bd80d4be23a3e0cf ON verify_student_softwaresecurephotoverification (copy_id_photo_from_id);
CREATE INDEX verify_studen_reviewing_user_id_727fae1d0bcf8aaf_fk_auth_user_id ON verify_student_softwaresecurephotoverification (reviewing_user_id);
CREATE INDEX verify_student_software_user_id_61ffab9c12020106_fk_auth_user_id ON verify_student_softwaresecurephotoverification (user_id);
CREATE INDEX verify_student_softwaresecurephotoverification_f6fc3014 ON verify_student_softwaresecurephotoverification (receipt_id);
CREATE INDEX verify_student_softwaresecurephotoverification_fde81f11 ON verify_student_softwaresecurephotoverification (created_at);
CREATE INDEX verify_student_softwaresecurephotoverification_afd1a1a8 ON verify_student_softwaresecurephotoverification (updated_at);
CREATE INDEX verify_student_softwaresecurephotoverification_ebf78b51 ON verify_student_softwaresecurephotoverification (display);
CREATE INDEX verify_student_softwaresecurephotoverification_22bb6ff9 ON verify_student_softwaresecurephotoverification (submitted_at);


CREATE SEQUENCE verify_student_ssoverification_seq;

CREATE TABLE verify_student_ssoverification (
  id int NOT NULL DEFAULT NEXTVAL ('verify_student_ssoverification_seq'),
  status varchar(100) NOT NULL,
  status_changed timestamptz(6) NOT NULL,
  name varchar(255) NOT NULL,
  created_at timestamptz(6) NOT NULL,
  updated_at timestamptz(6) NOT NULL,
  identity_provider_type varchar(100) NOT NULL,
  identity_provider_slug varchar(30) NOT NULL,
  user_id int NOT NULL,
  PRIMARY KEY (id)
 ,
  CONSTRAINT verify_student_ssoverification_user_id_5e6186eb_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES auth_user (id)
) ;

CREATE INDEX verify_student_ssoverification_user_id_5e6186eb_fk_auth_user_id ON verify_student_ssoverification (user_id);
CREATE INDEX verify_student_ssoverification_created_at_6381e5a4 ON verify_student_ssoverification (created_at);
CREATE INDEX verify_student_ssoverification_updated_at_9d6cc952 ON verify_student_ssoverification (updated_at);
CREATE INDEX verify_student_ssoverification_identity_provider_slug_56c53eb6 ON verify_student_ssoverification (identity_provider_slug);


CREATE SEQUENCE verify_student_manualverification_seq;

CREATE TABLE verify_student_manualverification (
  id int NOT NULL DEFAULT NEXTVAL ('verify_student_manualverification_seq'),
  status varchar(100) NOT NULL,
  status_changed timestamptz(6) NOT NULL,
  name varchar(255) NOT NULL,
  created_at timestamptz(6) NOT NULL,
  updated_at timestamptz(6) NOT NULL,
  reason varchar(255) NOT NULL,
  user_id int NOT NULL,
  PRIMARY KEY (id)
 ,
  CONSTRAINT verify_student_manua_user_id_f38b72b4_fk_auth_user FOREIGN KEY (user_id) REFERENCES auth_user (id)
) ;

CREATE INDEX verify_student_manua_user_id_f38b72b4_fk_auth_user ON verify_student_manualverification (user_id);
CREATE INDEX verify_student_manualverification_created_at_e4e3731a ON verify_student_manualverification (created_at);
CREATE INDEX verify_student_manualverification_updated_at_1a350690 ON verify_student_manualverification (updated_at);

CREATE SEQUENCE lms_xblock_xblockasidesconfig_seq;

CREATE TABLE lms_xblock_xblockasidesconfig (
  id int NOT NULL DEFAULT NEXTVAL ('lms_xblock_xblockasidesconfig_seq'),
  change_date timestamptz(6) NOT NULL,
  enabled bool NOT NULL,
  disabled_blocks text NOT NULL,
  changed_by_id int DEFAULT NULL,
  PRIMARY KEY (id)
 ,
  CONSTRAINT lms_xblock_xblockasidesconfig_changed_by_id_71928be3_fk FOREIGN KEY (changed_by_id) REFERENCES auth_user (id)
) ;

CREATE INDEX lms_xblock_xblocka_changed_by_id_eabf5ef3e34dfb8_fk_auth_user_id ON lms_xblock_xblockasidesconfig (changed_by_id);



CREATE SEQUENCE courseware_dynamicupgradedeadlineconfiguration_seq;

CREATE TABLE courseware_dynamicupgradedeadlineconfiguration (
  id int NOT NULL DEFAULT NEXTVAL ('courseware_dynamicupgradedeadlineconfiguration_seq'),
  change_date timestamptz(6) NOT NULL,
  enabled smallint NOT NULL,
  deadline_days smallint check (deadline_days > 0) NOT NULL,
  changed_by_id int DEFAULT NULL,
  PRIMARY KEY (id)
 ,
  CONSTRAINT courseware_dynamicupgrade_changed_by_id_6a450e2c_fk FOREIGN KEY (changed_by_id) REFERENCES auth_user (id)
) ;

CREATE INDEX courseware_dynami_changed_by_id_77da0c73df07c112_fk_auth_user_id ON courseware_dynamicupgradedeadlineconfiguration (changed_by_id);


CREATE SEQUENCE django_comment_common_coursediscussionsettings_seq;

CREATE TABLE django_comment_common_coursediscussionsettings (
  id int NOT NULL DEFAULT NEXTVAL ('django_comment_common_coursediscussionsettings_seq'),
  course_id varchar(255) NOT NULL,
  always_divide_inline_discussions bool NOT NULL,
  divided_discussions text,
  division_scheme varchar(20) NOT NULL,
  discussions_id_map text,
  PRIMARY KEY (id),
  CONSTRAINT django_comment_common_coursediscussionsettings_course_id_ux UNIQUE  (course_id)
) ;

CREATE SEQUENCE django_comment_common_forumsconfig_seq;

CREATE TABLE django_comment_common_forumsconfig (
  id int NOT NULL DEFAULT NEXTVAL ('django_comment_common_forumsconfig_seq'),
  change_date timestamptz(6) NOT NULL,
  enabled bool NOT NULL,
  connection_timeout double precision NOT NULL,
  changed_by_id int DEFAULT NULL,
  PRIMARY KEY (id)
 ,
  CONSTRAINT django_comment_common_forumsconfig_changed_by_id_9292e296_fk FOREIGN KEY (changed_by_id) REFERENCES auth_user (id)
)  ;

ALTER SEQUENCE django_comment_common_forumsconfig_seq RESTART WITH 2;

CREATE INDEX django_comment_co_changed_by_id_18a7f46ff6309996_fk_auth_user_id ON django_comment_common_forumsconfig (changed_by_id);

CREATE SEQUENCE entitlements_courseentitlementsupportdetail_seq;

CREATE TABLE entitlements_courseentitlementsupportdetail (
  id int NOT NULL DEFAULT NEXTVAL ('entitlements_courseentitlementsupportdetail_seq'),
  created timestamptz(6) NOT NULL,
  modified timestamptz(6) NOT NULL,
  reason varchar(1) NOT NULL,
  comments text,
  entitlement_id int NOT NULL,
  support_user_id int NOT NULL,
  unenrolled_run_id varchar(255) DEFAULT NULL,
  action varchar(15) NOT NULL,
  PRIMARY KEY (id)
 ,
  CONSTRAINT b0fed354de33791839d87a8d13813a8b FOREIGN KEY (entitlement_id) REFERENCES entitlements_courseentitlement (id),
  CONSTRAINT entitlements_courseentitl_support_user_id_97d3095e_fk FOREIGN KEY (support_user_id) REFERENCES auth_user (id)
) ;

CREATE INDEX b0fed354de33791839d87a8d13813a8b ON entitlements_courseentitlementsupportdetail (entitlement_id);
CREATE INDEX entitlements_co_support_user_id_778aba40a383c157_fk_auth_user_id ON entitlements_courseentitlementsupportdetail (support_user_id);

CREATE SEQUENCE libraries_seq;

CREATE TABLE libraries (
  id INT NOT NULL DEFAULT NEXTVAL ('libraries_seq'),
  user_id INT NULL,
  name VARCHAR(450) NULL,
  description VARCHAR(2000) NULL,
  created_on TIMESTAMPTZ(0) NULL,
  key VARCHAR(450) NULL,
  PRIMARY KEY (id))
;

CREATE SEQUENCE courseware_orgdynamicupgradedeadlineconfiguration_seq;

CREATE TABLE courseware_orgdynamicupgradedeadlineconfiguration (
  id int NOT NULL DEFAULT NEXTVAL ('courseware_orgdynamicupgradedeadlineconfiguration_seq'),
  change_date timestamptz(6) NOT NULL,
  enabled bool NOT NULL,
  org_id varchar(255) NOT NULL,
  deadline_days smallint check (deadline_days > 0) NOT NULL,
  opt_out bool NOT NULL,
  changed_by_id int DEFAULT NULL,
  PRIMARY KEY (id)
 ,
  CONSTRAINT courseware_orgdynamicupgr_changed_by_id_b557a1ea_fk FOREIGN KEY (changed_by_id) REFERENCES auth_user (id)
) ;

CREATE INDEX courseware_orgdyn_changed_by_id_700576c3bbcdc12f_fk_auth_user_id ON courseware_orgdynamicupgradedeadlineconfiguration (changed_by_id);
CREATE INDEX courseware_orgdynamicupgradedeadlineconfiguration_9cf869aa ON courseware_orgdynamicupgradedeadlineconfiguration (org_id);

CREATE SEQUENCE courseware_coursedynamicupgradedeadlineconfiguration_seq;

CREATE TABLE courseware_coursedynamicupgradedeadlineconfiguration (
  id int NOT NULL DEFAULT NEXTVAL ('courseware_coursedynamicupgradedeadlineconfiguration_seq'),
  change_date timestamptz(6) NOT NULL,
  enabled bool NOT NULL,
  course_id varchar(255) NOT NULL,
  deadline_days smallint check (deadline_days > 0) NOT NULL,
  opt_out bool NOT NULL,
  changed_by_id int DEFAULT NULL,
  PRIMARY KEY (id)
 ,
  CONSTRAINT courseware_coursedynamicu_changed_by_id_2c4efc3a_fk FOREIGN KEY (changed_by_id) REFERENCES auth_user (id)
) ;

CREATE INDEX courseware_course_changed_by_id_71dd51ee4b44e9e1_fk_auth_user_id ON courseware_coursedynamicupgradedeadlineconfiguration (changed_by_id);
CREATE INDEX courseware_coursedynamicupgradedeadlineconfiguration_ea134da7 ON courseware_coursedynamicupgradedeadlineconfiguration (course_id);

CREATE SEQUENCE courseware_authors_seq;

CREATE TABLE courseware_authors (
  id INT NOT NULL DEFAULT NEXTVAL ('courseware_authors_seq'),
  user_id INT NULL,
  course_id VARCHAR(100) NULL,
  created_on TIMESTAMPTZ(0) NULL,
  PRIMARY KEY (id));

 CREATE SEQUENCE course_modes_coursemode_seq;

CREATE TABLE course_modes_coursemode (
  id int NOT NULL DEFAULT NEXTVAL ('course_modes_coursemode_seq'),
  course_id varchar(255) NOT NULL,
  mode_slug varchar(100) NOT NULL,
  mode_display_name varchar(255) NOT NULL,
  min_price int NOT NULL,
  currency varchar(8) NOT NULL,
  expiration_datetime timestamptz(6) DEFAULT NULL,
  expiration_date date DEFAULT NULL,
  suggested_prices varchar(255) NOT NULL,
  description text,
  sku varchar(255) DEFAULT NULL,
  expiration_datetime_is_explicit bool NOT NULL,
  bulk_sku varchar(255) DEFAULT NULL,
  PRIMARY KEY (id),
  CONSTRAINT course_modes_coursemode_course_id_6fbb1796ace558b4_uniq UNIQUE  (course_id,mode_slug,currency)
) ;

CREATE INDEX course_modes_coursemode_ea134da7 ON course_modes_coursemode (course_id);

CREATE SEQUENCE catalog_catalogintegration_seq;

CREATE TABLE catalog_catalogintegration (
  id int NOT NULL DEFAULT NEXTVAL ('catalog_catalogintegration_seq'),
  change_date timestamptz(6) NOT NULL,
  enabled bool NOT NULL,
  internal_api_url varchar(200) NOT NULL,
  cache_ttl int check (cache_ttl > 0) NOT NULL,
  changed_by_id int DEFAULT NULL,
  service_username varchar(100) NOT NULL,
  page_size int check (page_size > 0) NOT NULL,
  long_term_cache_ttl int check (long_term_cache_ttl > 0) NOT NULL,
  PRIMARY KEY (id)
 ,
  CONSTRAINT catalog_catalogintegration_changed_by_id_cde406de_fk FOREIGN KEY (changed_by_id) REFERENCES auth_user (id)
) ;

CREATE INDEX catalog_catalogin_changed_by_id_4c786efa531d484b_fk_auth_user_id ON catalog_catalogintegration (changed_by_id);

CREATE SEQUENCE badges_courseeventbadgesconfiguration_seq;

CREATE TABLE badges_courseeventbadgesconfiguration (
  id int NOT NULL DEFAULT NEXTVAL ('badges_courseeventbadgesconfiguration_seq'),
  change_date timestamptz(6) NOT NULL,
  enabled bool NOT NULL,
  courses_completed text NOT NULL,
  courses_enrolled text NOT NULL,
  course_groups text NOT NULL,
  changed_by_id int DEFAULT NULL,
  PRIMARY KEY (id)
 ,
  CONSTRAINT badges_courseeventbadgesconfiguration_changed_by_id_db04ed01_fk FOREIGN KEY (changed_by_id) REFERENCES auth_user (id)
) ;

CREATE INDEX badges_courseeven_changed_by_id_50986a94d73238b9_fk_auth_user_id ON badges_courseeventbadgesconfiguration (changed_by_id);

CREATE SEQUENCE student_pendingemailchange_seq;

CREATE TABLE student_pendingemailchange (
  id int NOT NULL DEFAULT NEXTVAL ('student_pendingemailchange_seq'),
  new_email varchar(255) NOT NULL,
  activation_key varchar(32) NOT NULL,
  user_id int NOT NULL,
  PRIMARY KEY (id),
  CONSTRAINT activation_key UNIQUE  (activation_key),
  CONSTRAINT student_pendingemailchange_user_id_ux UNIQUE  (user_id) ,
  CONSTRAINT student_pendingemailchange_user_id_8f2778c5_fk FOREIGN KEY (user_id) REFERENCES auth_user (id)
) ;

CREATE INDEX student_pendingemailchange_a4a65cd1 ON student_pendingemailchange (new_email);

CREATE SEQUENCE certificates_generatedcertificate_seq;

CREATE TABLE certificates_generatedcertificate (
  id int NOT NULL DEFAULT NEXTVAL ('certificates_generatedcertificate_seq'),
  course_id varchar(255) NOT NULL,
  verify_uuid varchar(32) NOT NULL,
  download_uuid varchar(32) NOT NULL,
  download_url varchar(128) NOT NULL,
  grade varchar(5) NOT NULL,
  key varchar(32) NOT NULL,
  distinction bool NOT NULL,
  status varchar(32) NOT NULL,
  mode varchar(32) NOT NULL,
  name varchar(255) NOT NULL,
  created_date timestamptz(6) NOT NULL,
  modified_date timestamptz(6) NOT NULL,
  error_reason varchar(512) NOT NULL,
  user_id int NOT NULL,
  PRIMARY KEY (id),
  CONSTRAINT certificates_generatedcertificate_user_id_552a0fa6f7d3f7e8_uniq UNIQUE  (user_id,course_id)
 ,
  CONSTRAINT certificates_generatedcertificate_user_id_54119d22_fk FOREIGN KEY (user_id) REFERENCES auth_user (id)
) ;

CREATE INDEX certificates_generatedcertific_verify_uuid_1b5a14bb83c471ff_uniq ON certificates_generatedcertificate (verify_uuid);



CREATE SEQUENCE bookmarks_xblockcache_seq;

CREATE TABLE bookmarks_xblockcache (
  id int NOT NULL DEFAULT NEXTVAL ('bookmarks_xblockcache_seq'),
  created timestamptz(6) NOT NULL,
  modified timestamptz(6) NOT NULL,
  course_key varchar(255) NOT NULL,
  usage_key varchar(255) NOT NULL,
  display_name varchar(255) NOT NULL,
  paths text NOT NULL,
  PRIMARY KEY (id),
  CONSTRAINT usage_key UNIQUE  (usage_key)
) ;

CREATE INDEX bookmarks_xblockcache_c8235886 ON bookmarks_xblockcache (course_key);


CREATE SEQUENCE bookmarks_bookmark_seq;

CREATE TABLE bookmarks_bookmark (
  id int NOT NULL DEFAULT NEXTVAL ('bookmarks_bookmark_seq'),
  created timestamptz(6) NOT NULL,
  modified timestamptz(6) NOT NULL,
  course_key varchar(255) NOT NULL,
  usage_key varchar(255) NOT NULL,
  path text NOT NULL,
  user_id int NOT NULL,
  xblock_cache_id int NOT NULL,
  PRIMARY KEY (id),
  CONSTRAINT bookmarks_bookmark_user_id_7059f67cddd52c9a_uniq UNIQUE  (user_id,usage_key)
 ,
  CONSTRAINT boo_xblock_cache_id_22d48842487ba2d2_fk_bookmarks_xblockcache_id FOREIGN KEY (xblock_cache_id) REFERENCES bookmarks_xblockcache (id),
  CONSTRAINT bookmarks_bookmark_user_id_a26bf17c_fk FOREIGN KEY (user_id) REFERENCES auth_user (id)
) ;

CREATE INDEX bookmarks_bookmark_c8235886 ON bookmarks_bookmark (course_key);
CREATE INDEX bookmarks_bookmark_4a93f0de ON bookmarks_bookmark (usage_key);
CREATE INDEX bookmarks_bookmark_d452fbf6 ON bookmarks_bookmark (xblock_cache_id);


alter table wiki_urlpath drop constraint wiki_urlpath_level_check;

CREATE SEQUENCE course_groups_coursecohortssettings_seq;

CREATE TABLE course_groups_coursecohortssettings (
  id int NOT NULL DEFAULT NEXTVAL ('course_groups_coursecohortssettings_seq'),
  is_cohorted bool NOT NULL,
  course_id varchar(255) NOT NULL,
  cohorted_discussions text,
  always_cohort_inline_discussions bool NOT NULL,
  PRIMARY KEY (id),
  CONSTRAINT course_groups_coursecohortssettings_course_id UNIQUE  (course_id)
) ;

CREATE SEQUENCE course_groups_courseusergroup_seq;

CREATE TABLE course_groups_courseusergroup (
  id int NOT NULL DEFAULT NEXTVAL ('course_groups_courseusergroup_seq'),
  name varchar(255) NOT NULL,
  course_id varchar(255) NOT NULL,
  group_type varchar(20) NOT NULL,
  PRIMARY KEY (id),
  CONSTRAINT course_groups_courseusergroup_name_63f7511804c52f38_uniq UNIQUE  (name,course_id)
) ;

CREATE INDEX course_groups_courseusergroup_ea134da7 ON course_groups_courseusergroup (course_id);

CREATE SEQUENCE bulk_email_bulkemailflag_seq;

CREATE TABLE bulk_email_bulkemailflag (
  id int NOT NULL DEFAULT NEXTVAL ('bulk_email_bulkemailflag_seq'),
  change_date timestamptz(6) NOT NULL,
  enabled bool NOT NULL,
  require_course_email_auth smallint NOT NULL,
  changed_by_id int DEFAULT NULL,
  PRIMARY KEY (id)
 ,
  CONSTRAINT bulk_email_bulkemailflag_changed_by_id_c510754b_fk FOREIGN KEY (changed_by_id) REFERENCES auth_user (id)
) ;

CREATE INDEX bulk_email_bulkem_changed_by_id_67960d6511f876aa_fk_auth_user_id ON bulk_email_bulkemailflag (changed_by_id);

CREATE SEQUENCE certificates_certificategenerationconfiguration_seq;

CREATE TABLE certificates_certificategenerationconfiguration (
  id int NOT NULL DEFAULT NEXTVAL ('certificates_certificategenerationconfiguration_seq'),
  change_date timestamptz(6) NOT NULL,
  enabled bool NOT NULL,
  changed_by_id int DEFAULT NULL,
  PRIMARY KEY (id)
 ,
  CONSTRAINT certificates_certificateg_changed_by_id_a6d06e99_fk FOREIGN KEY (changed_by_id) REFERENCES auth_user (id)
) ;

CREATE INDEX certificates_cert_changed_by_id_2a1d896cdbd5fec5_fk_auth_user_id ON certificates_certificategenerationconfiguration (changed_by_id);

CREATE SEQUENCE certificates_certificatewhitelist_seq;

CREATE TABLE certificates_certificatewhitelist (
  id int NOT NULL DEFAULT NEXTVAL ('certificates_certificatewhitelist_seq'),
  course_id varchar(255) NOT NULL,
  whitelist bool NOT NULL,
  created timestamptz(6) NOT NULL,
  notes text,
  user_id int NOT NULL,
  PRIMARY KEY (id)
 ,
  CONSTRAINT certificates_certificatewhitelist_user_id_c2ab1b7c_fk FOREIGN KEY (user_id) REFERENCES auth_user (id)
) ;

CREATE INDEX certificates_certificat_user_id_50b0bc90075a5407_fk_auth_user_id ON certificates_certificatewhitelist (user_id);

CREATE SEQUENCE certificates_certificateinvalidation_seq;

CREATE TABLE certificates_certificateinvalidation (
  id int NOT NULL DEFAULT NEXTVAL ('certificates_certificateinvalidation_seq'),
  created timestamptz(6) NOT NULL,
  modified timestamptz(6) NOT NULL,
  notes text,
  active bool NOT NULL,
  generated_certificate_id int NOT NULL,
  invalidated_by_id int NOT NULL,
  PRIMARY KEY (id)
 ,
  CONSTRAINT certificates_certificatei_invalidated_by_id_e3c101f1_fk FOREIGN KEY (invalidated_by_id) REFERENCES auth_user (id),
  CONSTRAINT fa0dc816ca8028cd93e5f2289d405d87 FOREIGN KEY (generated_certificate_id) REFERENCES certificates_generatedcertificate (id)
) ;

CREATE INDEX fa0dc816ca8028cd93e5f2289d405d87 ON certificates_certificateinvalidation (generated_certificate_id);
CREATE INDEX certificates__invalidated_by_id_5198db337fb56b7b_fk_auth_user_id ON certificates_certificateinvalidation (invalidated_by_id);

CREATE SEQUENCE instructor_task_instructortask_seq;

CREATE TABLE instructor_task_instructortask (
  id int NOT NULL DEFAULT NEXTVAL ('instructor_task_instructortask_seq'),
  task_type varchar(50) NOT NULL,
  course_id varchar(255) NOT NULL,
  task_key varchar(255) NOT NULL,
  task_input varchar(255) NOT NULL,
  task_id varchar(255) NOT NULL,
  task_state varchar(50) DEFAULT NULL,
  task_output varchar(1024) DEFAULT NULL,
  created timestamptz(6) DEFAULT NULL,
  updated timestamptz(6) NOT NULL,
  subtasks text NOT NULL,
  requester_id int NOT NULL,
  PRIMARY KEY (id)
 ,
  CONSTRAINT instructor_task_instructortask_requester_id_307f955d_fk FOREIGN KEY (requester_id) REFERENCES auth_user (id)
) ;

CREATE INDEX instructor_task_in_requester_id_3383acfe2fe42391_fk_auth_user_id ON instructor_task_instructortask (requester_id);
CREATE INDEX instructor_task_instructortask_5361aa34 ON instructor_task_instructortask (task_type);
CREATE INDEX instructor_task_instructortask_ea134da7 ON instructor_task_instructortask (course_id);
CREATE INDEX instructor_task_instructortask_a2903537 ON instructor_task_instructortask (task_key);
CREATE INDEX instructor_task_instructortask_57746cc8 ON instructor_task_instructortask (task_id);
CREATE INDEX instructor_task_instructortask_76980a94 ON instructor_task_instructortask (task_state);

CREATE SEQUENCE block_structure_config_seq;

CREATE TABLE block_structure_config (
  id int NOT NULL DEFAULT NEXTVAL ('block_structure_config_seq'),
  change_date timestamptz(6) NOT NULL,
  enabled bool NOT NULL,
  num_versions_to_keep int DEFAULT NULL,
  cache_timeout_in_seconds int DEFAULT NULL,
  changed_by_id int DEFAULT NULL,
  PRIMARY KEY (id)
 ,
  CONSTRAINT block_structure_config_changed_by_id_45af0b10_fk FOREIGN KEY (changed_by_id) REFERENCES auth_user (id)
) ;

CREATE INDEX block_structure_c_changed_by_id_1b1edef3e5767b34_fk_auth_user_id ON block_structure_config (changed_by_id);

CREATE SEQUENCE contentstore_pushnotificationconfig_seq;

CREATE TABLE contentstore_pushnotificationconfig (
  id int NOT NULL DEFAULT NEXTVAL ('contentstore_pushnotificationconfig_seq'),
  change_date timestamptz(6) NOT NULL,
  enabled bool NOT NULL,
  changed_by_id int DEFAULT NULL,
  PRIMARY KEY (id)
 ,
  CONSTRAINT contentstore_push_changed_by_id_72c47af098f7f8b1_fk_auth_user_id FOREIGN KEY (changed_by_id) REFERENCES auth_user (id)
) ;

CREATE INDEX contentstore_push_changed_by_id_72c47af098f7f8b1_fk_auth_user_id ON contentstore_pushnotificationconfig (changed_by_id);

CREATE SEQUENCE xblock_config_studioconfig_seq;

CREATE TABLE xblock_config_studioconfig (
  id int NOT NULL DEFAULT NEXTVAL ('xblock_config_studioconfig_seq'),
  change_date timestamptz(6) NOT NULL,
  enabled bool NOT NULL,
  disabled_blocks text NOT NULL,
  changed_by_id int DEFAULT NULL,
  PRIMARY KEY (id)
 ,
  CONSTRAINT xblock_config_stu_changed_by_id_58f0a899052499fd_fk_auth_user_id FOREIGN KEY (changed_by_id) REFERENCES auth_user (id)
) ;

CREATE INDEX xblock_config_stu_changed_by_id_58f0a899052499fd_fk_auth_user_id ON xblock_config_studioconfig (changed_by_id);


CREATE SEQUENCE user_tasks_usertaskstatus_seq;

CREATE TABLE user_tasks_usertaskstatus (
  id int NOT NULL DEFAULT NEXTVAL ('user_tasks_usertaskstatus_seq'),
  created timestamptz(6) NOT NULL,
  modified timestamptz(6) NOT NULL,
  uuid varchar(36) NOT NULL,
  task_id varchar(128) NOT NULL,
  is_container bool NOT NULL,
  task_class varchar(128) NOT NULL,
  name varchar(255) NOT NULL,
  state varchar(128) NOT NULL,
  completed_steps smallint check (completed_steps > 0) NOT NULL,
  total_steps smallint check (total_steps > 0) NOT NULL,
  attempts smallint check (attempts > 0) NOT NULL,
  parent_id int DEFAULT NULL,
  user_id int NOT NULL,
  PRIMARY KEY (id),
  CONSTRAINT uuid UNIQUE  (uuid),
  CONSTRAINT task_id UNIQUE  (task_id)
 ,
  CONSTRAINT user__parent_id_2a1a586c3c2ac2a4_fk_user_tasks_usertaskstatus_id FOREIGN KEY (parent_id) REFERENCES user_tasks_usertaskstatus (id),
  CONSTRAINT user_tasks_usertaskstat_user_id_5ceae753d027017b_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES auth_user (id)
) ;

CREATE INDEX user__parent_id_2a1a586c3c2ac2a4_fk_user_tasks_usertaskstatus_id ON user_tasks_usertaskstatus (parent_id);
CREATE INDEX user_tasks_usertaskstat_user_id_5ceae753d027017b_fk_auth_user_id ON user_tasks_usertaskstatus (user_id);


CREATE SEQUENCE edxval_video_seq;

CREATE TABLE edxval_video (
  id int NOT NULL DEFAULT NEXTVAL ('edxval_video_seq'),
  created timestamptz(6) NOT NULL,
  edx_video_id varchar(100) NOT NULL,
  client_video_id varchar(255) NOT NULL,
  duration double precision NOT NULL,
  status varchar(255) NOT NULL,
  PRIMARY KEY (id),
  CONSTRAINT edx_video_id UNIQUE  (edx_video_id)
) ;

CREATE INDEX edxval_video_8d63c4f7 ON edxval_video (client_video_id);
CREATE INDEX edxval_video_9acb4454 ON edxval_video (status);

alter table  user_tasks_usertaskstatus drop CONSTRAINT user_tasks_usertaskstatus_completed_steps_check;


CREATE SEQUENCE user_tasks_usertaskartifact_seq;

CREATE TABLE user_tasks_usertaskartifact (
  id int NOT NULL DEFAULT NEXTVAL ('user_tasks_usertaskartifact_seq'),
  created timestamptz(6) NOT NULL,
  modified timestamptz(6) NOT NULL,
  uuid varchar(36) NOT NULL,
  name varchar(255) NOT NULL,
  file varchar(100) DEFAULT NULL,
  url varchar(200) NOT NULL,
  "text" text NOT NULL,
  status_id int NOT NULL,
  PRIMARY KEY (id),
  CONSTRAINT user_tasks_usertaskartifact_uuid UNIQUE  (uuid)
 ,
  CONSTRAINT user__status_id_265997facac95070_fk_user_tasks_usertaskstatus_id FOREIGN KEY (status_id) REFERENCES user_tasks_usertaskstatus (id)
) ;

CREATE INDEX user_tasks_usertaskartifact_dc91ed4b ON user_tasks_usertaskartifact (status_id);


CREATE SEQUENCE contentserver_courseassetcachettlconfig_seq;

CREATE TABLE contentserver_courseassetcachettlconfig (
  id int NOT NULL DEFAULT NEXTVAL ('contentserver_courseassetcachettlconfig_seq'),
  change_date timestamptz(6) NOT NULL,
  enabled bool NOT NULL,
  cache_ttl int check (cache_ttl > 0) NOT NULL,
  changed_by_id int DEFAULT NULL,
  PRIMARY KEY (id)
 ,
  CONSTRAINT contentserver_courseasset_changed_by_id_a9213047_fk FOREIGN KEY (changed_by_id) REFERENCES auth_user (id)
) ;

CREATE INDEX contentserver_cou_changed_by_id_3b5e5ff6c6df495d_fk_auth_user_id ON contentserver_courseassetcachettlconfig (changed_by_id);

CREATE SEQUENCE edxval_videotranscript_seq;

CREATE TABLE edxval_videotranscript (
  id int NOT NULL DEFAULT NEXTVAL ('edxval_videotranscript_seq'),
  created timestamptz(6) NOT NULL,
  modified timestamptz(6) NOT NULL,
  transcript varchar(255) DEFAULT NULL,
  language_code varchar(50) NOT NULL,
  provider varchar(30) NOT NULL,
  file_format varchar(20) NOT NULL,
  video_id int DEFAULT NULL,
  PRIMARY KEY (id),
  CONSTRAINT edxval_videotranscript_video_id_729fab369c0f7028_uniq UNIQUE  (video_id,language_code)
 ,
  CONSTRAINT edxval_videotranscr_video_id_2578e231c810d058_fk_edxval_video_id FOREIGN KEY (video_id) REFERENCES edxval_video (id)
) ;

CREATE INDEX edxval_videotranscript_60716c2f ON edxval_videotranscript (language_code);
CREATE INDEX edxval_videotranscript_e1be1ad3 ON edxval_videotranscript (file_format);
CREATE INDEX edxval_videotranscript_b58b747e ON edxval_videotranscript (video_id);


CREATE SEQUENCE video_config_coursehlsplaybackenabledflag_seq;

CREATE TABLE video_config_coursehlsplaybackenabledflag (
  id int NOT NULL DEFAULT NEXTVAL ('video_config_coursehlsplaybackenabledflag_seq'),
  change_date timestamptz(6) NOT NULL,
  enabled bool NOT NULL,
  course_id varchar(255) NOT NULL,
  changed_by_id int DEFAULT NULL,
  PRIMARY KEY (id)
 ,
  CONSTRAINT video_config_coursehlspla_changed_by_id_fa268d53_fk FOREIGN KEY (changed_by_id) REFERENCES auth_user (id)
) ;

CREATE INDEX video_config_cour_changed_by_id_28b01cb29cfcd9a2_fk_auth_user_id ON video_config_coursehlsplaybackenabledflag (changed_by_id);
CREATE INDEX video_config_coursehlsplaybackenabledflag_ea134da7 ON video_config_coursehlsplaybackenabledflag (course_id);

CREATE SEQUENCE video_config_hlsplaybackenabledflag_seq;

CREATE TABLE video_config_hlsplaybackenabledflag (
  id int NOT NULL DEFAULT NEXTVAL ('video_config_hlsplaybackenabledflag_seq'),
  change_date timestamptz(6) NOT NULL,
  enabled bool NOT NULL,
  enabled_for_all_courses smallint NOT NULL,
  changed_by_id int DEFAULT NULL,
  PRIMARY KEY (id)
 ,
  CONSTRAINT video_config_hlsplaybackenabledflag_changed_by_id_d93f2234_fk FOREIGN KEY (changed_by_id) REFERENCES auth_user (id)
) ;

CREATE INDEX video_config_hlsp_changed_by_id_15b74d899e55b62b_fk_auth_user_id ON video_config_hlsplaybackenabledflag (changed_by_id);


CREATE SEQUENCE assessment_rubric_seq;

CREATE TABLE assessment_rubric (
  id int NOT NULL DEFAULT NEXTVAL ('assessment_rubric_seq'),
  content_hash varchar(40) NOT NULL,
  structure_hash varchar(40) NOT NULL,
  PRIMARY KEY (id),
  CONSTRAINT content_hash UNIQUE  (content_hash)
) ;

CREATE INDEX assessment_rubric_873e9e2d ON assessment_rubric (structure_hash);


CREATE SEQUENCE proctoring_proctoredexam_seq;

CREATE TABLE proctoring_proctoredexam (
  id int NOT NULL DEFAULT NEXTVAL ('proctoring_proctoredexam_seq'),
  created timestamptz(6) NOT NULL,
  modified timestamptz(6) NOT NULL,
  course_id varchar(255) NOT NULL,
  content_id varchar(255) NOT NULL,
  external_id varchar(255) DEFAULT NULL,
  exam_name text NOT NULL,
  time_limit_mins int NOT NULL,
  due_date timestamptz(6) DEFAULT NULL,
  is_proctored bool NOT NULL,
  is_practice_exam bool NOT NULL,
  is_active bool NOT NULL,
  hide_after_due bool NOT NULL,
  PRIMARY KEY (id),
  CONSTRAINT proctoring_proctoredexam_course_id_7d8ab189323890c0_uniq UNIQUE  (course_id,content_id)
) ;

CREATE INDEX proctoring_proctoredexam_ea134da7 ON proctoring_proctoredexam (course_id);
CREATE INDEX proctoring_proctoredexam_e14f02ad ON proctoring_proctoredexam (content_id);
CREATE INDEX proctoring_proctoredexam_0e684294 ON proctoring_proctoredexam (external_id);






CREATE SEQUENCE edxval_profile_seq;

CREATE TABLE edxval_profile (
  id int NOT NULL DEFAULT NEXTVAL ('edxval_profile_seq'),
  profile_name varchar(50) NOT NULL,
  PRIMARY KEY (id),
  CONSTRAINT profile_name UNIQUE  (profile_name)
)  ;

ALTER SEQUENCE edxval_profile_seq RESTART WITH 8;

CREATE SEQUENCE edxval_encodedvideo_seq;

CREATE TABLE edxval_encodedvideo (
  id int NOT NULL DEFAULT NEXTVAL ('edxval_encodedvideo_seq'),
  created timestamptz(6) NOT NULL,
  modified timestamptz(6) NOT NULL,
  url varchar(200) NOT NULL,
  file_size int check (file_size > 0) NOT NULL,
  bitrate int check (bitrate > 0) NOT NULL,
  profile_id int NOT NULL,
  video_id int NOT NULL,
  PRIMARY KEY (id)
 ,
  CONSTRAINT edxval_encodedv_profile_id_484a111092acafb3_fk_edxval_profile_id FOREIGN KEY (profile_id) REFERENCES edxval_profile (id),
  CONSTRAINT edxval_encodedvideo_video_id_56934bca09fc3b13_fk_edxval_video_id FOREIGN KEY (video_id) REFERENCES edxval_video (id)
) ;

CREATE INDEX edxval_encodedvideo_83a0eb3f ON edxval_encodedvideo (profile_id);
CREATE INDEX edxval_encodedvideo_b58b747e ON edxval_encodedvideo (video_id);


CREATE SEQUENCE edxval_coursevideo_seq;

CREATE TABLE edxval_coursevideo (
  id int NOT NULL DEFAULT NEXTVAL ('edxval_coursevideo_seq'),
  course_id varchar(255) NOT NULL,
  video_id int NOT NULL,
  is_hidden bool NOT NULL,
  PRIMARY KEY (id),
  CONSTRAINT edxval_coursevideo_course_id_42cecee05cff2d8c_uniq UNIQUE  (course_id,video_id)
 ,
  CONSTRAINT edxval_coursevideo_video_id_68b2969f352edd03_fk_edxval_video_id FOREIGN KEY (video_id) REFERENCES edxval_video (id)
) ;
CREATE INDEX edxval_coursevideo_b58b747e ON edxval_coursevideo (video_id);

CREATE SEQUENCE milestones_coursecontentmilestone_seq;

CREATE TABLE milestones_coursecontentmilestone (
  id int NOT NULL DEFAULT NEXTVAL ('milestones_coursecontentmilestone_seq'),
  created timestamptz(6) NOT NULL,
  modified timestamptz(6) NOT NULL,
  course_id varchar(255) NOT NULL,
  content_id varchar(255) NOT NULL,
  active bool NOT NULL,
  milestone_id int NOT NULL,
  milestone_relationship_type_id int NOT NULL,
  requirements varchar(255) DEFAULT NULL,
  PRIMARY KEY (id),
  CONSTRAINT milestones_coursecontentmileston_course_id_68d1457cd52d6dff_uniq UNIQUE  (course_id,content_id,milestone_id)
 ,
  CONSTRAINT D84e404851bc6d6b9fe0d60955e8729c FOREIGN KEY (milestone_relationship_type_id) REFERENCES milestones_milestonerelationshiptype (id),
  CONSTRAINT milesto_milestone_id_73b6eddde5b205a8_fk_milestones_milestone_id FOREIGN KEY (milestone_id) REFERENCES milestones_milestone (id)
) ;

CREATE INDEX milestones_coursecontentmilestone_ea134da7 ON milestones_coursecontentmilestone (course_id);
CREATE INDEX milestones_coursecontentmilestone_e14f02ad ON milestones_coursecontentmilestone (content_id);
CREATE INDEX milestones_coursecontentmilestone_dbb5cd1e ON milestones_coursecontentmilestone (milestone_id);
CREATE INDEX milestones_coursecontentmilestone_db6866e3 ON milestones_coursecontentmilestone (milestone_relationship_type_id);
CREATE INDEX milestones_coursecontentmilestone_active_39b5c645fa33bfee_uniq ON milestones_coursecontentmilestone (active);