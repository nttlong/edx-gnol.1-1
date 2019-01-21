# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1548073574.916078
_enable_loop = True
_template_filename = u'/home/nttlong/code/edx/apps/edx/edx-platform/xdj-gnol-lms-templates/x-static-content.html'
_template_uri = u'x-static-content.html'
_source_encoding = 'utf-8'
_exports = ['get_page_title_breadcrumbs', 'is_request_in_themed_site', 'marketing_link', 'get_platform_name', 'url', 'get_tech_support_email_address', 'get_value', 'studiofrontend', 'optional_include_mako', 'js', 'get_contact_email_address', 'webpack', 'dir_rtl', 'renderReact', 'require_module', 'require_module_async', 'include', 'get_template_path', 'css', 'certificate_asset_url']



import logging
import json
from django.contrib.staticfiles.storage import staticfiles_storage
from pipeline_mako import compressed_css, compressed_js
from pipeline_mako.helpers.studiofrontend import load_sfe_i18n_messages
from django.utils.translation import get_language_bidi
from mako.exceptions import TemplateLookupException
from edxmako.shortcuts import marketing_link
import xdj
from openedx.core.djangolib.js_utils import js_escaped_string, dump_js_escaped_json
from openedx.core.djangolib.markup import HTML
from openedx.core.djangoapps.site_configuration.helpers import (
  page_title_breadcrumbs,
  get_value,
)

from openedx.core.djangoapps.theming.helpers import (
  get_template_path,
  is_request_in_themed_site,
)
from lms.djangoapps.certificates.api import get_asset_url_by_slug
from webpack_loader.templatetags.webpack_loader import render_bundle
logger = logging.getLogger(__name__)


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        __M_writer(u'\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_get_page_title_breadcrumbs(context,*args):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()

        return page_title_breadcrumbs(*args)
        
        
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_is_request_in_themed_site(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()

        return is_request_in_themed_site()
        
        
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_marketing_link(context,name):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()

        link = marketing_link(name)
        return "/" if link == "#" else link
        
        
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_get_platform_name(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        settings = context.get('settings', UNDEFINED)
        __M_writer = context.writer()

        return get_value('platform_name', settings.PLATFORM_NAME)
        
        
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_url(context,file,raw=True):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()

        xdj.debugTemplate(file)
        print "/lms/static/"+file
        return "/lms/static/"+file
        try:
            url = "staticfiles_storage.url(file)"
        except:
            url = "file"
        ## HTML-escaping must be handled by caller
        
        
        __M_writer(filters.decode.utf8(url ))
        __M_writer(filters.html_escape(filters.decode.utf8("?raw" if raw else "")))
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_get_tech_support_email_address(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        settings = context.get('settings', UNDEFINED)
        __M_writer = context.writer()

        return get_value('email_from_address', settings.TECH_SUPPORT_EMAIL)
        
        
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_get_value(context,val_name,default=None,**kwargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()

        return get_value(val_name, default=default, **kwargs)
        
        
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_studiofrontend(context,entry):
    __M_caller = context.caller_stack._push_frame()
    try:
        def url(file,raw=True):
            return render_url(context,file,raw)
        capture = context.get('capture', UNDEFINED)
        caller = context.get('caller', UNDEFINED)
        settings = context.get('settings', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n    ')
        __M_writer(u'\n    ')

        body = capture(caller.body)
        body_dict = json.loads(body)
        locale = body_dict['lang']
        
        messages = load_sfe_i18n_messages(locale)
            
        
        __M_writer(u'\n    <script type="application/json" id="SFE_i18n_data">\n      {\n        "locale": "')
        __M_writer(filters.decode.utf8( locale ))
        __M_writer(u'",\n        "messages": ')
        __M_writer(filters.decode.utf8( messages ))
        __M_writer(u'\n      }\n    </script>\n    <script type="application/javascript" id=\'courseContext\'>\n        var studioContext = ')
        __M_writer(filters.decode.utf8( body ))
        __M_writer(u';\n    </script>\n    <div id="root" class="SFE"></div>\n')
        if settings.STUDIO_FRONTEND_CONTAINER_URL:
            __M_writer(u'        <script type="text/javascript" src="')
            __M_writer(filters.html_escape(filters.decode.utf8(settings.STUDIO_FRONTEND_CONTAINER_URL)))
            __M_writer(u'/')
            __M_writer(filters.html_escape(filters.decode.utf8(entry)))
            __M_writer(u'.js"></script>\n')
        else:
            __M_writer(u'        <script type="text/javascript" src="')
            __M_writer(filters.html_escape(filters.decode.utf8(url('common/js/vendor/runtime.min.js'))))
            __M_writer(u'"></script>\n        <script type="text/javascript" src="')
            __M_writer(filters.html_escape(filters.decode.utf8(url('common/js/vendor/common.min.js'))))
            __M_writer(u'"></script>\n        <script type="text/javascript" src="')
            __M_writer(filters.html_escape(filters.decode.utf8(url('common/js/vendor/{}.min.js'.format(entry)))))
            __M_writer(u'"></script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_optional_include_mako(context,file,is_theming_enabled=False):
    __M_caller = context.caller_stack._push_frame()
    try:
        self = context.get('self', UNDEFINED)
        __M_writer = context.writer()

# http://stackoverflow.com/q/21219531
        if is_theming_enabled:
            file = get_template_path(file)
        try:
            tmpl = self.get_template(file)
        except TemplateLookupException:
            pass
        else:
            tmpl.render_context(context)
        
        
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_js(context,group):
    __M_caller = context.caller_stack._push_frame()
    try:
        settings = context.get('settings', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n')
        if settings.PIPELINE_ENABLED:
            __M_writer(u'    ')
            __M_writer(filters.decode.utf8(compressed_js(group) ))
            __M_writer(u'\n')
        else:
            for filename in settings.PIPELINE_JS[group]['source_filenames']:
                __M_writer(u'      <script type="text/javascript" src="')
                __M_writer(filters.html_escape(filters.decode.utf8(staticfiles_storage.url(filename.replace('.coffee', '.js')))))
                __M_writer(u'"></script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_get_contact_email_address(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        settings = context.get('settings', UNDEFINED)
        __M_writer = context.writer()

        return get_value('email_from_address', settings.CONTACT_EMAIL)
        
        
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_webpack(context,entry,extension=None,config='DEFAULT',attrs=''):
    __M_caller = context.caller_stack._push_frame()
    try:
        capture = context.get('capture', UNDEFINED)
        caller = context.get('caller', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n    ')
        __M_writer(u'\n    ')

        body = capture(caller.body)
            
        
        __M_writer(u'\n    ')
        __M_writer(filters.html_escape(filters.decode.utf8(HTML(render_bundle(entry, extension=None, config='DEFAULT', attrs=attrs)))))
        __M_writer(u'\n')
        if body:
            __M_writer(u'      <script type="text/javascript">\n        ')
            __M_writer(filters.decode.utf8(body ))
            __M_writer(u'\n      </script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_dir_rtl(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()

        return 'rtl' if get_language_bidi() else 'ltr'
        
        
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_renderReact(context,component,id,props={}):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        __M_writer(u'\n    ')
        __M_writer(u'\n\n    ')
        __M_writer(filters.html_escape(filters.decode.utf8(HTML(render_bundle(component)))))
        __M_writer(u'\n    ')
        __M_writer(filters.html_escape(filters.decode.utf8(HTML(render_bundle('ReactRenderer')))))
        __M_writer(u'\n\n    <div id="')
        __M_writer(filters.html_escape(filters.decode.utf8(id)))
        __M_writer(u'"></div>\n    <script type="text/javascript">\n      var c;\n      try { c = ')
        __M_writer(filters.decode.utf8(component ))
        __M_writer(u"; } catch (e) { c = null; }\n      new ReactRenderer({\n        component: c,\n        selector: '#")
        __M_writer(filters.decode.utf8(id ))
        __M_writer(u"',\n        componentName: '")
        __M_writer(js_escaped_string(component ))
        __M_writer(u"',\n        props: ")
        __M_writer(dump_js_escaped_json(props ))
        __M_writer(u'\n      });\n    </script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_require_module(context,module_name,class_name):
    __M_caller = context.caller_stack._push_frame()
    try:
        caller = context.get('caller', UNDEFINED)
        settings = context.get('settings', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n    ')
        __M_writer(u'\n')
        if not settings.REQUIRE_DEBUG:
            __M_writer(u'      <script type="text/javascript" src="')
            __M_writer(filters.html_escape(filters.decode.utf8(staticfiles_storage.url(module_name + '.js') + '?raw')))
            __M_writer(u'"></script>\n')
        __M_writer(u'    <script type="text/javascript">\n        (function (require) {\n            require([\'')
        __M_writer(js_escaped_string(module_name ))
        __M_writer(u"'], function (")
        __M_writer(filters.decode.utf8(class_name ))
        __M_writer(u') {\n                ')
        __M_writer(filters.decode.utf8(caller.body() ))
        __M_writer(u'\n            });\n        }).call(this, require || RequireJS.require);\n    </script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_require_module_async(context,module_name,class_name):
    __M_caller = context.caller_stack._push_frame()
    try:
        caller = context.get('caller', UNDEFINED)
        settings = context.get('settings', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n  ')
        __M_writer(u'\n  <script type="text/javascript">\n    (function (require) {\n')
        if settings.REQUIRE_DEBUG:
            __M_writer(u"          (function (require) {\n              require(['")
            __M_writer(js_escaped_string(module_name ))
            __M_writer(u"'], function (")
            __M_writer(filters.decode.utf8(class_name ))
            __M_writer(u') {\n                  ')
            __M_writer(filters.decode.utf8(caller.body() ))
            __M_writer(u'\n              });\n          }).call(this, require || RequireJS.require);\n')
        else:
            __M_writer(u"        require(['")
            __M_writer(js_escaped_string(staticfiles_storage.url(module_name + ".js") + "?raw" ))
            __M_writer(u"'], function () {\n          require(['")
            __M_writer(js_escaped_string(module_name ))
            __M_writer(u"'], function (")
            __M_writer(filters.decode.utf8(class_name ))
            __M_writer(u') {\n            ')
            __M_writer(filters.decode.utf8(caller.body() ))
            __M_writer(u'\n          });\n        });\n')
        __M_writer(u'    }).call(this, require || RequireJS.require);\n  </script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_include(context,path):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()

        from django.conf import settings
        from django.template.engine import Engine
        from django.template.loaders.filesystem import Loader
        engine = Engine(dirs=settings.DEFAULT_TEMPLATE_ENGINE['DIRS'])
        source, template_path = Loader(engine).load_template_source(path)
        
        
        __M_writer(filters.decode.utf8(source ))
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_get_template_path(context,relative_path,**kwargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()

        return get_template_path(relative_path, **kwargs)
        
        
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_css(context,group,raw=False):
    __M_caller = context.caller_stack._push_frame()
    try:
        settings = context.get('settings', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n  ')

        rtl_group = '{}-rtl'.format(group)
        
        if get_language_bidi() and rtl_group in settings.PIPELINE_CSS:
          group = rtl_group
          
        
        __M_writer(u'\n\n')
        if settings.PIPELINE_ENABLED:
            __M_writer(u'    ')
            __M_writer(filters.decode.utf8(compressed_css(group, raw=raw) ))
            __M_writer(u'\n')
        else:
            for filename in settings.PIPELINE_CSS[group]['source_filenames']:
                __M_writer(u'      <link rel="stylesheet" href="')
                __M_writer(filters.html_escape(filters.decode.utf8(staticfiles_storage.url(filename.replace('.scss', '.css')))))
                __M_writer(filters.html_escape(filters.decode.utf8("?raw" if raw else "")))
                __M_writer(u'" type="text/css" media="all" / >\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_certificate_asset_url(context,slug):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()

        try:
            url = get_asset_url_by_slug(slug)
        except:
            url = ''
        ## HTML-escaping must be handled by caller
        
        
        __M_writer(filters.decode.utf8(url ))
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"16": 2, "42": 1, "47": 1, "48": 26, "49": 31, "50": 42, "51": 50, "52": 67, "53": 77, "54": 86, "55": 94, "56": 125, "57": 141, "58": 168, "59": 186, "60": 215, "61": 227, "62": 232, "63": 236, "64": 240, "65": 244, "66": 248, "67": 252, "68": 256, "74": 230, "78": 230, "87": 246, "91": 246, "100": 28, "104": 28, "114": 234, "119": 234, "128": 33, "132": 33, "143": 42, "144": 42, "150": 250, "155": 250, "164": 238, "168": 238, "177": 96, "186": 96, "187": 100, "188": 101, "196": 107, "197": 110, "198": 110, "199": 111, "200": 111, "201": 115, "202": 115, "203": 118, "204": 119, "205": 119, "206": 119, "207": 119, "208": 119, "209": 120, "210": 121, "211": 121, "212": 121, "213": 122, "214": 122, "215": 123, "216": 123, "222": 217, "227": 217, "244": 69, "249": 69, "250": 70, "251": 71, "252": 71, "253": 71, "254": 72, "255": 73, "256": 74, "257": 74, "258": 74, "264": 254, "269": 254, "278": 127, "284": 127, "285": 131, "286": 132, "290": 134, "291": 135, "292": 135, "293": 136, "294": 137, "295": 138, "296": 138, "302": 84, "306": 84, "315": 143, "319": 143, "320": 152, "321": 154, "322": 154, "323": 155, "324": 155, "325": 157, "326": 157, "327": 160, "328": 160, "329": 163, "330": 163, "331": 164, "332": 164, "333": 165, "334": 165, "340": 170, "346": 170, "347": 175, "348": 176, "349": 177, "350": 177, "351": 177, "352": 179, "353": 181, "354": 181, "355": 181, "356": 181, "357": 182, "358": 182, "364": 188, "370": 188, "371": 193, "372": 196, "373": 197, "374": 198, "375": 198, "376": 198, "377": 198, "378": 199, "379": 199, "380": 202, "381": 207, "382": 207, "383": 207, "384": 208, "385": 208, "386": 208, "387": 208, "388": 209, "389": 209, "390": 213, "396": 88, "400": 88, "408": 94, "414": 242, "418": 242, "427": 52, "432": 52, "433": 53, "440": 58, "441": 60, "442": 61, "443": 61, "444": 61, "445": 62, "446": 63, "447": 64, "448": 64, "449": 64, "450": 64, "456": 44, "460": 44, "468": 50, "474": 468}, "uri": "x-static-content.html", "filename": "/home/nttlong/code/edx/apps/edx/edx-platform/xdj-gnol-lms-templates/x-static-content.html"}
__M_END_METADATA
"""
