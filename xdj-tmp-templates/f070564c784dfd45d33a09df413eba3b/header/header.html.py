# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1548073578.077268
_enable_loop = True
_template_filename = u'/home/nttlong/code/edx/apps/edx/edx-platform/xdj-gnol-lms-templates/header/header.html'
_template_uri = u'/header/header.html'
_source_encoding = 'utf-8'
_exports = [u'js_extra', u'navigation_top']



from django.urls import reverse
from django.utils.translation import ugettext as _

from lms.djangoapps.ccx.overrides import get_current_ccx
from openedx.core.djangolib.markup import HTML, Text

# App that handles subdomain specific branding
from branding import api as branding_api
from openedx.core.djangoapps.lang_pref.api import header_language_selector_is_enabled, released_languages



def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace(u'static', context._clean_inheritance_tokens(), templateuri=u'../x-static-content.html', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, u'static')] = ns

    ns = runtime.TemplateNamespace('__anon_0x7f0c349e93d0', context._clean_inheritance_tokens(), templateuri=u'../main.html', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7f0c349e93d0')] = ns

def render_body(context,online_help_token,use_cookie_banner=False,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(use_cookie_banner=use_cookie_banner,pageargs=pageargs,online_help_token=online_help_token)
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f0c349e93d0')._populate(_import_ns, [u'login_query'])
        csrf_token = _import_ns.get('csrf_token', context.get('csrf_token', UNDEFINED))
        settings = _import_ns.get('settings', context.get('settings', UNDEFINED))
        def navigation_top():
            return render_navigation_top(context._locals(__M_locals))
        len = _import_ns.get('len', context.get('len', UNDEFINED))
        course = _import_ns.get('course', context.get('course', UNDEFINED))
        def js_extra():
            return render_js_extra(context._locals(__M_locals))
        static = _mako_get_namespace(context, 'static')
        user = _import_ns.get('user', context.get('user', UNDEFINED))
        LANGUAGE_CODE = _import_ns.get('LANGUAGE_CODE', context.get('LANGUAGE_CODE', UNDEFINED))
        uses_pattern_library = _import_ns.get('uses_pattern_library', context.get('uses_pattern_library', UNDEFINED))
        __M_writer = context.writer()
        __M_writer(u'\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n')
        __M_writer(u'\n')
        __M_writer(u'\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'navigation_top'):
            context['self'].navigation_top(**pageargs)
        

        __M_writer(u'\n\n')
        if uses_pattern_library:
            __M_writer(u'    ')
            if 'parent' not in context._data or not hasattr(context._data['parent'], 'js_extra'):
                context['self'].js_extra(**pageargs)
            

            __M_writer(u'\n')
        __M_writer(u'\n<header class="global-header ')
        __M_writer(filters.html_escape(filters.decode.utf8('slim' if course else '')))
        __M_writer(u'" style="overflow: visible;">\n')
        if use_cookie_banner:
            __M_writer(u'        ')
            __M_writer(filters.html_escape(filters.decode.utf8(static.renderReact(
            component="CookiePolicyBanner",
            id="cookie-policy-banner",
            props={}
        ))))
            __M_writer(u'\n')
        __M_writer(u'    <div class="main-header">\n        ')
        runtime._include_file(context, u'navbar-logo-header.html', _template_uri, online_help_token=online_help_token)
        __M_writer(u'\n        <div class="hamburger-menu" role="button" aria-label=')
        __M_writer(filters.html_escape(filters.decode.utf8(_("Options Menu"))))
        __M_writer(u' aria-expanded="false" aria-controls="mobile-menu" tabindex="0">\n            <span class="line"></span>\n            <span class="line"></span>\n            <span class="line"></span>\n            <span class="line"></span>\n        </div>\n')
        if user.is_authenticated:
            __M_writer(u'            ')
            runtime._include_file(context, u'navbar-authenticated.html', _template_uri, online_help_token=online_help_token)
            __M_writer(u'\n')
        else:
            __M_writer(u'            ')
            runtime._include_file(context, u'navbar-not-authenticated.html', _template_uri, online_help_token=online_help_token)
            __M_writer(u'\n')
        __M_writer(u'       \n        ')
        runtime._include_file(context, u'select_languages.html', _template_uri)
        __M_writer(u'\n    </div>\n    <div class="mobile-menu hidden" aria-label=')
        __M_writer(filters.html_escape(filters.decode.utf8(_("More Options"))))
        __M_writer(u' role="menu" id="mobile-menu"></div>\n    \n</header>\n\n')
        if course:
            __M_writer(u'<!--[if lte IE 9]>\n<div class="ie-banner" aria-hidden="true">')
            __M_writer(filters.html_escape(filters.decode.utf8(Text(_('{begin_strong}Warning:{end_strong} Your browser is not fully supported. We strongly recommend using {chrome_link} or {ff_link}.')).format(
    begin_strong=HTML('<strong>'),
    end_strong=HTML('</strong>'),
    chrome_link=HTML('<a href="https://www.google.com/chrome" target="_blank">Chrome</a>'),
    ff_link=HTML('<a href="http://www.mozilla.org/firefox" target="_blank">Firefox</a>'),
))))
            __M_writer(u'</div>\n<![endif]-->\n')
        __M_writer(u'\n')
        if settings.FEATURES.get('ENABLE_COOKIE_CONSENT', False):
            __M_writer(u'  ')
            runtime._include_file(context, u'../widgets/cookie-consent.html', _template_uri)
            __M_writer(u'\n')
        __M_writer(u'\n')
        if header_language_selector_is_enabled():
            __M_writer(u'    ')
            languages = released_languages() 
            
            __M_locals_builtin_stored = __M_locals_builtin()
            __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['languages'] if __M_key in __M_locals_builtin_stored]))
            __M_writer(u'\n')
            if len(languages) > 1:
                __M_writer(u'       \n        <form action="/i18n/setlang/" method="post" class="settings-language-form" id="language-settings-form">\n            <input type="hidden" id="csrf_token" name="csrfmiddlewaretoken" value="')
                __M_writer(filters.html_escape(filters.decode.utf8(csrf_token)))
                __M_writer(u'">\n            \n')
                if user.is_authenticated:
                    __M_writer(u'                <input title="preference api" type="hidden" class="url-endpoint" value="')
                    __M_writer(filters.html_escape(filters.decode.utf8(reverse('preferences_api', kwargs={'username': user.username}))))
                    __M_writer(u'" data-user-is-authenticated="true">\n')
                else:
                    __M_writer(u'                <input title="session update url" type="hidden" class="url-endpoint" value="')
                    __M_writer(filters.html_escape(filters.decode.utf8(reverse('session_language'))))
                    __M_writer(u'" data-user-is-authenticated="false">\n')
                __M_writer(u'            <label><span class="sr">')
                __M_writer(filters.html_escape(filters.decode.utf8(_("Choose Language"))))
                __M_writer(u'</span>\n                \n            <select class="input select language-selector" id="settings-language-value" name="language">\n')
                for language in languages:
                    if language[0] == LANGUAGE_CODE:
                        __M_writer(u'                        <option value="')
                        __M_writer(filters.html_escape(filters.decode.utf8(language[0])))
                        __M_writer(u'" selected="selected">')
                        __M_writer(filters.html_escape(filters.decode.utf8(language[1])))
                        __M_writer(u'</option>\n')
                    else:
                        __M_writer(u'                        <option value="')
                        __M_writer(filters.html_escape(filters.decode.utf8(language[0])))
                        __M_writer(u'" >')
                        __M_writer(filters.html_escape(filters.decode.utf8(language[1])))
                        __M_writer(u'</option>\n')
                __M_writer(u'            </select>\n            </label>\n        </form>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_js_extra(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f0c349e93d0')._populate(_import_ns, [u'login_query'])
        def js_extra():
            return render_js_extra(context)
        static = _mako_get_namespace(context, 'static')
        __M_writer = context.writer()
        __M_writer(u'\n    ')
        def ccall(caller):
            def body():
                __M_writer = context.writer()
                __M_writer(u'\n    HeaderFactory();\n    ')
                return ''
            return [body]
        context.caller_stack.nextcaller = runtime.Namespace('caller', context, callables=ccall(__M_caller))
        try:
            __M_writer(filters.html_escape(filters.decode.utf8(static.require_module(class_name=u'HeaderFactory',module_name=u'js/header_factory'))))
        finally:
            context.caller_stack.nextcaller = None
        __M_writer(u'\n    ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_navigation_top(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f0c349e93d0')._populate(_import_ns, [u'login_query'])
        def navigation_top():
            return render_navigation_top(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"16": 7, "36": 5, "39": 6, "42": 3, "61": 2, "62": 3, "63": 5, "64": 6, "65": 18, "70": 21, "71": 24, "72": 25, "77": 29, "78": 31, "79": 32, "80": 32, "81": 33, "82": 34, "83": 34, "88": 38, "89": 40, "90": 41, "91": 41, "92": 42, "93": 42, "94": 48, "95": 49, "96": 49, "97": 49, "98": 50, "99": 51, "100": 51, "101": 51, "102": 53, "103": 54, "104": 54, "105": 56, "106": 56, "107": 60, "108": 61, "109": 62, "115": 67, "116": 70, "117": 71, "118": 72, "119": 72, "120": 72, "121": 74, "122": 75, "123": 76, "124": 76, "128": 76, "129": 77, "130": 78, "131": 80, "132": 80, "133": 82, "134": 83, "135": 83, "136": 83, "137": 84, "138": 85, "139": 85, "140": 85, "141": 87, "142": 87, "143": 87, "144": 90, "145": 91, "146": 92, "147": 92, "148": 92, "149": 92, "150": 92, "151": 93, "152": 94, "153": 94, "154": 94, "155": 94, "156": 94, "157": 97, "163": 25, "172": 25, "176": 26, "181": 26, "184": 28, "190": 21, "203": 190}, "uri": "/header/header.html", "filename": "/home/nttlong/code/edx/apps/edx/edx-platform/xdj-gnol-lms-templates/header/header.html"}
__M_END_METADATA
"""
