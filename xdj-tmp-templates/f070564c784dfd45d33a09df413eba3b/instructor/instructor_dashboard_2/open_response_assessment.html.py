# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1548073810.099042
_enable_loop = True
_template_filename = u'/home/nttlong/code/edx/apps/edx/edx-platform/xdj-gnol-lms-templates/instructor/instructor_dashboard_2/open_response_assessment.html'
_template_uri = u'instructor/instructor_dashboard_2/open_response_assessment.html'
_source_encoding = 'utf-8'
_exports = []


from openedx.core.djangolib.markup import HTML 

def render_body(context,section_data,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs,section_data=section_data)
        __M_writer = context.writer()
        __M_writer(u'\n')
        __M_writer(u'\n\n<section class="open-response-assessment">\n    ')
        __M_writer(filters.html_escape(filters.decode.utf8(HTML(section_data['fragment'].body_html()))))
        __M_writer(u'\n</section>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"32": 26, "16": 2, "18": 1, "23": 1, "24": 2, "25": 5, "26": 5}, "uri": "instructor/instructor_dashboard_2/open_response_assessment.html", "filename": "/home/nttlong/code/edx/apps/edx/edx-platform/xdj-gnol-lms-templates/instructor/instructor_dashboard_2/open_response_assessment.html"}
__M_END_METADATA
"""
