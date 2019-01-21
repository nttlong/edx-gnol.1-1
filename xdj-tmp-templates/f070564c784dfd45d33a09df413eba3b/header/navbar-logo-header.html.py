# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1548073578.099874
_enable_loop = True
_template_filename = u'/home/nttlong/code/edx/apps/edx/edx-platform/xdj-gnol-lms-templates/header/navbar-logo-header.html'
_template_uri = u'/header/navbar-logo-header.html'
_source_encoding = 'utf-8'
_exports = [u'navigation_logo']



from django.urls import reverse
from django.utils.translation import ugettext as _
from lms.djangoapps.ccx.overrides import get_current_ccx
from openedx.core.djangoapps.site_configuration import helpers as configuration_helpers

# App that handles subdomain specific branding
from branding import api as branding_api


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace(u'static', context._clean_inheritance_tokens(), templateuri=u'/x-static-content.html', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, u'static')] = ns

def render_body(context,online_help_token,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs,online_help_token=online_help_token)
        settings = context.get('settings', UNDEFINED)
        enable_enterprise_sidebar = context.get('enable_enterprise_sidebar', UNDEFINED)
        course = context.get('course', UNDEFINED)
        static = _mako_get_namespace(context, 'static')
        def navigation_logo():
            return render_navigation_logo(context._locals(__M_locals))
        is_secure = context.get('is_secure', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n')
        __M_writer(u'\n\n<h1 class="header-logo">\n  <a href="')
        __M_writer(filters.html_escape(filters.decode.utf8(branding_api.get_home_url())))
        __M_writer(u'">\n    ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'navigation_logo'):
            context['self'].navigation_logo(**pageargs)
        

        __M_writer(u'\n  </a>\n')
        if course:
            __M_writer(u'    <div class="course-header">\n      <span class="provider">')
            __M_writer(filters.html_escape(filters.decode.utf8(course.display_org_with_default)))
            __M_writer(u':</span>\n      <span class="course-number">')
            __M_writer(filters.html_escape(filters.decode.utf8(course.display_number_with_default)))
            __M_writer(u'</span>\n      ')

            display_name = course.display_name_with_default
            if settings.FEATURES.get('CUSTOM_COURSES_EDX', False):
              ccx = get_current_ccx(course.id)
              if ccx:
                display_name = ccx.display_name
            
            
            __M_locals_builtin_stored = __M_locals_builtin()
            __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['display_name','ccx'] if __M_key in __M_locals_builtin_stored]))
            __M_writer(u'\n      <span class="course-name">')
            __M_writer(filters.html_escape(filters.decode.utf8(display_name)))
            __M_writer(u'</span>\n    </div>\n')
        __M_writer(u'</h1>\n')
        if enable_enterprise_sidebar:
            __M_writer(u'  <div class="enterprise-tagline">\n    ')
            tagline = configuration_helpers.get_value('ENTERPRISE_TAGLINE', settings.ENTERPRISE_TAGLINE) 
            
            __M_locals_builtin_stored = __M_locals_builtin()
            __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['tagline'] if __M_key in __M_locals_builtin_stored]))
            __M_writer(u'\n')
            if tagline:
                __M_writer(u'      ')
                __M_writer(filters.html_escape(filters.decode.utf8(tagline)))
                __M_writer(u'\n')
            __M_writer(u'  </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_navigation_logo(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        is_secure = context.get('is_secure', UNDEFINED)
        static = _mako_get_namespace(context, 'static')
        def navigation_logo():
            return render_navigation_logo(context)
        __M_writer = context.writer()
        __M_writer(u'\n    <!--<img  class="logo" src="')
        __M_writer(filters.html_escape(filters.decode.utf8(branding_api.get_logo_url(is_secure))))
        __M_writer(u'" alt="')
        __M_writer(filters.html_escape(filters.decode.utf8(_("{platform_name} Home Page").format(platform_name=static.get_platform_name()))))
        __M_writer(u'"/>-->\n    <img  class="logo" src="')
        __M_writer(filters.html_escape(filters.decode.utf8(static.url('logo.png'))))
        __M_writer(u'" alt="')
        __M_writer(filters.html_escape(filters.decode.utf8(_("{platform_name} Home Page").format(platform_name=static.get_platform_name()))))
        __M_writer(u'"/>\n    ')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"16": 6, "33": 5, "36": 3, "48": 2, "49": 3, "50": 5, "51": 14, "52": 17, "53": 17, "58": 21, "59": 23, "60": 24, "61": 25, "62": 25, "63": 26, "64": 26, "65": 27, "75": 33, "76": 34, "77": 34, "78": 37, "79": 38, "80": 39, "81": 40, "85": 40, "86": 41, "87": 42, "88": 42, "89": 42, "90": 44, "96": 18, "104": 18, "105": 19, "106": 19, "107": 19, "108": 19, "109": 20, "110": 20, "111": 20, "112": 20, "118": 112}, "uri": "/header/navbar-logo-header.html", "filename": "/home/nttlong/code/edx/apps/edx/edx-platform/xdj-gnol-lms-templates/header/navbar-logo-header.html"}
__M_END_METADATA
"""
