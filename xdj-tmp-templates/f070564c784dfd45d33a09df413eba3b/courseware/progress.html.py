# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1548073821.49898
_enable_loop = True
_template_filename = u'/home/nttlong/code/edx/apps/edx/edx-platform/xdj-gnol-lms-templates/courseware/progress.html'
_template_uri = 'courseware/progress.html'
_source_encoding = 'utf-8'
_exports = [u'pagetitle', u'headextra', u'js_extra', u'bodyclass', 'online_help_token']



from course_modes.models import CourseMode
from lms.djangoapps.certificates.models import CertificateStatuses
from django.utils.translation import ugettext as _
from openedx.core.djangolib.markup import HTML, Text
from django.urls import reverse
from django.conf import settings
from django.utils.http import urlquote_plus
from six import text_type

from openedx.features.enterprise_support.utils import get_enterprise_learner_generic_name


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace(u'static', context._clean_inheritance_tokens(), templateuri=u'/x-static-content.html', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, u'static')] = ns

    ns = runtime.TemplateNamespace(u'progress_graph', context._clean_inheritance_tokens(), templateuri=u'/courseware/progress_graph.js', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, u'progress_graph')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, u'/main.html', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        loop = __M_loop = runtime.LoopStack()
        int = context.get('int', UNDEFINED)
        float = context.get('float', UNDEFINED)
        def pagetitle():
            return render_pagetitle(context._locals(__M_locals))
        course = context.get('course', UNDEFINED)
        static = _mako_get_namespace(context, 'static')
        unicode = context.get('unicode', UNDEFINED)
        def bodyclass():
            return render_bodyclass(context._locals(__M_locals))
        credit_course_requirements = context.get('credit_course_requirements', UNDEFINED)
        def js_extra():
            return render_js_extra(context._locals(__M_locals))
        studio_url = context.get('studio_url', UNDEFINED)
        getattr = context.get('getattr', UNDEFINED)
        dict = context.get('dict', UNDEFINED)
        user_timezone = context.get('user_timezone', UNDEFINED)
        len = context.get('len', UNDEFINED)
        student = context.get('student', UNDEFINED)
        user_language = context.get('user_language', UNDEFINED)
        staff_access = context.get('staff_access', UNDEFINED)
        certificate_data = context.get('certificate_data', UNDEFINED)
        progress_graph = _mako_get_namespace(context, 'progress_graph')
        request = context.get('request', UNDEFINED)
        grade_summary = context.get('grade_summary', UNDEFINED)
        def headextra():
            return render_headextra(context._locals(__M_locals))
        courseware_summary = context.get('courseware_summary', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n')
        __M_writer(u'\n')
        __M_writer(u'\n')
        __M_writer(u'\n')
        __M_writer(u'\n\n')

        username = get_enterprise_learner_generic_name(request) or student.username
        
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['username'] if __M_key in __M_locals_builtin_stored]))
        __M_writer(u'\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'bodyclass'):
            context['self'].bodyclass(**pageargs)
        

        __M_writer(u'\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'headextra'):
            context['self'].headextra(**pageargs)
        

        __M_writer(u'\n\n\n')
        __M_writer(u'\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'pagetitle'):
            context['self'].pagetitle(**pageargs)
        

        __M_writer(u'\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'js_extra'):
            context['self'].js_extra(**pageargs)
        

        __M_writer(u'\n\n')
        runtime._include_file(context, u'/courseware/course_navigation.html', _template_uri, active_page='progress')
        __M_writer(u'\n\n<main id="main" aria-label="Content" tabindex="-1">\n    <div class="container">\n        <div class="profile-wrapper">\n            <section class="course-info" id="course-info-progress"\n')
        if getattr(course, 'language'):
            __M_writer(u'                lang="')
            __M_writer(filters.html_escape(filters.decode.utf8(course.language)))
            __M_writer(u'"\n')
        __M_writer(u'              >\n')
        if staff_access and studio_url is not None:
            __M_writer(u'                <div class="wrap-instructor-info">\n                    <a class="instructor-info-action studio-view" href="')
            __M_writer(filters.html_escape(filters.decode.utf8(studio_url)))
            __M_writer(u'">')
            __M_writer(filters.html_escape(filters.decode.utf8(_("View Grading in studio"))))
            __M_writer(u'</a>\n                </div>\n')
        __M_writer(u'                <h2 class="hd hd-2 progress-certificates-title">\n                    ')
        __M_writer(filters.html_escape(filters.decode.utf8(_("Course Progress for Student '{username}' ({email})").format(username=username, email=student.email))))
        __M_writer(u'\n                </h2>\n\n                <div class="wrapper-msg wrapper-auto-cert">\n                    <div id="errors-info" class="errors-info"></div>\n')
        if certificate_data:
            __M_writer(u'                    <div class="auto-cert-message" id="course-success">\n                        <div class="has-actions">\n                            ')
            post_url = reverse('generate_user_cert', args=[unicode(course.id)]) 
            
            __M_locals_builtin_stored = __M_locals_builtin()
            __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['post_url'] if __M_key in __M_locals_builtin_stored]))
            __M_writer(u'\n                            <div class="msg-content">\n                                <h4 class="hd hd-4 title">')
            __M_writer(filters.html_escape(filters.decode.utf8(certificate_data.title)))
            __M_writer(u'</h4>\n                                <p class="copy">')
            __M_writer(filters.html_escape(filters.decode.utf8(certificate_data.msg)))
            __M_writer(u'</p>\n                            </div>\n                            <div class="msg-actions">\n')
            if certificate_data.cert_web_view_url:
                __M_writer(u'                                <a class="btn" href="')
                __M_writer(filters.html_escape(filters.decode.utf8(certificate_data.cert_web_view_url)))
                __M_writer(u'" target="_blank">')
                __M_writer(filters.html_escape(filters.decode.utf8(_("View Certificate"))))
                __M_writer(u' <span class="sr">')
                __M_writer(filters.html_escape(filters.decode.utf8(_("Opens in a new browser window"))))
                __M_writer(u'</span></a>\n')
            elif certificate_data.cert_status == CertificateStatuses.downloadable and certificate_data.download_url:
                __M_writer(u'                                <a class="btn" href="')
                __M_writer(filters.html_escape(filters.decode.utf8(certificate_data.download_url)))
                __M_writer(u'" target="_blank">')
                __M_writer(filters.html_escape(filters.decode.utf8(_("Download Your Certificate"))))
                __M_writer(u' <span class="sr">')
                __M_writer(filters.html_escape(filters.decode.utf8(_("Opens in a new browser window"))))
                __M_writer(u'</span></a>\n')
            elif certificate_data.cert_status == CertificateStatuses.requesting:
                __M_writer(u'                                <button class="btn generate_certs" data-endpoint="')
                __M_writer(filters.html_escape(filters.decode.utf8(post_url)))
                __M_writer(u'" id="btn_generate_cert">')
                __M_writer(filters.html_escape(filters.decode.utf8(_('Request Certificate'))))
                __M_writer(u'</button>\n')
            __M_writer(u'                            </div>\n                        </div>\n                    </div>\n')
        __M_writer(u'                </div>\n\n')
        if not course.disable_progress_graph:
            __M_writer(u'                <div class="grade-detail-graph" id="grade-detail-graph"></div>\n')
        __M_writer(u'\n')
        if credit_course_requirements:
            __M_writer(u'                <section class="credit-eligibility">\n                    <h3 class="hd hd-4 eligibility-heading">')
            __M_writer(filters.html_escape(filters.decode.utf8(_("Requirements for Course Credit"))))
            __M_writer(u'</h3>\n                    <div class="credit-eligibility-container">\n')
            if credit_course_requirements['eligibility_status'] == 'not_eligible':
                __M_writer(u'                        <span class="eligibility_msg">')
                __M_writer(filters.html_escape(filters.decode.utf8(_("{student_name}, you are no longer eligible for credit in this course.").format(student_name=student.profile.name))))
                __M_writer(u'</span>\n')
            elif credit_course_requirements['eligibility_status'] == 'eligible':
                __M_writer(u'                        <span class="eligibility_msg">\n                            ')
                __M_writer(filters.html_escape(filters.decode.utf8(Text(_("{student_name}, you have met the requirements for credit in this course. {a_start}Go to your dashboard{a_end} to purchase course credit.")).format(
                                student_name=student.profile.name,
                                a_start=HTML("<a href={url}>").format(url=reverse('dashboard')),
                                a_end=HTML("</a>")
                            ))))
                __M_writer(u'\n                        </span>\n')
            elif credit_course_requirements['eligibility_status'] == 'partial_eligible':
                __M_writer(u'                        <span>')
                __M_writer(filters.html_escape(filters.decode.utf8(_("{student_name}, you have not yet met the requirements for credit.").format(student_name=student.profile.name))))
                __M_writer(u'</span>\n')
            __M_writer(u'\n                        <a href="')
            __M_writer(filters.html_escape(filters.decode.utf8(settings.CREDIT_HELP_LINK_URL)))
            __M_writer(u'" class="credit-help">\n                            <span class="fa fa-question" aria-hidden="true"></span>\n                            <span class="sr">')
            __M_writer(filters.html_escape(filters.decode.utf8(_("Information about course credit requirements"))))
            __M_writer(u'</span>\n                        </a><br />\n\n                        <div class="requirement-container" data-eligible="')
            __M_writer(filters.html_escape(filters.decode.utf8(credit_course_requirements['eligibility_status'])))
            __M_writer(u'">\n')
            for requirement in credit_course_requirements['requirements']:
                __M_writer(u'                            <div class="requirement">\n                                <div class="requirement-name">\n                                    ')
                __M_writer(filters.html_escape(filters.decode.utf8(_(requirement['display_name']))))
                __M_writer(u'\n')
                if requirement['namespace'] == 'grade':
                    __M_writer(u'                                    <span>')
                    __M_writer(filters.html_escape(filters.decode.utf8(int(requirement['criteria']['min_grade'] * 100))))
                    __M_writer(u'%</span>\n')
                __M_writer(u'                                </div>\n                                <div class="requirement-status">\n')
                if requirement['status']:
                    if requirement['status'] == 'submitted':
                        __M_writer(u'                                        <span class="requirement-submitted">')
                        __M_writer(filters.html_escape(filters.decode.utf8(_("Verification Submitted"))))
                        __M_writer(u'</span>\n')
                    elif requirement['status'] == 'failed':
                        __M_writer(u'                                        <span class="fa fa-times" aria-hidden="true"></span>\n                                        <span>')
                        __M_writer(filters.html_escape(filters.decode.utf8(_("Verification Failed" ))))
                        __M_writer(u'</span>\n')
                    elif requirement['status'] == 'declined':
                        __M_writer(u'                                        <span class="fa fa-times" aria-hidden="true"></span>\n                                        <span>')
                        __M_writer(filters.html_escape(filters.decode.utf8(_("Verification Declined" ))))
                        __M_writer(u'</span>\n')
                    elif requirement['status'] == 'satisfied':
                        __M_writer(u'                                        <span class="fa fa-check" aria-hidden="true"></span>\n                                        <span class="localized-datetime" data-datetime="')
                        __M_writer(filters.html_escape(filters.decode.utf8(requirement['status_date'])))
                        __M_writer(u'" data-string="')
                        __M_writer(filters.html_escape(filters.decode.utf8(_('Completed by {date}'))))
                        __M_writer(u'" data-timezone="')
                        __M_writer(filters.html_escape(filters.decode.utf8(user_timezone)))
                        __M_writer(u'" data-language="')
                        __M_writer(filters.html_escape(filters.decode.utf8(user_language)))
                        __M_writer(u'"></span>\n')
                else:
                    __M_writer(u'                                    <span class="not-achieve">')
                    __M_writer(filters.html_escape(filters.decode.utf8(_("Upcoming"))))
                    __M_writer(u'</span>\n')
                __M_writer(u'                                </div>\n                            </div>\n')
            __M_writer(u'                        </div>\n                        <button class="detail-collapse">\n                            <span class="fa fa-caret-up" aria-hidden="true"></span>\n                            <span class="requirement-detail">')
            __M_writer(filters.html_escape(filters.decode.utf8(_("Less"))))
            __M_writer(u'</span>\n                        </button>\n                    </div>\n                </section>\n')
        __M_writer(u'\n')
        if courseware_summary:
            __M_writer(u'                <section class="chapters">\n                    <h2 class="sr">')
            __M_writer(filters.html_escape(filters.decode.utf8(_('Details for each chapter'))))
            __M_writer(u'</h2>\n')
            loop = __M_loop._enter(courseware_summary)
            try:
                for chapter in loop:
                    if not chapter['display_name'] == "hidden":
                        __M_writer(u'                        <section aria-labelledby="chapter_')
                        __M_writer(filters.html_escape(filters.decode.utf8(loop.index)))
                        __M_writer(u'">\n                            <h3 class="hd hd-3" id="chapter_')
                        __M_writer(filters.html_escape(filters.decode.utf8(loop.index)))
                        __M_writer(u'">')
                        __M_writer(filters.html_escape(filters.decode.utf8( chapter['display_name'])))
                        __M_writer(u'</h3>\n                            <div class="sections">\n')
                        for section in chapter['sections']:
                            __M_writer(u'                                    <div>\n                                        ')

                            earned = section.all_total.earned
                            total = section.all_total.possible
                            
                            percentageString = "{0:.0%}".format(section.percent_graded) if earned > 0 and total > 0 else ""
                            
                            
                            __M_locals_builtin_stored = __M_locals_builtin()
                            __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['percentageString','total','earned'] if __M_key in __M_locals_builtin_stored]))
                            __M_writer(u'\n                                        <h4 class="hd hd-4">\n                                            <a href="')
                            __M_writer(filters.html_escape(filters.decode.utf8(reverse('courseware_section', kwargs=dict(course_id=text_type(course.id), chapter=chapter['url_name'], section=section.url_name)))))
                            __M_writer(u'">\n                                                ')
                            __M_writer(filters.html_escape(filters.decode.utf8( section.display_name)))
                            __M_writer(u'\n')
                            if total > 0 or earned > 0:
                                __M_writer(u'                                                <span class="sr">\n                                                    ')
                                __M_writer(filters.html_escape(filters.decode.utf8(_("{earned} of {total} possible points").format(earned='{:.3n}'.format(float(earned)), total='{:.3n}'.format(float(total))))))
                                __M_writer(u'\n                                                </span>\n')
                            __M_writer(u'                                            </a>\n')
                            if total > 0 or earned > 0:
                                __M_writer(u'                                            <span> ')
                                __M_writer(filters.html_escape(filters.decode.utf8("({0:.3n}/{1:.3n}) {2}".format( float(earned), float(total), percentageString ))))
                                __M_writer(u'</span>\n')
                            __M_writer(u'                                        </h4>\n                                        <p>\n')
                            if section.format is not None:
                                __M_writer(u'                                                ')
                                __M_writer(filters.html_escape(filters.decode.utf8(section.format)))
                                __M_writer(u'\n')
                            if section.due is not None:
                                __M_writer(u'                                                <em class="localized-datetime" data-datetime="')
                                __M_writer(filters.html_escape(filters.decode.utf8(section.due)))
                                __M_writer(u'" data-string="')
                                __M_writer(filters.html_escape(filters.decode.utf8(_('due {date}'))))
                                __M_writer(u'" data-timezone="')
                                __M_writer(filters.html_escape(filters.decode.utf8(user_timezone)))
                                __M_writer(u'" data-language="')
                                __M_writer(filters.html_escape(filters.decode.utf8(user_language)))
                                __M_writer(u'"></em>\n')
                            __M_writer(u'                                        </p>\n                                        <p class="override-notice">\n')
                            if section.override is not None:
                                if section.format is not None and section.format == "Exam":
                                    __M_writer(u'                                                    ')
                                    __M_writer(filters.html_escape(filters.decode.utf8(_("Suspicious activity detected during proctored exam review. Exam score 0."))))
                                    __M_writer(u'\n')
                                else:
                                    __M_writer(u'                                                    ')
                                    __M_writer(filters.html_escape(filters.decode.utf8(_("Section grade has been overridden."))))
                                    __M_writer(u'\n')
                            __M_writer(u'                                        </p>\n')
                            if len(section.problem_scores.values()) > 0:
                                if section.show_grades(staff_access):
                                    __M_writer(u'                                          <dl class="scores">\n                                              <dt class="hd hd-6">')
                                    __M_writer(filters.html_escape(filters.decode.utf8( _("Problem Scores: ") if section.graded else _("Practice Scores: "))))
                                    __M_writer(u'</dt>\n')
                                    for score in section.problem_scores.values():
                                        __M_writer(u'                                              <dd>')
                                        __M_writer(filters.html_escape(filters.decode.utf8("{0:.3n}/{1:.3n}".format(float(score.earned),float(score.possible)))))
                                        __M_writer(u'</dd>\n')
                                    __M_writer(u'                                          </dl>\n')
                                else:
                                    __M_writer(u'                                            <p class="hide-scores">\n')
                                    if section.show_correctness == 'past_due':
                                        if section.graded:
                                            __M_writer(u'                                                  ')
                                            __M_writer(filters.html_escape(filters.decode.utf8(_("Problem scores are hidden until the due date."))))
                                            __M_writer(u'\n')
                                        else:
                                            __M_writer(u'                                                  ')
                                            __M_writer(filters.html_escape(filters.decode.utf8(_("Practice scores are hidden until the due date."))))
                                            __M_writer(u'\n')
                                    else:
                                        if section.graded:
                                            __M_writer(u'                                                  ')
                                            __M_writer(filters.html_escape(filters.decode.utf8(_("Problem scores are hidden."))))
                                            __M_writer(u'\n')
                                        else:
                                            __M_writer(u'                                                  ')
                                            __M_writer(filters.html_escape(filters.decode.utf8(_("Practice scores are hidden."))))
                                            __M_writer(u'\n')
                                    __M_writer(u'                                            </p>\n')
                            else:
                                __M_writer(u'                                        <p class="no-scores">')
                                __M_writer(filters.html_escape(filters.decode.utf8(_("No problem scores in this section"))))
                                __M_writer(u'</p>\n')
                            __M_writer(u'                                    </div>\n')
                        __M_writer(u'                            </div>\n                        </section>\n')
            finally:
                loop = __M_loop._exit()
            __M_writer(u'                </section>\n')
        __M_writer(u'            </section>\n        </div>\n    </div>\n</main>\n')
        def ccall(caller):
            def body():
                __M_writer = context.writer()
                __M_writer(u'\n    DateUtilFactory.transform(iterationKey=".localized-datetime");\n')
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


def render_pagetitle(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def pagetitle():
            return render_pagetitle(context)
        course = context.get('course', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(filters.html_escape(filters.decode.utf8(_("{course_number} Progress").format(course_number=course.display_number_with_default))))
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_headextra(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def headextra():
            return render_headextra(context)
        static = _mako_get_namespace(context, 'static')
        __M_writer = context.writer()
        __M_writer(u'\n')
        def ccall(caller):
            def body():
                __M_writer = context.writer()
                return ''
            return [body]
        context.caller_stack.nextcaller = runtime.Namespace('caller', context, callables=ccall(__M_caller))
        try:
            __M_writer(filters.html_escape(filters.decode.utf8(static.css(group=u'style-course-vendor'))))
        finally:
            context.caller_stack.nextcaller = None
        __M_writer(u'\n')
        def ccall(caller):
            def body():
                __M_writer = context.writer()
                return ''
            return [body]
        context.caller_stack.nextcaller = runtime.Namespace('caller', context, callables=ccall(__M_caller))
        try:
            __M_writer(filters.html_escape(filters.decode.utf8(static.css(group=u'style-course'))))
        finally:
            context.caller_stack.nextcaller = None
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_js_extra(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        course = context.get('course', UNDEFINED)
        def js_extra():
            return render_js_extra(context)
        static = _mako_get_namespace(context, 'static')
        grade_summary = context.get('grade_summary', UNDEFINED)
        progress_graph = _mako_get_namespace(context, 'progress_graph')
        __M_writer = context.writer()
        __M_writer(u'\n<script type="text/javascript" src="')
        __M_writer(filters.html_escape(filters.decode.utf8(static.url('js/vendor/flot/jquery.flot.js'))))
        __M_writer(u'"></script>\n<script type="text/javascript" src="')
        __M_writer(filters.html_escape(filters.decode.utf8(static.url('js/vendor/flot/jquery.flot.stack.js'))))
        __M_writer(u'"></script>\n<script type="text/javascript" src="')
        __M_writer(filters.html_escape(filters.decode.utf8(static.url('js/vendor/flot/jquery.flot.symbol.js'))))
        __M_writer(u'"></script>\n<script type="text/javascript" src="')
        __M_writer(filters.html_escape(filters.decode.utf8(static.url('js/courseware/certificates_api.js'))))
        __M_writer(u'"></script>\n<script type="text/javascript" src="')
        __M_writer(filters.html_escape(filters.decode.utf8(static.url('js/courseware/credit_progress.js'))))
        __M_writer(u'"></script>\n<script>\n')
        __M_writer(u'    ')
        __M_writer(filters.html_escape(filters.decode.utf8(progress_graph.body(grade_summary, course.grade_cutoffs, "grade-detail-graph", not course.no_grade, not course.no_grade))))
        __M_writer(u'\n</script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_bodyclass(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def bodyclass():
            return render_bodyclass(context)
        __M_writer = context.writer()
        __M_writer(u'view-in-course view-progress')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_online_help_token(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        return "progress" 
        
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"16": 5, "36": 3, "39": 30, "45": 1, "78": 1, "79": 2, "80": 3, "81": 4, "82": 16, "83": 18, "89": 20, "94": 22, "99": 27, "100": 30, "105": 32, "110": 46, "111": 48, "112": 48, "113": 54, "114": 55, "115": 55, "116": 55, "117": 57, "118": 58, "119": 59, "120": 60, "121": 60, "122": 60, "123": 60, "124": 63, "125": 64, "126": 64, "127": 69, "128": 70, "129": 72, "133": 72, "134": 74, "135": 74, "136": 75, "137": 75, "138": 78, "139": 79, "140": 79, "141": 79, "142": 79, "143": 79, "144": 79, "145": 79, "146": 80, "147": 81, "148": 81, "149": 81, "150": 81, "151": 81, "152": 81, "153": 81, "154": 82, "155": 83, "156": 83, "157": 83, "158": 83, "159": 83, "160": 85, "161": 89, "162": 91, "163": 92, "164": 94, "165": 95, "166": 96, "167": 97, "168": 97, "169": 99, "170": 100, "171": 100, "172": 100, "173": 101, "174": 102, "175": 103, "180": 107, "181": 109, "182": 110, "183": 110, "184": 110, "185": 112, "186": 113, "187": 113, "188": 115, "189": 115, "190": 118, "191": 118, "192": 119, "193": 120, "194": 122, "195": 122, "196": 123, "197": 124, "198": 124, "199": 124, "200": 126, "201": 128, "202": 129, "203": 130, "204": 130, "205": 130, "206": 131, "207": 132, "208": 133, "209": 133, "210": 134, "211": 135, "212": 136, "213": 136, "214": 137, "215": 138, "216": 139, "217": 139, "218": 139, "219": 139, "220": 139, "221": 139, "222": 139, "223": 139, "224": 141, "225": 142, "226": 142, "227": 142, "228": 144, "229": 147, "230": 150, "231": 150, "232": 155, "233": 156, "234": 157, "235": 158, "236": 158, "237": 159, "240": 160, "241": 161, "242": 161, "243": 161, "244": 162, "245": 162, "246": 162, "247": 162, "248": 164, "249": 165, "250": 166, "259": 171, "260": 173, "261": 173, "262": 174, "263": 174, "264": 175, "265": 176, "266": 177, "267": 177, "268": 180, "269": 181, "270": 182, "271": 182, "272": 182, "273": 184, "274": 186, "275": 187, "276": 187, "277": 187, "278": 189, "279": 190, "280": 190, "281": 190, "282": 190, "283": 190, "284": 190, "285": 190, "286": 190, "287": 190, "288": 192, "289": 194, "290": 195, "291": 196, "292": 196, "293": 196, "294": 197, "295": 198, "296": 198, "297": 198, "298": 201, "299": 202, "300": 203, "301": 204, "302": 205, "303": 205, "304": 206, "305": 207, "306": 207, "307": 207, "308": 209, "309": 210, "310": 211, "311": 212, "312": 213, "313": 214, "314": 214, "315": 214, "316": 215, "317": 216, "318": 216, "319": 216, "320": 218, "321": 219, "322": 220, "323": 220, "324": 220, "325": 221, "326": 222, "327": 222, "328": 222, "329": 225, "330": 227, "331": 228, "332": 228, "333": 228, "334": 230, "335": 232, "338": 236, "339": 238, "343": 242, "348": 242, "351": 244, "357": 32, "364": 32, "370": 24, "377": 24, "385": 25, "388": 25, "396": 26, "399": 26, "405": 34, "415": 34, "416": 35, "417": 35, "418": 36, "419": 36, "420": 37, "421": 37, "422": 38, "423": 38, "424": 39, "425": 39, "426": 44, "427": 44, "428": 44, "434": 22, "440": 22, "446": 4, "450": 4, "457": 450}, "uri": "courseware/progress.html", "filename": "/home/nttlong/code/edx/apps/edx/edx-platform/xdj-gnol-lms-templates/courseware/progress.html"}
__M_END_METADATA
"""
