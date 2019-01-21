# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1548073575.307199
_enable_loop = True
_template_filename = u'/home/nttlong/code/edx/apps/edx/edx-platform/common/lib/capa/capa/templates/status_span.html'
_template_uri = u'status_span.html'
_source_encoding = 'utf-8'
_exports = []


def render_body(context,status,status_id='',hide_correctness=False,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(status=status,hide_correctness=hide_correctness,pageargs=pageargs,status_id=status_id)
        __M_writer = context.writer()
        __M_writer(u'\n\n')
        if status_id == '':
            __M_writer(u'<span class="status ')
            __M_writer(filters.html_escape(filters.decode.utf8('' if hide_correctness == True else status.classname)))
            __M_writer(u'"\n      data-tooltip="')
            __M_writer(filters.html_escape(filters.decode.utf8('' if hide_correctness == True else status.display_tooltip)))
            __M_writer(u'">\n')
        else:
            __M_writer(u'<span class="status ')
            __M_writer(filters.html_escape(filters.decode.utf8('' if hide_correctness == True else status.classname)))
            __M_writer(u'" id="status_')
            __M_writer(filters.html_escape(filters.decode.utf8(status_id)))
            __M_writer(u'"\n      data-tooltip="')
            __M_writer(filters.html_escape(filters.decode.utf8('' if hide_correctness == True else status.display_tooltip)))
            __M_writer(u'">\n')
        if hide_correctness == False:
            __M_writer(u'  <span class="sr">')
            __M_writer(filters.html_escape(filters.decode.utf8(status.display_name)))
            __M_writer(u'</span><span class="status-icon" aria-hidden="true"></span>\n')
        __M_writer(u'</span>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"16": 1, "21": 1, "22": 3, "23": 4, "24": 4, "25": 4, "26": 5, "27": 5, "28": 6, "29": 7, "30": 7, "31": 7, "32": 7, "33": 7, "34": 8, "35": 8, "36": 10, "37": 11, "38": 11, "39": 11, "40": 13, "46": 40}, "uri": "status_span.html", "filename": "/home/nttlong/code/edx/apps/edx/edx-platform/common/lib/capa/capa/templates/status_span.html"}
__M_END_METADATA
"""
