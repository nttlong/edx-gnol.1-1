# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1548073576.632577
_enable_loop = True
_template_filename = u'/home/nttlong/code/edx/apps/edx/edx-platform/xdj-gnol-lms-templates/discussion/_discussion_inline.html'
_template_uri = 'discussion/_discussion_inline.html'
_source_encoding = 'utf-8'
_exports = []



from django.utils.translation import ugettext as _
from json import dumps as json_dumps
from openedx.core.djangolib.js_utils import js_escaped_string


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        can_create_subcomment = context.get('can_create_subcomment', UNDEFINED)
        display_name = context.get('display_name', UNDEFINED)
        discussion_target = context.get('discussion_target', UNDEFINED)
        discussion_category = context.get('discussion_category', UNDEFINED)
        can_create_thread = context.get('can_create_thread', UNDEFINED)
        user = context.get('user', UNDEFINED)
        login_msg = context.get('login_msg', UNDEFINED)
        can_create_comment = context.get('can_create_comment', UNDEFINED)
        course_id = context.get('course_id', UNDEFINED)
        discussion_id = context.get('discussion_id', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n\n')
        runtime._include_file(context, u'_underscore_templates.html', _template_uri)
        __M_writer(u'\n')
        runtime._include_file(context, u'_thread_list_template.html', _template_uri)
        __M_writer(u'\n\n')
        __M_writer(u'\n\n<div class="discussion-module" data-discussion-id="')
        __M_writer(filters.html_escape(filters.decode.utf8(discussion_id)))
        __M_writer(u'"\n    data-user-create-comment="')
        __M_writer(filters.html_escape(filters.decode.utf8(json_dumps(can_create_comment))))
        __M_writer(u'"\n    data-user-create-subcomment="')
        __M_writer(filters.html_escape(filters.decode.utf8(json_dumps(can_create_subcomment))))
        __M_writer(u'"\n    data-read-only="')
        __M_writer(filters.html_escape(filters.decode.utf8('false' if can_create_thread else 'true')))
        __M_writer(u'">\n')
        if not user.is_authenticated:
            __M_writer(u'        <div class="page-banner">\n            <div class="alert alert-warning" role="alert">\n                <span class="icon icon-alert fa fa fa-warning" aria-hidden="true"></span>\n                <div class="message-content">')
            __M_writer(filters.html_escape(filters.decode.utf8(login_msg)))
            __M_writer(u'</div>\n            </div>\n        </div>\n        <br>\n')
        __M_writer(u'    <div class="discussion-module-header">\n        <h3 class="hd hd-3 discussion-module-title">')
        __M_writer(filters.html_escape(filters.decode.utf8(_(display_name))))
        __M_writer(u'</h3>\n        <div class="inline-discussion-topic"><span class="inline-discussion-topic-title">')
        __M_writer(filters.html_escape(filters.decode.utf8(_("Topic:"))))
        __M_writer(u'</span> ')
        __M_writer(filters.html_escape(filters.decode.utf8(discussion_category)))
        __M_writer(u'\n')
        if discussion_target:
            __M_writer(u'                    / ')
            __M_writer(filters.html_escape(filters.decode.utf8(discussion_target)))
            __M_writer(u'\n')
        __M_writer(u'           </div>\n    </div>\n    <button class="discussion-show btn"\n        data-discussion-id="')
        __M_writer(filters.html_escape(filters.decode.utf8(discussion_id)))
        __M_writer(u'"\n        ')
        __M_writer(filters.html_escape(filters.decode.utf8("disabled=disabled" if not user.is_authenticated else "")))
        __M_writer(u'>\n        <span class="button-text">')
        __M_writer(filters.html_escape(filters.decode.utf8(_("Show Discussion"))))
        __M_writer(u'</span>\n    </button>\n\n</div>\n<script type="text/javascript">\nvar $$course_id = "')
        __M_writer(js_escaped_string(course_id ))
        __M_writer(u'";\n\nfunction DiscussionInlineBlock(runtime, element) {\n    \'use strict\';\n    var el = $(element).find(\'.discussion-module\');\n    new DiscussionInlineView({ el: el, readOnly: el.data(\'read-only\') });\n}\n</script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"16": 6, "22": 1, "37": 1, "38": 3, "39": 3, "40": 4, "41": 4, "42": 10, "43": 12, "44": 12, "45": 13, "46": 13, "47": 14, "48": 14, "49": 15, "50": 15, "51": 16, "52": 17, "53": 20, "54": 20, "55": 25, "56": 26, "57": 26, "58": 27, "59": 27, "60": 27, "61": 27, "62": 28, "63": 29, "64": 29, "65": 29, "66": 31, "67": 34, "68": 34, "69": 35, "70": 35, "71": 36, "72": 36, "73": 41, "74": 41, "80": 74}, "uri": "discussion/_discussion_inline.html", "filename": "/home/nttlong/code/edx/apps/edx/edx-platform/xdj-gnol-lms-templates/discussion/_discussion_inline.html"}
__M_END_METADATA
"""
