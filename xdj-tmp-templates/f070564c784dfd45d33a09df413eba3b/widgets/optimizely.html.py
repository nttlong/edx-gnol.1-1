# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1548073578.047083
_enable_loop = True
_template_filename = u'/home/nttlong/code/edx/apps/edx/edx-platform/xdj-gnol-lms-templates/widgets/optimizely.html'
_template_uri = u'/widgets/optimizely.html'
_source_encoding = 'utf-8'
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        disable_optimizely = context.get('disable_optimizely', UNDEFINED)
        is_from_mobile_app = context.get('is_from_mobile_app', UNDEFINED)
        settings = context.get('settings', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n\n')
        if settings.OPTIMIZELY_PROJECT_ID and not disable_optimizely and not is_from_mobile_app:
            __M_writer(u'<script src=')
            __M_writer(filters.html_escape(filters.decode.utf8( '//cdn.optimizely.com/js/{}.js'.format(settings.OPTIMIZELY_PROJECT_ID) )))
            __M_writer(u'></script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"34": 28, "16": 1, "24": 1, "25": 3, "26": 4, "27": 4, "28": 4}, "uri": "/widgets/optimizely.html", "filename": "/home/nttlong/code/edx/apps/edx/edx-platform/xdj-gnol-lms-templates/widgets/optimizely.html"}
__M_END_METADATA
"""
