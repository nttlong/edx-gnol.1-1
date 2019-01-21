# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1548073579.280674
_enable_loop = True
_template_filename = u'/home/nttlong/code/edx/apps/edx/edx-platform/xdj-gnol-lms-templates/widgets/segment-io-footer.html'
_template_uri = u'/widgets/segment-io-footer.html'
_source_encoding = 'utf-8'
_exports = []


from openedx.core.djangolib.js_utils import js_escaped_string 

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        user = context.get('user', UNDEFINED)
        settings = context.get('settings', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n')
        __M_writer(u'\n\n')
        if settings.LMS_SEGMENT_KEY:
            __M_writer(u'    <!-- begin segment footer -->\n    <script type="text/javascript">\n')
            if user.is_authenticated:
                __M_writer(u'        $(window).load(function() {\n            analytics.identify(\n                "')
                __M_writer(js_escaped_string( user.id ))
                __M_writer(u'",\n                {\n                    email: "')
                __M_writer(js_escaped_string( user.email ))
                __M_writer(u'",\n                    username: "')
                __M_writer(js_escaped_string( user.username ))
                __M_writer(u'"\n                },\n                {\n                    integrations: {\n                        // Disable MailChimp because we don\'t want to update the user\'s email\n                        // and username in MailChimp on every page load. We only need to capture\n                        // this data on registration/activation.\n                        MailChimp: false\n                    }\n                }\n            );\n        });\n')
            __M_writer(u'    </script>\n    <!-- end segment footer -->\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"32": 10, "33": 12, "34": 12, "35": 13, "36": 13, "37": 26, "43": 37, "16": 2, "18": 1, "25": 1, "26": 2, "27": 4, "28": 5, "29": 7, "30": 8, "31": 10}, "uri": "/widgets/segment-io-footer.html", "filename": "/home/nttlong/code/edx/apps/edx/edx-platform/xdj-gnol-lms-templates/widgets/segment-io-footer.html"}
__M_END_METADATA
"""
