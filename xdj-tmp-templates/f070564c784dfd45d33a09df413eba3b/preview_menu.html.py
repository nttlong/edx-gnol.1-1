# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1548073578.836224
_enable_loop = True
_template_filename = u'/home/nttlong/code/edx/apps/edx/edx-platform/xdj-gnol-lms-templates/preview_menu.html'
_template_uri = u'/preview_menu.html'
_source_encoding = 'utf-8'
_exports = []



from django.utils.translation import ugettext as _
from django.conf import settings
from openedx.core.djangolib.js_utils import dump_js_escaped_json
from openedx.core.djangolib.markup import HTML, Text
from xmodule.partitions.partitions_service import get_all_partitions_for_course


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace(u'static', context._clean_inheritance_tokens(), templateuri=u'/x-static-content.html', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, u'static')] = ns

def render_body(context,active_page=None,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs,active_page=active_page)
        masquerade = context.get('masquerade', UNDEFINED)
        supports_preview_menu = context.get('supports_preview_menu', UNDEFINED)
        course = context.get('course', UNDEFINED)
        static = _mako_get_namespace(context, 'static')
        sorted = context.get('sorted', UNDEFINED)
        disable_student_access = context.get('disable_student_access', UNDEFINED)
        staff_access = context.get('staff_access', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n')
        __M_writer(u'\n')
        __M_writer(u'\n')
        __M_writer(u'\n\n')

        show_preview_menu = course and staff_access and supports_preview_menu
        
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['show_preview_menu'] if __M_key in __M_locals_builtin_stored]))
        __M_writer(u'\n\n')
        if show_preview_menu:
            __M_writer(u'    ')

            def selected(is_selected):
              return "selected" if is_selected else ""
            
            course_partitions = get_all_partitions_for_course(course)
            masquerade_user_name = masquerade.user_name if masquerade else None
            masquerade_group_id = masquerade.group_id if masquerade else None
            staff_selected = selected(not masquerade or masquerade.role != "student")
            specific_student_selected = selected(not staff_selected and masquerade.user_name)
            student_selected = selected(not staff_selected and not specific_student_selected and not masquerade_group_id)
            
            
            __M_locals_builtin_stored = __M_locals_builtin()
            __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['masquerade_user_name','selected','specific_student_selected','course_partitions','staff_selected','masquerade_group_id','student_selected'] if __M_key in __M_locals_builtin_stored]))
            __M_writer(u'\n    <nav class="wrapper-preview-menu" aria-label="')
            __M_writer(filters.html_escape(filters.decode.utf8(_('Course View'))))
            __M_writer(u'">\n        <div class="preview-menu">\n            <ol class="preview-actions">\n                <li class="action-preview">\n                    <form action="#" class="action-preview-form" method="post">\n                        <label for="action-preview-select" class="action-preview-label">')
            __M_writer(filters.html_escape(filters.decode.utf8(_("View this course as:"))))
            __M_writer(u'</label>\n                        <select class="action-preview-select" id="action-preview-select" name="select">\n                            <option value="staff" ')
            __M_writer(filters.html_escape(filters.decode.utf8(staff_selected)))
            __M_writer(u'>')
            __M_writer(filters.html_escape(filters.decode.utf8(_("Staff"))))
            __M_writer(u'</option>\n                            <option value="student" ')
            __M_writer(filters.html_escape(filters.decode.utf8(student_selected)))
            __M_writer(u'>')
            __M_writer(filters.html_escape(filters.decode.utf8(_("Learner"))))
            __M_writer(u'</option>\n                            <option value="specific student" ')
            __M_writer(filters.html_escape(filters.decode.utf8(specific_student_selected)))
            __M_writer(u'>')
            __M_writer(filters.html_escape(filters.decode.utf8(_("Specific learner"))))
            __M_writer(u'</option>\n')
            if course_partitions:
                for course_partition in course_partitions:
                    for group in sorted(course_partition.groups, key=lambda group: group.name):
                        __M_writer(u'                                    <option value="group.id" data-group-id="')
                        __M_writer(filters.html_escape(filters.decode.utf8(group.id)))
                        __M_writer(u'" data-partition-id="')
                        __M_writer(filters.html_escape(filters.decode.utf8(course_partition.id)))
                        __M_writer(u'" ')
                        __M_writer(filters.html_escape(filters.decode.utf8(selected(masquerade_group_id == group.id))))
                        __M_writer(u'>\n                                        ')
                        __M_writer(filters.html_escape(filters.decode.utf8(_("Learner in {content_group}").format(content_group=group.name))))
                        __M_writer(u'\n                                    </option>\n')
            __M_writer(u'                        </select>\n                        <div class="action-preview-username-container">\n                          <label for="action-preview-username" class="action-preview-label">')
            __M_writer(filters.html_escape(filters.decode.utf8(_("Username or email:"))))
            __M_writer(u'</label>\n                          <input type="text" class="action-preview-username" id="action-preview-username">\n                        </div>\n                        <button type="submit" class="sr-only" name="submit" value="submit">')
            __M_writer(filters.html_escape(filters.decode.utf8(_("Set preview mode"))))
            __M_writer(u'</button>\n                    </form>\n                </li>\n            </ol>\n')
            if specific_student_selected:
                __M_writer(u'                <div class="preview-specific-student-notice">\n                    <p>\n                        ')
                __M_writer(filters.html_escape(filters.decode.utf8(Text(_("You are now viewing the course as {i_start}{user_name}{i_end}.")).format(
                            user_name=masquerade_user_name,
                            i_start=HTML(u'<i>'),
                            i_end=HTML(u'</i>'),
                        ))))
                __M_writer(u'\n                    </p>\n                </div>\n')
            __M_writer(u'        </div>\n    </nav>\n\n    ')

            preview_options = {
                "courseId": course.id,
                "disableStudentAccess": disable_student_access if disable_student_access is not UNDEFINED else False,
                "specificStudentSelected": specific_student_selected,
                "masqueradeUsername" : masquerade_user_name if masquerade_user_name is not UNDEFINED else None,
            }
            
            
            __M_locals_builtin_stored = __M_locals_builtin()
            __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['preview_options'] if __M_key in __M_locals_builtin_stored]))
            __M_writer(u'\n    ')
            def ccall(caller):
                def body():
                    __M_writer = context.writer()
                    __M_writer(u'\n        PreviewFactory(')
                    __M_writer(dump_js_escaped_json(preview_options ))
                    __M_writer(u');\n    ')
                    return ''
                return [body]
            context.caller_stack.nextcaller = runtime.Namespace('caller', context, callables=ccall(__M_caller))
            try:
                __M_writer(filters.html_escape(filters.decode.utf8(static.require_module_async(class_name=u'PreviewFactory',module_name=u'lms/js/preview/preview_factory'))))
            finally:
                context.caller_stack.nextcaller = None
            __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"131": 79, "132": 80, "133": 80, "138": 79, "141": 81, "16": 5, "147": 141, "31": 4, "34": 3, "46": 2, "47": 3, "48": 4, "49": 11, "50": 13, "56": 15, "57": 17, "58": 18, "59": 18, "73": 28, "74": 29, "75": 29, "76": 34, "77": 34, "78": 36, "79": 36, "80": 36, "81": 36, "82": 37, "83": 37, "84": 37, "85": 37, "86": 38, "87": 38, "88": 38, "89": 38, "90": 39, "91": 40, "92": 41, "93": 42, "94": 42, "95": 42, "96": 42, "97": 42, "98": 42, "99": 42, "100": 43, "101": 43, "102": 48, "103": 50, "104": 50, "105": 53, "106": 53, "107": 57, "108": 58, "109": 60, "114": 64, "115": 68, "116": 71, "127": 78}, "uri": "/preview_menu.html", "filename": "/home/nttlong/code/edx/apps/edx/edx-platform/xdj-gnol-lms-templates/preview_menu.html"}
__M_END_METADATA
"""
