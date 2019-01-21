# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1548073578.850257
_enable_loop = True
_template_filename = u'/home/nttlong/code/edx/apps/edx/edx-platform/xdj-gnol-lms-templates/page_banner.html'
_template_uri = u'/page_banner.html'
_source_encoding = 'utf-8'
_exports = []



from django.utils.translation import ugettext as _
from openedx.core.djangolib.markup import HTML
from openedx.core.djangoapps.util.user_messages import PageLevelMessages, UserMessage, UserMessageType
# app that handles site status messages
from status.status import get_site_status_msg


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace(u'static', context._clean_inheritance_tokens(), templateuri=u'static_content.html', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, u'static')] = ns

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        request = context.get('request', UNDEFINED)
        self = context.get('self', UNDEFINED)
        list = context.get('list', UNDEFINED)
        hasattr = context.get('hasattr', UNDEFINED)
        course = context.get('course', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n')
        online_help_token = self.online_help_token() if hasattr(self, 'online_help_token') else None 
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['online_help_token'] if __M_key in __M_locals_builtin_stored]))
        __M_writer(u'\n')
        __M_writer(u'\n\n')

        banner_messages = list(PageLevelMessages.user_messages(request))
        
        # insert the global status message
        course_id = course.id if course else None
        site_status_message = get_site_status_msg(course_id)
        if site_status_message:
            banner_messages.insert(0, UserMessage(UserMessageType.WARNING, site_status_message))
        
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['course_id','site_status_message','banner_messages'] if __M_key in __M_locals_builtin_stored]))
        __M_writer(u'\n\n')
        if banner_messages:
            __M_writer(u'    <div class="page-banner">\n        <div class="user-messages">\n')
            for message in banner_messages:
                __M_writer(u'                <div class="alert ')
                __M_writer(filters.html_escape(filters.decode.utf8(message.css_class)))
                __M_writer(u'" role="alert">\n                    <span class="icon icon-alert fa ')
                __M_writer(filters.html_escape(filters.decode.utf8(message.icon_class)))
                __M_writer(u'" aria-hidden="true"></span>\n                    ')
                __M_writer(filters.html_escape(filters.decode.utf8(HTML(message.message_html))))
                __M_writer(u'\n                </div>\n')
            __M_writer(u'        </div>\n    </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"16": 7, "31": 5, "34": 3, "44": 2, "45": 3, "46": 5, "47": 6, "51": 6, "52": 13, "53": 15, "65": 23, "66": 25, "67": 26, "68": 28, "69": 29, "70": 29, "71": 29, "72": 30, "73": 30, "74": 31, "75": 31, "76": 34, "82": 76}, "uri": "/page_banner.html", "filename": "/home/nttlong/code/edx/apps/edx/edx-platform/xdj-gnol-lms-templates/page_banner.html"}
__M_END_METADATA
"""
