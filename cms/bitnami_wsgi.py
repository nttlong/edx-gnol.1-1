"""
WSGI config for CMS.

This module contains the WSGI application used by Django's development server
and any production WSGI deployments.
It exposes a module-level variable named ``application``. Django's
``runserver`` and ``runfcgi`` commands discover this application via the
``WSGI_APPLICATION`` setting.
"""
from __future__ import absolute_import

from openedx.core.lib.logsettings import log_python_warnings
log_python_warnings()

# Patch the xml libs before anything else.
from safe_lxml import defuse_xml_libs
defuse_xml_libs()

# Disable PyContract contract checking when running as a webserver
import contracts
contracts.disable_all()

import os
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "cms.envs.bitnami")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "cms.envs.devstack")
os.environ.setdefault("SERVICE_VARIANT", "cms")
os.environ.setdefault("MYSQL_UNIX_PORT", "/opt/edx-hawthorn.2-4/mysql/tmp/mysql.sock")
# Some clouds create /etc/boto.cfg, causing 'boto' import to fail in some cases
os.environ.setdefault("BOTO_CONFIG", "")
os.environ.setdefault("CONFIG_ROOT", "/opt/edx-hawthorn.2-4/apps/edx/conf")
os.environ.setdefault("TMPDIR", "/opt/edx-hawthorn.2-4/.tmp/")


import cms.startup as startup
startup.run()

# This application object is used by the development server
# as well as any WSGI server configured to use this file.
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
