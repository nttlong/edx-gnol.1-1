# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1548073579.234903
_enable_loop = True
_template_filename = u'/home/nttlong/code/edx/apps/edx/edx-platform/xdj-gnol-lms-templates/widgets/footer-language-selector.html'
_template_uri = u'/widgets/footer-language-selector.html'
_source_encoding = 'utf-8'
_exports = []



from babel import Locale
from django.conf import settings
from django.utils.translation import ugettext as _

from openedx.core.djangoapps.lang_pref import COOKIE_DURATION
from openedx.core.djangoapps.lang_pref.api import released_languages
from openedx.core.djangolib.js_utils import js_escaped_string

# Make sure LANGUAGE_COOKIE is present.
if not settings.LANGUAGE_COOKIE:
    raise ValueError('settings.LANGUAGE_COOKIE is required to use footer-language-selector.')


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace(u'static', context._clean_inheritance_tokens(), templateuri=u'../x-static-content.html', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, u'static')] = ns

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        sorted = context.get('sorted', UNDEFINED)
        static = _mako_get_namespace(context, 'static')
        LANGUAGE_CODE = context.get('LANGUAGE_CODE', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n')
        __M_writer(u'\n')
        __M_writer(u'\n\n<div class="footer-language-selector">\n    <label for="footer-language-select">\n        <span class="icon fa fa-globe" aria-hidden="true"></span>\n        <span class="sr">')
        __M_writer(filters.html_escape(filters.decode.utf8(_("Choose Language"))))
        __M_writer(u'</span>\n    </label>\n    <select id="footer-language-select" name="language" onchange="footerLanguageSelector.handleSelection(this)">\n')
        for language in sorted(released_languages(), key=lambda x: x.code):
            __M_writer(u'            ')
            language_name = Locale.parse(language.code.replace('_', '-'), sep='-').language_name 
            
            __M_locals_builtin_stored = __M_locals_builtin()
            __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['language_name'] if __M_key in __M_locals_builtin_stored]))
            __M_writer(u'\n')
            if language.code == LANGUAGE_CODE:
                __M_writer(u'                <option value="')
                __M_writer(filters.html_escape(filters.decode.utf8(language.code)))
                __M_writer(u'" selected="selected">')
                __M_writer(filters.html_escape(filters.decode.utf8(language_name)))
                __M_writer(u'</option>\n')
            else:
                __M_writer(u'                <option value="')
                __M_writer(filters.html_escape(filters.decode.utf8(language.code)))
                __M_writer(u'">')
                __M_writer(filters.html_escape(filters.decode.utf8(language_name)))
                __M_writer(u'</option>\n')
        __M_writer(u'    </select>\n</div>\n\n<script type="text/javascript">\n    window.footerLanguageSelector = {\n')
        __M_writer(u"        handleSelection: function($select) {\n            this.setLanguageCookie($select.value, this.refreshPage);\n        },\n\n        setLanguageCookie: function(value, callback) {\n            var cookie = '")
        __M_writer(js_escaped_string(settings.LANGUAGE_COOKIE ))
        __M_writer(u"=' + value + ';path=/';\n\n            ")
        session_cookie_domain = static.get_value('SESSION_COOKIE_DOMAIN', settings.SESSION_COOKIE_DOMAIN) 
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['session_cookie_domain'] if __M_key in __M_locals_builtin_stored]))
        __M_writer(u'\n')
        if session_cookie_domain:
            __M_writer(u"                cookie += ';domain=")
            __M_writer(js_escaped_string(session_cookie_domain ))
            __M_writer(u"';\n")
        if COOKIE_DURATION:
            __M_writer(u"                cookie += ';max-age=")
            __M_writer(js_escaped_string(COOKIE_DURATION ))
            __M_writer(u"';\n")
        __M_writer(u'\n            document.cookie = cookie;\n\n            callback();\n        },\n\n        refreshPage: function() {\n            window.location.reload();\n        }\n    };\n</script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"16": 5, "37": 18, "40": 4, "48": 4, "49": 17, "50": 18, "51": 23, "52": 23, "53": 26, "54": 27, "55": 27, "59": 27, "60": 28, "61": 29, "62": 29, "63": 29, "64": 29, "65": 29, "66": 30, "67": 31, "68": 31, "69": 31, "70": 31, "71": 31, "72": 34, "73": 51, "74": 56, "75": 56, "76": 58, "80": 58, "81": 59, "82": 60, "83": 60, "84": 60, "85": 62, "86": 63, "87": 63, "88": 63, "89": 65, "95": 89}, "uri": "/widgets/footer-language-selector.html", "filename": "/home/nttlong/code/edx/apps/edx/edx-platform/xdj-gnol-lms-templates/widgets/footer-language-selector.html"}
__M_END_METADATA
"""
