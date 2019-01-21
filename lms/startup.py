"""
Module for code that should run during LMS startup (deprecated)
"""

import django
from django.conf import settings

# Force settings to run so that the python path is modified
settings.INSTALLED_APPS  # pylint: disable=pointless-statement


def run():
    """
    Executed during django startup

    NOTE: DO **NOT** add additional code to this method or this file! The Platform Team
          is moving all startup code to more standard locations using Django best practices.
    """
    import sys
    sys.path.append("/opt/edx-hawthorn.2-4/apps/edx/edx-platform")
    import xdj
    xdj.register_INSTALLED_APPS(True)
    django.setup()
