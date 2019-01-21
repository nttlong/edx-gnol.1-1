# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1548073808.370411
_enable_loop = True
_template_filename = u'/home/nttlong/code/edx/apps/edx/edx-platform/xdj-gnol-lms-templates/instructor/instructor_dashboard_2/instructor_dashboard_2.html'
_template_uri = 'instructor/instructor_dashboard_2/instructor_dashboard_2.html'
_source_encoding = 'utf-8'
_exports = [u'bodyclass', 'online_help_token', u'pagetitle', u'js_extra', u'headextra', u'header_extras']



from django.utils.translation import ugettext as _
from django.urls import reverse
from openedx.core.djangolib.markup import HTML


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
        def bodyclass():
            return render_bodyclass(context._locals(__M_locals))
        studio_url = context.get('studio_url', UNDEFINED)
        def pagetitle():
            return render_pagetitle(context._locals(__M_locals))
        def js_extra():
            return render_js_extra(context._locals(__M_locals))
        static = _mako_get_namespace(context, 'static')
        def headextra():
            return render_headextra(context._locals(__M_locals))
        def header_extras():
            return render_header_extras(context._locals(__M_locals))
        sections = context.get('sections', UNDEFINED)
        hidden = context.get('hidden', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n')
        __M_writer(u'\n')
        __M_writer(u'\n')
        __M_writer(u'\n')
        __M_writer(u'\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'bodyclass'):
            context['self'].bodyclass(**pageargs)
        

        __M_writer(u'\n\n')
        __M_writer(u'\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'pagetitle'):
            context['self'].pagetitle(**pageargs)
        

        __M_writer(u'\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'headextra'):
            context['self'].headextra(**pageargs)
        

        __M_writer(u'\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'js_extra'):
            context['self'].js_extra(**pageargs)
        

        __M_writer(u'\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'header_extras'):
            context['self'].header_extras(**pageargs)
        

        __M_writer(u'\n\n')
        runtime._include_file(context, u'/courseware/course_navigation.html', _template_uri, active_page='instructor')
        __M_writer(u'\n\n<style type="text/css"></style>\n\n<script language="JavaScript" type="text/javascript"></script>\n\n<div class="container">\n  <div class="instructor-dashboard-wrapper-2">\n        <main id="main" aria-label="Content" tabindex="-1">\n        <section class="instructor-dashboard-content-2" id="instructor-dashboard-content">\n          <h2 class="hd hd-2 instructor-dashboard-title">')
        __M_writer(filters.html_escape(filters.decode.utf8(_("Instructor Dashboard"))))
        __M_writer(u'</h2>\n          <div class="wrap-instructor-info studio-view">\n')
        if studio_url:
            __M_writer(u'            <a class="instructor-info-action" href="')
            __M_writer(filters.html_escape(filters.decode.utf8(studio_url)))
            __M_writer(u'">')
            __M_writer(filters.html_escape(filters.decode.utf8(_("View Course in Studio"))))
            __M_writer(u'</a>\n')
        __M_writer(u'          </div>\n\n')
        __M_writer(u'        <ul class="instructor-nav">\n')
        for section_data in sections:
            __M_writer(u'            ')
            is_hidden = section_data.get('is_hidden', False) 
            
            __M_locals_builtin_stored = __M_locals_builtin()
            __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['is_hidden'] if __M_key in __M_locals_builtin_stored]))
            __M_writer(u'\n')
            __M_writer(u'            ')
            dname = section_data['section_display_name'] 
            
            __M_locals_builtin_stored = __M_locals_builtin()
            __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['dname'] if __M_key in __M_locals_builtin_stored]))
            __M_writer(u'\n')
            if not is_hidden:
                __M_writer(u'              <li class="nav-item"><button type="button" class="btn-link ')
                __M_writer(filters.html_escape(filters.decode.utf8( section_data['section_key'] )))
                __M_writer(filters.html_escape(filters.decode.utf8(' hidden' if is_hidden else '')))
                __M_writer(u'" data-section="')
                __M_writer(filters.html_escape(filters.decode.utf8( section_data['section_key'] )))
                __M_writer(u'">')
                __M_writer(filters.html_escape(filters.decode.utf8(_(dname))))
                __M_writer(u'</button></li>\n')
        __M_writer(u'        </ul>\n\n')
        __M_writer(u'\n')
        for section_data in sections:
            __M_writer(u'          ')
            is_hidden = section_data.get('is_hidden', False) 
            
            __M_locals_builtin_stored = __M_locals_builtin()
            __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['is_hidden'] if __M_key in __M_locals_builtin_stored]))
            __M_writer(u'\n          <section id="')
            __M_writer(filters.html_escape(filters.decode.utf8( section_data['section_key'] )))
            __M_writer(u'" class="idash-section')
            __M_writer(filters.html_escape(filters.decode.utf8(' hidden' if hidden else '')))
            __M_writer(u'" aria-labelledby="header-')
            __M_writer(filters.html_escape(filters.decode.utf8(section_data['section_key'])))
            __M_writer(u'">\n              <h3 class="hd hd-3" id="header-')
            __M_writer(filters.html_escape(filters.decode.utf8( section_data['section_key'] )))
            __M_writer(u'">')
            __M_writer(filters.html_escape(filters.decode.utf8( section_data['section_display_name'] )))
            __M_writer(u'</h3>\n              ')
            runtime._include_file(context, ( section_data['section_key'] ) + u'.html', _template_uri, section_data=section_data)
            __M_writer(u'\n          </section>\n')
        __M_writer(u'        </section>\n        </main>\n  </div>\n</div>\n\n')
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


def render_bodyclass(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def bodyclass():
            return render_bodyclass(context)
        __M_writer = context.writer()
        __M_writer(u'view-in-course view-instructordash')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_online_help_token(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        return "instructor" 
        
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_pagetitle(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def pagetitle():
            return render_pagetitle(context)
        __M_writer = context.writer()
        __M_writer(filters.html_escape(filters.decode.utf8(_("Instructor Dashboard"))))
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_js_extra(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def js_extra():
            return render_js_extra(context)
        sections = context.get('sections', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n')
        for section_data in sections:
            if 'fragment' in section_data:
                __M_writer(u'      ')
                __M_writer(filters.html_escape(filters.decode.utf8(HTML(section_data['fragment'].foot_html()))))
                __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_headextra(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def headextra():
            return render_headextra(context)
        static = _mako_get_namespace(context, 'static')
        sections = context.get('sections', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n  ')
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
        __M_writer(u'\n  ')
        def ccall(caller):
            def body():
                __M_writer = context.writer()
                return ''
            return [body]
        context.caller_stack.nextcaller = runtime.Namespace('caller', context, callables=ccall(__M_caller))
        try:
            __M_writer(filters.html_escape(filters.decode.utf8(static.css(group=u'style-vendor-tinymce-content'))))
        finally:
            context.caller_stack.nextcaller = None
        __M_writer(u'\n  ')
        def ccall(caller):
            def body():
                __M_writer = context.writer()
                return ''
            return [body]
        context.caller_stack.nextcaller = runtime.Namespace('caller', context, callables=ccall(__M_caller))
        try:
            __M_writer(filters.html_escape(filters.decode.utf8(static.css(group=u'style-vendor-tinymce-skin'))))
        finally:
            context.caller_stack.nextcaller = None
        __M_writer(u'\n  ')
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
        __M_writer(u'\n  <script type="text/javascript">\n    // This is a hack to get tinymce to work correctly in Firefox until the annotator tool is refactored to not include\n    // tinymce globally.\n    if(typeof window.Range.prototype === "undefined") {\n        window.Range.prototype = { };\n    }\n  </script>\n  <script type="text/javascript" src="')
        __M_writer(filters.html_escape(filters.decode.utf8(static.url('js/instructor_dashboard/proctoring.js'))))
        __M_writer(u'"></script>\n  <script type="text/javascript" src="')
        __M_writer(filters.html_escape(filters.decode.utf8(static.url('js/vendor/date.js'))))
        __M_writer(u'"></script>\n  <script type="text/javascript" src="')
        __M_writer(filters.html_escape(filters.decode.utf8(static.url('js/vendor/flot/jquery.flot.js'))))
        __M_writer(u'"></script>\n  <script type="text/javascript" src="')
        __M_writer(filters.html_escape(filters.decode.utf8(static.url('js/vendor/flot/jquery.flot.axislabels.js'))))
        __M_writer(u'"></script>\n  <script type="text/javascript" src="')
        __M_writer(filters.html_escape(filters.decode.utf8(static.url('js/vendor/jquery-jvectormap-1.1.1/jquery-jvectormap-1.1.1.min.js'))))
        __M_writer(u'"></script>\n  <script type="text/javascript" src="')
        __M_writer(filters.html_escape(filters.decode.utf8(static.url('js/vendor/jquery-jvectormap-1.1.1/jquery-jvectormap-world-mill-en.js'))))
        __M_writer(u'"></script>\n  <script type="text/javascript" src="')
        __M_writer(filters.html_escape(filters.decode.utf8(static.url('js/vendor/jquery.event.drag-2.2.js'))))
        __M_writer(u'"></script>\n  <script type="text/javascript" src="')
        __M_writer(filters.html_escape(filters.decode.utf8(static.url('js/vendor/jquery.event.drop-2.2.js'))))
        __M_writer(u'"></script>\n  <script type="text/javascript" src="')
        __M_writer(filters.html_escape(filters.decode.utf8(static.url('js/vendor/slick.core.js'))))
        __M_writer(u'"></script>\n  <script type="text/javascript" src="')
        __M_writer(filters.html_escape(filters.decode.utf8(static.url('js/vendor/slick.grid.js'))))
        __M_writer(u'"></script>\n  <link rel="stylesheet" href="')
        __M_writer(filters.html_escape(filters.decode.utf8(static.url('css/vendor/slickgrid/smoothness/jquery-ui-1.8.16.custom.css'))))
        __M_writer(u'">\n  <link rel="stylesheet" href="')
        __M_writer(filters.html_escape(filters.decode.utf8(static.url('css/vendor/slickgrid/slick.grid.css'))))
        __M_writer(u'">\n  <script type="text/javascript" src="')
        __M_writer(filters.html_escape(filters.decode.utf8(static.url('js/vendor/codemirror-compressed.js'))))
        __M_writer(u'"></script>\n  <script type="text/javascript" src="')
        __M_writer(filters.html_escape(filters.decode.utf8(static.url('js/vendor/tinymce/js/tinymce/tinymce.full.min.js'))))
        __M_writer(u'"></script>\n  <script type="text/javascript" src="')
        __M_writer(filters.html_escape(filters.decode.utf8(static.url('js/vendor/tinymce/js/tinymce/jquery.tinymce.min.js'))))
        __M_writer(u'"></script>\n  <script type="text/javascript" src="')
        __M_writer(filters.html_escape(filters.decode.utf8(static.url('js/vendor/jQuery-File-Upload/js/jquery.fileupload.js'))))
        __M_writer(u'"></script>\n  <script type="text/javascript" src="')
        __M_writer(filters.html_escape(filters.decode.utf8(static.url('js/vendor/jquery.qubit.js'))))
        __M_writer(u'"></script>\n\n  ')
        def ccall(caller):
            def body():
                __M_writer = context.writer()
                return ''
            return [body]
        context.caller_stack.nextcaller = runtime.Namespace('caller', context, callables=ccall(__M_caller))
        try:
            __M_writer(filters.html_escape(filters.decode.utf8(static.js(group=u'module-descriptor-js'))))
        finally:
            context.caller_stack.nextcaller = None
        __M_writer(u'\n  ')
        def ccall(caller):
            def body():
                __M_writer = context.writer()
                return ''
            return [body]
        context.caller_stack.nextcaller = runtime.Namespace('caller', context, callables=ccall(__M_caller))
        try:
            __M_writer(filters.html_escape(filters.decode.utf8(static.js(group=u'instructor_dash'))))
        finally:
            context.caller_stack.nextcaller = None
        __M_writer(u'\n  ')
        def ccall(caller):
            def body():
                __M_writer = context.writer()
                return ''
            return [body]
        context.caller_stack.nextcaller = runtime.Namespace('caller', context, callables=ccall(__M_caller))
        try:
            __M_writer(filters.html_escape(filters.decode.utf8(static.js(group=u'application'))))
        finally:
            context.caller_stack.nextcaller = None
        __M_writer(u'\n\n')
        __M_writer(u'  <script type="text/javascript" src="')
        __M_writer(filters.html_escape(filters.decode.utf8(static.url('js/models/notification.js'))))
        __M_writer(u'"></script>\n  <script type="text/javascript" src="')
        __M_writer(filters.html_escape(filters.decode.utf8(static.url('js/views/notification.js'))))
        __M_writer(u'"></script>\n  <script type="text/javascript" src="')
        __M_writer(filters.html_escape(filters.decode.utf8(static.url('js/views/file_uploader.js'))))
        __M_writer(u'"></script>\n  <script type="text/javascript" src="')
        __M_writer(filters.html_escape(filters.decode.utf8(static.url('js/utils/animation.js'))))
        __M_writer(u'"></script>\n')
        for section_data in sections:
            if 'fragment' in section_data:
                __M_writer(u'      ')
                __M_writer(filters.html_escape(filters.decode.utf8(HTML(section_data['fragment'].head_html()))))
                __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_header_extras(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def header_extras():
            return render_header_extras(context)
        static = _mako_get_namespace(context, 'static')
        __M_writer = context.writer()
        __M_writer(u'\n')
        for template_name in ["cohorts", "discussions", "enrollment-code-lookup-links", "cohort-editor", "cohort-group-header", "cohort-selector", "cohort-form", "notification", "cohort-state", "divided-discussions-inline", "divided-discussions-course-wide", "cohort-discussions-category", "cohort-discussions-subcategory", "certificate-white-list", "certificate-white-list-editor", "certificate-bulk-white-list", "certificate-invalidation", "membership-list-widget"]:
            __M_writer(u'<script type="text/template" id="')
            __M_writer(filters.html_escape(filters.decode.utf8(template_name)))
            __M_writer(u'-tpl">\n  ')
            def ccall(caller):
                def body():
                    __M_writer = context.writer()
                    return ''
                return [body]
            context.caller_stack.nextcaller = runtime.Namespace('caller', context, callables=ccall(__M_caller))
            try:
                __M_writer(filters.html_escape(filters.decode.utf8(static.include(path=u'instructor/instructor_dashboard_2/' + (template_name) + u'.underscore'))))
            finally:
                context.caller_stack.nextcaller = None
            __M_writer(u'\n</script>\n')
        __M_writer(u'\n<script type="text/template" id="file-upload-tpl">\n  ')
        def ccall(caller):
            def body():
                __M_writer = context.writer()
                return ''
            return [body]
        context.caller_stack.nextcaller = runtime.Namespace('caller', context, callables=ccall(__M_caller))
        try:
            __M_writer(filters.html_escape(filters.decode.utf8(static.include(path=u'file-upload.underscore'))))
        finally:
            context.caller_stack.nextcaller = None
        __M_writer(u'\n</script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"16": 5, "29": 3, "35": 1, "54": 1, "55": 2, "56": 3, "57": 4, "58": 9, "63": 10, "64": 24, "69": 25, "74": 71, "79": 79, "84": 92, "85": 95, "86": 95, "87": 105, "88": 105, "89": 107, "90": 108, "91": 108, "92": 108, "93": 108, "94": 108, "95": 110, "96": 115, "97": 116, "98": 117, "99": 117, "103": 117, "104": 119, "105": 119, "109": 119, "110": 120, "111": 121, "112": 121, "113": 121, "114": 121, "115": 121, "116": 121, "117": 121, "118": 121, "119": 124, "120": 128, "121": 129, "122": 130, "123": 130, "127": 130, "128": 131, "129": 131, "130": 131, "131": 131, "132": 131, "133": 131, "134": 132, "135": 132, "136": 132, "137": 132, "138": 133, "139": 133, "140": 136, "144": 141, "149": 141, "152": 143, "158": 10, "164": 10, "170": 4, "174": 4, "181": 25, "187": 25, "193": 73, "200": 73, "201": 74, "202": 75, "203": 76, "204": 76, "205": 76, "211": 27, "219": 27, "227": 28, "230": 28, "238": 29, "241": 29, "249": 30, "252": 30, "260": 31, "263": 31, "264": 39, "265": 39, "266": 40, "267": 40, "268": 41, "269": 41, "270": 42, "271": 42, "272": 43, "273": 43, "274": 44, "275": 44, "276": 45, "277": 45, "278": 46, "279": 46, "280": 47, "281": 47, "282": 48, "283": 48, "284": 49, "285": 49, "286": 50, "287": 50, "288": 51, "289": 51, "290": 52, "291": 52, "292": 53, "293": 53, "294": 54, "295": 54, "296": 55, "297": 55, "305": 57, "308": 57, "316": 58, "319": 58, "327": 59, "330": 59, "331": 62, "332": 62, "333": 62, "334": 63, "335": 63, "336": 64, "337": 64, "338": 65, "339": 65, "340": 66, "341": 67, "342": 68, "343": 68, "344": 68, "350": 82, "357": 82, "358": 83, "359": 84, "360": 84, "361": 84, "369": 85, "372": 85, "373": 88, "381": 90, "384": 90, "390": 384}, "uri": "instructor/instructor_dashboard_2/instructor_dashboard_2.html", "filename": "/home/nttlong/code/edx/apps/edx/edx-platform/xdj-gnol-lms-templates/instructor/instructor_dashboard_2/instructor_dashboard_2.html"}
__M_END_METADATA
"""
