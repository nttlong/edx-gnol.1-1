# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1548073576.060419
_enable_loop = True
_template_filename = u'/home/nttlong/code/edx/apps/edx/edx-platform/xdj-gnol-lms-templates/edit_unit_link.html'
_template_uri = 'edit_unit_link.html'
_source_encoding = 'utf-8'
_exports = []


from django.utils.translation import ugettext as _ 

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        frag_content = context.get('frag_content', UNDEFINED)
        edit_link = context.get('edit_link', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n\n<div class="wrap-instructor-info studio-view">\n  <a class="instructor-info-action" href="')
        __M_writer(filters.decode.utf8(edit_link))
        __M_writer(u'">')
        __M_writer(filters.decode.utf8(_("View Unit in Studio")))
        __M_writer(u'</a>\n</div>\n')
        __M_writer(filters.decode.utf8(frag_content))
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"36": 30, "16": 1, "18": 0, "25": 1, "26": 4, "27": 4, "28": 4, "29": 4, "30": 6}, "uri": "edit_unit_link.html", "filename": "/home/nttlong/code/edx/apps/edx/edx-platform/xdj-gnol-lms-templates/edit_unit_link.html"}
__M_END_METADATA
"""
