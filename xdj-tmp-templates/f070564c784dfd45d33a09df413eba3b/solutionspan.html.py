# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1548073576.159434
_enable_loop = True
_template_filename = u'/home/nttlong/code/edx/apps/edx/edx-platform/common/lib/capa/capa/templates/solutionspan.html'
_template_uri = 'solutionspan.html'
_source_encoding = 'utf-8'
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        id = context.get('id', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n<div class="solution-span">\n <span id="solution_')
        __M_writer(filters.html_escape(filters.decode.utf8(id)))
        __M_writer(u'"></span>\n</div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"16": 1, "24": 3, "30": 24, "22": 1, "23": 3}, "uri": "solutionspan.html", "filename": "/home/nttlong/code/edx/apps/edx/edx-platform/common/lib/capa/capa/templates/solutionspan.html"}
__M_END_METADATA
"""
