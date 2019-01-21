# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1548073578.032627
_enable_loop = True
_template_filename = u'/home/nttlong/code/edx/apps/edx/edx-platform/xdj-gnol-lms-templates/courseware/experiments.html'
_template_uri = u'/courseware/experiments.html'
_source_encoding = 'utf-8'
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        upgrade_link = context.get('upgrade_link', UNDEFINED)
        upgrade_price = context.get('upgrade_price', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n\n')
        if upgrade_link:
            __M_writer(u'<script type="text/plain"\n    id="upgrade_user"\n    data-link="')
            __M_writer(filters.html_escape(filters.decode.utf8(upgrade_link)))
            __M_writer(u'"\n    data-price="')
            __M_writer(filters.html_escape(filters.decode.utf8(upgrade_price)))
            __M_writer(u'">\n</script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"35": 29, "16": 1, "23": 1, "24": 4, "25": 5, "26": 7, "27": 7, "28": 8, "29": 8}, "uri": "/courseware/experiments.html", "filename": "/home/nttlong/code/edx/apps/edx/edx-platform/xdj-gnol-lms-templates/courseware/experiments.html"}
__M_END_METADATA
"""
