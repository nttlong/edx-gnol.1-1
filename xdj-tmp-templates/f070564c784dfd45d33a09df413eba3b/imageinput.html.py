# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1548073576.432676
_enable_loop = True
_template_filename = u'/home/nttlong/code/edx/apps/edx/edx-platform/common/lib/capa/capa/templates/imageinput.html'
_template_uri = 'imageinput.html'
_source_encoding = 'utf-8'
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        status = context.get('status', UNDEFINED)
        src = context.get('src', UNDEFINED)
        value = context.get('value', UNDEFINED)
        gx = context.get('gx', UNDEFINED)
        width = context.get('width', UNDEFINED)
        gy = context.get('gy', UNDEFINED)
        height = context.get('height', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        id = context.get('id', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'<div class="imageinput capa_inputtype" id="inputtype_')
        __M_writer(filters.decode.utf8(id))
        __M_writer(u'">\n  <input\n    type="hidden"\n    class="imageinput"\n    src="')
        __M_writer(filters.decode.utf8(src))
        __M_writer(u'"\n    name="input_')
        __M_writer(filters.decode.utf8(id))
        __M_writer(u'"\n    id="input_')
        __M_writer(filters.decode.utf8(id))
        __M_writer(u'"\n    value="')
        __M_writer(filters.decode.utf8(value))
        __M_writer(u'"\n  />\n  <div style="position:relative;">\n    <div\n      id="imageinput_')
        __M_writer(filters.decode.utf8(id))
        __M_writer(u'"\n      style="\n        background-image: url(\'')
        __M_writer(filters.decode.utf8(src))
        __M_writer(u"');\n        width: ")
        __M_writer(filters.decode.utf8(width))
        __M_writer(u'px;\n        height: ')
        __M_writer(filters.decode.utf8(height))
        __M_writer(u'px;\n        position: relative;\n        left: 0;\n        top: 0;"\n    >\n      <img\n        src="')
        __M_writer(filters.decode.utf8(STATIC_URL))
        __M_writer(u'images/green-pointer.png"\n        id="cross_')
        __M_writer(filters.decode.utf8(id))
        __M_writer(u'"\n        style="position: absolute; top: ')
        __M_writer(filters.decode.utf8(gy))
        __M_writer(u'px; left: ')
        __M_writer(filters.decode.utf8(gx))
        __M_writer(u'px;"\n        alt="Selection indicator"\n      />\n    </div>\n    <div\n      data-width="')
        __M_writer(filters.decode.utf8(width))
        __M_writer(u'"\n      data-height="')
        __M_writer(filters.decode.utf8(height))
        __M_writer(u'"\n      id="answer_')
        __M_writer(filters.decode.utf8(id))
        __M_writer(u'"\n      style="\n        position: absolute;\n        left: 0;\n        top: 0;"\n    ></div>\n  </div>\n\n  <script type="text/javascript" charset="utf-8">\n    (new ImageInput(\'')
        __M_writer(filters.decode.utf8(id))
        __M_writer(u"'));\n  </script>\n\n  ")
        runtime._include_file(context, u'status_span.html', _template_uri, status=status, status_id=id)
        __M_writer(u'\n</div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"16": 0, "30": 1, "31": 1, "32": 1, "33": 5, "34": 5, "35": 6, "36": 6, "37": 7, "38": 7, "39": 8, "40": 8, "41": 12, "42": 12, "43": 14, "44": 14, "45": 15, "46": 15, "47": 16, "48": 16, "49": 22, "50": 22, "51": 23, "52": 23, "53": 24, "54": 24, "55": 24, "56": 24, "57": 29, "58": 29, "59": 30, "60": 30, "61": 31, "62": 31, "63": 40, "64": 40, "65": 43, "66": 43, "72": 66}, "uri": "imageinput.html", "filename": "/home/nttlong/code/edx/apps/edx/edx-platform/common/lib/capa/capa/templates/imageinput.html"}
__M_END_METADATA
"""
