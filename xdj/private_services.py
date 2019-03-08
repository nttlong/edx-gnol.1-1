#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Every service just serve for this package please put here
"""


def __find_url_by_pattern__(urls, pattern):


    """
        Find url in urls by url pattern recursive with full structured tree, example:
        ── Home
            │         ├── register
            │         │        ├── complete
            │         │
            │         │        ...
            │         │
            │         │
            │         ├── login
            │         ├── catalogs
    :param urls:
    :param pattern:
    :return:
    """


    for x in urls:
        if x.regex.pattern == pattern:
            return x
        elif hasattr(x, "url_patterns"):
            ret = __find_url_by_pattern__(x.url_patterns, pattern)
            if ret:
                return ret


def __load_installed_apps__():
    """
    Load apps.json file into list of string which will be appended the list of applications to django.conf.settings.INSTALLED_APPS
    Tải tập tin apps.json vào danh sách chuỗi sẽ được thêm vào danh sách các ứng dụng vào django.conf.sinstall.INSTALLED_APPS
    :return:
    """
    import json
    import os
    file_of_isntalled_apps_config = os.sep.join([os.path.dirname(__file__), "config", "apps.json"])
    with open(file_of_isntalled_apps_config, 'r') as data_file:
        data = json.loads(data_file.read())
        from django.conf import settings
        settings.INSTALLED_APPS.extend(data)


def __load_middle_ware__():
    """
    Load middleware.json and parse into list of string. The list of middleware will be append to django.conf.settings.MIDDLEWARE_CLASSES
    Tải tệp middleware.json và phân tích thành danh sách chuỗi. Danh sách các phần mềm trung gian sẽ được thêm vào django.conf.sinstall.MIDDLEWARE_CLASSES
    :return:
    """
    import json
    import os
    file_of_middle_ware_config = os.sep.join([os.path.dirname(__file__), "config", "middleware.json"])
    with open(file_of_middle_ware_config, 'r') as data_file:
        from django.conf import settings
        data = json.loads(data_file.read())
        from django.conf import settings
        settings.MIDDLEWARE_CLASSES.extend(data)


def __apply_settings__():
    """
    This method just serve for Openedx nothing more.
    https://openedx.atlassian.net/wiki/spaces/AC/pages/34734726/edX+Feature+Flags
    :return:
    """
    from django.conf import settings
    setattr(settings,"USE_DJANGO_PIPELINE",True)
    """
    http://django-pipeline.readthedocs.org/ – whatever version we specify in our requirements.txt
    """
    setattr(settings,"DISPLAY_DEBUG_INFO_TO_STAFF",True)
    """For large courses this slows down courseware access for staff."""
    setattr(settings,"MILESTONES_APP",True)


def __load_config__():
    """
    Load data.json file where database configuration was declared and rebuild all django.conf.settings.DATABASE['default']
    Tải tệp data.json nơi cấu hình cơ sở dữ liệu được khai báo và xây dựng lại tất cả django.conf.settings.DATABASE ['default']
    :return:
    """
    import json
    import os
    file_of_data_config = os.sep.join([os.path.dirname(__file__), "config", "data.json"])
    with open(file_of_data_config, 'r') as data_file:
        from django.conf import settings
        data = json.loads(data_file.read())
        settings.DATABASES['default']['ENGINE'] = data["sql"]["engine"]
        settings.DATABASES['default']['NAME'] = data["sql"]["name"]
        settings.DATABASES['default']['PORT'] = data["sql"]["port"]
        settings.DATABASES['default']['HOST'] = data["sql"]["host"]
        settings.DATABASES['default']['USER'] = data["sql"]["user"]
        settings.DATABASES['default']['PASSWORD'] = data["sql"]["password"]

        settings.DATABASES["read_replica"]['ENGINE'] = data["sql"]["engine"]
        settings.DATABASES["read_replica"]['NAME'] = data["sql"]["name"]
        settings.DATABASES["read_replica"]['PORT'] = data["sql"]["port"]
        settings.DATABASES["read_replica"]['HOST'] = data["sql"]["host"]
        settings.DATABASES["read_replica"]['USER'] = data["sql"]["user"]
        settings.DATABASES["read_replica"]['PASSWORD'] = data["sql"]["password"]

        settings.DATABASES['student_module_history']['ENGINE'] = data["sql"]["engine"]
        settings.DATABASES['student_module_history']['NAME'] = data["sql"]["name"]
        settings.DATABASES['student_module_history']['PORT'] = data["sql"]["port"]
        settings.DATABASES['student_module_history']['HOST'] = data["sql"]["host"]
        settings.DATABASES['student_module_history']['USER'] = data["sql"]["user"]
        settings.DATABASES['student_module_history']['PASSWORD'] = data["sql"]["password"]

        settings.CONTENTSTORE["DOC_STORE_CONFIG"]["db"] = data["mongo"]["name"]
        settings.CONTENTSTORE["DOC_STORE_CONFIG"]["host"] = data["mongo"]["host"]
        settings.CONTENTSTORE["DOC_STORE_CONFIG"]["user"] = data["mongo"]["user"]
        settings.CONTENTSTORE["DOC_STORE_CONFIG"]["password"] = data["mongo"]["password"]
        settings.CONTENTSTORE["DOC_STORE_CONFIG"]["port"] = data["mongo"]["port"]

        settings.CONTENTSTORE["OPTIONS"]["db"] = data["mongo"]["name"]
        settings.CONTENTSTORE["OPTIONS"]["host"] = data["mongo"]["host"]
        settings.CONTENTSTORE["OPTIONS"]["user"] = data["mongo"]["user"]
        settings.CONTENTSTORE["OPTIONS"]["password"] = data["mongo"]["password"]
        settings.CONTENTSTORE["OPTIONS"]["port"] = data["mongo"]["port"]

        settings.DOC_STORE_CONFIG["db"] = data["mongo"]["name"]
        settings.DOC_STORE_CONFIG["host"] = data["mongo"]["host"]
        settings.DOC_STORE_CONFIG["user"] = data["mongo"]["user"]
        settings.DOC_STORE_CONFIG["password"] = data["mongo"]["password"]
        settings.DOC_STORE_CONFIG["port"] = data["mongo"]["port"]

        settings.MODULESTORE["default"]["OPTIONS"]["stores"][0]["DOC_STORE_CONFIG"]["db"] = data["mongo"]["name"]
        settings.MODULESTORE["default"]["OPTIONS"]["stores"][0]["DOC_STORE_CONFIG"]["host"] = data["mongo"]["host"]
        settings.MODULESTORE["default"]["OPTIONS"]["stores"][0]["DOC_STORE_CONFIG"]["user"] = data["mongo"]["user"]
        settings.MODULESTORE["default"]["OPTIONS"]["stores"][0]["DOC_STORE_CONFIG"]["password"] = data["mongo"]["password"]
        settings.MODULESTORE["default"]["OPTIONS"]["stores"][0]["DOC_STORE_CONFIG"]["port"] = data["mongo"]["port"]

        settings.MODULESTORE["default"]["OPTIONS"]["stores"][1]["DOC_STORE_CONFIG"]["db"] = data["mongo"]["name"]
        settings.MODULESTORE["default"]["OPTIONS"]["stores"][1]["DOC_STORE_CONFIG"]["host"] = data["mongo"]["host"]
        settings.MODULESTORE["default"]["OPTIONS"]["stores"][1]["DOC_STORE_CONFIG"]["user"] = data["mongo"]["user"]
        settings.MODULESTORE["default"]["OPTIONS"]["stores"][1]["DOC_STORE_CONFIG"]["password"] = data["mongo"]["password"]
        settings.MODULESTORE["default"]["OPTIONS"]["stores"][1]["DOC_STORE_CONFIG"]["port"] = data["mongo"]["port"]


def __load_models__():
    """
    Load models.json file where django model was declared and rebuild django.conf.settings
    Tải tập tin model.json nơi django model được khai báo và xây dựng lại django.conf.sinstall
    :return:
    """
    import json
    import os
    file_of_models_config = os.sep.join([os.path.dirname(__file__), "config", "models.json"])
    with open(file_of_models_config, 'r') as data_file:
        from django.conf import settings
        data = json.loads(data_file.read())
        for item in data:
            if settings.INSTALLED_APPS.count(item) ==0:
                settings.INSTALLED_APPS.append(item)


def __load_settings__(for_lms):

    """
    Load settings.json file and rebuild django.conf.settings
    Tải tập tin settings.json và xây dựng lại django.conf.settingss
    :param for_lms:
    :return:
    """

    from django.conf import settings
    import json
    import os
    import logging
    logger = logging.getLogger(__name__)
    logger.info("load settings")

    file_of_settings_config = os.sep.join([os.path.dirname(__file__), "config", "settings.json"])
    with open(file_of_settings_config, 'r') as data_file:

        data = json.loads(data_file.read())
        logger.info(data)
        for k,v in data.items():
            setattr(settings,k,v)
        if data.has_key("MAKO_TEMPLATE_DIRS_BASE"):
            r = settings.REPO_ROOT
            for x in data["MAKO_TEMPLATE_DIRS_BASE"]:
                import path
                import os
                settings.TEMPLATES[0]['DIRS'].append(path.Path(os.sep.join([r,x])))
                settings.TEMPLATES[1]['DIRS'].append(path.Path(os.sep.join([r,x])))

    import path
    if data.has_key("STATIC_ROOT"):
        settings.STATIC_ROOT = path.path(data["STATIC_ROOT"])
        p = [x for x in settings.STATICFILES_DIRS if
             x.__str__()[x.__str__().__len__() - "/lms/static".__len__():] not in ["/lms/static", "/cms/static"]]
        settings.STATICFILES_DIRS = p
    if for_lms:
        if hasattr(settings,"LMS_TEMPLATE"):
            x = os.sep.join([settings.REPO_ROOT, "lms","templates"])
            settings.MAKO_TEMPLATE_DIRS_BASE = [p for p in settings.MAKO_TEMPLATE_DIRS_BASE if p.__str__() != x]
            settings.MAKO_TEMPLATE_DIRS_BASE.append(settings.LMS_TEMPLATE)
            settings.DEFAULT_TEMPLATE_ENGINE_DIRS=settings.MAKO_TEMPLATE_DIRS_BASE
            settings.TEMPLATES[0]['DIRS'] = settings.MAKO_TEMPLATE_DIRS_BASE
            settings.TEMPLATES[1]['DIRS'] = settings.MAKO_TEMPLATE_DIRS_BASE
    else:
        if hasattr(settings,"CMS_TEMPLATE"):
            x = os.sep.join([settings.REPO_ROOT, "cms", "templates"])
            settings.MAKO_TEMPLATE_DIRS_BASE = [p for p in settings.MAKO_TEMPLATE_DIRS_BASE if p.__str__() != x]
            settings.MAKO_TEMPLATE_DIRS_BASE.append(settings.CMS_TEMPLATE)
            settings.DEFAULT_TEMPLATE_ENGINE_DIRS=settings.MAKO_TEMPLATE_DIRS_BASE
            settings.TEMPLATES[0]['DIRS'] = settings.MAKO_TEMPLATE_DIRS_BASE
            settings.TEMPLATES[1]['DIRS'] = settings.MAKO_TEMPLATE_DIRS_BASE
    settings.WEBPACK_LOADER["DEFAULT"]["STATS_FILE"] = settings.WEBPACK_LOADER["DEFAULT"]["STATS_FILE"].replace(",/",
                                                                                                                "/")

    return None


def __load_email_settings__():
    try:
        import json
        import os
        import sys
        file_of_settings_config = os.sep.join([os.path.dirname(__file__), "config", "email.json"])
        with open(file_of_settings_config, 'r') as data_file:
            from django.conf import settings
            data = json.loads(data_file.read())
            settings.EMAIL_HOST = data['host']
            settings.EMAIL_HOST_USER = data['user']
            settings.EMAIL_HOST_PASSWORD = data['password']
            settings.EMAIL_USE_TLS = data["tsl"]
            settings.EMAIL_PORT = data["port"]
            settings.EMAIL_FILE_PATH = data["path"]
            settings.SERVER_EMAIL = data["email"]
            settings.DEFAULT_FROM_EMAIL =data["email"]
            settings.CONTACT_EMAIL = data["contact_email"]
            settings.API_ACCESS_FROM_EMAIL = data["email"]
            settings.API_ACCESS_MANAGER_EMAIL = data["email"]
            settings.BUGS_EMAIL = data["email"]
            settings.BULK_EMAIL_DEFAULT_FROM_EMAIL = data["email"]
            settings.FEEDBACK_SUBMISSION_EMAIL =data["email"]
    except Exception as ex:
        from xdj.errors import LoadConfigError
        raise LoadConfigError(file_of_settings_config,ex.message,ex)


def __load_forum_config__():
    import json
    import os
    import sys
    file_of_forum_config = os.sep.join([os.path.dirname(__file__), "config", "forum.json"])
    with open(file_of_forum_config, 'r') as data_file:
        from django.conf import settings
        data = json.loads(data_file.read())
        """
        "COMMENTS_SERVICE_KEY": "9198a36ca5349defcc6ecc1d3235390bd47a",
        "COMMENTS_SERVICE_URL": "http://localhost:18080"
        """
        settings.COMMENTS_SERVICE_KEY = data['key']
        settings.COMMENTS_SERVICE_URL = data['url']


def __load_feature_settings__():
    import json
    import os
    import sys
    file_of_feature_config = os.sep.join([os.path.dirname(__file__), "config", "feature.json"])
    with open(file_of_feature_config, 'r') as data_file:
        from django.conf import settings
        data = json.loads(data_file.read())
        for k,v in data.items():
            settings.FEATURES.update({
                k:v
            })


def __load_elastic_search_config__():
    import json
    import os
    import sys
    file_of_elasticsearch_config = os.sep.join([os.path.dirname(__file__), "config", "elastic_search.json"])
    with open(file_of_elasticsearch_config, 'r') as data_file:
        from django.conf import settings
        data = json.loads(data_file.read())
        settings.ELASTIC_SEARCH_CONFIG=data
