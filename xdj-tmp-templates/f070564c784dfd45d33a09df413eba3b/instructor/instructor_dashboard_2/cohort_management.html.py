# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1548073809.971588
_enable_loop = True
_template_filename = u'/home/nttlong/code/edx/apps/edx/edx-platform/xdj-gnol-lms-templates/instructor/instructor_dashboard_2/cohort_management.html'
_template_uri = u'instructor/instructor_dashboard_2/cohort_management.html'
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
        __M_writer(u'\n\n\n<div class="cohort-management"\n     data-cohorts_url="')
        __M_writer(filters.html_escape(filters.decode.utf8(section_data['cohorts_url'])))
        __M_writer(u'"\n     data-upload_cohorts_csv_url="')
        __M_writer(filters.html_escape(filters.decode.utf8(section_data['upload_cohorts_csv_url'])))
        __M_writer(u'"\n     data-course_cohort_settings_url="')
        __M_writer(filters.html_escape(filters.decode.utf8(section_data['course_cohort_settings_url'])))
        __M_writer(u'"\n     data-verified_track_cohorting_url="')
        __M_writer(filters.html_escape(filters.decode.utf8(section_data['verified_track_cohorting_url'])))
        __M_writer(u'"\n     data-is_ccx_enabled="')
        __M_writer(filters.html_escape(filters.decode.utf8('true' if section_data['ccx_is_enabled'] else 'false')))
        __M_writer(u'"\n>\n</div>\n\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'js_extra'):
            context['self'].js_extra(**pageargs)
        

        __M_writer(u'\n<div class="cohort-state-message"></div>\n')
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
                course = context.get('course', UNDEFINED)
                __M_writer = context.writer()
                __M_writer(u'\n    ')

                cohorted_user_partition = get_cohorted_user_partition(course)
                content_groups = cohorted_user_partition.groups if cohorted_user_partition else []
                
                
                __M_writer(u'\n    var cohortUserPartitionId = ')
                __M_writer(dump_js_escaped_json(cohorted_user_partition.id if cohorted_user_partition else None ))
                __M_writer(u',\n        contentGroups = [\n')
                for content_group in content_groups:
                    __M_writer(u'            {\n                id: ')
                    __M_writer(dump_js_escaped_json(content_group.id ))
                    __M_writer(u',\n                name: "')
                    __M_writer(js_escaped_string(content_group.name ))
                    __M_writer(u'",\n                user_partition_id: cohortUserPartitionId\n            },\n')
                __M_writer(u'        ];\n    CohortsFactory(contentGroups, "')
                __M_writer(js_escaped_string(get_studio_url(course, 'group_configurations') ))
                __M_writer(u'");\n')
                return ''
            return [body]
        context.caller_stack.nextcaller = runtime.Namespace('caller', context, callables=ccall(__M_caller))
        try:
            __M_writer(filters.html_escape(filters.decode.utf8(static.require_module(class_name=u'CohortsFactory',module_name=u'js/groups/views/cohorts_dashboard_factory'))))
        finally:
            context.caller_stack.nextcaller = None
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"16": 4, "30": 3, "33": 1, "41": 1, "42": 3, "43": 9, "44": 13, "45": 13, "46": 14, "47": 14, "48": 15, "49": 15, "50": 16, "51": 16, "52": 17, "53": 17, "58": 40, "64": 22, "71": 22, "76": 23, "77": 24, "82": 27, "83": 28, "84": 28, "85": 30, "86": 31, "87": 32, "88": 32, "89": 33, "90": 33, "91": 37, "92": 38, "93": 38, "98": 23, "101": 39, "107": 101}, "uri": "instructor/instructor_dashboard_2/cohort_management.html", "filename": "/home/nttlong/code/edx/apps/edx/edx-platform/xdj-gnol-lms-templates/instructor/instructor_dashboard_2/cohort_management.html"}
__M_END_METADATA
"""
