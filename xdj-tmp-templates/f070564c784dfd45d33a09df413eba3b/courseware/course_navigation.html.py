# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1548073578.873404
_enable_loop = True
_template_filename = u'/home/nttlong/code/edx/apps/edx/edx-platform/xdj-gnol-lms-templates/courseware/course_navigation.html'
_template_uri = u'/courseware/course_navigation.html'
_source_encoding = 'utf-8'
_exports = [u'extratabs']



from courseware.tabs import get_course_tab_list
from django.conf import settings
from django.urls import reverse
from django.utils.translation import ugettext as _


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
        uses_bootstrap = context.get('uses_bootstrap', UNDEFINED)
        tab_image = context.get('tab_image', UNDEFINED)
        request = context.get('request', UNDEFINED)
        def extratabs():
            return render_extratabs(context._locals(__M_locals))
        course = context.get('course', UNDEFINED)
        static = _mako_get_namespace(context, 'static')
        active_page_context = context.get('active_page_context', UNDEFINED)
        default_tab = context.get('default_tab', UNDEFINED)
        disable_tabs = context.get('disable_tabs', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n')
        __M_writer(u'\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')

        if active_page is None and active_page_context is not UNDEFINED:
            # If active_page is not passed in as an argument, it may be in the context as active_page_context
            active_page = active_page_context
        
        if course is not None:
            include_special_exams = settings.FEATURES.get('ENABLE_SPECIAL_EXAMS', False) and (course.enable_proctored_exams or course.enable_timed_exams)
        
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['include_special_exams','active_page'] if __M_key in __M_locals_builtin_stored]))
        __M_writer(u'\n\n')
        if include_special_exams is not UNDEFINED and include_special_exams:
            __M_writer(u'    ')
            def ccall(caller):
                def body():
                    __M_writer = context.writer()
                    return ''
                return [body]
            context.caller_stack.nextcaller = runtime.Namespace('caller', context, callables=ccall(__M_caller))
            try:
                __M_writer(filters.html_escape(filters.decode.utf8(static.js(group=u'proctoring'))))
            finally:
                context.caller_stack.nextcaller = None
            __M_writer(u'\n')
            for template_name in ["proctored-exam-status"]:
                __M_writer(u'        <script type="text/template" id="')
                __M_writer(filters.html_escape(filters.decode.utf8(template_name)))
                __M_writer(u'-tpl">\n            ')
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
                __M_writer(u'\n        </script>\n')
            __M_writer(u'    <div class="proctored_exam_status"></div>\n')
        __M_writer(u'\n')
        if disable_tabs is UNDEFINED or not disable_tabs:
            __M_writer(u'    ')

            tab_list = get_course_tab_list(request, course)
            
            
            __M_locals_builtin_stored = __M_locals_builtin()
            __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['tab_list'] if __M_key in __M_locals_builtin_stored]))
            __M_writer(u'\n')
            if uses_bootstrap:
                __M_writer(u'        <nav class="navbar course-tabs pb-0 navbar-expand" aria-label="')
                __M_writer(filters.html_escape(filters.decode.utf8(_('Course'))))
                __M_writer(u'">\n            <ul class="navbar-nav mr-auto">\n')
                for tab in tab_list:
                    __M_writer(u'                    ')

                    tab_is_active = tab.tab_id in (active_page, default_tab)
                    
                    
                    __M_locals_builtin_stored = __M_locals_builtin()
                    __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['tab_is_active'] if __M_key in __M_locals_builtin_stored]))
                    __M_writer(u'\n                    <li class="nav-item ')
                    __M_writer(filters.html_escape(filters.decode.utf8('active' if tab_is_active else '')))
                    __M_writer(u'">\n                        <a href="')
                    __M_writer(filters.html_escape(filters.decode.utf8(tab.link_func(course, reverse))))
                    __M_writer(u'" class="nav-link">\n                            ')
                    __M_writer(filters.html_escape(filters.decode.utf8(_(tab.name))))
                    __M_writer(u'\n')
                    if tab_is_active:
                        __M_writer(u'                                <span class="sr-only">, ')
                        __M_writer(filters.html_escape(filters.decode.utf8(_('current location'))))
                        __M_writer(u'</span>\n')
                    if tab_image:
                        __M_writer(u'                                <img src="')
                        __M_writer(filters.html_escape(filters.decode.utf8(tab_image)))
                        __M_writer(u'" alt="')
                        __M_writer(filters.html_escape(filters.decode.utf8(_('needs attention'))))
                        __M_writer(u'" />\n')
                    __M_writer(u'                        </a>\n                    </li>\n')
                __M_writer(u'            </ul>\n        </nav>\n')
            else:
                __M_writer(u'        <nav class="')
                __M_writer(filters.html_escape(filters.decode.utf8(active_page)))
                __M_writer(u' wrapper-course-material" aria-label="')
                __M_writer(filters.html_escape(filters.decode.utf8(_('Course Material'))))
                __M_writer(u'">\n            <div class="course-material">\n                ')

                tabs_tmpl = static.get_template_path('/courseware/tabs.html')
                
                
                __M_locals_builtin_stored = __M_locals_builtin()
                __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['tabs_tmpl'] if __M_key in __M_locals_builtin_stored]))
                __M_writer(u'\n                <ol class="tabs course-tabs">\n                    ')
                runtime._include_file(context, (tabs_tmpl), _template_uri, tab_list=tab_list,active_page=active_page,default_tab=default_tab,tab_image=tab_image)
                __M_writer(u'\n                    ')
                if 'parent' not in context._data or not hasattr(context._data['parent'], 'extratabs'):
                    context['self'].extratabs(**pageargs)
                

                __M_writer(u'\n                </ol>\n            </div>\n        </nav>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_extratabs(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def extratabs():
            return render_extratabs(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"128": 52, "129": 52, "130": 52, "131": 52, "132": 54, "133": 57, "134": 59, "135": 60, "136": 60, "137": 60, "138": 60, "139": 60, "140": 62, "16": 6, "146": 64, "147": 66, "148": 66, "153": 67, "30": 4, "159": 67, "33": 3, "170": 159, "48": 2, "49": 3, "50": 4, "51": 11, "52": 13, "63": 20, "64": 22, "65": 23, "73": 23, "76": 23, "77": 24, "78": 25, "79": 25, "80": 25, "88": 26, "91": 26, "92": 29, "93": 31, "94": 32, "95": 33, "96": 33, "102": 35, "103": 36, "104": 37, "105": 37, "106": 37, "107": 39, "108": 40, "109": 40, "115": 42, "116": 43, "117": 43, "118": 44, "119": 44, "120": 45, "121": 45, "122": 46, "123": 47, "124": 47, "125": 47, "126": 49, "127": 52}, "uri": "/courseware/course_navigation.html", "filename": "/home/nttlong/code/edx/apps/edx/edx-platform/xdj-gnol-lms-templates/courseware/course_navigation.html"}
__M_END_METADATA
"""
