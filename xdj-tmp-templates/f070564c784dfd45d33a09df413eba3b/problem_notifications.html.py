# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1548073575.437518
_enable_loop = True
_template_filename = u'/home/nttlong/code/edx/apps/edx/edx-platform/xdj-gnol-lms-templates/problem_notifications.html'
_template_uri = u'problem_notifications.html'
_source_encoding = 'utf-8'
_exports = []


from django.utils.translation import ugettext as _ 

def render_body(context,notification_name,notification_type,notification_icon,notification_message,should_enable_next_hint,is_hidden=True,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(notification_name=notification_name,should_enable_next_hint=should_enable_next_hint,pageargs=pageargs,notification_message=notification_message,notification_type=notification_type,notification_icon=notification_icon,is_hidden=is_hidden)
        short_id = context.get('short_id', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n')
        __M_writer(u'\n\n<div class="notification ')
        __M_writer(filters.html_escape(filters.decode.utf8(notification_type)))
        __M_writer(u' ')
        __M_writer(filters.html_escape(filters.decode.utf8('notification-')))
        __M_writer(filters.html_escape(filters.decode.utf8(notification_name)))
        __M_writer(u'\n      ')
        __M_writer(filters.html_escape(filters.decode.utf8('' if not is_hidden else 'is-hidden' )))
        __M_writer(u'"\n     tabindex="-1">\n    <span class="icon fa ')
        __M_writer(filters.html_escape(filters.decode.utf8(notification_icon)))
        __M_writer(u'" aria-hidden="true"></span>\n    <span class="notification-message" aria-describedby="')
        __M_writer(filters.html_escape(filters.decode.utf8( short_id )))
        __M_writer(u'-problem-title">')
        __M_writer(filters.html_escape(filters.decode.utf8(notification_message)))
        __M_writer(u'\n    </span>\n    <div class="notification-btn-wrapper">\n')
        if notification_name is 'hint':
            __M_writer(u'        <button type="button" class="btn btn-default btn-small notification-btn hint-button">\n          ')
            __M_writer(filters.html_escape(filters.decode.utf8(_('Next Hint'))))
            __M_writer(u'\n        </button>\n')
        __M_writer(u'        <button type="button" class="btn btn-default btn-small notification-btn review-btn sr">')
        __M_writer(filters.html_escape(filters.decode.utf8(_('Review'))))
        __M_writer(u'</button>\n    </div>\n</div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"16": 3, "18": 1, "24": 2, "25": 3, "26": 5, "27": 5, "28": 5, "29": 5, "30": 5, "31": 6, "32": 6, "33": 8, "34": 8, "35": 9, "36": 9, "37": 9, "38": 9, "39": 12, "40": 13, "41": 14, "42": 14, "43": 17, "44": 17, "45": 17, "51": 45}, "uri": "problem_notifications.html", "filename": "/home/nttlong/code/edx/apps/edx/edx-platform/xdj-gnol-lms-templates/problem_notifications.html"}
__M_END_METADATA
"""
