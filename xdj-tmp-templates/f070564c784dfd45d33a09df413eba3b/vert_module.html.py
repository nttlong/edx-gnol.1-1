# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1548073575.66442
_enable_loop = True
_template_filename = u'/home/nttlong/code/edx/apps/edx/edx-platform/xdj-gnol-lms-templates/vert_module.html'
_template_uri = 'vert_module.html'
_source_encoding = 'utf-8'
_exports = []


from openedx.core.djangolib.markup import HTML 

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        bookmarked = context.get('bookmarked', UNDEFINED)
        items = context.get('items', UNDEFINED)
        unit_title = context.get('unit_title', UNDEFINED)
        bookmark_id = context.get('bookmark_id', UNDEFINED)
        enumerate = context.get('enumerate', UNDEFINED)
        show_bookmark_button = context.get('show_bookmark_button', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n')
        __M_writer(u'\n')
        if unit_title:
            __M_writer(u'  <h2 class="hd hd-2 unit-title">')
            __M_writer(filters.html_escape(filters.decode.utf8(unit_title)))
            __M_writer(u'</h2>\n')
        __M_writer(u'\n')
        if show_bookmark_button:
            __M_writer(u'    ')
            runtime._include_file(context, u'bookmark_button.html', _template_uri, bookmark_id=bookmark_id, is_bookmarked=bookmarked)
            __M_writer(u'\n')
        __M_writer(u'\n<div class="vert-mod">\n')
        for idx, item in enumerate(items):
            __M_writer(u'  <div class="vert vert-')
            __M_writer(filters.html_escape(filters.decode.utf8(idx)))
            __M_writer(u'" data-id="')
            __M_writer(filters.html_escape(filters.decode.utf8(item['id'])))
            __M_writer(u'">\n    ')
            __M_writer(filters.html_escape(filters.decode.utf8(HTML(item['content']))))
            __M_writer(u'\n  </div>\n')
        __M_writer(u'</div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"16": 2, "18": 1, "29": 1, "30": 2, "31": 3, "32": 4, "33": 4, "34": 4, "35": 6, "36": 7, "37": 8, "38": 8, "39": 8, "40": 10, "41": 12, "42": 13, "43": 13, "44": 13, "45": 13, "46": 13, "47": 14, "48": 14, "49": 17, "55": 49}, "uri": "vert_module.html", "filename": "/home/nttlong/code/edx/apps/edx/edx-platform/xdj-gnol-lms-templates/vert_module.html"}
__M_END_METADATA
"""
