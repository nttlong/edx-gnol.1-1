DO $$
DECLARE
   lms_site_dev text := '0.0.0.0:8000';
   cms_site_dev text := '0.0.0.0:8001';
   /*
      change lms_site value into your domain ex:lms_site:='suredx.net'
   */
   lms_site text := 'localhost';
   cms_site text :='localhost:18010'



BEGIN
    insert into django_site(domain,name) values(lms_site_dev,'lms_dev');
    insert into django_site(domain,name) values(cms_site_dev,'cms_dev');
    insert into django_site(domain,name) values(lms_site,'lms_dev');
    insert into django_site(domain,name) values(cms_site,'cms_dev');


END $$;

