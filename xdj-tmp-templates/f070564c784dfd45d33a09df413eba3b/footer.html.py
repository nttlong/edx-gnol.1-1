# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1548073579.201314
_enable_loop = True
_template_filename = u'/home/nttlong/code/edx/apps/edx/edx-platform/xdj-gnol-lms-templates/footer.html'
_template_uri = u'/footer.html'
_source_encoding = 'utf-8'
_exports = []



from django.urls import reverse
from django.utils.translation import ugettext as _
from branding.api import get_footer
from openedx.core.djangoapps.lang_pref.api import footer_language_selector_is_enabled


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
        include_dependencies = context.get('include_dependencies', UNDEFINED)
        uses_bootstrap = context.get('uses_bootstrap', UNDEFINED)
        settings = context.get('settings', UNDEFINED)
        footer_css_urls = context.get('footer_css_urls', UNDEFINED)
        getattr = context.get('getattr', UNDEFINED)
        static = _mako_get_namespace(context, 'static')
        bidi = context.get('bidi', UNDEFINED)
        enumerate = context.get('enumerate', UNDEFINED)
        is_secure = context.get('is_secure', UNDEFINED)
        hide_openedx_link = context.get('hide_openedx_link', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n')
        __M_writer(u'\n')
        footer = get_footer(is_secure=is_secure) 
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['footer'] if __M_key in __M_locals_builtin_stored]))
        __M_writer(u'\n')
        __M_writer(u'\n\n')
        if uses_bootstrap:
            __M_writer(u'  <div class="container-fluid wrapper-footer">\n    <footer>\n      <div class="row">\n        <div class="col-md-9">\n          <nav class="navbar site-nav navbar-expand-sm" aria-label="')
            __M_writer(filters.html_escape(filters.decode.utf8(_('About'))))
            __M_writer(u'">\n            <ul class="navbar-nav">\n')
            for item_num, link in enumerate(footer['navigation_links'], start=1):
                __M_writer(u'                <li class="nav-item">\n                  <a class="nav-link" href="')
                __M_writer(filters.html_escape(filters.decode.utf8(link['url'])))
                __M_writer(u'">')
                __M_writer(filters.html_escape(filters.decode.utf8(link['title'])))
                __M_writer(u'</a>\n                </li>\n')
            __M_writer(u'            </ul>\n          </nav>\n\n')
            __M_writer(u'          <p class="copyright">')
            __M_writer(filters.html_escape(filters.decode.utf8(footer['copyright'])))
            __M_writer(u' ')
            __M_writer(filters.html_escape(filters.decode.utf8(u" | {icp}".format(icp=getattr(settings,'ICP_LICENSE')) if getattr(settings,'ICP_LICENSE',False) else "")))
            __M_writer(u'</p>\n\n          <nav class="navbar legal-nav navbar-expand-sm" aria-label="')
            __M_writer(filters.html_escape(filters.decode.utf8(_('Legal'))))
            __M_writer(u'">\n            <ul class="navbar-nav">\n')
            for item_num, link in enumerate(footer['legal_links'], start=1):
                __M_writer(u'                <li class="nav-item">\n                  <a class="nav-link" href="')
                __M_writer(filters.html_escape(filters.decode.utf8(link['url'])))
                __M_writer(u'">')
                __M_writer(filters.html_escape(filters.decode.utf8(link['title'])))
                __M_writer(u'</a>\n                </li>\n')
            __M_writer(u'              <li class="nav-item">\n                <a class="nav-link" href="')
            __M_writer(filters.html_escape(filters.decode.utf8(footer['edx_org_link']['url'])))
            __M_writer(u'">')
            __M_writer(filters.html_escape(filters.decode.utf8(footer['edx_org_link']['text'])))
            __M_writer(u'</a>\n              </li>\n            </ul>\n          </nav>\n        </div>\n        <div class="col-md-3">\n')
            if not hide_openedx_link:
                __M_writer(u'            <div class="footer-about-openedx">\n              <p>\n                <a href="')
                __M_writer(filters.html_escape(filters.decode.utf8(footer['openedx_link']['url'])))
                __M_writer(u'">\n                  <img src="')
                __M_writer(filters.html_escape(filters.decode.utf8(footer['openedx_link']['image'])))
                __M_writer(u'" alt="')
                __M_writer(filters.html_escape(filters.decode.utf8(footer['openedx_link']['title'])))
                __M_writer(u'" width="140" />\n                </a>\n              </p>\n            </div>\n')
            __M_writer(u'        </div>\n      </div>\n    </footer>\n  </div>\n')
        else:
            __M_writer(u'  <div class="wrapper wrapper-footer">\n    <footer id="footer-openedx" class="grid-container"\n')
            if bidi:
                __M_writer(u'        dir=')
                __M_writer(filters.html_escape(filters.decode.utf8(bidi)))
                __M_writer(u'\n')
            __M_writer(u'    >\n      <div class="colophon">\n        <nav class="nav-colophon" aria-label="')
            __M_writer(filters.html_escape(filters.decode.utf8(_('About'))))
            __M_writer(u'">\n          <ol>\n')
            for item_num, link in enumerate(footer['navigation_links'], start=1):
                __M_writer(u'              <li class="nav-colophon-0')
                __M_writer(filters.html_escape(filters.decode.utf8(item_num)))
                __M_writer(u'">\n                <a id="')
                __M_writer(filters.html_escape(filters.decode.utf8(link['name'])))
                __M_writer(u'" href="')
                __M_writer(filters.html_escape(filters.decode.utf8(link['url'])))
                __M_writer(u'">')
                __M_writer(filters.html_escape(filters.decode.utf8(link['title'])))
                __M_writer(u'</a>\n              </li>\n')
            __M_writer(u'          </ol>\n        </nav>\n\n')
            if context.get('include_language_selector', footer_language_selector_is_enabled()):
                __M_writer(u'            ')
                runtime._include_file(context, (static.get_template_path('widgets/footer-language-selector.html')), _template_uri)
                __M_writer(u'\n')
            __M_writer(u'\n        <div class="wrapper-logo">\n          <p>\n            <a href="/">\n')
            __M_writer(u'              <!--<img alt="organization logo" src="')
            __M_writer(filters.html_escape(filters.decode.utf8(footer['logo_image'])))
            __M_writer(u'">-->\n              <img alt="organization logo" src="/lms')
            __M_writer(filters.html_escape(filters.decode.utf8(static.url('logo.footer.png'))))
            __M_writer(u'">\n            </a>\n          </p>\n        </div>\n\n')
            __M_writer(u'        <p class="copyright">')
            __M_writer(filters.html_escape(filters.decode.utf8(footer['copyright'])))
            __M_writer(u' ')
            __M_writer(filters.html_escape(filters.decode.utf8(u" | {icp}".format(icp=getattr(settings,'ICP_LICENSE')) if getattr(settings,'ICP_LICENSE',False) else "")))
            __M_writer(u'</p>\n\n        <nav class="nav-legal" aria-label="')
            __M_writer(filters.html_escape(filters.decode.utf8(_('Legal'))))
            __M_writer(u'">\n          <ul>\n')
            for item_num, link in enumerate(footer['legal_links'], start=1):
                __M_writer(u'              <li class="nav-legal-0')
                __M_writer(filters.html_escape(filters.decode.utf8(item_num)))
                __M_writer(u'">\n                <a href="')
                __M_writer(filters.html_escape(filters.decode.utf8(link['url'])))
                __M_writer(u'">')
                __M_writer(filters.html_escape(filters.decode.utf8(link['title'])))
                __M_writer(u'</a>\n              </li>\n')
            __M_writer(u'            <li><a href="')
            __M_writer(filters.html_escape(filters.decode.utf8(footer['edx_org_link']['url'])))
            __M_writer(u'">')
            __M_writer(filters.html_escape(filters.decode.utf8(footer['edx_org_link']['text'])))
            __M_writer(u'</a></li>\n          </ul>\n        </nav>\n      </div>\n\n')
            if not hide_openedx_link:
                __M_writer(u'      <div class="footer-about-openedx">\n        <p>\n          <a href="')
                __M_writer(filters.html_escape(filters.decode.utf8(footer['openedx_link']['url'])))
                __M_writer(u'">\n            <img src="')
                __M_writer(filters.html_escape(filters.decode.utf8(footer['openedx_link']['image'])))
                __M_writer(u'" alt="')
                __M_writer(filters.html_escape(filters.decode.utf8(footer['openedx_link']['title'])))
                __M_writer(u'" width="140" />\n          </a>\n        </p>\n      </div>\n')
            __M_writer(u'    </footer>\n  </div>\n')
        if include_dependencies:
            __M_writer(u'  ')
            def ccall(caller):
                def body():
                    __M_writer = context.writer()
                    return ''
                return [body]
            context.caller_stack.nextcaller = runtime.Namespace('caller', context, callables=ccall(__M_caller))
            try:
                __M_writer(filters.html_escape(filters.decode.utf8(static.js(group=u'base_vendor'))))
            finally:
                context.caller_stack.nextcaller = None
            __M_writer(u'\n  ')
            def ccall(caller):
                def body():
                    __M_writer = context.writer()
                    return ''
                return [body]
            context.caller_stack.nextcaller = runtime.Namespace('caller', context, callables=ccall(__M_caller))
            try:
                __M_writer(filters.html_escape(filters.decode.utf8(static.css(group=u'style-vendor'))))
            finally:
                context.caller_stack.nextcaller = None
            __M_writer(u'\n  ')
            runtime._include_file(context, u'widgets/segment-io.html', _template_uri)
            __M_writer(u'\n  ')
            runtime._include_file(context, u'widgets/segment-io-footer.html', _template_uri)
            __M_writer(u'\n')
        if footer_css_urls:
            for url in footer_css_urls:
                __M_writer(u'    <link rel="stylesheet" type="text/css" href="')
                __M_writer(filters.html_escape(filters.decode.utf8(url)))
                __M_writer(u'"></link>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"16": 3, "30": 10, "33": 2, "48": 2, "49": 8, "50": 9, "54": 9, "55": 10, "56": 12, "57": 13, "58": 17, "59": 17, "60": 19, "61": 20, "62": 21, "63": 21, "64": 21, "65": 21, "66": 24, "67": 28, "68": 28, "69": 28, "70": 28, "71": 28, "72": 30, "73": 30, "74": 32, "75": 33, "76": 34, "77": 34, "78": 34, "79": 34, "80": 37, "81": 38, "82": 38, "83": 38, "84": 38, "85": 48, "86": 49, "87": 51, "88": 51, "89": 52, "90": 52, "91": 52, "92": 52, "93": 57, "94": 61, "95": 62, "96": 67, "97": 68, "98": 68, "99": 68, "100": 70, "101": 72, "102": 72, "103": 74, "104": 75, "105": 75, "106": 75, "107": 76, "108": 76, "109": 76, "110": 76, "111": 76, "112": 76, "113": 79, "114": 82, "115": 83, "116": 83, "117": 83, "118": 85, "119": 96, "120": 96, "121": 96, "122": 97, "123": 97, "124": 103, "125": 103, "126": 103, "127": 103, "128": 103, "129": 105, "130": 105, "131": 107, "132": 108, "133": 108, "134": 108, "135": 109, "136": 109, "137": 109, "138": 109, "139": 112, "140": 112, "141": 112, "142": 112, "143": 112, "144": 121, "145": 122, "146": 124, "147": 124, "148": 125, "149": 125, "150": 125, "151": 125, "152": 130, "153": 133, "154": 134, "162": 134, "165": 134, "173": 135, "176": 135, "177": 136, "178": 136, "179": 137, "180": 137, "181": 139, "182": 140, "183": 141, "184": 141, "185": 141, "191": 185}, "uri": "/footer.html", "filename": "/home/nttlong/code/edx/apps/edx/edx-platform/xdj-gnol-lms-templates/footer.html"}
__M_END_METADATA
"""
