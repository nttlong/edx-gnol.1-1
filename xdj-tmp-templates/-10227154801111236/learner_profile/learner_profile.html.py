# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1548075125.035797
_enable_loop = True
_template_filename = u'/home/nttlong/code/edx/apps/edx/edx-platform/xdj-gnol-lms-templates/learner_profile/learner_profile.html'
_template_uri = 'learner_profile/learner_profile.html'
_source_encoding = 'utf-8'
_exports = [u'pagetitle', u'headextra', u'js_extra', u'bodyclass', 'online_help_token']



import json
from django.urls import reverse
from django.utils.translation import ugettext as _
from openedx.core.djangolib.js_utils import dump_js_escaped_json
from openedx.core.djangolib.markup import HTML


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace(u'static', context._clean_inheritance_tokens(), templateuri=u'/static_content.html', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, u'static')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, u'/main.html', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        platform_name = context.get('platform_name', UNDEFINED)
        def bodyclass():
            return render_bodyclass(context._locals(__M_locals))
        achievements_fragment = context.get('achievements_fragment', UNDEFINED)
        own_profile = context.get('own_profile', UNDEFINED)
        def pagetitle():
            return render_pagetitle(context._locals(__M_locals))
        def js_extra():
            return render_js_extra(context._locals(__M_locals))
        static = _mako_get_namespace(context, 'static')
        def headextra():
            return render_headextra(context._locals(__M_locals))
        records_url = context.get('records_url', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n')
        __M_writer(u'\n')
        __M_writer(u'\n')
        __M_writer(u'\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'pagetitle'):
            context['self'].pagetitle(**pageargs)
        

        __M_writer(u'\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'bodyclass'):
            context['self'].bodyclass(**pageargs)
        

        __M_writer(u'\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'headextra'):
            context['self'].headextra(**pageargs)
        

        __M_writer(u'\n\n<div class="message-banner" aria-live="polite"></div>\n<main id="main" aria-label="Content" tabindex="-1">\n    <div class="wrapper-profile">\n        <div class="profile ')
        __M_writer(filters.html_escape(filters.decode.utf8('profile-self' if own_profile else 'profile-other')))
        __M_writer(u'">\n            <div class="wrapper-profile-field-account-privacy">\n')
        if own_profile and records_url:
            __M_writer(u'                    <div class="wrapper-profile-records">\n                        <a href="')
            __M_writer(filters.html_escape(filters.decode.utf8(records_url)))
            __M_writer(u'">\n                            <button class="btn profile-records-button">')
            __M_writer(filters.html_escape(filters.decode.utf8(_("View My Records"))))
            __M_writer(u'</button>\n                        </a>\n                    </div>\n')
        __M_writer(u'            </div>\n')
        if own_profile:
            __M_writer(u'                <div class="profile-header">\n                    <div class="header">')
            __M_writer(filters.html_escape(filters.decode.utf8(_("My Profile"))))
            __M_writer(u'</div>\n                    <div class="subheader">\n                        ')
            __M_writer(filters.html_escape(filters.decode.utf8(_('Build out your profile to personalize your identity on {platform_name}.').format(
                            platform_name=platform_name,
                        ))))
            __M_writer(u'\n                    </div>\n                </div>\n')
        __M_writer(u'            <div class="wrapper-profile-sections account-settings-container">\n                <div class="ui-loading-indicator">\n                    <p><span class="spin"><span class="icon fa fa-refresh" aria-hidden="true"></span></span> <span class="copy">')
        __M_writer(filters.html_escape(filters.decode.utf8(_("Loading"))))
        __M_writer(u'</span></p>\n                </div>\n                <div class="wrapper-profile-section-container-one is-hidden">\n                    <div class="wrapper-profile-section-one">\n                        <div class="profile-image-field">\n                        </div>\n                        <div class="profile-section-one-fields">\n                        </div>\n                    </div>\n                    <div class="ui-loading-error is-hidden">\n                        <span class="fa fa-exclamation-triangle message-error" aria-hidden="true"></span>\n                        <span class="copy">')
        __M_writer(filters.html_escape(filters.decode.utf8(_("An error occurred. Try loading the page again."))))
        __M_writer(u'</span>\n                    </div>\n                </div>\n                <div class="wrapper-profile-section-container-two is-hidden">\n                    <div class="wrapper-profile-bio"></div>\n')
        if achievements_fragment:
            __M_writer(u'                        ')
            __M_writer(filters.html_escape(filters.decode.utf8(HTML(achievements_fragment.body_html()))))
            __M_writer(u'\n')
        __M_writer(u'                </div>\n            </div>\n        </div>\n    </div>\n</main>\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'js_extra'):
            context['self'].js_extra(**pageargs)
        

        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_pagetitle(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def pagetitle():
            return render_pagetitle(context)
        __M_writer = context.writer()
        __M_writer(filters.html_escape(filters.decode.utf8(_("Learner Profile"))))
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
        def js_extra():
            return render_js_extra(context)
        static = _mako_get_namespace(context, 'static')
        __M_writer = context.writer()
        __M_writer(u'\n')
        def ccall(caller):
            def body():
                data = context.get('data', UNDEFINED)
                __M_writer = context.writer()
                __M_writer(u'\n    var options = ')
                __M_writer(dump_js_escaped_json(data ))
                __M_writer(u';\n    LearnerProfileFactory(options);\n')
                return ''
            return [body]
        context.caller_stack.nextcaller = runtime.Namespace('caller', context, callables=ccall(__M_caller))
        try:
            __M_writer(filters.html_escape(filters.decode.utf8(static.require_module(class_name=u'LearnerProfileFactory',module_name=u'learner_profile/js/learner_profile_factory'))))
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
        __M_writer(u'view-profile')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_online_help_token(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        return "profile" 
        
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"132": 20, "193": 5, "140": 21, "143": 21, "16": 8, "149": 74, "156": 74, "31": 6, "161": 75, "162": 76, "163": 76, "37": 3, "168": 75, "171": 78, "177": 18, "55": 2, "56": 3, "57": 4, "58": 5, "59": 6, "60": 14, "189": 5, "65": 16, "70": 18, "200": 193, "75": 22, "76": 27, "77": 27, "78": 29, "79": 30, "80": 31, "81": 31, "82": 32, "83": 32, "84": 36, "85": 37, "86": 38, "87": 39, "88": 39, "89": 41, "92": 43, "93": 47, "94": 49, "95": 49, "96": 60, "97": 60, "98": 65, "99": 66, "100": 66, "101": 66, "102": 68, "107": 79, "113": 16, "183": 18, "119": 16, "125": 20}, "uri": "learner_profile/learner_profile.html", "filename": "/home/nttlong/code/edx/apps/edx/edx-platform/xdj-gnol-lms-templates/learner_profile/learner_profile.html"}
__M_END_METADATA
"""
