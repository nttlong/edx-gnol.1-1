# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1548073576.037486
_enable_loop = True
_template_filename = u'/home/nttlong/code/edx/apps/edx/edx-platform/xdj-gnol-lms-templates/bookmark_button.html'
_template_uri = u'bookmark_button.html'
_source_encoding = 'utf-8'
_exports = []



from django.urls import reverse
from django.utils.translation import ugettext as _


def render_body(context,bookmark_id,is_bookmarked,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs,bookmark_id=bookmark_id,is_bookmarked=is_bookmarked)
        __M_writer = context.writer()
        __M_writer(u'\n\n')
        __M_writer(u'\n\n<div class="bookmark-button-wrapper">\n  <button class="btn btn-link bookmark-button ')
        __M_writer(filters.html_escape(filters.decode.utf8("bookmarked" if is_bookmarked else "")))
        __M_writer(u'"\n    aria-pressed="')
        __M_writer(filters.html_escape(filters.decode.utf8("true" if is_bookmarked else "false")))
        __M_writer(u'"\n    data-bookmark-id="')
        __M_writer(filters.html_escape(filters.decode.utf8(bookmark_id)))
        __M_writer(u'"\n    data-bookmarks-api-url="')
        __M_writer(filters.html_escape(filters.decode.utf8(reverse('bookmarks'))))
        __M_writer(u'">\n     <span class="bookmark-text">')
        __M_writer(filters.html_escape(filters.decode.utf8(_("Bookmarked") if is_bookmarked else _("Bookmark this page"))))
        __M_writer(u'</span>\n    </button>\n</div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"32": 11, "33": 11, "34": 12, "35": 12, "36": 13, "37": 13, "43": 37, "16": 3, "21": 1, "26": 1, "27": 6, "28": 9, "29": 9, "30": 10, "31": 10}, "uri": "bookmark_button.html", "filename": "/home/nttlong/code/edx/apps/edx/edx-platform/xdj-gnol-lms-templates/bookmark_button.html"}
__M_END_METADATA
"""
