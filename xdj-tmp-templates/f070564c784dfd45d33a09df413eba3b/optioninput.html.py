# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1548073575.600188
_enable_loop = True
_template_filename = u'/home/nttlong/code/edx/apps/edx/edx-platform/common/lib/capa/capa/templates/optioninput.html'
_template_uri = 'optioninput.html'
_source_encoding = 'utf-8'
_exports = []


from openedx.core.djangolib.markup import HTML 

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        status = context.get('status', UNDEFINED)
        default_option_text = context.get('default_option_text', UNDEFINED)
        value = context.get('value', UNDEFINED)
        id = context.get('id', UNDEFINED)
        answervariable = context.get('answervariable', UNDEFINED)
        response_data = context.get('response_data', UNDEFINED)
        msg = context.get('msg', UNDEFINED)
        inline = context.get('inline', UNDEFINED)
        options = context.get('options', UNDEFINED)
        describedby_html = context.get('describedby_html', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n')
        __M_writer(u'\n')
        doinline = "inline" if inline else "" 
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['doinline'] if __M_key in __M_locals_builtin_stored]))
        __M_writer(u'\n\n<div class="inputtype option-input ')
        __M_writer(filters.html_escape(filters.decode.utf8(doinline)))
        __M_writer(u'">\n')
        if response_data['label']:
            __M_writer(u'      <label class="problem-group-label" for="input_')
            __M_writer(filters.html_escape(filters.decode.utf8(id)))
            __M_writer(u'" id="label_')
            __M_writer(filters.html_escape(filters.decode.utf8(id)))
            __M_writer(u'">')
            __M_writer(filters.html_escape(filters.decode.utf8(response_data['label'])))
            __M_writer(u'</label>\n')
        __M_writer(u'\n')
        for description_id, description_text in response_data['descriptions'].items():
            __M_writer(u'    <p class="question-description" id="')
            __M_writer(filters.html_escape(filters.decode.utf8(description_id)))
            __M_writer(u'">')
            __M_writer(filters.html_escape(filters.decode.utf8(description_text)))
            __M_writer(u'</p>\n')
        __M_writer(u'\n   <select name="input_')
        __M_writer(filters.html_escape(filters.decode.utf8(id)))
        __M_writer(u'" id="input_')
        __M_writer(filters.html_escape(filters.decode.utf8(id)))
        __M_writer(u'" ')
        __M_writer(filters.html_escape(filters.decode.utf8(describedby_html)))
        __M_writer(u'>\n      <option value="option_')
        __M_writer(filters.html_escape(filters.decode.utf8(id)))
        __M_writer(u'_dummy_default">')
        __M_writer(filters.html_escape(filters.decode.utf8(default_option_text)))
        __M_writer(u'</option>\n')
        for option_id, option_description in options:
            __M_writer(u'          <option value="')
            __M_writer(filters.html_escape(filters.decode.utf8(option_id)))
            __M_writer(u'"\n')
            if (option_id == value or option_id == answervariable):
                __M_writer(u'        \tselected="true"\n')
            __M_writer(u'          > ')
            __M_writer(filters.html_escape(filters.decode.utf8(option_description)))
            __M_writer(u'</option>\n')
        __M_writer(u'    </select>\n\n  <div class="indicator-container">\n    ')
        runtime._include_file(context, u'status_span.html', _template_uri, status=status, status_id=id)
        __M_writer(u'\n  </div>\n  <p class="answer" id="answer_')
        __M_writer(filters.html_escape(filters.decode.utf8(id)))
        __M_writer(u'"></p>\n')
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
{"source_encoding": "utf-8", "line_map": {"16": 2, "18": 1, "33": 1, "34": 2, "35": 3, "39": 3, "40": 5, "41": 5, "42": 6, "43": 7, "44": 7, "45": 7, "46": 7, "47": 7, "48": 7, "49": 7, "50": 9, "51": 10, "52": 11, "53": 11, "54": 11, "55": 11, "56": 11, "57": 13, "58": 14, "59": 14, "60": 14, "61": 14, "62": 14, "63": 14, "64": 15, "65": 15, "66": 15, "67": 15, "68": 16, "69": 17, "70": 17, "71": 17, "72": 18, "73": 19, "74": 21, "75": 21, "76": 21, "77": 23, "78": 26, "79": 26, "80": 28, "81": 28, "82": 29, "83": 30, "84": 30, "85": 30, "86": 30, "87": 30, "88": 32, "94": 88}, "uri": "optioninput.html", "filename": "/home/nttlong/code/edx/apps/edx/edx-platform/common/lib/capa/capa/templates/optioninput.html"}
__M_END_METADATA
"""
