# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1548073575.282024
_enable_loop = True
_template_filename = u'/home/nttlong/code/edx/apps/edx/edx-platform/common/lib/capa/capa/templates/choicegroup.html'
_template_uri = 'choicegroup.html'
_source_encoding = 'utf-8'
_exports = []


from openedx.core.djangolib.markup import HTML 

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        status = context.get('status', UNDEFINED)
        basestring = context.get('basestring', UNDEFINED)
        input_type = context.get('input_type', UNDEFINED)
        value = context.get('value', UNDEFINED)
        choices = context.get('choices', UNDEFINED)
        submitted_message = context.get('submitted_message', UNDEFINED)
        msg = context.get('msg', UNDEFINED)
        show_correctness = context.get('show_correctness', UNDEFINED)
        isinstance = context.get('isinstance', UNDEFINED)
        name_array_suffix = context.get('name_array_suffix', UNDEFINED)
        id = context.get('id', UNDEFINED)
        describedby_html = context.get('describedby_html', UNDEFINED)
        response_data = context.get('response_data', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n')
        __M_writer(u'\n')

        def is_radio_input(choice_id):
          return input_type == 'radio' and ((isinstance(value, basestring) and (choice_id == value)) or (
            not isinstance(value, basestring) and choice_id in value
          ))
        
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['is_radio_input'] if __M_key in __M_locals_builtin_stored]))
        __M_writer(u'\n<div class="choicegroup capa_inputtype" id="inputtype_')
        __M_writer(filters.html_escape(filters.decode.utf8(id)))
        __M_writer(u'">\n    <fieldset ')
        __M_writer(filters.html_escape(filters.decode.utf8(describedby_html)))
        __M_writer(u'>\n')
        if response_data['label']:
            __M_writer(u'        <legend id="')
            __M_writer(filters.html_escape(filters.decode.utf8(id)))
            __M_writer(u'-legend" class="response-fieldset-legend field-group-hd">')
            __M_writer(filters.html_escape(filters.decode.utf8(response_data['label'])))
            __M_writer(u'</legend>\n')
        for description_id, description_text in response_data['descriptions'].items():
            __M_writer(u'        <p class="question-description" id="')
            __M_writer(filters.html_escape(filters.decode.utf8(description_id)))
            __M_writer(u'">')
            __M_writer(filters.html_escape(filters.decode.utf8(description_text)))
            __M_writer(u'</p>\n')
        for choice_id, choice_label in choices:
            __M_writer(u'          <div class="field">\n            ')

            label_class = 'response-label field-label label-inline'
                        
            
            __M_locals_builtin_stored = __M_locals_builtin()
            __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['label_class'] if __M_key in __M_locals_builtin_stored]))
            __M_writer(u'\n\n            <label id="')
            __M_writer(filters.html_escape(filters.decode.utf8(id)))
            __M_writer(u'-')
            __M_writer(filters.html_escape(filters.decode.utf8(choice_id)))
            __M_writer(u'-label"\n')
            if is_radio_input(choice_id):
                __M_writer(u'\n')
                if status.classname and not show_correctness == 'never':
                    __M_writer(u'                        ')
                    label_class += ' choicegroup_' + status.classname 
                    
                    __M_locals_builtin_stored = __M_locals_builtin()
                    __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['label_class'] if __M_key in __M_locals_builtin_stored]))
                    __M_writer(u'\n')
            __M_writer(u'                class="')
            __M_writer(filters.html_escape(filters.decode.utf8(label_class)))
            __M_writer(u'"\n                ')
            __M_writer(filters.html_escape(filters.decode.utf8(describedby_html)))
            __M_writer(u'\n                >\n                <input type="')
            __M_writer(filters.html_escape(filters.decode.utf8(input_type)))
            __M_writer(u'" name="input_')
            __M_writer(filters.html_escape(filters.decode.utf8(id)))
            __M_writer(filters.html_escape(filters.decode.utf8(name_array_suffix)))
            __M_writer(u'" id="input_')
            __M_writer(filters.html_escape(filters.decode.utf8(id)))
            __M_writer(u'_')
            __M_writer(filters.html_escape(filters.decode.utf8(choice_id)))
            __M_writer(u'" class="field-input input-')
            __M_writer(filters.html_escape(filters.decode.utf8(input_type)))
            __M_writer(u'" value="')
            __M_writer(filters.html_escape(filters.decode.utf8(choice_id)))
            __M_writer(u'"\n')
            if is_radio_input(choice_id):
                __M_writer(u'                checked="true"\n')
            elif input_type != 'radio' and choice_id in value:
                __M_writer(u'                checked="true"\n')
            __M_writer(u'                /> ')
            __M_writer(filters.html_escape(filters.decode.utf8(HTML(choice_label))))
            __M_writer(u'\n')
            if is_radio_input(choice_id):
                if not show_correctness == 'never' and status.classname != 'unanswered':
                    __M_writer(u'                    ')
                    runtime._include_file(context, u'status_span.html', _template_uri, status=status, status_id=id)
                    __M_writer(u'\n')
            __M_writer(u'            </label>\n          </div>\n')
        __M_writer(u'        <span id="answer_')
        __M_writer(filters.html_escape(filters.decode.utf8(id)))
        __M_writer(u'"></span>\n    </fieldset>\n    <div class="indicator-container">\n')
        if input_type == 'checkbox' or status.classname == 'unanswered':
            if show_correctness != 'never':
                __M_writer(u'            ')
                runtime._include_file(context, u'status_span.html', _template_uri, status=status, status_id=id)
                __M_writer(u'\n')
            else:
                __M_writer(u'            ')
                runtime._include_file(context, u'status_span.html', _template_uri, status=status, status_id=id, hide_correctness=True)
                __M_writer(u'\n')
        __M_writer(u'    </div>\n')
        if show_correctness == "never" and (value or status not in ['unsubmitted']):
            __M_writer(u'    <div class="capa_alert">')
            __M_writer(filters.html_escape(filters.decode.utf8(submitted_message)))
            __M_writer(u'</div>\n')
        if msg:
            __M_writer(u'    <span class="message" aria-describedby="')
            __M_writer(filters.html_escape(filters.decode.utf8(id)))
            __M_writer(u'-legend" tabindex="-1">')
            __M_writer(filters.html_escape(filters.decode.utf8(HTML(msg))))
            __M_writer(u'</span>\n')
        __M_writer(u'</div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"16": 2, "18": 1, "36": 1, "37": 2, "38": 3, "47": 8, "48": 9, "49": 9, "50": 10, "51": 10, "52": 11, "53": 12, "54": 12, "55": 12, "56": 12, "57": 12, "58": 14, "59": 15, "60": 15, "61": 15, "62": 15, "63": 15, "64": 17, "65": 18, "66": 19, "72": 21, "73": 23, "74": 23, "75": 23, "76": 23, "77": 25, "78": 26, "79": 27, "80": 28, "81": 28, "85": 28, "86": 31, "87": 31, "88": 31, "89": 32, "90": 32, "91": 34, "92": 34, "93": 34, "94": 34, "95": 34, "96": 34, "97": 34, "98": 34, "99": 34, "100": 34, "101": 34, "102": 34, "103": 34, "104": 36, "105": 37, "106": 38, "107": 39, "108": 41, "109": 41, "110": 41, "111": 42, "112": 43, "113": 44, "114": 44, "115": 44, "116": 47, "117": 50, "118": 50, "119": 50, "120": 53, "121": 54, "122": 55, "123": 55, "124": 55, "125": 56, "126": 57, "127": 57, "128": 57, "129": 60, "130": 61, "131": 62, "132": 62, "133": 62, "134": 64, "135": 65, "136": 65, "137": 65, "138": 65, "139": 65, "140": 67, "146": 140}, "uri": "choicegroup.html", "filename": "/home/nttlong/code/edx/apps/edx/edx-platform/common/lib/capa/capa/templates/choicegroup.html"}
__M_END_METADATA
"""
