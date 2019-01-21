# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1548073576.399902
_enable_loop = True
_template_filename = u'/home/nttlong/code/edx/apps/edx/edx-platform/common/lib/capa/capa/templates/drag_and_drop_input.html'
_template_uri = 'drag_and_drop_input.html'
_source_encoding = 'utf-8'
_exports = []


from openedx.core.djangolib.markup import HTML 

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        status = context.get('status', UNDEFINED)
        value = context.get('value', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        drag_and_drop_json = context.get('drag_and_drop_json', UNDEFINED)
        msg = context.get('msg', UNDEFINED)
        id = context.get('id', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n<div id="inputtype_')
        __M_writer(filters.decode.utf8(id))
        __M_writer(u'" class="capa_inputtype">\n    <div class="drag_and_drop_problem_div" id="drag_and_drop_div_')
        __M_writer(filters.decode.utf8(id))
        __M_writer(u'"\n     data-plain-id="')
        __M_writer(filters.decode.utf8(id))
        __M_writer(u'">\n    </div>\n\n    <div class="drag_and_drop_problem_json" id="drag_and_drop_json_')
        __M_writer(filters.decode.utf8(id))
        __M_writer(u'"\n        style="display:none;">')
        __M_writer(filters.decode.utf8(drag_and_drop_json))
        __M_writer(u'</div>\n\n    <div class="script_placeholder" data-src="')
        __M_writer(filters.decode.utf8(STATIC_URL))
        __M_writer(u'js/capa/drag_and_drop.js"></div>\n\n')
        if status in ['unsubmitted', 'correct', 'incorrect', 'partially-correct', 'incomplete']:
            __M_writer(u'        <div class="')
            __M_writer(filters.decode.utf8(status.classname))
            __M_writer(u'" id="status_')
            __M_writer(filters.decode.utf8(id))
            __M_writer(u'">\n')
        __M_writer(u'\n\n    <input type="text" name="input_')
        __M_writer(filters.decode.utf8(id))
        __M_writer(u'" id="input_')
        __M_writer(filters.decode.utf8(id))
        __M_writer(u'" aria-describedby="answer_')
        __M_writer(filters.decode.utf8(id))
        __M_writer(u'" value="')
        __M_writer(filters.html_escape(filters.decode.utf8(value)))
        __M_writer(u'"\n    style="display:none;"/>\n\n\n    <p class="indicator-container drag-and-drop--status" aria-describedby="input_')
        __M_writer(filters.decode.utf8(id))
        __M_writer(u'">\n        ')
        runtime._include_file(context, u'status_span.html', _template_uri, status=status, status_id=id)
        __M_writer(u'\n    </p>\n\n    <p id="answer_')
        __M_writer(filters.decode.utf8(id))
        __M_writer(u'" class="answer"></p>\n\n')
        if msg:
            __M_writer(u'        <span class="message" tabindex="-1">')
            __M_writer(filters.decode.utf8(HTML(msg)))
            __M_writer(u'</span>\n')
        __M_writer(u'\n')
        if status in ['unsubmitted', 'correct', 'incorrect', 'partially-correct', 'incomplete']:
            __M_writer(u'        </div>\n')
        __M_writer(u'</div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"16": 1, "18": 0, "29": 1, "30": 2, "31": 2, "32": 3, "33": 3, "34": 4, "35": 4, "36": 7, "37": 7, "38": 8, "39": 8, "40": 10, "41": 10, "42": 12, "43": 13, "44": 13, "45": 13, "46": 13, "47": 13, "48": 15, "49": 17, "50": 17, "51": 17, "52": 17, "53": 17, "54": 17, "55": 17, "56": 17, "57": 21, "58": 21, "59": 22, "60": 22, "61": 25, "62": 25, "63": 27, "64": 28, "65": 28, "66": 28, "67": 30, "68": 31, "69": 32, "70": 34, "76": 70}, "uri": "drag_and_drop_input.html", "filename": "/home/nttlong/code/edx/apps/edx/edx-platform/common/lib/capa/capa/templates/drag_and_drop_input.html"}
__M_END_METADATA
"""
