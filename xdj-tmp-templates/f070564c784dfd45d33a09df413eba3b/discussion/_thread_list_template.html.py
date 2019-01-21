# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1548073576.692509
_enable_loop = True
_template_filename = u'/home/nttlong/code/edx/apps/edx/edx-platform/xdj-gnol-lms-templates/discussion/_thread_list_template.html'
_template_uri = u'discussion/_thread_list_template.html'
_source_encoding = 'utf-8'
_exports = []


from django.utils.translation import ugettext as _ 

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        flag_moderator = context.get('flag_moderator', UNDEFINED)
        groups = context.get('groups', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n')
        __M_writer(u'\n<script type="text/template" id="thread-list-template">\n    <div class="forum-nav-thread-list-wrapper" id="sort-filter-wrapper" tabindex="-1">\n        <div class="forum-nav-refine-bar">\n            <label class="forum-nav-filter-main">\n')
        __M_writer(u'                <span class="sr">')
        __M_writer(filters.html_escape(filters.decode.utf8(_("Filter:"))))
        __M_writer(u'</span>\n                <select class="forum-nav-filter-main-control">\n')
        __M_writer(u'                    <option value="all">')
        __M_writer(filters.html_escape(filters.decode.utf8(_("Show all posts"))))
        __M_writer(u'</option>\n')
        __M_writer(u'                    <option value="unread">')
        __M_writer(filters.html_escape(filters.decode.utf8(_("Unread posts"))))
        __M_writer(u'</option>\n')
        __M_writer(u'                    <option value="unanswered">')
        __M_writer(filters.html_escape(filters.decode.utf8(_("Unanswered posts"))))
        __M_writer(u'</option>\n')
        if flag_moderator:
            __M_writer(u'                        <option value="flagged">')
            __M_writer(filters.html_escape(filters.decode.utf8(_("Flagged"))))
            __M_writer(u'</option>\n')
        __M_writer(u'                </select>\n')
        __M_writer(u'            </label>')
        __M_writer(filters.decode.utf8("<% if (isDiscussionDivisionEnabled && isPrivilegedUser) { %>" ))
        __M_writer(u'<label class="forum-nav-filter-cohort">\n')
        __M_writer(u'                <span class="sr">')
        __M_writer(filters.html_escape(filters.decode.utf8(_("Group:"))))
        __M_writer(u'</span>\n                <select class="forum-nav-filter-cohort-control">\n                    <option value="">')
        __M_writer(filters.html_escape(filters.decode.utf8(_("in all groups"))))
        __M_writer(u'</option>\n')
        for group in (groups or []):
            __M_writer(u'                            <option value="')
            __M_writer(filters.html_escape(filters.decode.utf8(group['id'])))
            __M_writer(u'">')
            __M_writer(filters.html_escape(filters.decode.utf8(group['name'])))
            __M_writer(u'</option>\n')
        __M_writer(u'                </select>\n')
        __M_writer(u'            </label>')
        __M_writer(filters.decode.utf8("<% } %>" ))
        __M_writer(u'<label class="forum-nav-sort">\n')
        __M_writer(u'                <span class="sr">')
        __M_writer(filters.html_escape(filters.decode.utf8(_("Sort:"))))
        __M_writer(u'</span>\n                <select class="forum-nav-sort-control">\n')
        __M_writer(u'                    <option value="activity">')
        __M_writer(filters.html_escape(filters.decode.utf8(_("by recent activity"))))
        __M_writer(u'</option>\n')
        __M_writer(u'                    <option value="comments">')
        __M_writer(filters.html_escape(filters.decode.utf8(_("by most activity"))))
        __M_writer(u'</option>\n')
        __M_writer(u'                    <option value="votes">')
        __M_writer(filters.html_escape(filters.decode.utf8(_("by most votes"))))
        __M_writer(u'</option>\n                </select>\n            </label>\n        </div>\n        <div class="search-alerts"></div>\n        <ul class="forum-nav-thread-list"></ul>\n    </div>\n</script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"16": 2, "18": 1, "25": 1, "26": 2, "27": 8, "28": 8, "29": 8, "30": 11, "31": 11, "32": 11, "33": 13, "34": 13, "35": 13, "36": 16, "37": 16, "38": 16, "39": 17, "40": 20, "41": 20, "42": 20, "43": 22, "44": 24, "45": 24, "46": 24, "47": 26, "48": 26, "49": 26, "50": 28, "51": 28, "52": 30, "53": 31, "54": 31, "55": 31, "56": 31, "57": 31, "58": 33, "59": 35, "60": 35, "61": 35, "62": 37, "63": 37, "64": 37, "65": 40, "66": 40, "67": 40, "68": 42, "69": 42, "70": 42, "71": 44, "72": 44, "73": 44, "79": 73}, "uri": "discussion/_thread_list_template.html", "filename": "/home/nttlong/code/edx/apps/edx/edx-platform/xdj-gnol-lms-templates/discussion/_thread_list_template.html"}
__M_END_METADATA
"""
