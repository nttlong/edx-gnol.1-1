# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1548073575.468577
_enable_loop = True
_template_filename = u'/home/nttlong/code/edx/apps/edx/edx-platform/common/templates/xblock_wrapper.html'
_template_uri = 'xblock_wrapper.html'
_source_encoding = 'utf-8'
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        content = context.get('content', UNDEFINED)
        classes = context.get('classes', UNDEFINED)
        data_attributes = context.get('data_attributes', UNDEFINED)
        js_init_parameters = context.get('js_init_parameters', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'<div class="')
        __M_writer(' '.join(classes) )
        __M_writer(u'" ')
        __M_writer(filters.decode.utf8(data_attributes))
        __M_writer(u'>\n')
        if js_init_parameters:
            __M_writer(u'  <script type="json/xblock-args" class="xblock-json-init-args">\n    ')
            __M_writer(filters.decode.utf8(js_init_parameters))
            __M_writer(u'\n  </script>\n')
        __M_writer(u'  ')
        __M_writer(filters.decode.utf8(content))
        __M_writer(u'\n</div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"32": 4, "33": 4, "34": 7, "35": 7, "36": 7, "42": 36, "16": 0, "25": 1, "26": 1, "27": 1, "28": 1, "29": 1, "30": 2, "31": 3}, "uri": "xblock_wrapper.html", "filename": "/home/nttlong/code/edx/apps/edx/edx-platform/common/templates/xblock_wrapper.html"}
__M_END_METADATA
"""
