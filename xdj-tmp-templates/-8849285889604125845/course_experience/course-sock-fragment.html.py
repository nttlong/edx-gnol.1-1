# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1548073574.992184
_enable_loop = True
_template_filename = u'/home/nttlong/code/edx/apps/edx/edx-platform/common/lib/capa/capa/templates/course_experience/course-sock-fragment.html'
_template_uri = 'course_experience/course-sock-fragment.html'
_source_encoding = 'utf-8'
_exports = [u'content']



from django.utils.translation import ugettext as _
from openedx.core.djangolib.markup import HTML, Text
from openedx.features.course_experience import DISPLAY_COURSE_SOCK_FLAG


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
        upgrade_url = context.get('upgrade_url', UNDEFINED)
        settings = context.get('settings', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        course_id = context.get('course_id', UNDEFINED)
        static = _mako_get_namespace(context, 'static')
        show_course_sock = context.get('show_course_sock', UNDEFINED)
        course_price = context.get('course_price', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n')
        __M_writer(u'\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer(u'\n\n')
        def ccall(caller):
            def body():
                __M_writer = context.writer()
                __M_writer(u"\n    new CourseSock({\n        el:'.verification-sock'\n    });\n")
                return ''
            return [body]
        context.caller_stack.nextcaller = runtime.Namespace('caller', context, callables=ccall(__M_caller))
        try:
            __M_writer(filters.html_escape(filters.decode.utf8(static.webpack(entry=u'CourseSock'))))
        finally:
            context.caller_stack.nextcaller = None
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        upgrade_url = context.get('upgrade_url', UNDEFINED)
        settings = context.get('settings', UNDEFINED)
        def content():
            return render_content(context)
        course_id = context.get('course_id', UNDEFINED)
        static = _mako_get_namespace(context, 'static')
        show_course_sock = context.get('show_course_sock', UNDEFINED)
        course_price = context.get('course_price', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n')
        if show_course_sock:
            __M_writer(u'    <div class="verification-sock"\n')
            if not DISPLAY_COURSE_SOCK_FLAG.is_enabled(course_id):
                __M_writer(u'        style="display: none"\n')
            __M_writer(u'    >\n        <button type="button" aria-expanded="false" class="btn btn-primary focusable action-toggle-verification-sock">\n            ')
            __M_writer(filters.html_escape(filters.decode.utf8(_('Learn About Verified Certificates'))))
            __M_writer(u'\n        </button>\n        <div class="verification-main-panel">\n            <div class="verification-desc-panel content-main">\n                <h2>')
            __M_writer(filters.html_escape(filters.decode.utf8(_('{platform_name} Verified Certificate').format(platform_name=settings.PLATFORM_NAME))))
            __M_writer(u'</h2>\n                <h3>')
            __M_writer(filters.html_escape(filters.decode.utf8(_('Why upgrade?'))))
            __M_writer(u'</h3>\n                <ul>\n                    <li>')
            __M_writer(filters.html_escape(filters.decode.utf8(_('Official proof of completion'))))
            __M_writer(u'</li>\n                    <li>')
            __M_writer(filters.html_escape(filters.decode.utf8(_('Easily shareable certificate'))))
            __M_writer(u'</li>\n                    <li>')
            __M_writer(filters.html_escape(filters.decode.utf8(_('Proven motivator to complete the course'))))
            __M_writer(u'</li>\n                    <li>')
            __M_writer(filters.html_escape(filters.decode.utf8(_('Certificate purchases help {platform_name} continue to offer free courses').format(platform_name=settings.PLATFORM_NAME))))
            __M_writer(u'</li>\n                </ul>\n                <h3>')
            __M_writer(filters.html_escape(filters.decode.utf8(_('How it works'))))
            __M_writer(u'</h3>\n                <ul>\n                    <li>')
            __M_writer(filters.html_escape(filters.decode.utf8(_('Pay the Verified Certificate upgrade fee'))))
            __M_writer(u'</li>\n                    <li>')
            __M_writer(filters.html_escape(filters.decode.utf8(_('Verify your identity with a webcam and government-issued ID'))))
            __M_writer(u'</li>\n                    <li>')
            __M_writer(filters.html_escape(filters.decode.utf8(_('Study hard and pass the course'))))
            __M_writer(u'</li>\n                    <li>')
            __M_writer(filters.html_escape(filters.decode.utf8(_('Share your certificate with friends, employers, and others'))))
            __M_writer(u'</li>\n                </ul>\n')
            if settings.PLATFORM_NAME == 'edX':
                __M_writer(u'                    <h3>')
                __M_writer(filters.html_escape(filters.decode.utf8(_('edX Learner Stories'))))
                __M_writer(u'</h3>\n                    <div class="learner-story-container">\n                        <img class="student-image" alt="Student Image" src="')
                __M_writer(filters.html_escape(filters.decode.utf8(static.url('course_experience/images/learner-quote.png'))))
                __M_writer(u'" />\n                        <div class="story-quote">\n                            ')
                __M_writer(filters.html_escape(filters.decode.utf8(_('My certificate has helped me showcase my knowledge on my \
                            resume - I feel like this certificate could really help me land \
                            my dream job!'))))
                __M_writer(u'\n                            <span class="author">- ')
                __M_writer(filters.html_escape(filters.decode.utf8(_('{learner_name}, edX Learner').format(learner_name='Christina Fong'))))
                __M_writer(u'</span>\n                        </div>\n                    </div>\n                    <div class="learner-story-container">\n                        <img class="student-image" alt="Student Image" src="')
                __M_writer(filters.html_escape(filters.decode.utf8(static.url('course_experience/images/learner-quote2.png'))))
                __M_writer(u'" />\n                        <div class="story-quote">\n                            ')
                __M_writer(filters.html_escape(filters.decode.utf8(_('I wanted to include a verified certificate on my resume and my profile to \
                            illustrate that I am working towards this goal I have and that I have \
                            achieved something while I was unemployed.'))))
                __M_writer(u'<br/>\n                            <span class="author">- ')
                __M_writer(filters.html_escape(filters.decode.utf8(_('{learner_name}, edX Learner').format(learner_name='Cheryl Troell'))))
                __M_writer(u'</span>\n                        </div>\n                    </div>\n')
            __M_writer(u'                <img class="mini-cert" alt="Example Certificate Image" src="')
            __M_writer(filters.html_escape(filters.decode.utf8(static.url('course_experience/images/verified-cert.png'))))
            __M_writer(u'"/>\n                <a href="')
            __M_writer(filters.html_escape(filters.decode.utf8(upgrade_url)))
            __M_writer(u'">\n                    <div class="btn btn-upgrade stuck-top focusable action-upgrade-certificate" data-creative="original_sock" data-position="sock">\n                        ')
            __M_writer(filters.html_escape(filters.decode.utf8(Text(_('Upgrade ({course_price})')).format(course_price=HTML(course_price)))))
            __M_writer(u'\n                    </div>\n                </a>\n            </div>\n        </div>\n    </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"130": 55, "131": 56, "132": 56, "133": 60, "134": 60, "135": 60, "136": 61, "137": 61, "138": 63, "139": 63, "16": 6, "145": 139, "29": 4, "32": 3, "45": 2, "46": 3, "47": 4, "48": 10, "53": 70, "57": 72, "62": 72, "65": 76, "71": 12, "83": 12, "84": 13, "85": 14, "86": 15, "87": 16, "88": 18, "89": 20, "90": 20, "91": 24, "92": 24, "93": 25, "94": 25, "95": 27, "96": 27, "97": 28, "98": 28, "99": 29, "100": 29, "101": 30, "102": 30, "103": 32, "104": 32, "105": 34, "106": 34, "107": 35, "108": 35, "109": 36, "110": 36, "111": 37, "112": 37, "113": 39, "114": 40, "115": 40, "116": 40, "117": 42, "118": 42, "119": 44, "122": 46, "123": 47, "124": 47, "125": 51, "126": 51, "127": 53}, "uri": "course_experience/course-sock-fragment.html", "filename": "/home/nttlong/code/edx/apps/edx/edx-platform/common/lib/capa/capa/templates/course_experience/course-sock-fragment.html"}
__M_END_METADATA
"""
