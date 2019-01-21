# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1548073576.151355
_enable_loop = True
_template_filename = u'/home/nttlong/code/edx/apps/edx/edx-platform/common/lib/capa/capa/templates/schematicinput.html'
_template_uri = 'schematicinput.html'
_source_encoding = 'utf-8'
_exports = []


from capa.util import remove_markup 

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        status = context.get('status', UNDEFINED)
        initial_value = context.get('initial_value', UNDEFINED)
        setup_script = context.get('setup_script', UNDEFINED)
        value = context.get('value', UNDEFINED)
        height = context.get('height', UNDEFINED)
        width = context.get('width', UNDEFINED)
        submit_analyses = context.get('submit_analyses', UNDEFINED)
        parts = context.get('parts', UNDEFINED)
        response_data = context.get('response_data', UNDEFINED)
        analyses = context.get('analyses', UNDEFINED)
        id = context.get('id', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n<div>\n  <div class="script_placeholder" data-src="')
        __M_writer(filters.decode.utf8(setup_script))
        __M_writer(u'"/>\n  <input type="hidden"\n    class="schematic"\n    height="')
        __M_writer(filters.decode.utf8(height))
        __M_writer(u'"\n    width="')
        __M_writer(filters.decode.utf8(width))
        __M_writer(u'"\n    parts="')
        __M_writer(filters.decode.utf8(parts))
        __M_writer(u'"\n    analyses="')
        __M_writer(filters.decode.utf8(analyses))
        __M_writer(u'"\n    name="input_')
        __M_writer(filters.decode.utf8(id))
        __M_writer(u'"\n    id="input_')
        __M_writer(filters.decode.utf8(id))
        __M_writer(u'"\n    aria-label="')
        __M_writer(filters.decode.utf8(remove_markup(response_data['label'])))
        __M_writer(u'"\n    aria-describedby="answer_')
        __M_writer(filters.decode.utf8(id))
        __M_writer(u'"\n    value="')
        __M_writer(filters.html_escape(filters.decode.utf8(value)))
        __M_writer(u'"\n    initial_value="')
        __M_writer(filters.html_escape(filters.decode.utf8(initial_value)))
        __M_writer(u'"\n    submit_analyses="')
        __M_writer(filters.html_escape(filters.decode.utf8(submit_analyses)))
        __M_writer(u'"\n    />\n\n  <span id="answer_')
        __M_writer(filters.decode.utf8(id))
        __M_writer(u'"></span>\n  <div class="indicator-container">\n    ')
        runtime._include_file(context, u'status_span.html', _template_uri, status=status, status_id=id)
        __M_writer(u'\n\n  </div>\n</div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"16": 1, "18": 0, "34": 1, "35": 3, "36": 3, "37": 6, "38": 6, "39": 7, "40": 7, "41": 8, "42": 8, "43": 9, "44": 9, "45": 10, "46": 10, "47": 11, "48": 11, "49": 12, "50": 12, "51": 13, "52": 13, "53": 14, "54": 14, "55": 15, "56": 15, "57": 16, "58": 16, "59": 19, "60": 19, "61": 21, "62": 21, "68": 62}, "uri": "schematicinput.html", "filename": "/home/nttlong/code/edx/apps/edx/edx-platform/common/lib/capa/capa/templates/schematicinput.html"}
__M_END_METADATA
"""
