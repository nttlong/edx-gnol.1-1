# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1548073628.898468
_enable_loop = True
_template_filename = u'/home/nttlong/code/edx/apps/edx/edx-platform/common/lib/capa/capa/templates/course_experience/course-messages-fragment.html'
_template_uri = 'course_experience/course-messages-fragment.html'
_source_encoding = 'utf-8'
_exports = []



from django.utils.translation import get_language_bidi
from django.utils.translation import ugettext as _
from openedx.core.djangolib.js_utils import js_escaped_string
from openedx.core.djangolib.markup import HTML
from openedx.features.course_experience import CourseHomeMessages


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace(u'static', context._clean_inheritance_tokens(), templateuri=u'../static_content.html', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, u'static')] = ns

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        static = _mako_get_namespace(context, 'static')
        image_src = context.get('image_src', UNDEFINED)
        course_home_messages = context.get('course_home_messages', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n')
        __M_writer(u'\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')

        is_rtl = get_language_bidi()
        
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['is_rtl'] if __M_key in __M_locals_builtin_stored]))
        __M_writer(u'\n\n')
        if course_home_messages:
            for message in course_home_messages:
                __M_writer(u'        <div class="course-message">\n')
                if not is_rtl:
                    __M_writer(u'                <img class="message-author" alt="" src="')
                    __M_writer(filters.html_escape(filters.decode.utf8(static.url(image_src))))
                    __M_writer(u'"/>\n')
                __M_writer(u'            <div class="message-content" aria-live="polite">\n                ')
                __M_writer(filters.html_escape(filters.decode.utf8(HTML(message.message_html))))
                __M_writer(u'\n            </div>\n')
                if is_rtl:
                    __M_writer(u'                <img class="message-author" alt="" src="')
                    __M_writer(filters.html_escape(filters.decode.utf8(static.url(image_src))))
                    __M_writer(u'"/>\n')
                __M_writer(u'        </div>\n')
        __M_writer(u'\n')
        def ccall(caller):
            def body():
                course_id = context.get('course_id', UNDEFINED)
                username = context.get('username', UNDEFINED)
                goal_api_url = context.get('goal_api_url', UNDEFINED)
                __M_writer = context.writer()
                __M_writer(u'\n    new CourseGoals({\n        goalApiUrl: "')
                __M_writer(js_escaped_string(goal_api_url ))
                __M_writer(u'",\n        courseId: "')
                __M_writer(js_escaped_string(course_id ))
                __M_writer(u'",\n        username: "')
                __M_writer(js_escaped_string(username ))
                __M_writer(u'",\n    });\n')
                return ''
            return [body]
        context.caller_stack.nextcaller = runtime.Namespace('caller', context, callables=ccall(__M_caller))
        try:
            __M_writer(filters.html_escape(filters.decode.utf8(static.webpack(entry=u'CourseGoals'))))
        finally:
            context.caller_stack.nextcaller = None
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"16": 6, "31": 4, "34": 3, "42": 2, "43": 3, "44": 4, "45": 12, "46": 14, "52": 16, "53": 18, "54": 19, "55": 20, "56": 21, "57": 22, "58": 22, "59": 22, "60": 24, "61": 25, "62": 25, "63": 27, "64": 28, "65": 28, "66": 28, "67": 30, "68": 33, "75": 34, "76": 36, "77": 36, "78": 37, "79": 37, "80": 38, "81": 38, "86": 34, "89": 40, "95": 89}, "uri": "course_experience/course-messages-fragment.html", "filename": "/home/nttlong/code/edx/apps/edx/edx-platform/common/lib/capa/capa/templates/course_experience/course-messages-fragment.html"}
__M_END_METADATA
"""
