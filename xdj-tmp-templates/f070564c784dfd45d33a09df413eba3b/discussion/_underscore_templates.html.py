# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1548073576.650397
_enable_loop = True
_template_filename = u'/home/nttlong/code/edx/apps/edx/edx-platform/xdj-gnol-lms-templates/discussion/_underscore_templates.html'
_template_uri = u'discussion/_underscore_templates.html'
_source_encoding = 'utf-8'
_exports = []


from openedx.core.djangolib.js_utils import js_escaped_string 

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
        static = _mako_get_namespace(context, 'static')
        settings = context.get('settings', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n')
        __M_writer(u'\n')
        __M_writer(u'\n\n<script type="text/javascript">\n  window.PLATFORM_NAME = "')
        __M_writer(js_escaped_string(settings.PLATFORM_NAME ))
        __M_writer(u'";\n')
        if settings.FEATURES.get('ENABLE_DISCUSSION_HOME_PANEL', False):
            __M_writer(u'    window.ENABLE_DISCUSSION_HOME_PANEL = true;\n')
        else:
            __M_writer(u'    window.ENABLE_DISCUSSION_HOME_PANEL = false;\n')
        __M_writer(u'</script>\n\n')

        template_names = [
            'thread',
            'thread-show',
            'thread-edit',
            'thread-response',
            'thread-response-show',
            'thread-response-edit',
            'response-comment-show',
            'response-comment-edit',
            'thread-list-item',
            'search-alert',
            'new-post',
            'new-post-menu-entry',
            'new-post-menu-category',
            'new-post-alert',
            'new-post-visibility',
            'topic',
            'post-user-display',
            'inline-discussion',
            'pagination',
            'profile-thread',
            'customwmd-prompt',
            'nav-loading',
            'thread-type'
        ]
        
        ## same, but without trailing "-template" in script ID - these templates does not contain any free variables
        template_names_no_suffix = [
          'forum-action-endorse', 'forum-action-answer', 'forum-action-follow', 'forum-action-vote', 'forum-action-report',
          'forum-action-pin', 'forum-action-close', 'forum-action-edit', 'forum-action-delete', 'forum-actions',
          'alert-popup', 'nav-load-more-link'
        ]
        
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['template_names','template_names_no_suffix'] if __M_key in __M_locals_builtin_stored]))
        __M_writer(u'\n\n')
        for template_name in template_names:
            __M_writer(u'<script aria-hidden="true" type="text/template" id="')
            __M_writer(filters.html_escape(filters.decode.utf8(template_name)))
            __M_writer(u'-template">\n    ')
            def ccall(caller):
                def body():
                    __M_writer = context.writer()
                    return ''
                return [body]
            context.caller_stack.nextcaller = runtime.Namespace('caller', context, callables=ccall(__M_caller))
            try:
                __M_writer(filters.html_escape(filters.decode.utf8(static.include(path=u'common/templates/discussion/' + (template_name) + u'.underscore'))))
            finally:
                context.caller_stack.nextcaller = None
            __M_writer(u'\n</script>\n')
        __M_writer(u'\n\n')
        for template_name in template_names_no_suffix:
            __M_writer(u'<script aria-hidden="true" type="text/template" id="')
            __M_writer(filters.html_escape(filters.decode.utf8(template_name)))
            __M_writer(u'">\n    ')
            def ccall(caller):
                def body():
                    __M_writer = context.writer()
                    return ''
                return [body]
            context.caller_stack.nextcaller = runtime.Namespace('caller', context, callables=ccall(__M_caller))
            try:
                __M_writer(filters.html_escape(filters.decode.utf8(static.include(path=u'common/templates/discussion/' + (template_name) + u'.underscore'))))
            finally:
                context.caller_stack.nextcaller = None
            __M_writer(u'\n</script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"16": 3, "25": 2, "28": 1, "35": 1, "36": 2, "37": 3, "38": 6, "39": 6, "40": 7, "41": 8, "42": 9, "43": 10, "44": 12, "45": 14, "82": 47, "83": 49, "84": 50, "85": 50, "86": 50, "94": 51, "97": 51, "98": 54, "99": 56, "100": 57, "101": 57, "102": 57, "110": 58, "113": 58, "119": 113}, "uri": "discussion/_underscore_templates.html", "filename": "/home/nttlong/code/edx/apps/edx/edx-platform/xdj-gnol-lms-templates/discussion/_underscore_templates.html"}
__M_END_METADATA
"""
