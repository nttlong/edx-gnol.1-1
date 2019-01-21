# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1548073577.995459
_enable_loop = True
_template_filename = u'/home/nttlong/code/edx/apps/edx/edx-platform/xdj-gnol-lms-templates/main.html'
_template_uri = u'/main.html'
_source_encoding = 'utf-8'
_exports = [u'head_extra', u'bodyclass', u'js_overrides', u'footer_extra', u'title', 'pagetitle', u'js_extra', u'marketing_hero', u'bodyextra', u'headextra', u'angular', 'login_query']


main_css = "style-main-v1" 


from branding import api as branding_api
from django.urls import reverse
from django.utils.http import urlquote_plus
from django.utils.translation import ugettext as _
from django.utils.translation import get_language_bidi
from openedx.core.djangoapps.site_configuration import helpers as configuration_helpers
from openedx.core.djangolib.js_utils import dump_js_escaped_json, js_escaped_string
from openedx.core.release import RELEASE_LINE
from pipeline_mako import render_require_js_path_overrides
import xdj


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace(u'static', context._clean_inheritance_tokens(), templateuri=u'static_content.html', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, u'static')] = ns

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        disable_window_wrap = context.get('disable_window_wrap', UNDEFINED)
        disable_courseware_js = context.get('disable_courseware_js', UNDEFINED)
        EDX_ROOT_URL = context.get('EDX_ROOT_URL', UNDEFINED)
        static = _mako_get_namespace(context, 'static')
        unicode = context.get('unicode', UNDEFINED)
        LANGUAGE_CODE = context.get('LANGUAGE_CODE', UNDEFINED)
        def angular():
            return render_angular(context._locals(__M_locals))
        disable_footer = context.get('disable_footer', UNDEFINED)
        def bodyclass():
            return render_bodyclass(context._locals(__M_locals))
        def title():
            return render_title(context._locals(__M_locals))
        self = context.get('self', UNDEFINED)
        getattr = context.get('getattr', UNDEFINED)
        def js_extra():
            return render_js_extra(context._locals(__M_locals))
        def marketing_hero():
            return render_marketing_hero(context._locals(__M_locals))
        uses_bootstrap = context.get('uses_bootstrap', UNDEFINED)
        def footer_extra():
            return render_footer_extra(context._locals(__M_locals))
        def headextra():
            return render_headextra(context._locals(__M_locals))
        uses_pattern_library = context.get('uses_pattern_library', UNDEFINED)
        hasattr = context.get('hasattr', UNDEFINED)
        def head_extra():
            return render_head_extra(context._locals(__M_locals))
        def bodyextra():
            return render_bodyextra(context._locals(__M_locals))
        disable_header = context.get('disable_header', UNDEFINED)
        def js_overrides():
            return render_js_overrides(context._locals(__M_locals))
        is_from_mobile_app = context.get('is_from_mobile_app', UNDEFINED)
        allow_iframing = context.get('allow_iframing', UNDEFINED)
        settings = context.get('settings', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n')
        __M_writer(u'\n')
        __M_writer(u'\n\n\n')
        __M_writer(u'\n')
        online_help_token = self.online_help_token() if hasattr(self, 'online_help_token') else None 
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['online_help_token'] if __M_key in __M_locals_builtin_stored]))
        __M_writer(u'\n')
        __M_writer(u'\n')

        import xdj
        xdj.apply_context(self)
        
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['xdj'] if __M_key in __M_locals_builtin_stored]))
        __M_writer(u'\n<!DOCTYPE html>\n<!--[if lte IE 9]><html class="ie ie9 lte9" lang="')
        __M_writer(filters.decode.utf8(LANGUAGE_CODE))
        __M_writer(u'" ng-app="cms"><![endif]-->\n<!--[if !IE]><!--><html lang="')
        __M_writer(filters.decode.utf8(LANGUAGE_CODE))
        __M_writer(u'" ng-app="cms"><!--<![endif]-->\n<head dir="')
        __M_writer(filters.decode.utf8(static.dir_rtl()))
        __M_writer(u'">\n    <meta charset="UTF-8">\n    <meta http-equiv="X-UA-Compatible" content="IE=edge">\n    <meta name="viewport" content="width=device-width, initial-scale=1">\n\n')
        __M_writer(u'\n')
        __M_writer(u'\n  ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'title'):
            context['self'].title(**pageargs)
        

        __M_writer(u'\n\n')
        if not allow_iframing:
            __M_writer(u'      <script type="text/javascript">\n        /* immediately break out of an iframe if coming from the marketing website */\n        (function(window) {\n          if (window.location !== window.top.location) {\n            window.top.location = window.location;\n          }\n        })(this);\n      </script>\n')
        __M_writer(u'\n  ')

        jsi18n_path = "js/i18n/{language}/djangojs.js".format(language=LANGUAGE_CODE)
        ie11_fix_path = "js/ie11_find_array.js"
          
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['jsi18n_path','ie11_fix_path'] if __M_key in __M_locals_builtin_stored]))
        __M_writer(u'\n\n')
        if getattr(settings, 'CAPTURE_CONSOLE_LOG', False):
            __M_writer(u'    <script type="text/javascript">\n      var oldOnError = window.onerror;\n      window.localStorage.setItem(\'console_log_capture\', JSON.stringify([]));\n\n      window.onerror = function (message, url, lineno, colno, error) {\n        if (oldOnError) {\n          oldOnError.apply(this, arguments);\n        }\n\n        var messages = JSON.parse(window.localStorage.getItem(\'console_log_capture\'));\n        messages.push([message, url, lineno, colno, (error || {}).stack]);\n        window.localStorage.setItem(\'console_log_capture\', JSON.stringify(messages));\n      }\n    </script>\n')
        __M_writer(u'  <script type="text/javascript" src="/lms/static/')
        __M_writer(filters.decode.utf8(jsi18n_path))
        __M_writer(u'"></script>\n  <script type="text/javascript" src="/lms/static/')
        __M_writer(filters.decode.utf8(ie11_fix_path))
        __M_writer(u'"></script>\n\n  <link rel="icon" type="image/x-icon" href="')
        __M_writer(filters.decode.utf8(static.url(static.get_value('favicon_path', settings.FAVICON_PATH))))
        __M_writer(u'" />\n  <link href="/lms/static/css/lms-style-vendor.css" rel="stylesheet" type="text/css" />\n  <link href="/lms/static/css/lms-main-v1.css" rel="stylesheet" type="text/css" />\n  <script type="text/javascript" src="/lms/static/js/lms-main_vendor.js" charset="utf-8"></script>\n  <script type="text/javascript" src="/lms/static/js/lms-application.js" charset="utf-8"></script>\n  <script type="text/javascript" src="/lms/static/bundles/commons.js" ></script>\n  ')
        def ccall(caller):
            def body():
                __M_writer = context.writer()
                return ''
            return [body]
        context.caller_stack.nextcaller = runtime.Namespace('caller', context, callables=ccall(__M_caller))
        try:
            __M_writer(filters.decode.utf8(static.css(group=u'style-vendor')))
        finally:
            context.caller_stack.nextcaller = None
        __M_writer(u'\n')
        if '/' in self.attr.main_css:
            if get_language_bidi():
                __M_writer(u'      ')

                rtl_css_file = self.attr.main_css.replace('.css', '-rtl.css')
                
                
                __M_locals_builtin_stored = __M_locals_builtin()
                __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['rtl_css_file'] if __M_key in __M_locals_builtin_stored]))
                __M_writer(u'\n      <link rel="stylesheet" href="/lms/static/')
                __M_writer(filters.decode.utf8(unicode(rtl_css_file)))
                __M_writer(u'" type="text/css" media="all" />\n')
            else:
                __M_writer(u'      <link rel="stylesheet" href="/lms/static/')
                __M_writer(filters.decode.utf8(self.attr.main_css))
                __M_writer(u'" type="text/css" media="all" />\n')
        else:
            __M_writer(u'    ')
            def ccall(caller):
                def body():
                    __M_writer = context.writer()
                    return ''
                return [body]
            context.caller_stack.nextcaller = runtime.Namespace('caller', context, callables=ccall(__M_caller))
            try:
                __M_writer(filters.decode.utf8(static.css(group=(self.attr.main_css))))
            finally:
                context.caller_stack.nextcaller = None
            __M_writer(u'\n')
        __M_writer(u'\n')
        if disable_courseware_js or uses_pattern_library:
            __M_writer(u'    ')
            def ccall(caller):
                def body():
                    __M_writer = context.writer()
                    return ''
                return [body]
            context.caller_stack.nextcaller = runtime.Namespace('caller', context, callables=ccall(__M_caller))
            try:
                __M_writer(filters.decode.utf8(static.js(group=u'base_vendor')))
            finally:
                context.caller_stack.nextcaller = None
            __M_writer(u'\n    ')
            def ccall(caller):
                def body():
                    __M_writer = context.writer()
                    return ''
                return [body]
            context.caller_stack.nextcaller = runtime.Namespace('caller', context, callables=ccall(__M_caller))
            try:
                __M_writer(filters.decode.utf8(static.js(group=u'base_application')))
            finally:
                context.caller_stack.nextcaller = None
            __M_writer(u'\n')
        else:
            __M_writer(u'    ')
            def ccall(caller):
                def body():
                    __M_writer = context.writer()
                    return ''
                return [body]
            context.caller_stack.nextcaller = runtime.Namespace('caller', context, callables=ccall(__M_caller))
            try:
                __M_writer(filters.decode.utf8(static.js(group=u'main_vendor')))
            finally:
                context.caller_stack.nextcaller = None
            __M_writer(u'\n    ')
            def ccall(caller):
                def body():
                    __M_writer = context.writer()
                    return ''
                return [body]
            context.caller_stack.nextcaller = runtime.Namespace('caller', context, callables=ccall(__M_caller))
            try:
                __M_writer(filters.decode.utf8(static.js(group=u'application')))
            finally:
                context.caller_stack.nextcaller = None
            __M_writer(u'\n')
        __M_writer(u'\n  ')
        def ccall(caller):
            def body():
                __M_writer = context.writer()
                return ''
            return [body]
        context.caller_stack.nextcaller = runtime.Namespace('caller', context, callables=ccall(__M_caller))
        try:
            __M_writer(filters.decode.utf8(static.webpack(entry=u'commons')))
        finally:
            context.caller_stack.nextcaller = None
        __M_writer(u'\n\n')
        if uses_bootstrap:
            __M_writer(u'    <script type="text/javascript" src="/lms/static/common/js/vendor/bootstrap.bundle.js"></script>\n')
        __M_writer(u'\n  <script>\n    window.baseUrl = "')
        __M_writer(js_escaped_string(settings.STATIC_URL ))
        __M_writer(u'";\n    (function (require) {\n      require.config({\n          baseUrl: window.baseUrl\n      });\n    }).call(this, require || RequireJS.require);\n  </script>\n  <script type="text/javascript" src="/lms/static/lms/js/require-config.js"></script>\n  ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'js_overrides'):
            context['self'].js_overrides(**pageargs)
        

        __M_writer(u'\n\n  ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'headextra'):
            context['self'].headextra(**pageargs)
        

        __M_writer(u'\n  ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'head_extra'):
            context['self'].head_extra(**pageargs)
        

        __M_writer(u'\n\n  ')
        runtime._include_file(context, u'/courseware/experiments.html', _template_uri)
        __M_writer(u'\n  ')
        runtime._include_file(context, u'user_metadata.html', _template_uri)
        __M_writer(u'\n  ')
        def ccall(caller):
            def body():
                __M_writer = context.writer()
                return ''
            return [body]
        context.caller_stack.nextcaller = runtime.Namespace('caller', context, callables=ccall(__M_caller))
        try:
            __M_writer(filters.decode.utf8(static.optional_include_mako(is_theming_enabled=u'True',file=u'head-extra.html')))
        finally:
            context.caller_stack.nextcaller = None
        __M_writer(u'\n\n  ')
        runtime._include_file(context, u'widgets/optimizely.html', _template_uri)
        __M_writer(u'\n  ')
        runtime._include_file(context, u'widgets/segment-io.html', _template_uri)
        __M_writer(u'\n\n  <meta name="path_prefix" content="')
        __M_writer(filters.decode.utf8(EDX_ROOT_URL))
        __M_writer(u'">\n  \n  ')
        google_site_verification_id = configuration_helpers.get_value('GOOGLE_SITE_VERIFICATION_ID', settings.GOOGLE_SITE_VERIFICATION_ID) 
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['google_site_verification_id'] if __M_key in __M_locals_builtin_stored]))
        __M_writer(u'\n')
        if google_site_verification_id:
            __M_writer(u'    <meta name="google-site-verification" content="')
            __M_writer(filters.decode.utf8(google_site_verification_id))
            __M_writer(u'" />\n')
        __M_writer(u'\n  <meta name="openedx-release-line" content="')
        __M_writer(filters.decode.utf8(RELEASE_LINE))
        __M_writer(u'" />\n\n')
        ga_acct = static.get_value("GOOGLE_ANALYTICS_ACCOUNT", settings.GOOGLE_ANALYTICS_ACCOUNT) 
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['ga_acct'] if __M_key in __M_locals_builtin_stored]))
        __M_writer(u'\n')
        if ga_acct:
            __M_writer(u'    <script type="text/javascript">\n    var _gaq = _gaq || [];\n    _gaq.push([\'_setAccount\', \'')
            __M_writer(js_escaped_string(ga_acct ))
            __M_writer(u"']);\n    _gaq.push(['_trackPageview']);\n\n    (function() {\n      var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;\n      ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';\n      var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s);\n    })();\n    </script>\n")
        __M_writer(u'\n')
        branch_key = static.get_value("BRANCH_IO_KEY", settings.BRANCH_IO_KEY) 
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['branch_key'] if __M_key in __M_locals_builtin_stored]))
        __M_writer(u'\n')
        if branch_key and not is_from_mobile_app:
            __M_writer(u'    <script type="text/javascript">\n        (function(b,r,a,n,c,h,_,s,d,k){if(!b[n]||!b[n]._q){for(;s<_.length;)c(h,_[s++]);d=r.createElement(a);d.async=1;d.src="https://cdn.branch.io/branch-latest.min.js";k=r.getElementsByTagName(a)[0];k.parentNode.insertBefore(d,k);b[n]=h}})(window,document,"script","branch",function(b,r){b[r]=function(){b._q.push([r,arguments])}},{_q:[],_v:1},"addListener applyCode banner closeBanner creditHistory credits data deepview deepviewCta first getCode init link logout redeem referrals removeListener sendSMS setBranchViewData setIdentity track validateCode".split(" "), 0);\n        branch.init(\'')
            __M_writer(js_escaped_string(branch_key ))
            __M_writer(u"');\n    </script>\n")
        __M_writer(u'<link rel="stylesheet" href="/lms/static/site.css" type="text/css" media="all" />\n<script src="/lms/static/client/angular.min.js"></script>\n<script src="/lms/static/client/ajax.js"></script>\n<script src="/lms/static/client/ui.js"></script>\n<script src="/lms/static/client/ui.directtives/ui.qTemplate.js"></script>\n<script src="/lms/static/client/ui.directtives/ui.service.ajax.js"></script>\n<script src="/lms/static/client/ui.directtives/ui.drectives.ajax.js"></script>\n<script src="/lms/static/client/ui.directtives/ui.directitive.ajax.call.js"></script>\n<script src="/lms/static/client/ui.directtives/ui.services.dialog.js"></script>\n<script src="/lms/static/client/ui.directtives/ui.bootstrap.layout.js"></script> \n</head>\n\n<body class="')
        __M_writer(filters.decode.utf8(static.dir_rtl()))
        __M_writer(u' ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'bodyclass'):
            context['self'].bodyclass(**pageargs)
        

        __M_writer(u' lang_')
        __M_writer(filters.decode.utf8(LANGUAGE_CODE))
        __M_writer(u'" ng-controller="cms">\n\n')
        def ccall(caller):
            def body():
                __M_writer = context.writer()
                return ''
            return [body]
        context.caller_stack.nextcaller = runtime.Namespace('caller', context, callables=ccall(__M_caller))
        try:
            __M_writer(filters.decode.utf8(static.optional_include_mako(is_theming_enabled=u'True',file=u'body-initial.html')))
        finally:
            context.caller_stack.nextcaller = None
        __M_writer(u'\n<div id="page-prompt"></div>\n')
        if not disable_window_wrap:
            __M_writer(u'  <div class="window-wrap" dir="')
            __M_writer(filters.decode.utf8(static.dir_rtl()))
            __M_writer(u'">\n')
        __M_writer(u'    <a class="nav-skip sr-only sr-only-focusable" href="#main">')
        __M_writer(filters.decode.utf8(_("Skip to main content")))
        __M_writer(u'</a>\n\n')
        if not disable_header:
            __M_writer(u'        ')
            runtime._include_file(context, (static.get_template_path('header.html')), _template_uri, online_help_token=online_help_token)
            __M_writer(u'\n        ')
            runtime._include_file(context, u'/preview_menu.html', _template_uri)
            __M_writer(u'\n')
        __M_writer(u'\n    ')
        runtime._include_file(context, u'/page_banner.html', _template_uri)
        __M_writer(u'\n\n    <div class="marketing-hero">')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'marketing_hero'):
            context['self'].marketing_hero(**pageargs)
        

        __M_writer(u'</div>\n\n    <div class="content-wrapper main-container" id="content">\n      ')
        __M_writer(filters.decode.utf8(self.body()))
        __M_writer(u'\n      ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'bodyextra'):
            context['self'].bodyextra(**pageargs)
        

        __M_writer(u'\n    </div>\n\n')
        if not disable_footer:
            __M_writer(u'        ')
            runtime._include_file(context, (static.get_template_path('footer.html')), _template_uri)
            __M_writer(u'\n')
        __M_writer(u'\n')
        if not disable_window_wrap:
            __M_writer(u'  </div>\n')
        __M_writer(u'\n  ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'footer_extra'):
            context['self'].footer_extra(**pageargs)
        

        __M_writer(u'\n  ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'js_extra'):
            context['self'].js_extra(**pageargs)
        

        __M_writer(u'\n\n  ')
        runtime._include_file(context, u'widgets/segment-io-footer.html', _template_uri)
        __M_writer(u'\n  <script type="text/javascript" src="/lms/static/js/vendor/noreferrer.js" charset="utf-8"></script>\n  <script type="text/javascript" src="/lms/static/js/utils/navigation.js" charset="utf-8"></script>\n  <script type="text/javascript" src="/lms/static/js/header/header.js"></script>\n  ')
        def ccall(caller):
            def body():
                __M_writer = context.writer()
                return ''
            return [body]
        context.caller_stack.nextcaller = runtime.Namespace('caller', context, callables=ccall(__M_caller))
        try:
            __M_writer(filters.decode.utf8(static.optional_include_mako(is_theming_enabled=u'True',file=u'body-extra.html')))
        finally:
            context.caller_stack.nextcaller = None
        __M_writer(u'\n<style>\n    input[type="submit"], input[type="button"], button, .button :hover {\n        background-color:none !important;\n        background-image:none !important;\n    }\n</style>\n<script src="/lms/static/boostrap/js/bootstrap.min.js"></script>\n<link href="/lms/static/boostrap/css/bootstrap.min.css" rel="stylesheet" type="text/css" />\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'angular'):
            context['self'].angular(**pageargs)
        

        __M_writer(u'\n  <script>\n    var mdl = angular.module("cms",[]);\n    var ctrl =mdl.controller("cms",["$scope",function($scope){\n       if(window.onInit){\n         window.onInit($scope);\n       }\n       \n    }])\n</script>\n</body>\n</html>\n\n')
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_head_extra(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def head_extra():
            return render_head_extra(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_bodyclass(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def bodyclass():
            return render_bodyclass(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_js_overrides(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        settings = context.get('settings', UNDEFINED)
        def js_overrides():
            return render_js_overrides(context)
        __M_writer = context.writer()
        __M_writer(u'\n    ')
        __M_writer(filters.decode.utf8(render_require_js_path_overrides(settings.REQUIRE_JS_PATH_OVERRIDES) ))
        __M_writer(u'\n  ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_footer_extra(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def footer_extra():
            return render_footer_extra(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        self = context.get('self', UNDEFINED)
        static = _mako_get_namespace(context, 'static')
        def title():
            return render_title(context)
        __M_writer = context.writer()
        __M_writer(u'\n      <title>\n       ')
        __M_writer(filters.decode.utf8(static.get_page_title_breadcrumbs(self.pagetitle())))
        __M_writer(u'\n      </title>\n  ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_pagetitle(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_js_extra(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def js_extra():
            return render_js_extra(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_marketing_hero(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def marketing_hero():
            return render_marketing_hero(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_bodyextra(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def bodyextra():
            return render_bodyextra(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_headextra(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def headextra():
            return render_headextra(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_angular(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def angular():
            return render_angular(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_login_query(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        login_redirect_url = context.get('login_redirect_url', UNDEFINED)
        request = context.get('request', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(filters.decode.utf8(
  u"?next={next}".format(
    next=urlquote_plus(login_redirect_url if login_redirect_url else request.path)
  ) if (login_redirect_url or request) else ""
))
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"514": 235, "525": 248, "16": 10, "18": 15, "531": 248, "541": 531, "38": 13, "41": 0, "82": 2, "83": 7, "84": 10, "85": 13, "86": 14, "90": 14, "91": 26, "92": 27, "99": 30, "100": 32, "101": 32, "102": 33, "103": 33, "104": 34, "105": 34, "106": 43, "107": 45, "112": 50, "113": 52, "114": 53, "115": 62, "116": 63, "123": 66, "124": 68, "125": 69, "126": 84, "127": 84, "128": 84, "129": 85, "130": 85, "131": 87, "132": 87, "140": 93, "143": 93, "144": 94, "145": 95, "146": 96, "147": 96, "153": 98, "154": 99, "155": 99, "156": 100, "157": 101, "158": 101, "159": 101, "160": 103, "161": 104, "169": 104, "172": 104, "173": 106, "174": 107, "175": 108, "183": 108, "186": 108, "194": 109, "197": 109, "198": 110, "199": 111, "207": 111, "210": 111, "218": 112, "221": 112, "222": 114, "230": 115, "233": 115, "234": 117, "235": 119, "236": 121, "237": 123, "238": 123, "243": 133, "248": 135, "253": 136, "254": 138, "255": 138, "256": 139, "257": 139, "265": 140, "268": 140, "269": 142, "270": 142, "271": 143, "272": 143, "273": 145, "274": 145, "275": 147, "279": 147, "280": 148, "281": 149, "282": 149, "283": 149, "284": 151, "285": 152, "286": 152, "287": 154, "291": 154, "292": 155, "293": 156, "294": 158, "295": 158, "296": 168, "297": 169, "301": 169, "302": 170, "303": 171, "304": 173, "305": 173, "306": 176, "307": 188, "308": 188, "313": 188, "314": 188, "315": 188, "323": 190, "326": 190, "327": 192, "328": 193, "329": 193, "330": 193, "331": 195, "332": 195, "333": 195, "334": 197, "335": 198, "336": 198, "337": 198, "338": 199, "339": 199, "340": 201, "341": 202, "342": 202, "347": 204, "348": 207, "349": 207, "354": 208, "355": 211, "356": 212, "357": 212, "358": 212, "359": 214, "360": 215, "361": 216, "362": 218, "367": 219, "372": 220, "373": 222, "374": 222, "382": 226, "385": 226, "390": 235, "391": 252, "397": 136, "408": 188, "419": 131, "426": 131, "427": 132, "428": 132, "434": 219, "445": 46, "453": 46, "454": 48, "455": 48, "461": 45, "470": 220, "481": 204, "492": 208, "503": 135}, "uri": "/main.html", "filename": "/home/nttlong/code/edx/apps/edx/edx-platform/xdj-gnol-lms-templates/main.html"}
__M_END_METADATA
"""
