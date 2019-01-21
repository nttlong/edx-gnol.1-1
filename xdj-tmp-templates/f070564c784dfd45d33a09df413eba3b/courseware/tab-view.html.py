# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1548073629.201176
_enable_loop = True
_template_filename = u'/home/nttlong/code/edx/apps/edx/edx-platform/xdj-gnol-lms-templates/courseware/tab-view.html'
_template_uri = 'courseware/tab-view.html'
_source_encoding = 'utf-8'
_exports = [u'content', u'head_extra', u'bodyclass', u'footer_extra', 'online_help_token', u'pagetitle']


main_css = "css/bootstrap/lms-main.css" 


from django.utils.translation import ugettext as _
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
        def content():
            return render_content(context._locals(__M_locals))
        def head_extra():
            return render_head_extra(context._locals(__M_locals))
        def bodyclass():
            return render_bodyclass(context._locals(__M_locals))
        fragment = context.get('fragment', UNDEFINED)
        def footer_extra():
            return render_footer_extra(context._locals(__M_locals))
        def pagetitle():
            return render_pagetitle(context._locals(__M_locals))
        course = context.get('course', UNDEFINED)
        tab = context.get('tab', UNDEFINED)
        active_page = context.get('active_page', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n')
        __M_writer(u'\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'bodyclass'):
            context['self'].bodyclass(**pageargs)
        

        __M_writer(u'\n\n')
        __M_writer(u'\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'pagetitle'):
            context['self'].pagetitle(**pageargs)
        

        __M_writer(u'\n\n')
        runtime._include_file(context, u'/courseware/course_navigation.html', _template_uri, active_page=active_page)
        __M_writer(u'\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'head_extra'):
            context['self'].head_extra(**pageargs)
        

        __M_writer(u'\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'footer_extra'):
            context['self'].footer_extra(**pageargs)
        

        __M_writer(u'\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        fragment = context.get('fragment', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n    ')
        __M_writer(filters.html_escape(filters.decode.utf8(HTML(fragment.body_html()))))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_head_extra(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        fragment = context.get('fragment', UNDEFINED)
        def head_extra():
            return render_head_extra(context)
        __M_writer = context.writer()
        __M_writer(u'\n')
        __M_writer(filters.html_escape(filters.decode.utf8(HTML(fragment.head_html()))))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_bodyclass(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def bodyclass():
            return render_bodyclass(context)
        tab = context.get('tab', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(filters.html_escape(filters.decode.utf8(tab['body_class'])))
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_footer_extra(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        fragment = context.get('fragment', UNDEFINED)
        def footer_extra():
            return render_footer_extra(context)
        __M_writer = context.writer()
        __M_writer(u'\n')
        runtime._include_file(context, u'/mathjax_include.html', _template_uri, disable_fast_preview=True)
        __M_writer(u'\n')
        __M_writer(filters.html_escape(filters.decode.utf8(HTML(fragment.foot_html()))))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_online_help_token(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        return "${tab['online_help_token']}" 
        
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_pagetitle(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def pagetitle():
            return render_pagetitle(context)
        course = context.get('course', UNDEFINED)
        tab = context.get('tab', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(filters.html_escape(filters.decode.utf8(_(tab['name']))))
        __M_writer(u' | ')
        __M_writer(filters.html_escape(filters.decode.utf8(course.display_number_with_default)))
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"131": 16, "137": 28, "16": 6, "145": 29, "18": 8, "147": 30, "148": 30, "154": 18, "30": 14, "36": 3, "165": 20, "146": 29, "173": 20, "174": 20, "175": 20, "158": 18, "55": 2, "56": 3, "57": 6, "58": 11, "59": 13, "60": 14, "181": 175, "65": 16, "66": 18, "71": 20, "72": 22, "73": 22, "78": 26, "83": 31, "88": 35, "94": 33, "144": 28, "101": 33, "102": 34, "103": 34, "109": 24, "116": 24, "117": 25, "118": 25, "124": 16}, "uri": "courseware/tab-view.html", "filename": "/home/nttlong/code/edx/apps/edx/edx-platform/xdj-gnol-lms-templates/courseware/tab-view.html"}
__M_END_METADATA
"""
