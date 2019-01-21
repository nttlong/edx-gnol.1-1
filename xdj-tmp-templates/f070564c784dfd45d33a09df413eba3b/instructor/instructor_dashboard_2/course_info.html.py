# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1548073809.882896
_enable_loop = True
_template_filename = u'/home/nttlong/code/edx/apps/edx/edx-platform/xdj-gnol-lms-templates/instructor/instructor_dashboard_2/course_info.html'
_template_uri = u'instructor/instructor_dashboard_2/course_info.html'
_source_encoding = 'utf-8'
_exports = []



from django.utils.translation import ugettext as _
from openedx.core.djangolib.markup import HTML, Text


def render_body(context,section_data,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs,section_data=section_data)
        user_timezone = context.get('user_timezone', UNDEFINED)
        settings = context.get('settings', UNDEFINED)
        len = context.get('len', UNDEFINED)
        course = context.get('course', UNDEFINED)
        user = context.get('user', UNDEFINED)
        user_language = context.get('user_language', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n')
        __M_writer(u'\n\n')
        if settings.FEATURES.get('DISPLAY_ANALYTICS_ENROLLMENTS') or section_data.get('enrollment_message'):
            __M_writer(u'  <h4 class="hd hd-4">')
            __M_writer(filters.html_escape(filters.decode.utf8(_("Enrollment Information"))))
            __M_writer(u'</h4>\n  <div class="enrollment-wrapper">\n')
            if settings.FEATURES.get('DISPLAY_ANALYTICS_ENROLLMENTS'):
                __M_writer(u'      ')
                modes = section_data['enrollment_count'] 
                
                __M_locals_builtin_stored = __M_locals_builtin()
                __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['modes'] if __M_key in __M_locals_builtin_stored]))
                __M_writer(u'\n        <table>\n            <caption class="tip">')
                __M_writer(filters.html_escape(filters.decode.utf8(_("Number of enrollees (admins, staff, and students) by track"))))
                __M_writer(u'</caption>\n            <tr>\n                <th scope="row">')
                __M_writer(filters.html_escape(filters.decode.utf8(_("Verified"))))
                __M_writer(u'</th><td>')
                __M_writer(filters.html_escape(filters.decode.utf8(modes['verified'])))
                __M_writer(u'</td>\n            </tr>\n            <tr>\n                <th scope="row">')
                __M_writer(filters.html_escape(filters.decode.utf8(_("Audit"))))
                __M_writer(u'</th><td>')
                __M_writer(filters.html_escape(filters.decode.utf8(modes['audit'])))
                __M_writer(u'</td>\n            </tr>\n            <tr>\n                <th scope="row">')
                __M_writer(filters.html_escape(filters.decode.utf8(_("Honor"))))
                __M_writer(u'</th><td>')
                __M_writer(filters.html_escape(filters.decode.utf8(modes['honor'])))
                __M_writer(u'</td>\n            </tr>\n            <tr>\n                <th scope="row">')
                __M_writer(filters.html_escape(filters.decode.utf8(_("Professional"))))
                __M_writer(u'</th><td>')
                __M_writer(filters.html_escape(filters.decode.utf8(modes['professional'] + modes['no-id-professional'])))
                __M_writer(u'</td>\n            </tr>\n            <tr style="color:green;border-top:1px solid #000">\n                <th scope="row" style="padding-top:10px;">\n                    <strong>')
                __M_writer(filters.html_escape(filters.decode.utf8(_("Total"))))
                __M_writer(u'</strong>\n                </th>\n                <td style="padding-top:10px;">\n                    <strong>')
                __M_writer(filters.html_escape(filters.decode.utf8(modes['total'])))
                __M_writer(u'</strong>\n                </td>\n            </tr>\n        </table>\n')
            elif section_data.get('enrollment_message'):
                __M_writer(u'        <p>')
                __M_writer(filters.html_escape(filters.decode.utf8(section_data['enrollment_message'])))
                __M_writer(u'</p>\n')
            __M_writer(u'  </div>\n  <hr>\n')
        __M_writer(u'\n<div class="basic-wrapper">\n  <h4 class="hd hd-4">')
        __M_writer(filters.html_escape(filters.decode.utf8(_("Basic Course Information"))))
        __M_writer(u'</h4>\n\n  <ul class="list-input">\n    <li class="field text is-not-editable" id="field-course-display-name">\n      <label for="course-display-name">')
        __M_writer(filters.html_escape(filters.decode.utf8(_("Course Name:"))))
        __M_writer(u'</label>\n      <b>')
        __M_writer(filters.html_escape(filters.decode.utf8( section_data['course_display_name'])))
        __M_writer(u'</b>\n    </li>\n\n    <li class="field text is-not-editable" id="field-course-name">\n      <label for="course-name">')
        __M_writer(filters.html_escape(filters.decode.utf8(_("Course Run:"))))
        __M_writer(u'</label>\n      <b>')
        __M_writer(filters.html_escape(filters.decode.utf8( section_data['course_id'].run)))
        __M_writer(u'</b>\n    </li>\n\n    <li class="field text is-not-editable" id="field-course-number">\n      <label for="course-number">')
        __M_writer(filters.html_escape(filters.decode.utf8(_("Course Number:"))))
        __M_writer(u'</label>\n      <b>')
        __M_writer(filters.html_escape(filters.decode.utf8( section_data['course_number'])))
        __M_writer(u'</b>\n    </li>\n\n    <li class="field text is-not-editable" id="field-course-organization">\n      <label for="course-organization">')
        __M_writer(filters.html_escape(filters.decode.utf8(_("Organization:"))))
        __M_writer(u'</label>\n      <b>')
        __M_writer(filters.html_escape(filters.decode.utf8( section_data['course_org'])))
        __M_writer(u'</b>\n    </li>\n\n    <li class="field text is-not-editable" id="field-course-start-date">\n      <label for="course-start-date">')
        __M_writer(filters.html_escape(filters.decode.utf8(_("Course Start Date:"))))
        __M_writer(u'</label>\n      <b class="localized-datetime" data-datetime="')
        __M_writer(filters.html_escape(filters.decode.utf8(section_data['start_date'])))
        __M_writer(u'" data-timezone="')
        __M_writer(filters.html_escape(filters.decode.utf8(user_timezone)))
        __M_writer(u'" data-language="')
        __M_writer(filters.html_escape(filters.decode.utf8(user_language)))
        __M_writer(u'"></b>\n    </li>\n\n    <li class="field text is-not-editable" id="field-course-end-date">\n      <label for="course-end-date">')
        __M_writer(filters.html_escape(filters.decode.utf8(_("Course End Date:"))))
        __M_writer(u'</label>\n')
        if course.end is None:
            __M_writer(u'            <b>')
            __M_writer(filters.html_escape(filters.decode.utf8(_("No end date set"))))
            __M_writer(u'</b>\n')
        else:
            __M_writer(u'            <b class="localized-datetime" data-datetime="')
            __M_writer(filters.html_escape(filters.decode.utf8(section_data['end_date'])))
            __M_writer(u'" data-timezone="')
            __M_writer(filters.html_escape(filters.decode.utf8(user_timezone)))
            __M_writer(u'" data-language="')
            __M_writer(filters.html_escape(filters.decode.utf8(user_language)))
            __M_writer(u'"></b>\n')
        __M_writer(u'    </li>\n    <li class="field text is-not-editable" id="field-course-started">\n      <label for="start-date">')
        __M_writer(filters.html_escape(filters.decode.utf8(_("Has the course started?"))))
        __M_writer(u'</label>\n\n      <b>')
        __M_writer(filters.html_escape(filters.decode.utf8(_("Yes") if section_data['has_started'] else _("No"))))
        __M_writer(u'</b>\n\n    </li>\n\n    <li class="field text is-not-editable" id="field-course-ended">\n      <label for="start-date">')
        __M_writer(filters.html_escape(filters.decode.utf8(_("Has the course ended?"))))
        __M_writer(u'</label>\n')
        if section_data['has_ended']:
            __M_writer(u'      <b>')
            __M_writer(filters.html_escape(filters.decode.utf8(_("Yes"))))
            __M_writer(u'</b>\n')
        else:
            __M_writer(u'      <b>')
            __M_writer(filters.html_escape(filters.decode.utf8(_("No"))))
            __M_writer(u'</b>\n')
        __M_writer(u'    </li>\n\n    <li class="field text is-not-editable" id="field-course-num-sections">\n      <label for="course-num-sections">')
        __M_writer(filters.html_escape(filters.decode.utf8(_("Number of sections:"))))
        __M_writer(u'</label>\n      <b>')
        __M_writer(filters.html_escape(filters.decode.utf8( section_data['num_sections'] )))
        __M_writer(u'</b>\n    </li>\n\n    <li class="field text is-not-editable" id="field-grade-cutoffs">\n      <label for="start-date">')
        __M_writer(filters.html_escape(filters.decode.utf8(_("Grade Cutoffs:"))))
        __M_writer(u'</label>\n      <b>')
        __M_writer(filters.html_escape(filters.decode.utf8( section_data['grade_cutoffs'] )))
        __M_writer(u'</b>\n    </li>\n  </ul>\n\n')
        if settings.FEATURES.get('ENABLE_SYSADMIN_DASHBOARD', '') and user.is_staff:
            __M_writer(u'      <p>\n')
            __M_writer(u'        ')
            __M_writer(filters.html_escape(filters.decode.utf8(Text(_("View detailed Git import logs for this course {link_start}by clicking here{link_end}.")).format(
            link_start=HTML('<a href="{}">').format(section_data['detailed_gitlogs_url']),
            link_end=HTML('</a>')
        ))))
            __M_writer(u'\n      </p>\n')
        __M_writer(u'\n</div>\n\n')
        if settings.FEATURES.get('ENABLE_INSTRUCTOR_BACKGROUND_TASKS'):
            __M_writer(u'  <div class="running-tasks-container action-type-container">\n    <hr>\n    <h4 class="hd hd-4"> ')
            __M_writer(filters.html_escape(filters.decode.utf8(_("Pending Tasks"))))
            __M_writer(u' </h4>\n    <div class="running-tasks-section">\n      <p>')
            __M_writer(filters.html_escape(filters.decode.utf8(_("The status for any active tasks appears in a table below."))))
            __M_writer(u' </p>\n      <br />\n\n      <div class="running-tasks-table" data-endpoint="')
            __M_writer(filters.html_escape(filters.decode.utf8( section_data['list_instructor_tasks_url'] )))
            __M_writer(u'"></div>\n    </div>\n    <div class="no-pending-tasks-message"></div>\n  </div>\n\n')
        __M_writer(u'\n')
        if len(section_data['course_errors']):
            __M_writer(u'  <div class="course-errors-wrapper">\n    <hr>\n    <p>\n    <div class="toggle-wrapper">\n      <h4 class="hd hd-4 title">')
            __M_writer(filters.html_escape(filters.decode.utf8(_("Course Warnings"))))
            __M_writer(u':</h4>\n      <div class="triangle"></div>\n    </div>\n    <div class="course-errors-visibility-wrapper">\n')
            for error in section_data['course_errors']:
                __M_writer(u'        <div class="course-error">\n          <code class=course-error-first>  ')
                __M_writer(filters.html_escape(filters.decode.utf8( error[0] )))
                __M_writer(u' </code><br>\n          <code class=course-error-second> ')
                __M_writer(filters.html_escape(filters.decode.utf8( error[1] )))
                __M_writer(u' </code>\n        </div>\n')
            __M_writer(u'    </div>\n    <p>\n  </div>\n<br>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"16": 2, "21": 1, "32": 1, "33": 5, "34": 7, "35": 8, "36": 8, "37": 8, "38": 10, "39": 12, "40": 12, "44": 12, "45": 14, "46": 14, "47": 16, "48": 16, "49": 16, "50": 16, "51": 19, "52": 19, "53": 19, "54": 19, "55": 22, "56": 22, "57": 22, "58": 22, "59": 25, "60": 25, "61": 25, "62": 25, "63": 29, "64": 29, "65": 32, "66": 32, "67": 36, "68": 37, "69": 37, "70": 37, "71": 39, "72": 42, "73": 44, "74": 44, "75": 48, "76": 48, "77": 49, "78": 49, "79": 53, "80": 53, "81": 54, "82": 54, "83": 58, "84": 58, "85": 59, "86": 59, "87": 63, "88": 63, "89": 64, "90": 64, "91": 68, "92": 68, "93": 69, "94": 69, "95": 69, "96": 69, "97": 69, "98": 69, "99": 73, "100": 73, "101": 74, "102": 75, "103": 75, "104": 75, "105": 76, "106": 77, "107": 77, "108": 77, "109": 77, "110": 77, "111": 77, "112": 77, "113": 79, "114": 81, "115": 81, "116": 83, "117": 83, "118": 88, "119": 88, "120": 89, "121": 90, "122": 90, "123": 90, "124": 91, "125": 92, "126": 92, "127": 92, "128": 94, "129": 97, "130": 97, "131": 98, "132": 98, "133": 102, "134": 102, "135": 103, "136": 103, "137": 107, "138": 108, "139": 110, "140": 110, "144": 113, "145": 116, "146": 119, "147": 120, "148": 122, "149": 122, "150": 124, "151": 124, "152": 127, "153": 127, "154": 133, "155": 134, "156": 135, "157": 139, "158": 139, "159": 143, "160": 144, "161": 145, "162": 145, "163": 146, "164": 146, "165": 149, "171": 165}, "uri": "instructor/instructor_dashboard_2/course_info.html", "filename": "/home/nttlong/code/edx/apps/edx/edx-platform/xdj-gnol-lms-templates/instructor/instructor_dashboard_2/course_info.html"}
__M_END_METADATA
"""
