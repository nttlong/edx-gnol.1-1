# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1548073575.056781
_enable_loop = True
_template_filename = u'/home/nttlong/code/edx/apps/edx/edx-platform/common/djangoapps/pipeline_mako/templates/static_content.html'
_template_uri = u'static_content.html'
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


def render_url(context,file,raw=False):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()

        try:
            url = staticfiles_storage.url(file)
        except:
            url = file
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
        def url(file,raw=False):
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
{"source_encoding": "utf-8", "line_map": {"16": 2, "42": 1, "47": 1, "48": 26, "49": 31, "50": 39, "51": 47, "52": 64, "53": 74, "54": 83, "55": 91, "56": 122, "57": 138, "58": 165, "59": 183, "60": 212, "61": 224, "62": 229, "63": 233, "64": 237, "65": 241, "66": 245, "67": 249, "68": 253, "74": 227, "78": 227, "87": 243, "91": 243, "100": 28, "104": 28, "114": 231, "119": 231, "128": 33, "132": 33, "140": 39, "141": 39, "147": 247, "152": 247, "161": 235, "165": 235, "174": 93, "183": 93, "184": 97, "185": 98, "193": 104, "194": 107, "195": 107, "196": 108, "197": 108, "198": 112, "199": 112, "200": 115, "201": 116, "202": 116, "203": 116, "204": 116, "205": 116, "206": 117, "207": 118, "208": 118, "209": 118, "210": 119, "211": 119, "212": 120, "213": 120, "219": 214, "224": 214, "241": 66, "246": 66, "247": 67, "248": 68, "249": 68, "250": 68, "251": 69, "252": 70, "253": 71, "254": 71, "255": 71, "261": 251, "266": 251, "275": 124, "281": 124, "282": 128, "283": 129, "287": 131, "288": 132, "289": 132, "290": 133, "291": 134, "292": 135, "293": 135, "299": 81, "303": 81, "312": 140, "316": 140, "317": 149, "318": 151, "319": 151, "320": 152, "321": 152, "322": 154, "323": 154, "324": 157, "325": 157, "326": 160, "327": 160, "328": 161, "329": 161, "330": 162, "331": 162, "337": 167, "343": 167, "344": 172, "345": 173, "346": 174, "347": 174, "348": 174, "349": 176, "350": 178, "351": 178, "352": 178, "353": 178, "354": 179, "355": 179, "361": 185, "367": 185, "368": 190, "369": 193, "370": 194, "371": 195, "372": 195, "373": 195, "374": 195, "375": 196, "376": 196, "377": 199, "378": 204, "379": 204, "380": 204, "381": 205, "382": 205, "383": 205, "384": 205, "385": 206, "386": 206, "387": 210, "393": 85, "397": 85, "405": 91, "411": 239, "415": 239, "424": 49, "429": 49, "430": 50, "437": 55, "438": 57, "439": 58, "440": 58, "441": 58, "442": 59, "443": 60, "444": 61, "445": 61, "446": 61, "447": 61, "453": 41, "457": 41, "465": 47, "471": 465}, "uri": "static_content.html", "filename": "/home/nttlong/code/edx/apps/edx/edx-platform/common/djangoapps/pipeline_mako/templates/static_content.html"}
__M_END_METADATA
"""
