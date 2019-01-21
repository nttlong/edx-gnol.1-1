# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1548073576.465848
_enable_loop = True
_template_filename = u'/home/nttlong/code/edx/apps/edx/edx-platform/common/lib/capa/capa/templates/formulaequationinput.html'
_template_uri = 'formulaequationinput.html'
_source_encoding = 'utf-8'
_exports = []


from openedx.core.djangolib.markup import HTML 

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        status = context.get('status', UNDEFINED)
        previewer = context.get('previewer', UNDEFINED)
        value = context.get('value', UNDEFINED)
        trailing_text = context.get('trailing_text', UNDEFINED)
        response_data = context.get('response_data', UNDEFINED)
        msg = context.get('msg', UNDEFINED)
        inline = context.get('inline', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        id = context.get('id', UNDEFINED)
        describedby_html = context.get('describedby_html', UNDEFINED)
        size = context.get('size', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n')
        __M_writer(u'\n')
        doinline = 'style="display:inline-block;vertical-align:top"' if inline else "" 
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['doinline'] if __M_key in __M_locals_builtin_stored]))
        __M_writer(u'\n<div id="formulaequationinput_')
        __M_writer(filters.html_escape(filters.decode.utf8(id)))
        __M_writer(u'" class="inputtype formulaequationinput" ')
        __M_writer(filters.decode.utf8(doinline ))
        __M_writer(u'>\n    <div class="')
        __M_writer(filters.html_escape(filters.decode.utf8(status.classname)))
        __M_writer(u'">\n')
        if response_data['label']:
            __M_writer(u'          <label class="problem-group-label" for="input_')
            __M_writer(filters.html_escape(filters.decode.utf8(id)))
            __M_writer(u'" id="label_')
            __M_writer(filters.html_escape(filters.decode.utf8(id)))
            __M_writer(u'">')
            __M_writer(filters.html_escape(filters.decode.utf8(response_data['label'])))
            __M_writer(u'</label>\n')
        for description_id, description_text in response_data['descriptions'].items():
            __M_writer(u'            <p class="question-description" id="')
            __M_writer(filters.html_escape(filters.decode.utf8(description_id)))
            __M_writer(u'">')
            __M_writer(filters.html_escape(filters.decode.utf8(description_text)))
            __M_writer(u'</p>\n')
        __M_writer(u'        <input type="text" name="input_')
        __M_writer(filters.html_escape(filters.decode.utf8(id)))
        __M_writer(u'" id="input_')
        __M_writer(filters.html_escape(filters.decode.utf8(id)))
        __M_writer(u'"\n            data-input-id="')
        __M_writer(filters.html_escape(filters.decode.utf8(id)))
        __M_writer(u'" value="')
        __M_writer(filters.html_escape(filters.decode.utf8(value)))
        __M_writer(u'"\n            ')
        __M_writer(filters.html_escape(filters.decode.utf8(describedby_html)))
        __M_writer(u'\n')
        if size:
            __M_writer(u'            size="')
            __M_writer(filters.html_escape(filters.decode.utf8(size)))
            __M_writer(u'"\n')
        __M_writer(u'            />\n        <span class="trailing_text" id="trailing_text_')
        __M_writer(filters.html_escape(filters.decode.utf8(id)))
        __M_writer(u'">')
        __M_writer(filters.html_escape(filters.decode.utf8(trailing_text)))
        __M_writer(u'</span>\n\n        ')
        runtime._include_file(context, u'status_span.html', _template_uri, status=status, status_id=id)
        __M_writer(u'\n\n        <p id="answer_')
        __M_writer(filters.html_escape(filters.decode.utf8(id)))
        __M_writer(u'" class="answer"></p>\n\n        <div id="input_')
        __M_writer(filters.html_escape(filters.decode.utf8(id)))
        __M_writer(u'_preview" class="equation">\n            \\(\\)\n            <img src="')
        __M_writer(filters.html_escape(filters.decode.utf8(STATIC_URL)))
        __M_writer(u'images/spinner.gif" class="loading" alt="Loading"/>\n        </div>\n    </div>\n\n    <div class="script_placeholder" data-src="')
        __M_writer(filters.html_escape(filters.decode.utf8(previewer)))
        __M_writer(u'"/>\n\n')
        if msg:
            __M_writer(u'      <span class="message" aria-describedby="label_')
            __M_writer(filters.html_escape(filters.decode.utf8(id)))
            __M_writer(u'" tabindex="-1">')
            __M_writer(filters.html_escape(filters.decode.utf8(HTML(msg))))
            __M_writer(u'</span>\n')
        __M_writer(u'</div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"16": 2, "18": 1, "34": 1, "35": 2, "36": 3, "40": 3, "41": 4, "42": 4, "43": 4, "44": 4, "45": 5, "46": 5, "47": 6, "48": 7, "49": 7, "50": 7, "51": 7, "52": 7, "53": 7, "54": 7, "55": 9, "56": 10, "57": 10, "58": 10, "59": 10, "60": 10, "61": 12, "62": 12, "63": 12, "64": 12, "65": 12, "66": 13, "67": 13, "68": 13, "69": 13, "70": 14, "71": 14, "72": 15, "73": 16, "74": 16, "75": 16, "76": 18, "77": 19, "78": 19, "79": 19, "80": 19, "81": 21, "82": 21, "83": 23, "84": 23, "85": 25, "86": 25, "87": 27, "88": 27, "89": 31, "90": 31, "91": 33, "92": 34, "93": 34, "94": 34, "95": 34, "96": 34, "97": 36, "103": 97}, "uri": "formulaequationinput.html", "filename": "/home/nttlong/code/edx/apps/edx/edx-platform/common/lib/capa/capa/templates/formulaequationinput.html"}
__M_END_METADATA
"""
