# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1548074573.914651
_enable_loop = True
_template_filename = u'/home/nttlong/code/edx/apps/edx/edx-platform/xdj-gnol-lms-templates/student_account/account_settings.html'
_template_uri = 'student_account/account_settings.html'
_source_encoding = 'utf-8'
_exports = [u'pagetitle', u'headextra', u'js_extra', 'online_help_token']



import json

from django.urls import reverse
from django.conf import settings
from django.utils.translation import ugettext as _

from openedx.core.djangolib.js_utils import dump_js_escaped_json, js_escaped_string
from openedx.core.djangolib.markup import HTML
from webpack_loader.templatetags.webpack_loader import render_bundle


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
        auth = context.get('auth', UNDEFINED)
        def pagetitle():
            return render_pagetitle(context._locals(__M_locals))
        def js_extra():
            return render_js_extra(context._locals(__M_locals))
        static = _mako_get_namespace(context, 'static')
        user = context.get('user', UNDEFINED)
        def headextra():
            return render_headextra(context._locals(__M_locals))
        duplicate_provider = context.get('duplicate_provider', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n')
        __M_writer(u'\n')
        __M_writer(u'\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'pagetitle'):
            context['self'].pagetitle(**pageargs)
        

        __M_writer(u'\n\n')
        if duplicate_provider:
            __M_writer(u'    <section>\n        ')
            runtime._include_file(context, u'/dashboard/_dashboard_third_party_error.html', _template_uri)
            __M_writer(u'\n    </section>\n')
        __M_writer(u'\n<div class="wrapper-account-settings"></div>\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'headextra'):
            context['self'].headextra(**pageargs)
        

        __M_writer(u'\n\n')
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
        __M_writer(filters.html_escape(filters.decode.utf8(_("Account Settings"))))
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
        __M_writer(u'\n    ')
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
        __M_writer(u'\n    <link type="text/css" rel="stylesheet" href="/lms/static/paragon/static/paragon.min.css">\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_js_extra(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def js_extra():
            return render_js_extra(context)
        static = _mako_get_namespace(context, 'static')
        user = context.get('user', UNDEFINED)
        auth = context.get('auth', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n')
        def ccall(caller):
            def body():
                password_reset_support_link = context.get('password_reset_support_link', UNDEFINED)
                extended_profile_fields = context.get('extended_profile_fields', UNDEFINED)
                enterprise_name = context.get('enterprise_name', UNDEFINED)
                user_preferences_api_url = context.get('user_preferences_api_url', UNDEFINED)
                fields = context.get('fields', UNDEFINED)
                enterprise_readonly_account_fields = context.get('enterprise_readonly_account_fields', UNDEFINED)
                sync_learner_profile_data = context.get('sync_learner_profile_data', UNDEFINED)
                edx_support_url = context.get('edx_support_url', UNDEFINED)
                bool = context.get('bool', UNDEFINED)
                user_accounts_api_url = context.get('user_accounts_api_url', UNDEFINED)
                enable_account_deletion = context.get('enable_account_deletion', UNDEFINED)
                order_history = context.get('order_history', UNDEFINED)
                __M_writer = context.writer()
                __M_writer(u'\n    var fieldsData = ')
                __M_writer(dump_js_escaped_json( fields ))
                __M_writer(u',\n        ordersHistoryData = ')
                __M_writer(dump_js_escaped_json( order_history ))
                __M_writer(u',\n        authData = ')
                __M_writer(dump_js_escaped_json( auth ))
                __M_writer(u",\n        platformName = '")
                __M_writer(js_escaped_string( static.get_platform_name() ))
                __M_writer(u"',\n        contactEmail = '")
                __M_writer(js_escaped_string( static.get_contact_email_address() ))
                __M_writer(u"',\n        allowEmailChange = ")
                __M_writer(dump_js_escaped_json( bool(settings.FEATURES['ALLOW_EMAIL_ADDRESS_CHANGE']) ))
                __M_writer(u',\n        socialPlatforms = ')
                __M_writer(dump_js_escaped_json( settings.SOCIAL_PLATFORMS ))
                __M_writer(u',\n\n        syncLearnerProfileData = ')
                __M_writer(dump_js_escaped_json( bool(sync_learner_profile_data) ))
                __M_writer(u",\n        enterpriseName = '")
                __M_writer(js_escaped_string( enterprise_name ))
                __M_writer(u"',\n        enterpriseReadonlyAccountFields = ")
                __M_writer(dump_js_escaped_json( enterprise_readonly_account_fields ))
                __M_writer(u",\n        edxSupportUrl = '")
                __M_writer(js_escaped_string( edx_support_url ))
                __M_writer(u"',\n        extendedProfileFields = ")
                __M_writer(dump_js_escaped_json( extended_profile_fields ))
                __M_writer(u',\n        displayAccountDeletion = ')
                __M_writer(dump_js_escaped_json( enable_account_deletion ))
                __M_writer(u";\n\n    AccountSettingsFactory(\n        fieldsData,\n        ordersHistoryData,\n        authData,\n        '")
                __M_writer(js_escaped_string( password_reset_support_link ))
                __M_writer(u"',\n        '")
                __M_writer(js_escaped_string( user_accounts_api_url ))
                __M_writer(u"',\n        '")
                __M_writer(js_escaped_string( user_preferences_api_url ))
                __M_writer(u"',\n        ")
                __M_writer(dump_js_escaped_json( user.id ))
                __M_writer(u',\n        platformName,\n        contactEmail,\n        allowEmailChange,\n        socialPlatforms,\n\n        syncLearnerProfileData,\n        enterpriseName,\n        enterpriseReadonlyAccountFields,\n        edxSupportUrl,\n        extendedProfileFields,\n        displayAccountDeletion\n    );\n')
                return ''
            return [body]
        context.caller_stack.nextcaller = runtime.Namespace('caller', context, callables=ccall(__M_caller))
        try:
            __M_writer(filters.html_escape(filters.decode.utf8(static.require_module(class_name=u'AccountSettingsFactory',module_name=u'js/student_account/views/account_settings_factory'))))
        finally:
            context.caller_stack.nextcaller = None
        __M_writer(u'\n\n<script type="text/javascript">\n     window.auth = ')
        __M_writer(dump_js_escaped_json( auth ))
        __M_writer(u';\n     window.isActive = ')
        __M_writer(dump_js_escaped_json( user.is_active ))
        __M_writer(u';\n</script>\n')
        def ccall(caller):
            def body():
                __M_writer = context.writer()
                __M_writer(u'\n')
                return ''
            return [body]
        context.caller_stack.nextcaller = runtime.Namespace('caller', context, callables=ccall(__M_caller))
        try:
            __M_writer(filters.html_escape(filters.decode.utf8(static.webpack(entry=u'StudentAccountDeletionInitializer'))))
        finally:
            context.caller_stack.nextcaller = None
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_online_help_token(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        return "learneraccountsettings" 
        
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"131": 33, "193": 74, "16": 3, "147": 34, "148": 35, "149": 35, "150": 36, "151": 36, "152": 37, "153": 37, "154": 38, "155": 38, "156": 39, "157": 39, "158": 40, "159": 40, "160": 41, "161": 41, "162": 43, "35": 17, "164": 44, "165": 44, "166": 45, "167": 45, "168": 46, "41": 1, "170": 47, "171": 47, "172": 48, "173": 48, "174": 54, "175": 54, "176": 55, "177": 55, "178": 56, "179": 56, "180": 57, "181": 57, "56": 1, "57": 13, "58": 15, "59": 16, "60": 17, "189": 70, "190": 73, "191": 73, "192": 74, "65": 19, "66": 21, "67": 22, "68": 23, "69": 23, "70": 26, "202": 76, "75": 31, "205": 77, "80": 78, "163": 43, "86": 19, "215": 16, "197": 76, "92": 19, "186": 34, "222": 215, "98": 28, "105": 28, "113": 29, "211": 16, "116": 29, "169": 46, "122": 33}, "uri": "student_account/account_settings.html", "filename": "/home/nttlong/code/edx/apps/edx/edx-platform/xdj-gnol-lms-templates/student_account/account_settings.html"}
__M_END_METADATA
"""
