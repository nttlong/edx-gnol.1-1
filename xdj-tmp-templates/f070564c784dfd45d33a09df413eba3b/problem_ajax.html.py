# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1548073575.457256
_enable_loop = True
_template_filename = u'/home/nttlong/code/edx/apps/edx/edx-platform/xdj-gnol-lms-templates/problem_ajax.html'
_template_uri = 'problem_ajax.html'
_source_encoding = 'utf-8'
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        graded = context.get('graded', UNDEFINED)
        current_score = context.get('current_score', UNDEFINED)
        content = context.get('content', UNDEFINED)
        total_possible = context.get('total_possible', UNDEFINED)
        ajax_url = context.get('ajax_url', UNDEFINED)
        element_id = context.get('element_id', UNDEFINED)
        attempts_used = context.get('attempts_used', UNDEFINED)
        id = context.get('id', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'<div id="problem_')
        __M_writer(filters.decode.utf8(element_id))
        __M_writer(u'" class="problems-wrapper" role="group"\n     aria-labelledby="')
        __M_writer(filters.decode.utf8(element_id))
        __M_writer(u'-problem-title"\n     data-problem-id="')
        __M_writer(filters.decode.utf8(id))
        __M_writer(u'" data-url="')
        __M_writer(filters.decode.utf8(ajax_url))
        __M_writer(u'"\n     data-problem-score="')
        __M_writer(filters.decode.utf8(current_score))
        __M_writer(u'"\n     data-problem-total-possible="')
        __M_writer(filters.decode.utf8(total_possible))
        __M_writer(u'"\n     data-attempts-used="')
        __M_writer(filters.decode.utf8(attempts_used))
        __M_writer(u'"\n     data-content="')
        __M_writer(filters.html_escape(filters.decode.utf8(content )))
        __M_writer(u'"\n     data-graded="')
        __M_writer(filters.decode.utf8(graded))
        __M_writer(u'">\n    <p class="loading-spinner">\n        <i class="fa fa-spinner fa-pulse fa-2x fa-fw"></i>\n        <span class="sr">Loading&hellip;</span>\n    </p>\n</div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"32": 2, "33": 2, "34": 3, "35": 3, "36": 3, "37": 3, "38": 4, "39": 4, "40": 5, "41": 5, "42": 6, "43": 6, "44": 7, "45": 7, "46": 8, "47": 8, "16": 0, "53": 47, "29": 1, "30": 1, "31": 1}, "uri": "problem_ajax.html", "filename": "/home/nttlong/code/edx/apps/edx/edx-platform/xdj-gnol-lms-templates/problem_ajax.html"}
__M_END_METADATA
"""
