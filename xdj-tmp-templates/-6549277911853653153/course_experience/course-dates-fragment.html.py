# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1548073627.819189
_enable_loop = True
_template_filename = u'/home/nttlong/code/edx/apps/edx/edx-platform/common/lib/capa/capa/templates/course_experience/course-dates-fragment.html'
_template_uri = 'course_experience/course-dates-fragment.html'
_source_encoding = 'utf-8'
_exports = []



from django.utils.translation import ugettext as _


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
        course_date_blocks = context.get('course_date_blocks', UNDEFINED)
        static = _mako_get_namespace(context, 'static')
        __M_writer = context.writer()
        __M_writer(u'\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n<h3 class="hd hd-6 handouts-header">')
        __M_writer(filters.html_escape(filters.decode.utf8(_("Important Course Dates"))))
        __M_writer(u'</h3>\n')
        __M_writer(u'\n')
        for course_date in course_date_blocks:
            __M_writer(u'    ')
            runtime._include_file(context, u'dates-summary.html', _template_uri, course_date=course_date)
            __M_writer(u'\n')
        __M_writer(u'\n')
        def ccall(caller):
            def body():
                __M_writer = context.writer()
                __M_writer(u"\n    DateUtilFactory.transform('.localized-datetime');\n")
                return ''
            return [body]
        context.caller_stack.nextcaller = runtime.Namespace('caller', context, callables=ccall(__M_caller))
        try:
            __M_writer(filters.html_escape(filters.decode.utf8(static.require_module_async(class_name=u'DateUtilFactory',module_name=u'js/dateutil_factory'))))
        finally:
            context.caller_stack.nextcaller = None
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"48": 16, "66": 60, "37": 2, "38": 3, "39": 5, "40": 9, "41": 10, "42": 10, "43": 12, "44": 13, "45": 14, "46": 14, "47": 14, "16": 7, "52": 17, "57": 17, "27": 5, "60": 19, "30": 3}, "uri": "course_experience/course-dates-fragment.html", "filename": "/home/nttlong/code/edx/apps/edx/edx-platform/common/lib/capa/capa/templates/course_experience/course-dates-fragment.html"}
__M_END_METADATA
"""
