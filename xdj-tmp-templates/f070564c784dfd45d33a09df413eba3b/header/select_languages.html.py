# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1548073578.816703
_enable_loop = True
_template_filename = u'/home/nttlong/code/edx/apps/edx/edx-platform/xdj-gnol-lms-templates/header/select_languages.html'
_template_uri = u'/header/select_languages.html'
_source_encoding = 'utf-8'
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        request = context.get('request', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'<style>\n    .flag-icon {\n        background-position-x:50%;\n        background-position-y:50%;\n        background-size:contain;\n        color:rgb(85, 85, 85);\n        cursor:pointer;\n        display:inline-block;\n        font-family:"Open Sans", Verdana, Geneva, sans-serif, sans-serif;\n        font-size:16px;\n        font-stretch:100%;\n        font-style:italic;\n        font-variant-caps:normal;\n        font-variant-east-asian:normal;\n        font-variant-ligatures:normal;\n        font-variant-numeric:normal;\n        font-weight:400;\n        height:32px !important;\n        line-height:16px;\n        list-style-image:none;\n        list-style-position:outside;\n        list-style-type:none;\n        position:relative;\n        text-align:left;\n        text-size-adjust:100%;\n        width:21.3333px;\n        margin: 0 !important;\n        padding: 0 !important;\n        -webkit-tap-highlight-color:rgba(0, 0, 0, 0);\n    }\n    .language span {\n            position: relative;\n            top: -12px;\n    }\n    .flag-icon-en {\n          background-image: url(\'/cms/static/flags/en.svg\');\n          background-repeat: no-repeat;\n          background-position: center center;\n          background-size: contain;\n          /* min-width: 30px;\n          max-width: 30px;\n          width: 30px;\n          height: 30px;\n          border: none !important; */\n     }\n     .flag-icon-vi {\n          background-image: url(\'/cms/static/flags/vn.svg\');\n          background-repeat: no-repeat;\n          background-position: center center;\n          background-size: contain;\n          /* min-width: 30px;\n          max-width: 30px;\n          width: 30px;\n          height: 30px;\n          border: none !important; */\n     }\n     .flag-icon, .flag-icon-background {\n        background-repeat: no-repeat;\n        background-size: contain;\n        background-position: 50%;\n    }\n    .navbar-nav{\n        list-style: none;\n    }\n    .main-header {\n        height: 60px;\n    }\n    #language-settings-form {\n        display:none;\n    }\n    .course-profile {\n        padding-top: 0 !important;\n    }\n    .course-info header.course-profile .intro-inner-wrapper{\n        \n    }\n    .course-info header.course-profile .intro-inner-wrapper .table {\n        max-height: 260px;\n    }\n    .course-info header.course-profile .intro-inner-wrapper .media .hero img {\n        display: block;\n        width: auto !important;\n        max-height: 230px !important;\n    }\n    html, body {\n        font-family: "Open Sans","Helvetica Neue",Helvetica,Arial,sans-serif;\n        font-size: 1rem !important;\n        font-style: normal;\n        line-height: 1em;\n    }\n    .footer-language-selector{\n        display: none;\n    }\n    .wrapper-logo {\n        display: none;\n    }\n    body.view-in-course .wrapper-course-material, body.view-in-course .wrapper-preview-menu {\n        padding: 0;\n        height: 57px;\n    }\n</style>\n<div class="mobile-nav-item hidden-mobile nav-item">\n    <ul class="navbar-nav navbar-right" style="margin-top: 21px;margin-right:8px">\n            <li class="dropdown language">\n                <a href="#"  data-toggle="dropdown"><i class="flag-icon flag-icon-')
        __M_writer(filters.decode.utf8(request.LANGUAGE_CODE))
        __M_writer(u'"></i>\n                    <span > \n                       \n                        <b class="caret"></b>\n                    </span>\n                </a>\n                <ul class="dropdown-menu">\n                    <li><a href="javascript:_do_select_lang(\'en\')"><i class="flag-icon flag-icon-en"></i><span>&nbsp;</span> <span>English</span></a></li>\n                    <li><a href="javascript:_do_select_lang(\'vi\')"><i class="flag-icon flag-icon-vi"></i><span>&nbsp;</span><span>Ti\u1ebfng Vi\u1ec7t</span></a></li>\n                </ul>\n            </li>\n        </ul>\n</div>\n<script>\n  function _do_select_lang(code){\n        $("#settings-language-value").val(code);\n        $("#settings-language-value").change();\n        // $("#url").val(window.location.href);\n        // $("#language").val(code);\n        // $("#form_change_language")[0].submit();\n  }\n</script>')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"16": 0, "24": 105, "30": 24, "22": 1, "23": 105}, "uri": "/header/select_languages.html", "filename": "/home/nttlong/code/edx/apps/edx/edx-platform/xdj-gnol-lms-templates/header/select_languages.html"}
__M_END_METADATA
"""
