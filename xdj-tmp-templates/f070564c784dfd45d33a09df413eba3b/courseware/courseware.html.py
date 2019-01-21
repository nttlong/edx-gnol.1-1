# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1548073577.932079
_enable_loop = True
_template_filename = u'/home/nttlong/code/edx/apps/edx/edx-platform/xdj-gnol-lms-templates/courseware/courseware.html'
_template_uri = 'courseware/courseware.html'
_source_encoding = 'utf-8'
_exports = ['course_name', u'bodyclass', u'title', 'online_help_token', u'js_extra', u'headextra', u'header_extras']



import waffle

from django.conf import settings
from django.urls import reverse
from django.utils.translation import ugettext as _

from edxnotes.helpers import is_feature_enabled as is_edxnotes_enabled
from openedx.core.djangolib.js_utils import js_escaped_string
from openedx.core.djangolib.markup import HTML
from openedx.features.course_experience import course_home_page_title, COURSE_OUTLINE_PAGE_FLAG


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace(u'static', context._clean_inheritance_tokens(), templateuri=u'/x-static-content.html', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, u'static')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, u'/main.html', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        disable_accordion = context.get('disable_accordion', UNDEFINED)
        int = context.get('int', UNDEFINED)
        course = context.get('course', UNDEFINED)
        static = _mako_get_namespace(context, 'static')
        unicode = context.get('unicode', UNDEFINED)
        default_tab = context.get('default_tab', UNDEFINED)
        def course_name():
            return render_course_name(context._locals(__M_locals))
        def bodyclass():
            return render_bodyclass(context._locals(__M_locals))
        def title():
            return render_title(context._locals(__M_locals))
        section = context.get('section', UNDEFINED)
        def js_extra():
            return render_js_extra(context._locals(__M_locals))
        getattr = context.get('getattr', UNDEFINED)
        language_preference = context.get('language_preference', UNDEFINED)
        entrance_exam_passed = context.get('entrance_exam_passed', UNDEFINED)
        fragment = context.get('fragment', UNDEFINED)
        sequence_title = context.get('sequence_title', UNDEFINED)
        staff_access = context.get('staff_access', UNDEFINED)
        chapter = context.get('chapter', UNDEFINED)
        section_title = context.get('section_title', UNDEFINED)
        accordion = context.get('accordion', UNDEFINED)
        request = context.get('request', UNDEFINED)
        course_url = context.get('course_url', UNDEFINED)
        entrance_exam_current_score = context.get('entrance_exam_current_score', UNDEFINED)
        course_sock_fragment = context.get('course_sock_fragment', UNDEFINED)
        def headextra():
            return render_headextra(context._locals(__M_locals))
        def header_extras():
            return render_header_extras(context._locals(__M_locals))
        round = context.get('round', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n')
        __M_writer(u'\n')
        __M_writer(u'\n')
        __M_writer(u'\n')
        __M_writer(u'\n')

        include_special_exams = settings.FEATURES.get('ENABLE_SPECIAL_EXAMS', False) and (course.enable_proctored_exams or course.enable_timed_exams)
        
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['include_special_exams'] if __M_key in __M_locals_builtin_stored]))
        __M_writer(u'\n')
        __M_writer(u'\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'bodyclass'):
            context['self'].bodyclass(**pageargs)
        

        __M_writer(u'\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'title'):
            context['self'].title(**pageargs)
        

        __M_writer(u'\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'header_extras'):
            context['self'].header_extras(**pageargs)
        

        __M_writer(u'\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'headextra'):
            context['self'].headextra(**pageargs)
        

        __M_writer(u'\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'js_extra'):
            context['self'].js_extra(**pageargs)
        

        __M_writer(u'\n\n<div class="message-banner" aria-live="polite"></div>\n\n')
        if default_tab:
            __M_writer(u'  ')
            runtime._include_file(context, u'/courseware/course_navigation.html', _template_uri)
            __M_writer(u'\n')
        else:
            __M_writer(u'  ')
            runtime._include_file(context, u'/courseware/course_navigation.html', _template_uri, active_page='courseware')
            __M_writer(u'\n')
        __M_writer(u'\n<div class="container"\n')
        if getattr(course, 'language'):
            __M_writer(u'    lang="')
            __M_writer(filters.html_escape(filters.decode.utf8(course.language)))
            __M_writer(u'"\n')
        __M_writer(u'  >\n  <div class="course-wrapper" role="presentation">\n\n')
        if disable_accordion is UNDEFINED or not disable_accordion:
            __M_writer(u'    <div class="course-index">\n\n      <div class="wrapper-course-modes">\n\n          <div class="courseware-bookmarks-button">\n              <a class="bookmarks-list-button" href="')
            __M_writer(filters.html_escape(filters.decode.utf8(reverse('openedx.course_bookmarks.home', args=[course.id]))))
            __M_writer(u'">\n                  ')
            __M_writer(filters.html_escape(filters.decode.utf8(_('Bookmarks'))))
            __M_writer(u'\n              </a>\n          </div>\n\n')
            if settings.FEATURES.get('ENABLE_COURSEWARE_SEARCH'):
                __M_writer(u'            <div id="courseware-search-bar" class="search-bar courseware-search-bar" role="search" aria-label="Course">\n              <form class="search-form">\n                <label for="course-search-input" class="sr">')
                __M_writer(filters.html_escape(filters.decode.utf8(_('Course Search'))))
                __M_writer(u'</label>\n                <div class="search-field-wrapper">\n                  <input id="course-search-input" type="text" class="search-field"/>\n                  <button type="submit" class="search-button">')
                __M_writer(filters.html_escape(filters.decode.utf8(_('Search'))))
                __M_writer(u'</button>\n                  <button type="button" class="cancel-button" title="')
                __M_writer(filters.html_escape(filters.decode.utf8(_('Clear search'))))
                __M_writer(u'">\n                    <span class="icon fa fa-remove" aria-hidden="true"></span>\n                  </button>\n                </div>\n              </form>\n            </div>\n')
            __M_writer(u'\n      </div>\n\n      <div class="accordion">\n        <nav class="course-navigation" aria-label="')
            __M_writer(filters.html_escape(filters.decode.utf8(_('Course'))))
            __M_writer(u'">\n')
            if accordion.strip():
                __M_writer(u'            ')
                __M_writer(filters.html_escape(filters.decode.utf8(HTML(accordion))))
                __M_writer(u'\n')
            else:
                __M_writer(u'            <div class="chapter">')
                __M_writer(filters.html_escape(filters.decode.utf8(_("No content has been added to this course"))))
                __M_writer(u'</div>\n')
            __M_writer(u'        </nav>\n      </div>\n\n    </div>\n')
        __M_writer(u'    <section class="course-content" id="course-content">\n        <header class="page-header has-secondary">\n            <div class="page-header-main">\n                <nav aria-label="')
        __M_writer(filters.html_escape(filters.decode.utf8(_('Course'))))
        __M_writer(u'" class="sr-is-focusable" tabindex="-1">\n                    <div class="has-breadcrumbs">\n                        <div class="breadcrumbs">\n')
        if COURSE_OUTLINE_PAGE_FLAG.is_enabled(course.id):
            __M_writer(u'                                <span class="nav-item nav-item-course">\n                                    <a href="')
            __M_writer(filters.html_escape(filters.decode.utf8(course_url)))
            __M_writer(u'">')
            __M_writer(filters.html_escape(filters.decode.utf8(course_home_page_title(course))))
            __M_writer(u'</a>\n                                </span>\n                                <span class="icon fa fa-angle-right" aria-hidden="true"></span>\n')
        if chapter:
            __M_writer(u'                                <span class="nav-item nav-item-chapter" data-course-position="')
            __M_writer(filters.html_escape(filters.decode.utf8(course.position)))
            __M_writer(u'" data-chapter-position="')
            __M_writer(filters.html_escape(filters.decode.utf8(chapter.position)))
            __M_writer(u'">\n                                    <a href="')
            __M_writer(filters.html_escape(filters.decode.utf8(course_url)))
            __M_writer(u'#')
            __M_writer(filters.html_escape(filters.decode.utf8(unicode(chapter.location))))
            __M_writer(u'">')
            __M_writer(filters.html_escape(filters.decode.utf8(chapter.display_name_with_default)))
            __M_writer(u'</a>\n                                </span>\n                                <span class="icon fa fa-angle-right" aria-hidden="true"></span>\n')
        if section:
            __M_writer(u'                                <span class="nav-item nav-item-section">\n                                    <a href="')
            __M_writer(filters.html_escape(filters.decode.utf8(course_url)))
            __M_writer(u'#')
            __M_writer(filters.html_escape(filters.decode.utf8(unicode(section.location))))
            __M_writer(u'">')
            __M_writer(filters.html_escape(filters.decode.utf8(section.display_name_with_default)))
            __M_writer(u'</a>\n                                </span>\n                                <span class="icon fa fa-angle-right" aria-hidden="true"></span>\n')
        __M_writer(u'                            <span class="nav-item nav-item-sequence">')
        __M_writer(filters.html_escape(filters.decode.utf8(sequence_title)))
        __M_writer(u'</span>\n                        </div>\n                    </div>\n                </nav>\n            </div>\n        </header>\n\n        <main id="main" tabindex="-1" aria-label="Content">\n')
        if getattr(course, 'entrance_exam_enabled') and \
               getattr(course, 'entrance_exam_minimum_score_pct') and \
               entrance_exam_current_score is not UNDEFINED:
            if not entrance_exam_passed:
                __M_writer(u'                <p class="sequential-status-message">\n                    ')
                __M_writer(filters.html_escape(filters.decode.utf8(_('To access course materials, you must score {required_score}% or higher on this \
                    exam. Your current score is {current_score}%.').format(
                        required_score=int(round(course.entrance_exam_minimum_score_pct * 100)),
                        current_score=int(round(entrance_exam_current_score * 100))
                    ))))
                __M_writer(u'\n                </p>\n                <script type="text/javascript">\n                $(document).ajaxSuccess(function(event, xhr, settings) {\n                    if (settings.url.indexOf("xmodule_handler/problem_check") > -1) {\n                        var data = JSON.parse(xhr.responseText);\n                        if (data.entrance_exam_passed){\n                            location.reload();\n                        }\n                    }\n                });\n                </script>\n')
            else:
                __M_writer(u'                  <p class="sequential-status-message">\n                    ')
                __M_writer(filters.html_escape(filters.decode.utf8(_('Your score is {current_score}%. You have passed the entrance exam.').format(
                        current_score=int(round(entrance_exam_current_score * 100))
                    ))))
                __M_writer(u'\n                </p>\n')
        __M_writer(u'\n              ')
        __M_writer(filters.html_escape(filters.decode.utf8(HTML(fragment.body_html()))))
        __M_writer(u'\n        </main>\n    </section>\n\n    <section class="courseware-results-wrapper">\n      <div id="loading-message" aria-live="polite" aria-relevant="all"></div>\n      <div id="error-message" aria-live="polite"></div>\n      <div class="courseware-results search-results" data-course-id="')
        __M_writer(filters.html_escape(filters.decode.utf8(course.id)))
        __M_writer(u'" data-lang-code="')
        __M_writer(filters.html_escape(filters.decode.utf8(language_preference)))
        __M_writer(u'"></div>\n    </section>\n\n  </div>\n  ')
        __M_writer(filters.html_escape(filters.decode.utf8(HTML(course_sock_fragment.body_html()))))
        __M_writer(u'\n</div>\n<div class="container-footer">\n')
        if settings.FEATURES.get("LICENSING", False):
            __M_writer(u'    <div class="course-license">\n')
            if getattr(course, "license", None):
                __M_writer(u'      ')
                runtime._include_file(context, u'../license.html', _template_uri, license=course.license)
                __M_writer(u'\n')
            else:
                __M_writer(u'      ')
                runtime._include_file(context, u'../license.html', _template_uri, license='all-rights-reserved')
                __M_writer(u'\n')
            __M_writer(u'    </div>\n')
        __M_writer(u'</div>\n')
        if course.show_calculator or is_edxnotes_enabled(course, request.user):
            __M_writer(u'    <nav class="nav-utilities ')
            __M_writer(filters.html_escape(filters.decode.utf8("has-utility-calculator" if course.show_calculator else "")))
            __M_writer(u'" aria-label="')
            __M_writer(filters.html_escape(filters.decode.utf8(_('Course Utilities'))))
            __M_writer(u'">\n')
            if is_edxnotes_enabled(course, request.user):
                __M_writer(u'        ')
                runtime._include_file(context, u'/edxnotes/toggle_notes.html', _template_uri, course=course)
                __M_writer(u'\n')
            __M_writer(u'\n')
            if course.show_calculator:
                __M_writer(u'        ')
                runtime._include_file(context, u'/calculator/toggle_calculator.html', _template_uri)
                __M_writer(u'\n')
            __M_writer(u'    </nav>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_course_name(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        course = context.get('course', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n ')
        return _("{course_number} Courseware").format(course_number=course.display_number_with_default) 
        
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_bodyclass(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        course = context.get('course', UNDEFINED)
        def bodyclass():
            return render_bodyclass(context)
        __M_writer = context.writer()
        __M_writer(u'view-in-course view-courseware courseware ')
        __M_writer(filters.html_escape(filters.decode.utf8(course.css_class or '')))
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        static = _mako_get_namespace(context, 'static')
        section_title = context.get('section_title', UNDEFINED)
        def course_name():
            return render_course_name(context)
        sequence_title = context.get('sequence_title', UNDEFINED)
        def title():
            return render_title(context)
        __M_writer = context.writer()
        __M_writer(u'\n<title data-base-title="')
        __M_writer(filters.html_escape(filters.decode.utf8(static.get_page_title_breadcrumbs(section_title, course_name()))))
        __M_writer(u'">\n  ')
        __M_writer(filters.html_escape(filters.decode.utf8(static.get_page_title_breadcrumbs(sequence_title, section_title, course_name()))))
        __M_writer(u'\n</title>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_online_help_token(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        return "courseware" 
        
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_js_extra(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        fragment = context.get('fragment', UNDEFINED)
        request = context.get('request', UNDEFINED)
        course = context.get('course', UNDEFINED)
        def js_extra():
            return render_js_extra(context)
        static = _mako_get_namespace(context, 'static')
        staff_access = context.get('staff_access', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n  <script type="text/javascript" src="')
        __M_writer(filters.html_escape(filters.decode.utf8(static.url('common/js/vendor/jquery.scrollTo.js'))))
        __M_writer(u'"></script>\n  <script type="text/javascript" src="')
        __M_writer(filters.html_escape(filters.decode.utf8(static.url('js/vendor/flot/jquery.flot.js'))))
        __M_writer(u'"></script>\n\n  ')
        def ccall(caller):
            def body():
                __M_writer = context.writer()
                return ''
            return [body]
        context.caller_stack.nextcaller = runtime.Namespace('caller', context, callables=ccall(__M_caller))
        try:
            __M_writer(filters.html_escape(filters.decode.utf8(static.js(group=u'courseware'))))
        finally:
            context.caller_stack.nextcaller = None
        __M_writer(u'\n  ')
        runtime._include_file(context, u'/mathjax_include.html', _template_uri, disable_fast_preview=True)
        __M_writer(u'\n\n')
        if settings.FEATURES.get('ENABLE_COURSEWARE_SEARCH'):
            __M_writer(u'    ')
            def ccall(caller):
                def body():
                    __M_writer = context.writer()
                    __M_writer(u"\n        var courseId = $('.courseware-results').data('courseId');\n        CourseSearchFactory({\n            courseId: courseId,\n            searchHeader: $('.search-bar')\n        });\n    ")
                    return ''
                return [body]
            context.caller_stack.nextcaller = runtime.Namespace('caller', context, callables=ccall(__M_caller))
            try:
                __M_writer(filters.html_escape(filters.decode.utf8(static.require_module(class_name=u'CourseSearchFactory',module_name=u'course_search/js/course_search_factory'))))
            finally:
                context.caller_stack.nextcaller = None
            __M_writer(u'\n')
        __M_writer(u'\n  ')
        def ccall(caller):
            def body():
                __M_writer = context.writer()
                __M_writer(u'\n    CoursewareFactory();\n  ')
                return ''
            return [body]
        context.caller_stack.nextcaller = runtime.Namespace('caller', context, callables=ccall(__M_caller))
        try:
            __M_writer(filters.html_escape(filters.decode.utf8(static.require_module(class_name=u'CoursewareFactory',module_name=u'js/courseware/courseware_factory'))))
        finally:
            context.caller_stack.nextcaller = None
        __M_writer(u'\n\n')
        if staff_access:
            __M_writer(u'  \t')
            runtime._include_file(context, u'xqa_interface.html', _template_uri)
            __M_writer(u'\n')
        __M_writer(u'\n  <script type="text/javascript">\n    var $$course_id = "')
        __M_writer(js_escaped_string(course.id ))
        __M_writer(u'";\n  </script>\n\n')
        if not request.user.is_authenticated:
            __M_writer(u'      <script type="text/javascript">\n        // Disable discussions\n        $(\'.xblock-student_view-discussion button.discussion-show\').attr(\'disabled\', true);\n\n        // Insert message informing user discussions are only available to logged in users.\n        $(\'.discussion-module\')\n      </script>\n')
        __M_writer(u'\n')
        __M_writer(filters.html_escape(filters.decode.utf8(HTML(fragment.foot_html()))))
        __M_writer(u'\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_headextra(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        fragment = context.get('fragment', UNDEFINED)
        def headextra():
            return render_headextra(context)
        static = _mako_get_namespace(context, 'static')
        request = context.get('request', UNDEFINED)
        course = context.get('course', UNDEFINED)
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
        if is_edxnotes_enabled(course, request.user):
            def ccall(caller):
                def body():
                    __M_writer = context.writer()
                    return ''
                return [body]
            context.caller_stack.nextcaller = runtime.Namespace('caller', context, callables=ccall(__M_caller))
            try:
                __M_writer(filters.html_escape(filters.decode.utf8(static.css(group=u'style-student-notes'))))
            finally:
                context.caller_stack.nextcaller = None
            __M_writer(u'\n')
        __M_writer(u'\n<script type="text/javascript" src="')
        __M_writer(filters.html_escape(filters.decode.utf8(static.url('js/jquery.autocomplete.js'))))
        __M_writer(u'"></script>\n<script type="text/javascript" src="')
        __M_writer(filters.html_escape(filters.decode.utf8(static.url('js/src/tooltip_manager.js'))))
        __M_writer(u'"></script>\n\n<link href="')
        __M_writer(filters.html_escape(filters.decode.utf8(static.url('css/vendor/jquery.autocomplete.css'))))
        __M_writer(u'" rel="stylesheet" type="text/css">\n  ')
        __M_writer(filters.html_escape(filters.decode.utf8(HTML(fragment.head_html()))))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_header_extras(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        include_special_exams = context.get('include_special_exams', UNDEFINED)
        def header_extras():
            return render_header_extras(context)
        static = _mako_get_namespace(context, 'static')
        __M_writer = context.writer()
        __M_writer(u'\n\n')
        for template_name in ["image-modal"]:
            __M_writer(u'<script type="text/template" id="')
            __M_writer(filters.html_escape(filters.decode.utf8(template_name)))
            __M_writer(u'-tpl">\n    ')
            def ccall(caller):
                def body():
                    __M_writer = context.writer()
                    return ''
                return [body]
            context.caller_stack.nextcaller = runtime.Namespace('caller', context, callables=ccall(__M_caller))
            try:
                __M_writer(filters.html_escape(filters.decode.utf8(static.include(path=u'common/templates/' + (template_name) + u'.underscore'))))
            finally:
                context.caller_stack.nextcaller = None
            __M_writer(u'\n</script>\n')
        __M_writer(u'\n')
        if include_special_exams is not UNDEFINED and include_special_exams:
            for template_name in ["proctored-exam-status"]:
                __M_writer(u'    <script type="text/template" id="')
                __M_writer(filters.html_escape(filters.decode.utf8(template_name)))
                __M_writer(u'-tpl">\n        ')
                def ccall(caller):
                    def body():
                        __M_writer = context.writer()
                        return ''
                    return [body]
                context.caller_stack.nextcaller = runtime.Namespace('caller', context, callables=ccall(__M_caller))
                try:
                    __M_writer(filters.html_escape(filters.decode.utf8(static.include(path=u'courseware/' + (template_name) + u'.underscore'))))
                finally:
                    context.caller_stack.nextcaller = None
                __M_writer(u'\n    </script>\n')
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"16": 5, "36": 3, "42": 1, "80": 1, "81": 2, "82": 3, "83": 4, "84": 16, "85": 17, "91": 19, "92": 22, "97": 24, "102": 30, "107": 48, "112": 63, "117": 106, "118": 110, "119": 111, "120": 111, "121": 111, "122": 112, "123": 113, "124": 113, "125": 113, "126": 115, "127": 117, "128": 118, "129": 118, "130": 118, "131": 120, "132": 123, "133": 124, "134": 129, "135": 129, "136": 130, "137": 130, "138": 134, "139": 135, "140": 137, "141": 137, "142": 140, "143": 140, "144": 141, "145": 141, "146": 148, "147": 152, "148": 152, "149": 153, "150": 154, "151": 154, "152": 154, "153": 155, "154": 156, "155": 156, "156": 156, "157": 158, "158": 163, "159": 166, "160": 166, "161": 169, "162": 170, "163": 171, "164": 171, "165": 171, "166": 171, "167": 175, "168": 176, "169": 176, "170": 176, "171": 176, "172": 176, "173": 177, "174": 177, "175": 177, "176": 177, "177": 177, "178": 177, "179": 181, "180": 182, "181": 183, "182": 183, "183": 183, "184": 183, "185": 183, "186": 183, "187": 187, "188": 187, "189": 187, "190": 195, "193": 198, "194": 199, "195": 200, "200": 204, "201": 216, "202": 217, "203": 218, "206": 220, "207": 224, "208": 225, "209": 225, "210": 232, "211": 232, "212": 232, "213": 232, "214": 236, "215": 236, "216": 239, "217": 240, "218": 241, "219": 242, "220": 242, "221": 242, "222": 243, "223": 245, "224": 245, "225": 245, "226": 247, "227": 249, "228": 250, "229": 251, "230": 251, "231": 251, "232": 251, "233": 251, "234": 253, "235": 254, "236": 254, "237": 254, "238": 256, "239": 258, "240": 259, "241": 259, "242": 259, "243": 261, "249": 20, "254": 20, "255": 21, "257": 21, "263": 24, "270": 24, "271": 24, "277": 26, "288": 26, "289": 27, "290": 27, "291": 28, "292": 28, "298": 4, "302": 4, "309": 65, "320": 65, "321": 66, "322": 66, "323": 67, "324": 67, "332": 69, "335": 69, "336": 70, "337": 70, "338": 72, "339": 73, "343": 73, "348": 73, "351": 79, "352": 81, "356": 82, "361": 82, "364": 84, "365": 86, "366": 87, "367": 87, "368": 87, "369": 89, "370": 91, "371": 91, "372": 94, "373": 95, "374": 103, "375": 104, "376": 104, "382": 50, "392": 50, "400": 51, "403": 51, "411": 52, "414": 52, "415": 54, "423": 55, "426": 55, "427": 57, "428": 58, "429": 58, "430": 59, "431": 59, "432": 61, "433": 61, "434": 62, "435": 62, "441": 32, "449": 32, "450": 34, "451": 35, "452": 35, "453": 35, "461": 36, "464": 36, "465": 39, "466": 40, "467": 41, "468": 42, "469": 42, "470": 42, "478": 43, "481": 43, "482": 47, "488": 482}, "uri": "courseware/courseware.html", "filename": "/home/nttlong/code/edx/apps/edx/edx-platform/xdj-gnol-lms-templates/courseware/courseware.html"}
__M_END_METADATA
"""
