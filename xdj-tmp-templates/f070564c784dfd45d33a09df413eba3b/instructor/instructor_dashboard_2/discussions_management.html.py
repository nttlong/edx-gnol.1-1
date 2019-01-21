# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1548073809.98158
_enable_loop = True
_template_filename = u'/home/nttlong/code/edx/apps/edx/edx-platform/xdj-gnol-lms-templates/instructor/instructor_dashboard_2/discussions_management.html'
_template_uri = u'instructor/instructor_dashboard_2/discussions_management.html'
_source_encoding = 'utf-8'
_exports = [u'js_extra']



from django.utils.translation import ugettext as _
from openedx.core.djangolib.js_utils import js_escaped_string, dump_js_escaped_json
from courseware.courses import get_studio_url
from openedx.core.djangoapps.course_groups.partition_scheme import get_cohorted_user_partition


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace(u'static', context._clean_inheritance_tokens(), templateuri=u'../../x-static-content.html', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, u'static')] = ns

def render_body(context,section_data,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs,section_data=section_data)
        def js_extra():
            return render_js_extra(context._locals(__M_locals))
        static = _mako_get_namespace(context, 'static')
        __M_writer = context.writer()
        __M_writer(u'\n\n')
        __M_writer(u'\n')
        __M_writer(u'\n\n\n<div class="discussions-management"\n     data-discussion-topics-url="')
        __M_writer(filters.html_escape(filters.decode.utf8(section_data['discussion_topics_url'])))
        __M_writer(u'"\n     data-course-discussion-settings-url="')
        __M_writer(filters.html_escape(filters.decode.utf8(section_data['course_discussion_settings'])))
        __M_writer(u'"\n>\n</div>\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'js_extra'):
            context['self'].js_extra(**pageargs)
        

        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_js_extra(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def js_extra():
            return render_js_extra(context)
        static = _mako_get_namespace(context, 'static')
        __M_writer = context.writer()
        __M_writer(u'\n')
        def ccall(caller):
            def body():
                __M_writer = context.writer()
                __M_writer(u'\n    DiscussionsFactory();\n')
                return ''
            return [body]
        context.caller_stack.nextcaller = runtime.Namespace('caller', context, callables=ccall(__M_caller))
        try:
            __M_writer(filters.html_escape(filters.decode.utf8(static.require_module(class_name=u'DiscussionsFactory',module_name=u'js/discussions_management/views/discussions_dashboard_factory'))))
        finally:
            context.caller_stack.nextcaller = None
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"33": 1, "77": 21, "69": 19, "65": 18, "41": 1, "42": 3, "43": 9, "44": 13, "45": 13, "46": 14, "47": 14, "16": 4, "83": 77, "52": 22, "58": 18, "74": 19, "30": 3}, "uri": "instructor/instructor_dashboard_2/discussions_management.html", "filename": "/home/nttlong/code/edx/apps/edx/edx-platform/xdj-gnol-lms-templates/instructor/instructor_dashboard_2/discussions_management.html"}
__M_END_METADATA
"""
