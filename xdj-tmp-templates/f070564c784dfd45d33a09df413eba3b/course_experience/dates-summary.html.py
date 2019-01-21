# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1548073627.856046
_enable_loop = True
_template_filename = u'/home/nttlong/code/edx/apps/edx/edx-platform/common/lib/capa/capa/templates/course_experience/dates-summary.html'
_template_uri = u'course_experience/dates-summary.html'
_source_encoding = 'utf-8'
_exports = []



from django.utils.translation import ugettext as _


def render_body(context,course_date,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs,course_date=course_date)
        user_timezone = context.get('user_timezone', UNDEFINED)
        user_language = context.get('user_language', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n')
        __M_writer(u'\n<div class="date-summary-container">\n    <div class="date-summary date-summary-')
        __M_writer(filters.html_escape(filters.decode.utf8(course_date.css_class)))
        __M_writer(u'">\n')
        if course_date.title:
            if course_date.title == 'current_datetime':
                __M_writer(u'                <span class="hd hd-6 heading localized-datetime" data-datetime="')
                __M_writer(filters.html_escape(filters.decode.utf8(course_date.date)))
                __M_writer(u'" data-string="')
                __M_writer(filters.html_escape(filters.decode.utf8(_(u'Today is {date}'))))
                __M_writer(u'" data-timezone="')
                __M_writer(filters.html_escape(filters.decode.utf8(user_timezone)))
                __M_writer(u'" data-language="')
                __M_writer(filters.html_escape(filters.decode.utf8(user_language)))
                __M_writer(u'"></span>\n')
            else:
                __M_writer(u'                <span class="hd hd-6 heading">')
                __M_writer(filters.html_escape(filters.decode.utf8(course_date.title)))
                __M_writer(u'</span>\n')
        if course_date.date and course_date.title != 'current_datetime':
            __M_writer(u'            <p class="hd hd-6 date localized-datetime" data-format="shortDate" data-datetime="')
            __M_writer(filters.html_escape(filters.decode.utf8(course_date.date)))
            __M_writer(u'" data-timezone="')
            __M_writer(filters.html_escape(filters.decode.utf8(user_timezone)))
            __M_writer(u'" data-language="')
            __M_writer(filters.html_escape(filters.decode.utf8(user_language)))
            __M_writer(u'" data-string="')
            __M_writer(filters.html_escape(filters.decode.utf8(_(course_date.relative_datestring))))
            __M_writer(u'"></p>\n')
        if course_date.description:
            __M_writer(u'            <p class="description">')
            __M_writer(filters.html_escape(filters.decode.utf8(course_date.description)))
            __M_writer(u'</p>\n')
        if course_date.link and course_date.link_text:
            __M_writer(u'            <span class="date-summary-link">\n                <a href="')
            __M_writer(filters.html_escape(filters.decode.utf8(course_date.link)))
            __M_writer(u'">')
            __M_writer(filters.html_escape(filters.decode.utf8(course_date.link_text)))
            __M_writer(u'</a>\n            </span>\n')
        __M_writer(u'    </div>\n</div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"16": 1, "20": 4, "27": 3, "28": 4, "29": 6, "30": 6, "31": 7, "32": 8, "33": 9, "34": 9, "35": 9, "36": 9, "37": 9, "38": 9, "39": 9, "40": 9, "41": 9, "42": 10, "43": 11, "44": 11, "45": 11, "46": 14, "47": 15, "48": 15, "49": 15, "50": 15, "51": 15, "52": 15, "53": 15, "54": 15, "55": 15, "56": 17, "57": 18, "58": 18, "59": 18, "60": 20, "61": 21, "62": 22, "63": 22, "64": 22, "65": 22, "66": 25, "72": 66}, "uri": "course_experience/dates-summary.html", "filename": "/home/nttlong/code/edx/apps/edx/edx-platform/common/lib/capa/capa/templates/course_experience/dates-summary.html"}
__M_END_METADATA
"""
