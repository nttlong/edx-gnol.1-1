"""
Middleware for theming app

Note:
    This middleware depends on "django_sites_extensions" app
    So it must be added to INSTALLED_APPS in django settings files.
"""
from django.conf import settings

from .models import SiteTheme
from .views import get_user_preview_site_theme

__site_theme_cache__ = None
__has_load_site_theme__ = None

class CurrentSiteThemeMiddleware(object):
    """
    Middleware that sets `site_theme` attribute to request object.
    """
    def process_request(self, request):
        """
        Set the request's 'site_theme' attribute based upon the current user.
        """
        # Determine if the user has specified a preview site
        global __site_theme_cache__
        global __has_load_site_theme__
        if __has_load_site_theme__:
            request.site_theme = __site_theme_cache__
            return
        preview_site_theme = get_user_preview_site_theme(request)
        if preview_site_theme:
            site_theme = preview_site_theme
        else:
            default_theme = None
            if settings.DEFAULT_SITE_THEME:
                default_theme = SiteTheme(site=request.site, theme_dir_name=settings.DEFAULT_SITE_THEME)
            site_theme = SiteTheme.get_theme(request.site, default=default_theme)
        request.site_theme = site_theme
        __site_theme_cache__ =request.site_theme
        __has_load_site_theme__ = True
