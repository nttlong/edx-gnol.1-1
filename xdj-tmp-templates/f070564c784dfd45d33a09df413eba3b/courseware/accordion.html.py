# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1548073574.777231
_enable_loop = True
_template_filename = u'/home/nttlong/code/edx/apps/edx/edx-platform/xdj-gnol-lms-templates/courseware/accordion.html'
_template_uri = 'courseware/accordion.html'
_source_encoding = 'utf-8'
_exports = ['make_chapter']



from django.urls import reverse
from django.utils.translation import ugettext as _
from django.conf import settings
from openedx.core.djangolib.markup import HTML, Text


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace(u'static', context._clean_inheritance_tokens(), templateuri=u'../x-static-content.html', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, u'static')] = ns

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        toc = context.get('toc', UNDEFINED)
        static = _mako_get_namespace(context, 'static')
        def make_chapter(chapter):
            return render_make_chapter(context._locals(__M_locals),chapter)
        __M_writer = context.writer()
        __M_writer(u'\n')
        __M_writer(u'\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')
        for chapter in toc:
            __M_writer(u'    ')
            __M_writer(filters.html_escape(filters.decode.utf8(make_chapter(chapter))))
            __M_writer(u'\n')
        __M_writer(u'\n\n')
        if toc:
            __M_writer(u'    ')
            def ccall(caller):
                def body():
                    __M_writer = context.writer()
                    __M_writer(u'\n        AccordionEvents();\n    ')
                    return ''
                return [body]
            context.caller_stack.nextcaller = runtime.Namespace('caller', context, callables=ccall(__M_caller))
            try:
                __M_writer(filters.html_escape(filters.decode.utf8(static.require_module_async(class_name=u'AccordionEvents',module_name=u'js/courseware/accordion_events'))))
            finally:
                context.caller_stack.nextcaller = None
            __M_writer(u'\n\n    ')
            def ccall(caller):
                def body():
                    __M_writer = context.writer()
                    __M_writer(u'\n        DateUtilFactory.transform(iterationKey=".localized-datetime");\n    ')
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


def render_make_chapter(context,chapter):
    __M_caller = context.caller_stack._push_frame()
    try:
        course_id = context.get('course_id', UNDEFINED)
        user_timezone = context.get('user_timezone', UNDEFINED)
        user_language = context.get('user_language', UNDEFINED)
        due_date = context.get('due_date', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n')

        if chapter.get('active'):
            aria_label = _('{chapter} current chapter').format(chapter=chapter['display_name'])
            active_class = 'active'
        else:
            aria_label = chapter['display_name']
            active_class = ''
        
        
        __M_writer(u'\n<a href="#')
        __M_writer(filters.html_escape(filters.decode.utf8(chapter['display_id'])))
        __M_writer(u'-child" role="button" class="button-chapter chapter ')
        __M_writer(filters.html_escape(filters.decode.utf8(active_class)))
        __M_writer(u'" id="')
        __M_writer(filters.html_escape(filters.decode.utf8(chapter['display_id'])))
        __M_writer(u'-parent" aria-controls="')
        __M_writer(filters.html_escape(filters.decode.utf8(chapter['display_id'])))
        __M_writer(u'-child" aria-expanded="false">\n    <span class="group-heading ')
        __M_writer(filters.html_escape(filters.decode.utf8(active_class)))
        __M_writer(u'" aria-label="')
        __M_writer(filters.html_escape(filters.decode.utf8(aria_label)))
        __M_writer(u'">\n        <span class="icon fa fa-caret-right" aria-hidden="true"></span>\n        ')
        __M_writer(filters.html_escape(filters.decode.utf8(HTML(chapter['display_name']))))
        __M_writer(u'\n    </span>\n</a>\n<div class="chapter-content-container" id="')
        __M_writer(filters.html_escape(filters.decode.utf8(chapter['display_id'])))
        __M_writer(u'-child" tabindex="-1" role="region" aria-label="')
        __M_writer(filters.html_escape(filters.decode.utf8(chapter['display_name'])))
        __M_writer(u' submenu">\n    <div class="chapter-menu">\n')
        for section in chapter['sections']:
            __M_writer(u'        <div class="menu-item ')
            __M_writer(filters.html_escape(filters.decode.utf8('active' if 'active' in section and section['active'] else '')))
            __M_writer(u' ')
            __M_writer(filters.html_escape(filters.decode.utf8('graded'  if 'graded' in section and section['graded'] else '')))
            __M_writer(u'">\n            <a class="accordion-nav" href="')
            __M_writer(filters.html_escape(filters.decode.utf8(reverse('courseware_section', args=[course_id, chapter['url_name'], section['url_name']]))))
            __M_writer(u'">\n                <p class="accordion-display-name">')
            __M_writer(filters.html_escape(filters.decode.utf8(HTML(section['display_name']))))
            __M_writer(u' ')
            __M_writer(filters.html_escape(filters.decode.utf8(Text(_('{span_start}current section{span_end}')).format(
                        span_start=HTML('<span class="sr">'),
                        span_end=HTML('</span>'),
                    ) if 'active' in section and section['active'] else '')))
            __M_writer(u'</p>\n\n')
            __M_writer(u'                ')

            if section.get('due') is None:
                data_string = section['format']
            else:
                if 'proctoring' in section:
                    data_string = _('due {date}')
                else:
                    data_string = _("{section_format} due {{date}}").format(section_format=section['format'])
                           
            
            __M_writer(u'\n')
            if section['format'] or due_date or 'proctoring' in section:
                __M_writer(u'                <p class="subtitle">\n')
                if 'proctoring' in section:
                    __M_writer(u'                        <span class="menu-icon icon fa ')
                    __M_writer(filters.html_escape(filters.decode.utf8(section['proctoring'].get('suggested_icon', 'fa-pencil-square-o'))))
                    __M_writer(u' ')
                    __M_writer(filters.html_escape(filters.decode.utf8(section['proctoring'].get('status', 'eligible'))))
                    __M_writer(u'" aria-hidden="true"></span>\n                        <span class="subtitle-name">')
                    __M_writer(filters.html_escape(filters.decode.utf8(section['proctoring'].get('short_description', ''))))
                    __M_writer(u'</span>\n\n')
                    if not section['proctoring'].get('in_completed_state', False):
                        __M_writer(u'                            <span class="localized-datetime subtitle-name" data-datetime="')
                        __M_writer(filters.html_escape(filters.decode.utf8(section['due'])))
                        __M_writer(u'" data-string="')
                        __M_writer(filters.html_escape(filters.decode.utf8(data_string)))
                        __M_writer(u'" data-timezone="')
                        __M_writer(filters.html_escape(filters.decode.utf8(user_timezone)))
                        __M_writer(u'" data-language="')
                        __M_writer(filters.html_escape(filters.decode.utf8(user_language)))
                        __M_writer(u'"></span>\n')
                else:
                    __M_writer(u'                        <span class="localized-datetime subtitle-name" data-datetime="')
                    __M_writer(filters.html_escape(filters.decode.utf8(section['due'])))
                    __M_writer(u'" data-string="')
                    __M_writer(filters.html_escape(filters.decode.utf8(data_string)))
                    __M_writer(u'" data-timezone="')
                    __M_writer(filters.html_escape(filters.decode.utf8(user_timezone)))
                    __M_writer(u'" data-language="')
                    __M_writer(filters.html_escape(filters.decode.utf8(user_language)))
                    __M_writer(u'"></span>\n\n')
                    if 'graded' in section and section['graded']:
                        __M_writer(u'                            <span class="menu-icon icon fa fa-pencil-square-o" aria-hidden="true"></span>\n                            <span class="sr">')
                        __M_writer(filters.html_escape(filters.decode.utf8(_("This content is graded"))))
                        __M_writer(u'</span>\n')
                __M_writer(u'                </p>\n')
            __M_writer(u'            </a>\n        </div>\n')
        __M_writer(u'    </div>\n</div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"16": 3, "30": 2, "33": 1, "42": 1, "43": 2, "44": 8, "45": 79, "46": 81, "47": 82, "48": 82, "49": 82, "50": 84, "51": 86, "52": 87, "56": 87, "61": 87, "64": 89, "68": 91, "73": 91, "76": 93, "82": 10, "90": 10, "91": 11, "100": 18, "101": 19, "102": 19, "103": 19, "104": 19, "105": 19, "106": 19, "107": 19, "108": 19, "109": 20, "110": 20, "111": 20, "112": 20, "113": 22, "114": 22, "115": 25, "116": 25, "117": 25, "118": 25, "119": 27, "120": 28, "121": 28, "122": 28, "123": 28, "124": 28, "125": 29, "126": 29, "127": 30, "128": 30, "129": 30, "133": 33, "134": 41, "135": 41, "145": 49, "146": 50, "147": 51, "148": 52, "149": 54, "150": 54, "151": 54, "152": 54, "153": 54, "154": 55, "155": 55, "156": 59, "157": 60, "158": 60, "159": 60, "160": 60, "161": 60, "162": 60, "163": 60, "164": 60, "165": 60, "166": 62, "167": 65, "168": 65, "169": 65, "170": 65, "171": 65, "172": 65, "173": 65, "174": 65, "175": 65, "176": 67, "177": 68, "178": 69, "179": 69, "180": 72, "181": 74, "182": 77, "188": 182}, "uri": "courseware/accordion.html", "filename": "/home/nttlong/code/edx/apps/edx/edx-platform/xdj-gnol-lms-templates/courseware/accordion.html"}
__M_END_METADATA
"""
