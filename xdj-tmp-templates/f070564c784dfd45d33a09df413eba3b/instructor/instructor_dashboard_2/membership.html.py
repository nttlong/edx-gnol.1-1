# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1548073809.945628
_enable_loop = True
_template_filename = u'/home/nttlong/code/edx/apps/edx/edx-platform/xdj-gnol-lms-templates/instructor/instructor_dashboard_2/membership.html'
_template_uri = u'instructor/instructor_dashboard_2/membership.html'
_source_encoding = 'utf-8'
_exports = []



from django.utils.translation import ugettext as _
from django.utils.translation import pgettext
from openedx.core.djangolib.markup import HTML, Text


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace(u'static', context._clean_inheritance_tokens(), templateuri=u'/x-static-content.html', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, u'static')] = ns

def render_body(context,section_data,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs,section_data=section_data)
        csrf_token = context.get('csrf_token', UNDEFINED)
        static = _mako_get_namespace(context, 'static')
        settings = context.get('settings', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n')
        __M_writer(u'\n')
        __M_writer(u'\n<fieldset class="batch-enrollment membership-section">\n    <legend id="heading-batch-enrollment" class="hd hd-3">')
        __M_writer(filters.html_escape(filters.decode.utf8(_("Batch Enrollment"))))
        __M_writer(u'</legend>\n    <label>\n        ')
        __M_writer(filters.html_escape(filters.decode.utf8(_("Enter email addresses and/or usernames separated by new lines or commas."))))
        __M_writer(u'\n        ')
        __M_writer(filters.html_escape(filters.decode.utf8(_("You will not get notification for emails that bounce, so please double-check spelling."))))
        __M_writer(u'\n        <textarea rows="6" name="student-ids" placeholder="')
        __M_writer(filters.html_escape(filters.decode.utf8(_("Email Addresses/Usernames"))))
        __M_writer(u'" spellcheck="false"></textarea>\n    </label>\n\n    <div class="role">\n        <label>\n            ')
        __M_writer(filters.html_escape(filters.decode.utf8(_("Role of the users being enrolled."))))
        __M_writer(u'\n            <select name="role">\n')
        for role in section_data['enrollment_role_choices']:
            __M_writer(u'                  <option value="')
            __M_writer(filters.html_escape(filters.decode.utf8(role)))
            __M_writer(u'">')
            __M_writer(filters.html_escape(filters.decode.utf8(role)))
            __M_writer(u'</option>\n')
        __M_writer(u'            </select>\n        </label>\n    </div>\n\n    <label>\n        ')
        __M_writer(filters.html_escape(filters.decode.utf8(_("Enter the reason why the students are to be manually enrolled or unenrolled."))))
        __M_writer(u'\n        ')
        __M_writer(filters.html_escape(filters.decode.utf8(_("This cannot be left blank and will be recorded and presented in Enrollment Reports."))))
        __M_writer(u'\n        ')
        __M_writer(filters.html_escape(filters.decode.utf8(_("Therefore, please give enough detail to account for this action."))))
        __M_writer(u'\n        <textarea rows="2" id="reason-field-id" name="reason-field" placeholder="')
        __M_writer(filters.html_escape(filters.decode.utf8(_('Reason'))))
        __M_writer(u'" spellcheck="false"></textarea>\n    </label>\n    <div class="enroll-option">\n        <label class="has-hint">\n            <input type="checkbox" name="auto-enroll" id="auto-enroll" value="Auto-Enroll" checked="yes" aria-describedby="heading-batch-enrollment">\n            <span class="label-text">')
        __M_writer(filters.html_escape(filters.decode.utf8(_("Auto Enroll"))))
        __M_writer(u'</span>\n            <div class="hint auto-enroll-hint">\n                <span class="hint-caret"></span>\n                <p id="auto-enroll-tip">\n                    ')
        __M_writer(filters.html_escape(filters.decode.utf8(Text(_("If this option is {em_start}checked{em_end}, users who have not yet registered for {platform_name} will be automatically enrolled.")).format(em_start=HTML('<em>'), em_end=HTML('</em>'), platform_name=settings.PLATFORM_NAME))))
        __M_writer(u'\n                    ')
        __M_writer(filters.html_escape(filters.decode.utf8(Text(_("If this option is left {em_start}unchecked{em_end}, users who have not yet registered for {platform_name} will not be enrolled, but will be allowed to enroll once they make an account.")).format(em_start=HTML('<em>'), em_end=HTML('</em>'), platform_name=settings.PLATFORM_NAME))))
        __M_writer(u'\n                    <br /><br />\n                    ')
        __M_writer(filters.html_escape(filters.decode.utf8(_("Checking this box has no effect if 'Unenroll' is selected."))))
        __M_writer(u'\n                </p>\n            </div>\n        </label>\n    </div>\n    <div class="enroll-option">\n        <label class="has-hint">\n          <input type="checkbox" name="email-students" id="email-students" value="Notify-students-by-email" aria-describedby="heading-batch-enrollment"\n                 ')
        __M_writer(filters.html_escape(filters.decode.utf8('checked="yes"' if settings.FEATURES.get('BATCH_ENROLLMENT_NOTIFY_USERS_DEFAULT') else '')))
        __M_writer(u'>\n            <span class="label-text">')
        __M_writer(filters.html_escape(filters.decode.utf8(_("Notify users by email"))))
        __M_writer(u'</span>\n            <div class="hint email-students-hint">\n                <span class="hint-caret"></span>\n                <p id="email-students-tip">\n                    ')
        __M_writer(filters.html_escape(filters.decode.utf8(Text(_("If this option is {em_start}checked{em_end}, users will receive an email notification.")).format(em_start=HTML('<em>'), em_end=HTML('</em>')))))
        __M_writer(u'\n                </p>\n            </div>\n        </label>\n    </div>\n    <div>\n        <input type="button" name="enrollment-button" class="enrollment-button" value="')
        __M_writer(filters.html_escape(filters.decode.utf8(pgettext('someone','Enroll'))))
        __M_writer(u'" data-endpoint="')
        __M_writer(filters.html_escape(filters.decode.utf8( section_data['enroll_button_url'] )))
        __M_writer(u'" data-action="enroll" >\n        <input type="button" name="enrollment-button" class="enrollment-button" value="')
        __M_writer(filters.html_escape(filters.decode.utf8(_("Unenroll"))))
        __M_writer(u'" data-endpoint="')
        __M_writer(filters.html_escape(filters.decode.utf8( section_data['unenroll_button_url'] )))
        __M_writer(u'" data-action="unenroll" >\n    </div>\n    <div class="request-response"></div>\n    <div class="request-response-error"></div>\n</fieldset>\n\n')
        if static.get_value('ALLOW_AUTOMATED_SIGNUPS', settings.FEATURES.get('ALLOW_AUTOMATED_SIGNUPS', False)):
            __M_writer(u'<hr class="divider" />\n\n  <div class="auto_enroll auto_enroll_csv membership-section">\n    <h3 class="hd hd-3">')
            __M_writer(filters.html_escape(filters.decode.utf8(_("Register/Enroll Students"))))
            __M_writer(u'</h3>\n    <p>')
            __M_writer(filters.html_escape(filters.decode.utf8(_("To register and enroll a list of users in this course, choose a CSV file that contains the following columns in this exact order: email, username, name, and country. Please include one student per row and do not include any headers, footers, or blank lines."))))
            __M_writer(u'</p>\n    <form id="student-auto-enroll-form" method="post" action="')
            __M_writer(filters.html_escape(filters.decode.utf8( section_data['upload_student_csv_button_url'] )))
            __M_writer(u'" enctype="multipart/form-data">\n      <div class="customBrowseBtn">\n        <label for="browseBtn-auto-enroll">')
            __M_writer(filters.html_escape(filters.decode.utf8(_("Upload a CSV for bulk enrollment"))))
            __M_writer(u'</label>\n        <span id="browseFile" class="enhanced-input-file"></span>\n        <div class="file-browse btn btn-primary" aria-hidden="true">\n            <span class="browse">')
            __M_writer(filters.html_escape(filters.decode.utf8(('Browse'))))
            __M_writer(u'</span>\n            <input class="file_field" id="browseBtn-auto-enroll" name="students_list" type="file" accept=".csv"/>\n        </div>\n      </div>\n      <button type="submit" class="btn-blue" id="submitBtn-auto_enroll_csv" name="enrollment_signup_button">')
            __M_writer(filters.html_escape(filters.decode.utf8(_("Upload CSV"))))
            __M_writer(u'</button>\n      <input type="hidden" name="csrfmiddlewaretoken" value="')
            __M_writer(filters.html_escape(filters.decode.utf8( csrf_token )))
            __M_writer(u'">\n    </form>\n    <div class="results"></div>\n</div>\n')
        __M_writer(u'\n<hr class="divider" />\n\n')
        if section_data['access']['instructor']:
            __M_writer(u'<fieldset class="batch-beta-testers membership-section">\n    <legend id="heading-batch-beta-testers" class="hd hd-3">')
            __M_writer(filters.html_escape(filters.decode.utf8(_("Batch Beta Tester Addition"))))
            __M_writer(u'</legend>\n    <label>\n        ')
            __M_writer(filters.html_escape(filters.decode.utf8(_("Enter email addresses and/or usernames separated by new lines or commas."))))
            __M_writer(u'<br/>\n        ')
            __M_writer(filters.html_escape(filters.decode.utf8(_("Note: Users must have an activated {platform_name} account before they can be enrolled as beta testers.").format(platform_name=settings.PLATFORM_NAME))))
            __M_writer(u'\n        <textarea rows="6" cols="50" name="student-ids-for-beta" placeholder="')
            __M_writer(filters.html_escape(filters.decode.utf8(_("Email Addresses/Usernames"))))
            __M_writer(u'" spellcheck="false"></textarea>\n    </label>\n    <div class="enroll-option">\n        <label class="has-hint">\n            <input type="checkbox" name="auto-enroll-beta" id="auto-enroll-beta" value="Auto-Enroll" checked="yes" aria-describedby="heading-batch-beta-testers">\n            <span class="label-text">')
            __M_writer(filters.html_escape(filters.decode.utf8(_("Auto Enroll"))))
            __M_writer(u'</span>\n            <div class="hint auto-enroll-beta-hint">\n                <span class="hint-caret"></span>\n                <p id="auto-enroll-beta-tip">\n                    ')
            __M_writer(filters.html_escape(filters.decode.utf8(Text(_("If this option is {em_start}checked{em_end}, users who have not enrolled in your course will be automatically enrolled.")).format(em_start=HTML('<em>'), em_end=HTML('</em>')))))
            __M_writer(u'\n                    <br /><br />\n                    ')
            __M_writer(filters.html_escape(filters.decode.utf8(_("Checking this box has no effect if 'Remove beta testers' is selected."))))
            __M_writer(u'\n                </p>\n            </div>\n        </label>\n    </div>\n    <div class="enroll-option">\n        <label class="has-hint">\n            <input type="checkbox" name="email-students-beta" id="email-students-beta" value="Notify-students-by-email" checked="yes" aria-describedby="heading-batch-beta-testers">\n            <span class="label-text">')
            __M_writer(filters.html_escape(filters.decode.utf8(_("Notify users by email"))))
            __M_writer(u'</span>\n            <div class="hint email-students-beta-hint">\n                <span class="hint-caret"></span>\n                <p id="email-students-beta-tip">\n                    ')
            __M_writer(filters.html_escape(filters.decode.utf8(Text(_("If this option is {em_start}checked{em_end}, users will receive an email notification.")).format(em_start=HTML('<em>'), em_end=HTML('</em>')))))
            __M_writer(u'\n                </p>\n            </div>\n        </label>\n    </div>\n    <div>\n        <input type="button" name="beta-testers" class="enrollment-button" value="')
            __M_writer(filters.html_escape(filters.decode.utf8(_("Add beta testers"))))
            __M_writer(u'" data-endpoint="')
            __M_writer(filters.html_escape(filters.decode.utf8( section_data['modify_beta_testers_button_url'] )))
            __M_writer(u'" data-action="add" >\n        <input type="button" name="beta-testers" class="enrollment-button" value="')
            __M_writer(filters.html_escape(filters.decode.utf8(_("Remove beta testers"))))
            __M_writer(u'" data-endpoint="')
            __M_writer(filters.html_escape(filters.decode.utf8( section_data['modify_beta_testers_button_url'] )))
            __M_writer(u'" data-action="remove" >\n    </div>\n    <div class="request-response"></div>\n    <div class="request-response-error"></div>\n</fieldset>\n\n<hr class="divider" />\n')
        __M_writer(u'\n<div class="member-lists-management membership-section" aria-live="polite">\n')
        __M_writer(u'  <h3 class="hd hd-3">')
        __M_writer(filters.html_escape(filters.decode.utf8(_("Course Team Management"))))
        __M_writer(u'</h3>\n\n  <div class="request-response-error"></div>\n\n  <div class="wrapper-member-select">\n')
        __M_writer(u'    <label>')
        __M_writer(filters.html_escape(filters.decode.utf8(_("Select a course team role:"))))
        __M_writer(u'\n        <select id="member-lists-selector" class="member-lists-selector">\n          <option> ')
        __M_writer(filters.html_escape(filters.decode.utf8(_("Getting available lists..."))))
        __M_writer(u' </option>\n        </select>\n    </label>\n  </div>\n\n\n')
        if not section_data['access']['instructor']:
            __M_writer(u'    <p>\n      ')
            __M_writer(filters.html_escape(filters.decode.utf8(_("Staff cannot modify these lists. To manage course team membership, "
      "a course Admin must give you the Admin role to add Staff or Beta Testers, "
      "or the Discussion Admin role to add discussion moderators and TAs."))))
            __M_writer(u'\n    </p>\n')
        __M_writer(u'\n')
        if section_data['access']['instructor']:
            __M_writer(u'    <div class="auth-list-container"\n      data-rolename="staff"\n      data-display-name="')
            __M_writer(filters.html_escape(filters.decode.utf8(_("Staff"))))
            __M_writer(u'"\n      data-info-text="\n        ')
            __M_writer(filters.html_escape(filters.decode.utf8(_("Course team members with the Staff role help you manage your course. "
        "Staff can enroll and unenroll learners, as well as modify their grades and "
        "access all course data. Staff also have access to your course in Studio and "
        "Insights. You can only give course team roles to enrolled users."))))
            __M_writer(u'"\n      data-list-endpoint="')
            __M_writer(filters.html_escape(filters.decode.utf8( section_data['list_course_role_members_url'] )))
            __M_writer(u'"\n      data-modify-endpoint="')
            __M_writer(filters.html_escape(filters.decode.utf8( section_data['modify_access_url'] )))
            __M_writer(u'"\n      data-add-button-label="')
            __M_writer(filters.html_escape(filters.decode.utf8(_("Add Staff"))))
            __M_writer(u'"\n    ></div>\n\n')
            __M_writer(u'    <div class="auth-list-container"\n      data-rolename="instructor"\n      data-display-name="')
            __M_writer(filters.html_escape(filters.decode.utf8(_("Admin"))))
            __M_writer(u'"\n      data-info-text="\n        ')
            __M_writer(filters.html_escape(filters.decode.utf8(_("Course team members with the Admin role help you manage your course. "
          "They can do all of the tasks that Staff can do, and can also add and "
          "remove the Staff and Admin roles, discussion moderation roles, and the "
          "beta tester role to manage course team membership. You can only give "
          "course team roles to enrolled users."))))
            __M_writer(u'"\n      data-list-endpoint="')
            __M_writer(filters.html_escape(filters.decode.utf8( section_data['list_course_role_members_url'] )))
            __M_writer(u'"\n      data-modify-endpoint="')
            __M_writer(filters.html_escape(filters.decode.utf8( section_data['modify_access_url'] )))
            __M_writer(u'"\n      data-add-button-label="')
            __M_writer(filters.html_escape(filters.decode.utf8(_("Add Admin"))))
            __M_writer(u'"\n    >\n    </div>\n\n    <div class="auth-list-container"\n      data-rolename="beta"\n      data-display-name="')
            __M_writer(filters.html_escape(filters.decode.utf8(_("Beta Testers"))))
            __M_writer(u'"\n      data-info-text="\n        ')
            __M_writer(filters.html_escape(filters.decode.utf8(_("Beta Testers can see course content before other learners. "
        "They can make sure that the content works, but have no additional "
        "privileges. You can only give course team roles to enrolled users."))))
            __M_writer(u'"\n      data-list-endpoint="')
            __M_writer(filters.html_escape(filters.decode.utf8( section_data['list_course_role_members_url'] )))
            __M_writer(u'"\n      data-modify-endpoint="')
            __M_writer(filters.html_escape(filters.decode.utf8( section_data['modify_access_url'] )))
            __M_writer(u'"\n      data-add-button-label="')
            __M_writer(filters.html_escape(filters.decode.utf8(_("Add Beta Tester"))))
            __M_writer(u'"\n    ></div>\n\n    <div class="auth-list-container"\n      data-rolename="Administrator"\n      data-display-name="')
            __M_writer(filters.html_escape(filters.decode.utf8(_("Discussion Admins"))))
            __M_writer(u'"\n      data-info-text="\n        ')
            __M_writer(filters.html_escape(filters.decode.utf8(_("Discussion Admins can edit or delete any post, clear misuse flags, close "
         "and re-open threads, endorse responses, and see posts from all groups. "
         "Their posts are marked as 'staff'. They can also add and remove the "
         "discussion moderation roles to manage course team membership. Only "
         "enrolled users can be added as Discussion Admins."))))
            __M_writer(u'"\n      data-list-endpoint="')
            __M_writer(filters.html_escape(filters.decode.utf8( section_data['list_forum_members_url'] )))
            __M_writer(u'"\n      data-modify-endpoint="')
            __M_writer(filters.html_escape(filters.decode.utf8( section_data['update_forum_role_membership_url'] )))
            __M_writer(u'"\n      data-add-button-label="')
            __M_writer(filters.html_escape(filters.decode.utf8(_("Add Discussion Admin"))))
            __M_writer(u'"\n    ></div>\n')
        __M_writer(u'\n')
        if section_data['access']['instructor'] or section_data['access']['forum_admin']:
            __M_writer(u'    <div class="auth-list-container"\n      data-rolename="Moderator"\n      data-display-name="')
            __M_writer(filters.html_escape(filters.decode.utf8(_("Discussion Moderators"))))
            __M_writer(u'"\n      data-info-text="\n        ')
            __M_writer(filters.html_escape(filters.decode.utf8(_("Discussion Moderators can edit or delete any post, clear misuse flags, close "
         "and re-open threads, endorse responses, and see posts from all groups. "
         "Their posts are marked as 'staff'. They cannot manage course team membership by "
         "adding or removing discussion moderation roles. Only enrolled users can be "
         "added as Discussion Moderators."))))
            __M_writer(u'"\n      data-list-endpoint="')
            __M_writer(filters.html_escape(filters.decode.utf8( section_data['list_forum_members_url'] )))
            __M_writer(u'"\n      data-modify-endpoint="')
            __M_writer(filters.html_escape(filters.decode.utf8( section_data['update_forum_role_membership_url'] )))
            __M_writer(u'"\n      data-add-button-label="')
            __M_writer(filters.html_escape(filters.decode.utf8(_("Add Moderator"))))
            __M_writer(u'"\n    ></div>\n\n    <div class="auth-list-container"\n      data-rolename="Group Moderator"\n      data-display-name="')
            __M_writer(filters.html_escape(filters.decode.utf8(_("Group Community TA"))))
            __M_writer(u'"\n      data-info-text="\n        ')
            __M_writer(filters.html_escape(filters.decode.utf8(_("Group Community TAs are members of the community who help course teams moderate discussions. Group "
            "Community TAs see only posts by learners in their assigned group. They can edit or delete posts, "
            "clear flags, close and re-open threads, and endorse responses, but only for posts by learners in "
            "their group. Their posts are marked as 'Community TA'. Only enrolled learners can be added as Group "
            "Community TAs."))))
            __M_writer(u'"\n      data-list-endpoint="')
            __M_writer(filters.html_escape(filters.decode.utf8( section_data['list_forum_members_url'] )))
            __M_writer(u'"\n      data-modify-endpoint="')
            __M_writer(filters.html_escape(filters.decode.utf8( section_data['update_forum_role_membership_url'] )))
            __M_writer(u'"\n      data-add-button-label="')
            __M_writer(filters.html_escape(filters.decode.utf8(_("Add Group Community TA"))))
            __M_writer(u'"\n    ></div>\n\n    <div class="auth-list-container"\n      data-rolename="Community TA"\n      data-display-name="')
            __M_writer(filters.html_escape(filters.decode.utf8(_("Community TA"))))
            __M_writer(u'"\n      data-info-text="\n        ')
            __M_writer(filters.html_escape(filters.decode.utf8(_("Community TAs are members of the community who help course teams moderate discussions. "
        "They can see posts by learners in their assigned cohort or enrollment track, and can edit or delete posts, "
        "clear flags, close or re-open threads, and endorse responses. Their posts are marked as 'Community TA'. "
        "Only enrolled learners can be added as Community TAs."))))
            __M_writer(u'"\n      data-list-endpoint="')
            __M_writer(filters.html_escape(filters.decode.utf8( section_data['list_forum_members_url'] )))
            __M_writer(u'"\n      data-modify-endpoint="')
            __M_writer(filters.html_escape(filters.decode.utf8( section_data['update_forum_role_membership_url'] )))
            __M_writer(u'"\n      data-add-button-label="')
            __M_writer(filters.html_escape(filters.decode.utf8(_("Add Community TA"))))
            __M_writer(u'"\n    ></div>\n')
        __M_writer(u'\n')
        if section_data['access']['instructor'] and section_data['ccx_is_enabled']:
            __M_writer(u'    <div class="auth-list-container"\n      data-rolename="ccx_coach"\n      data-display-name="')
            __M_writer(filters.html_escape(filters.decode.utf8(_("CCX Coaches"))))
            __M_writer(u'"\n      data-info-text="\n        ')
            __M_writer(filters.html_escape(filters.decode.utf8(_("CCX Coaches are able to create their own Custom Courses "
            "based on this course, which they can use to provide personalized "
            "instruction to their own students based in this course material."))))
            __M_writer(u'"\n      data-list-endpoint="')
            __M_writer(filters.html_escape(filters.decode.utf8(section_data['list_course_role_members_url'])))
            __M_writer(u'"\n      data-modify-endpoint="')
            __M_writer(filters.html_escape(filters.decode.utf8(section_data['modify_access_url'])))
            __M_writer(u'"\n      data-add-button-label="')
            __M_writer(filters.html_escape(filters.decode.utf8(_("Add CCX Coach"))))
            __M_writer(u'"\n    ></div>\n')
        __M_writer(u'</div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"16": 3, "29": 2, "32": 1, "40": 1, "41": 2, "42": 7, "43": 9, "44": 9, "45": 11, "46": 11, "47": 12, "48": 12, "49": 13, "50": 13, "51": 18, "52": 18, "53": 20, "54": 21, "55": 21, "56": 21, "57": 21, "58": 21, "59": 23, "60": 28, "61": 28, "62": 29, "63": 29, "64": 30, "65": 30, "66": 31, "67": 31, "68": 36, "69": 36, "70": 40, "71": 40, "72": 41, "73": 41, "74": 43, "75": 43, "76": 51, "77": 51, "78": 52, "79": 52, "80": 56, "81": 56, "82": 62, "83": 62, "84": 62, "85": 62, "86": 63, "87": 63, "88": 63, "89": 63, "90": 69, "91": 70, "92": 73, "93": 73, "94": 74, "95": 74, "96": 75, "97": 75, "98": 77, "99": 77, "100": 80, "101": 80, "102": 84, "103": 84, "104": 85, "105": 85, "106": 90, "107": 93, "108": 94, "109": 95, "110": 95, "111": 97, "112": 97, "113": 98, "114": 98, "115": 99, "116": 99, "117": 104, "118": 104, "119": 108, "120": 108, "121": 110, "122": 110, "123": 118, "124": 118, "125": 122, "126": 122, "127": 128, "128": 128, "129": 128, "130": 128, "131": 129, "132": 129, "133": 129, "134": 129, "135": 137, "136": 140, "137": 140, "138": 140, "139": 146, "140": 146, "141": 146, "142": 148, "143": 148, "144": 154, "145": 155, "146": 156, "149": 158, "150": 161, "151": 162, "152": 163, "153": 165, "154": 165, "155": 167, "159": 170, "160": 171, "161": 171, "162": 172, "163": 172, "164": 173, "165": 173, "166": 177, "167": 179, "168": 179, "169": 181, "174": 185, "175": 186, "176": 186, "177": 187, "178": 187, "179": 188, "180": 188, "181": 194, "182": 194, "183": 196, "186": 198, "187": 199, "188": 199, "189": 200, "190": 200, "191": 201, "192": 201, "193": 206, "194": 206, "195": 208, "200": 212, "201": 213, "202": 213, "203": 214, "204": 214, "205": 215, "206": 215, "207": 218, "208": 219, "209": 220, "210": 222, "211": 222, "212": 224, "217": 228, "218": 229, "219": 229, "220": 230, "221": 230, "222": 231, "223": 231, "224": 236, "225": 236, "226": 238, "231": 242, "232": 243, "233": 243, "234": 244, "235": 244, "236": 245, "237": 245, "238": 250, "239": 250, "240": 252, "244": 255, "245": 256, "246": 256, "247": 257, "248": 257, "249": 258, "250": 258, "251": 261, "252": 262, "253": 263, "254": 265, "255": 265, "256": 267, "259": 269, "260": 270, "261": 270, "262": 271, "263": 271, "264": 272, "265": 272, "266": 275, "272": 266}, "uri": "instructor/instructor_dashboard_2/membership.html", "filename": "/home/nttlong/code/edx/apps/edx/edx-platform/xdj-gnol-lms-templates/instructor/instructor_dashboard_2/membership.html"}
__M_END_METADATA
"""
