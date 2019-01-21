# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1548075124.954925
_enable_loop = True
_template_filename = u'/home/nttlong/code/edx/apps/edx/edx-platform/xdj-gnol-lms-templates/learner_profile/learner-achievements-fragment.html'
_template_uri = 'learner_profile/learner-achievements-fragment.html'
_source_encoding = 'utf-8'
_exports = []



from django.utils.translation import ugettext as _
from openedx.core.djangolib.markup import HTML, Text


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace(u'static', context._clean_inheritance_tokens(), templateuri=u'/static_content.html', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, u'static')] = ns

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        user_timezone = context.get('user_timezone', UNDEFINED)
        marketing_link = context.get('marketing_link', UNDEFINED)
        settings = context.get('settings', UNDEFINED)
        own_profile = context.get('own_profile', UNDEFINED)
        static = _mako_get_namespace(context, 'static')
        user_language = context.get('user_language', UNDEFINED)
        course_certificates = context.get('course_certificates', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n<div class="learner-achievements">\n')
        if course_certificates or own_profile:
            __M_writer(u'        <h3 class="u-field-title">Course Certificates</h3>\n')
            if course_certificates:
                for certificate in course_certificates:
                    __M_writer(u'                ')

                    certificate_url = certificate['download_url']
                    course = certificate['course']
                    
                    completion_date_message_html = Text(_('Completed {completion_date_html}')).format(
                        completion_date_html=HTML(
                            '<span'
                            '    class="localized-datetime start-date"'
                            '    data-datetime="{completion_date}"'
                            '    data-format="shortDate"'
                            '    data-timezone="{user_timezone}"'
                            '    data-language="{user_language}"'
                            '></span>'
                        ).format(
                            completion_date=certificate['created'],
                            user_timezone=user_timezone,
                            user_language=user_language,
                        ),
                    )
                    
                    
                    __M_locals_builtin_stored = __M_locals_builtin()
                    __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['course','completion_date_message_html','certificate_url'] if __M_key in __M_locals_builtin_stored]))
                    __M_writer(u'\n')
                    if certificate_url:
                        __M_writer(u'                    <a href="')
                        __M_writer(filters.html_escape(filters.decode.utf8(certificate_url)))
                        __M_writer(u'" target="_blank">\n                        <div class="card certificate-card mode-')
                        __M_writer(filters.html_escape(filters.decode.utf8(certificate['type'])))
                        __M_writer(u'">\n                            <div class="card-logo">\n                                <h4 class="sr-only">\n                                    ')
                        __M_writer(filters.html_escape(filters.decode.utf8(_('{course_mode} certificate').format(
                                        course_mode=certificate['type'],
                                    ))))
                        __M_writer(u'\n                                </h4>\n                            </div>\n                            <div class="card-content">\n                                <div class="card-supertitle">')
                        __M_writer(filters.html_escape(filters.decode.utf8(course.display_org_with_default)))
                        __M_writer(u'</div>\n                                <div class="card-title">')
                        __M_writer(filters.html_escape(filters.decode.utf8(course.display_name_with_default)))
                        __M_writer(u'</div>\n                                <p class="card-text">')
                        __M_writer(filters.html_escape(filters.decode.utf8(completion_date_message_html)))
                        __M_writer(u'</p>\n                            </div>\n                        </div>\n                    </a>\n')
                    else:
                        __M_writer(u'                    <div class="card certificate-card mode-')
                        __M_writer(filters.html_escape(filters.decode.utf8(certificate['type'])))
                        __M_writer(u'">\n                        <div class="card-logo">\n                            <h4 class="sr-only">\n                                ')
                        __M_writer(filters.html_escape(filters.decode.utf8(_('{course_mode} certificate').format(
                                    course_mode=certificate['type'],
                                ))))
                        __M_writer(u'\n                            </h4>\n                        </div>\n                        <div class="card-content">\n                            <div class="card-supertitle">')
                        __M_writer(filters.html_escape(filters.decode.utf8(course.display_org_with_default)))
                        __M_writer(u'</div>\n                            <div class="card-title">')
                        __M_writer(filters.html_escape(filters.decode.utf8(course.display_name_with_default)))
                        __M_writer(u'</div>\n                            <p class="card-text">')
                        __M_writer(filters.html_escape(filters.decode.utf8(completion_date_message_html)))
                        __M_writer(u'</p>\n                        </div>\n                    </div>\n')
            elif own_profile:
                __M_writer(u'            <div class="learner-message">\n                <h4 class="message-header">')
                __M_writer(filters.html_escape(filters.decode.utf8(_("You haven't earned any certificates yet."))))
                __M_writer(u'</h4>\n')
                if settings.FEATURES.get('COURSES_ARE_BROWSABLE'):
                    __M_writer(u'                    <p class="message-actions">\n                        <a class="btn btn-brand" href="')
                    __M_writer(filters.html_escape(filters.decode.utf8(marketing_link('COURSES'))))
                    __M_writer(u'">\n                            <span class="icon fa fa-search" aria-hidden="true"></span>\n                            ')
                    __M_writer(filters.html_escape(filters.decode.utf8(_('Explore New Courses'))))
                    __M_writer(u'\n                        </a>\n                    </p>\n')
                __M_writer(u'            </div>\n')
        __M_writer(u'</div>\n\n')
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
{"source_encoding": "utf-8", "line_map": {"129": 89, "135": 129, "16": 7, "28": 5, "31": 3, "43": 2, "44": 3, "45": 5, "46": 10, "47": 13, "48": 14, "49": 15, "50": 16, "51": 17, "52": 17, "75": 36, "76": 37, "77": 38, "78": 38, "79": 38, "80": 39, "81": 39, "82": 42, "85": 44, "86": 48, "87": 48, "88": 49, "89": 49, "90": 50, "91": 50, "92": 54, "93": 55, "94": 55, "95": 55, "96": 58, "99": 60, "100": 64, "101": 64, "102": 65, "103": 65, "104": 66, "105": 66, "106": 71, "107": 72, "108": 73, "109": 73, "110": 74, "111": 75, "112": 76, "113": 76, "114": 78, "115": 78, "116": 82, "117": 85, "121": 87, "126": 87}, "uri": "learner_profile/learner-achievements-fragment.html", "filename": "/home/nttlong/code/edx/apps/edx/edx-platform/xdj-gnol-lms-templates/learner_profile/learner-achievements-fragment.html"}
__M_END_METADATA
"""
