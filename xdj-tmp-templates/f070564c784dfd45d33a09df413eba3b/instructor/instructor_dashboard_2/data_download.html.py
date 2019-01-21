# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1548073810.0857
_enable_loop = True
_template_filename = u'/home/nttlong/code/edx/apps/edx/edx-platform/xdj-gnol-lms-templates/instructor/instructor_dashboard_2/data_download.html'
_template_uri = u'instructor/instructor_dashboard_2/data_download.html'
_source_encoding = 'utf-8'
_exports = []



from django.utils.translation import ugettext as _
from openedx.core.djangolib.markup import HTML, Text


def render_body(context,section_data,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs,section_data=section_data)
        disable_buttons = context.get('disable_buttons', UNDEFINED)
        settings = context.get('settings', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n')
        __M_writer(u'\n\n<div class="data-download-container action-type-container">\n  <div class="request-response-error msg msg-error copy" id="data-request-response-error"></div>\n\n\n  <br>\n  <p>')
        __M_writer(filters.html_escape(filters.decode.utf8(_("Click to display the grading configuration for the course. The grading configuration is the breakdown of graded subsections of the course (such as exams and problem sets), and can be changed on the 'Grading' page (under 'Settings') in Studio."))))
        __M_writer(u'</p>\n  <p><input type="button" name="dump-gradeconf" value="')
        __M_writer(filters.html_escape(filters.decode.utf8(_("Grading Configuration"))))
        __M_writer(u'" data-endpoint="')
        __M_writer(filters.html_escape(filters.decode.utf8( section_data['get_grading_config_url'] )))
        __M_writer(u'"></p>\n\n  <div class="data-display-text" id="data-grade-config-text"></div>\n  <br>\n\n  <p>')
        __M_writer(filters.html_escape(filters.decode.utf8(_("Click to download a CSV of anonymized student IDs:"))))
        __M_writer(u'</p>\n  <p><input type="button" name="list-anon-ids" value="')
        __M_writer(filters.html_escape(filters.decode.utf8(_("Get Student Anonymized IDs CSV"))))
        __M_writer(u'" data-csv="true" class="csv" data-endpoint="')
        __M_writer(filters.html_escape(filters.decode.utf8( section_data['get_anon_ids_url'] )))
        __M_writer(u'" class="')
        __M_writer(filters.html_escape(filters.decode.utf8('is-disabled' if disable_buttons else '')))
        __M_writer(u'" aria-disabled="')
        __M_writer(filters.html_escape(filters.decode.utf8('true' if disable_buttons else 'false')))
        __M_writer(u'" ></p>\n</div>\n\n')
        if settings.FEATURES.get('ENABLE_GRADE_DOWNLOADS'):
            __M_writer(u'  <div class="reports-download-container action-type-container">\n    <hr>\n    <h3 class="hd hd-3">')
            __M_writer(filters.html_escape(filters.decode.utf8(_("Reports"))))
            __M_writer(u'</h3>\n\n    <p>')
            __M_writer(filters.html_escape(filters.decode.utf8(_("For large courses, generating some reports can take several hours. When report generation is complete, a link that includes the date and time of generation appears in the table below. These reports are generated in the background, meaning it is OK to navigate away from this page while your report is generating."))))
            __M_writer(u'</p>\n\n    <p>')
            __M_writer(filters.html_escape(filters.decode.utf8(_("Please be patient and do not click these buttons multiple times. Clicking these buttons multiple times will significantly slow the generation process."))))
            __M_writer(u'</p>\n\n    <p>')
            __M_writer(filters.html_escape(filters.decode.utf8(_("Click to generate a CSV file of all students enrolled in this course, along with profile information such as email address and username:"))))
            __M_writer(u'</p>\n\n    <p><input type="button" name="list-profiles-csv" value="')
            __M_writer(filters.html_escape(filters.decode.utf8(_("Download profile information as a CSV"))))
            __M_writer(u'" data-endpoint="')
            __M_writer(filters.html_escape(filters.decode.utf8( section_data['get_students_features_url'] )))
            __M_writer(u'" data-csv="true"></p>\n\n    <p>')
            __M_writer(filters.html_escape(filters.decode.utf8(_("Click to generate a CSV file that lists learners who can enroll in the course but have not yet done so."))))
            __M_writer(u'</p>\n\n    <p><input type="button" name="list-may-enroll-csv" value="')
            __M_writer(filters.html_escape(filters.decode.utf8(_("Download a CSV of learners who can enroll"))))
            __M_writer(u'" data-endpoint="')
            __M_writer(filters.html_escape(filters.decode.utf8( section_data['get_students_who_may_enroll_url'] )))
            __M_writer(u'" data-csv="true"></p>\n\n')
            if section_data['show_generate_proctored_exam_report_button']:
                __M_writer(u'      <p>')
                __M_writer(filters.html_escape(filters.decode.utf8(_("Click to generate a CSV file of all proctored exam results in this course."))))
                __M_writer(u'</p>\n      <p><input type="button" name="proctored-exam-results-report" value="')
                __M_writer(filters.html_escape(filters.decode.utf8(_("Generate Proctored Exam Results Report"))))
                __M_writer(u'" data-endpoint="')
                __M_writer(filters.html_escape(filters.decode.utf8( section_data['list_proctored_results_url'] )))
                __M_writer(u'"/></p>\n')
            __M_writer(u'\n')
            if section_data['course_has_survey']:
                __M_writer(u'      <p>')
                __M_writer(filters.html_escape(filters.decode.utf8(_("Click to generate a CSV file of survey results for this course."))))
                __M_writer(u'</p>\n      <p><input type="button" name="survey-results-report" value="')
                __M_writer(filters.html_escape(filters.decode.utf8(_("Generate Survey Results Report"))))
                __M_writer(u'" data-endpoint="')
                __M_writer(filters.html_escape(filters.decode.utf8( section_data['course_survey_results_url'] )))
                __M_writer(u'"/></p>\n')
            __M_writer(u'\n    <p>')
            __M_writer(filters.html_escape(filters.decode.utf8(_("To generate a CSV file that lists all student answers to a given problem, enter the location of the problem (from its Staff Debug Info)."))))
            __M_writer(u'</p>\n\n    <p>\n      <label>\n        <span>')
            __M_writer(filters.html_escape(filters.decode.utf8(_("Problem location: "))))
            __M_writer(u'</span>\n        <input type="text" name="problem-location" />\n      </label>\n    </p>\n    <p>\n      <input type="button" name="list-problem-responses-csv" value="')
            __M_writer(filters.html_escape(filters.decode.utf8(_("Download a CSV of problem responses"))))
            __M_writer(u'" data-endpoint="')
            __M_writer(filters.html_escape(filters.decode.utf8( section_data['get_problem_responses_url'] )))
            __M_writer(u'" data-csv="true">\n    </p>\n\n    <div class="issued_certificates">\n      <p>')
            __M_writer(filters.html_escape(filters.decode.utf8(_("Click to list certificates that are issued for this course:"))))
            __M_writer(u'</p>\n      <p>\n        <input type="button" name="issued-certificates-list" value="')
            __M_writer(filters.html_escape(filters.decode.utf8(_("View Certificates Issued"))))
            __M_writer(u'" data-csv="false" data-endpoint="')
            __M_writer(filters.html_escape(filters.decode.utf8( section_data['get_issued_certificates_url'] )))
            __M_writer(u'">\n        <input type="button" name="issued-certificates-csv" value="')
            __M_writer(filters.html_escape(filters.decode.utf8(_("Download CSV of Certificates Issued"))))
            __M_writer(u'" data-csv="true" data-endpoint="')
            __M_writer(filters.html_escape(filters.decode.utf8( section_data['get_issued_certificates_url'] )))
            __M_writer(u'">\n      </p>\n      <div class="data-display-table certificate-data-display-table" id="data-issued-certificates-table"></div>\n      <div class="issued-certificates-error request-response-error msg msg-error copy"></div>\n    </div>\n\n')
            if not disable_buttons:
                __M_writer(u'    <p>')
                __M_writer(filters.html_escape(filters.decode.utf8(_("For smaller courses, click to list profile information for enrolled students directly on this page:"))))
                __M_writer(u'</p>\n    <p><input type="button" name="list-profiles" value="')
                __M_writer(filters.html_escape(filters.decode.utf8(_("List enrolled students' profile information"))))
                __M_writer(u'" data-endpoint="')
                __M_writer(filters.html_escape(filters.decode.utf8( section_data['get_students_features_url'] )))
                __M_writer(u'"></p>\n')
            __M_writer(u'  <div class="data-display-table profile-data-display-table" id="data-student-profiles-table"></div>\n\n')
            if settings.FEATURES.get('ALLOW_COURSE_STAFF_GRADE_DOWNLOADS') or section_data['access']['admin']:
                __M_writer(u'    <p>')
                __M_writer(filters.html_escape(filters.decode.utf8(_("Click to generate a CSV grade report for all currently enrolled students."))))
                __M_writer(u'</p>\n    <p>\n      <input type="button" name="calculate-grades-csv" class="async-report-btn" value="')
                __M_writer(filters.html_escape(filters.decode.utf8(_("Generate Grade Report"))))
                __M_writer(u'" data-endpoint="')
                __M_writer(filters.html_escape(filters.decode.utf8( section_data['calculate_grades_csv_url'] )))
                __M_writer(u'"/>\n      <input type="button" name="problem-grade-report" class="async-report-btn" value="')
                __M_writer(filters.html_escape(filters.decode.utf8(_("Generate Problem Grade Report"))))
                __M_writer(u'" data-endpoint="')
                __M_writer(filters.html_escape(filters.decode.utf8( section_data['problem_grade_report_url'] )))
                __M_writer(u'"/>\n      <input type="button" name="export-ora2-data" class="async-report-btn" value="')
                __M_writer(filters.html_escape(filters.decode.utf8(_("Generate ORA Data Report"))))
                __M_writer(u'" data-endpoint="')
                __M_writer(filters.html_escape(filters.decode.utf8( section_data['export_ora2_data_url'] )))
                __M_writer(u'"/>\n    </p>\n')
            __M_writer(u'\n    <div class="request-response msg msg-confirm copy" id="report-request-response"></div>\n    <div class="request-response-error msg msg-error copy" id="report-request-response-error"></div>\n    <br>\n\n    <h3 class="hd hd-3">')
            __M_writer(filters.html_escape(filters.decode.utf8(_("Reports Available for Download"))))
            __M_writer(u'</h3>\n    <p>\n      ')
            __M_writer(filters.html_escape(filters.decode.utf8(_("The reports listed below are available for download. A link to every report remains available on this page, identified by the UTC date and time of generation. Reports are not deleted, so you will always be able to access previously generated reports from this page."))))
            __M_writer(u'\n    </p>\n\n')
            if settings.FEATURES.get('ENABLE_ASYNC_ANSWER_DISTRIBUTION'):
                __M_writer(u'    <p>\n      ')
                __M_writer(filters.html_escape(filters.decode.utf8(_("The answer distribution report listed below is generated periodically by an automated background process. The report is cumulative, so answers submitted after the process starts are included in a subsequent report. The report is generated several times per day."))))
                __M_writer(u'\n    </p>\n')
            __M_writer(u'\n')
            __M_writer(u'    <p>\n        ')
            __M_writer(filters.html_escape(filters.decode.utf8(Text(_("{strong_start}Note{strong_end}: To keep student data secure, you cannot save or email these links for direct access. Copies of links expire within 5 minutes.")).format(
            strong_start=HTML("<strong>"),
            strong_end=HTML("</strong>"),
        ))))
            __M_writer(u'\n    </p><br>\n\n    <div class="report-downloads-table" id="report-downloads-table" data-endpoint="')
            __M_writer(filters.html_escape(filters.decode.utf8( section_data['list_report_downloads_url'] )))
            __M_writer(u'" ></div>\n  </div>\n')
        __M_writer(u'\n')
        if settings.FEATURES.get('ENABLE_INSTRUCTOR_BACKGROUND_TASKS'):
            __M_writer(u'  <div class="running-tasks-container action-type-container">\n    <hr>\n    <h3 class="hd hd-3">')
            __M_writer(filters.html_escape(filters.decode.utf8(_("Pending Tasks"))))
            __M_writer(u'</h3>\n    <div class="running-tasks-section">\n      <p>')
            __M_writer(filters.html_escape(filters.decode.utf8(_("The status for any active tasks appears in a table below."))))
            __M_writer(u' </p>\n      <br />\n      <div class="running-tasks-table" data-endpoint="')
            __M_writer(filters.html_escape(filters.decode.utf8( section_data['list_instructor_tasks_url'] )))
            __M_writer(u'"></div>\n    </div>\n    <div class="no-pending-tasks-message"></div>\n  </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"16": 2, "21": 1, "28": 1, "29": 5, "30": 12, "31": 12, "32": 13, "33": 13, "34": 13, "35": 13, "36": 18, "37": 18, "38": 19, "39": 19, "40": 19, "41": 19, "42": 19, "43": 19, "44": 19, "45": 19, "46": 22, "47": 23, "48": 25, "49": 25, "50": 27, "51": 27, "52": 29, "53": 29, "54": 31, "55": 31, "56": 33, "57": 33, "58": 33, "59": 33, "60": 35, "61": 35, "62": 37, "63": 37, "64": 37, "65": 37, "66": 39, "67": 40, "68": 40, "69": 40, "70": 41, "71": 41, "72": 41, "73": 41, "74": 43, "75": 44, "76": 45, "77": 45, "78": 45, "79": 46, "80": 46, "81": 46, "82": 46, "83": 48, "84": 49, "85": 49, "86": 53, "87": 53, "88": 58, "89": 58, "90": 58, "91": 58, "92": 62, "93": 62, "94": 64, "95": 64, "96": 64, "97": 64, "98": 65, "99": 65, "100": 65, "101": 65, "102": 71, "103": 72, "104": 72, "105": 72, "106": 73, "107": 73, "108": 73, "109": 73, "110": 75, "111": 77, "112": 78, "113": 78, "114": 78, "115": 80, "116": 80, "117": 80, "118": 80, "119": 81, "120": 81, "121": 81, "122": 81, "123": 82, "124": 82, "125": 82, "126": 82, "127": 85, "128": 90, "129": 90, "130": 92, "131": 92, "132": 95, "133": 96, "134": 97, "135": 97, "136": 100, "137": 102, "138": 103, "142": 106, "143": 109, "144": 109, "145": 112, "146": 113, "147": 114, "148": 116, "149": 116, "150": 118, "151": 118, "152": 120, "153": 120, "159": 153}, "uri": "instructor/instructor_dashboard_2/data_download.html", "filename": "/home/nttlong/code/edx/apps/edx/edx-platform/xdj-gnol-lms-templates/instructor/instructor_dashboard_2/data_download.html"}
__M_END_METADATA
"""
