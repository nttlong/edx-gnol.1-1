# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1548073579.09327
_enable_loop = True
_template_filename = u'/home/nttlong/code/edx/apps/edx/edx-platform/xdj-gnol-lms-templates/courseware/tabs.html'
_template_uri = '/courseware/tabs.html'
_source_encoding = 'utf-8'
_exports = []



from django.utils.translation import ugettext as _
from django.urls import reverse


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace(u'static', context._clean_inheritance_tokens(), templateuri=u'/x-static-content.html', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, u'static')] = ns

def render_body(context,tab_list,active_page,default_tab,tab_image,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(tab_list=tab_list,pageargs=pageargs,default_tab=default_tab,tab_image=tab_image,active_page=active_page)
        course = context.get('course', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n')
        __M_writer(u'\n')
        __M_writer(u'\n')
        __M_writer(u'\n\n')

        def url_class(is_active):
          if is_active:
            return "active"
          return ""
        
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['url_class'] if __M_key in __M_locals_builtin_stored]))
        __M_writer(u'\n')
        for tab in tab_list:
            __M_writer(u'  ')

            tab_is_active = tab.tab_id in (active_page, default_tab)
            tab_class = url_class(tab_is_active)
              
            
            __M_locals_builtin_stored = __M_locals_builtin()
            __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['tab_is_active','tab_class'] if __M_key in __M_locals_builtin_stored]))
            __M_writer(u'\n  <li class="tab">\n  <a href="')
            __M_writer(filters.html_escape(filters.decode.utf8(tab.link_func(course, reverse))))
            __M_writer(u'" class="')
            __M_writer(filters.html_escape(filters.decode.utf8(tab_class)))
            __M_writer(u'">\n  ')
            __M_writer(filters.html_escape(filters.decode.utf8(_(tab.name))))
            __M_writer(u'\n')
            if tab_is_active:
                __M_writer(u'      <span class="sr">, current location</span>\n')
            if tab_image:
                __M_writer(u'      <img src="')
                __M_writer(filters.html_escape(filters.decode.utf8(tab_image)))
                __M_writer(u'" alt="')
                __M_writer(filters.html_escape(filters.decode.utf8(_('needs attention'))))
                __M_writer(u'" />\n')
            __M_writer(u'  </a>\n  </li>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"16": 4, "28": 3, "31": 8, "37": 2, "38": 3, "39": 7, "40": 8, "41": 10, "50": 15, "51": 16, "52": 17, "53": 17, "60": 20, "61": 22, "62": 22, "63": 22, "64": 22, "65": 23, "66": 23, "67": 24, "68": 25, "69": 27, "70": 30, "71": 30, "72": 30, "73": 30, "74": 30, "75": 32, "81": 75}, "uri": "/courseware/tabs.html", "filename": "/home/nttlong/code/edx/apps/edx/edx-platform/xdj-gnol-lms-templates/courseware/tabs.html"}
__M_END_METADATA
"""
