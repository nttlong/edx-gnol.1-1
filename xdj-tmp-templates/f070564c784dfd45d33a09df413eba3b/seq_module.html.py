# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1548073577.670238
_enable_loop = True
_template_filename = u'/home/nttlong/code/edx/apps/edx/edx-platform/xdj-gnol-lms-templates/seq_module.html'
_template_uri = 'seq_module.html'
_source_encoding = 'utf-8'
_exports = []


from django.utils.translation import ugettext as _ 

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        prev_url = context.get('prev_url', UNDEFINED)
        banner_text = context.get('banner_text', UNDEFINED)
        items = context.get('items', UNDEFINED)
        disable_navigation = context.get('disable_navigation', UNDEFINED)
        next_url = context.get('next_url', UNDEFINED)
        ajax_url = context.get('ajax_url', UNDEFINED)
        gated_content = context.get('gated_content', UNDEFINED)
        enumerate = context.get('enumerate', UNDEFINED)
        item_id = context.get('item_id', UNDEFINED)
        position = context.get('position', UNDEFINED)
        element_id = context.get('element_id', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n')
        __M_writer(u'\n\n<div id="sequence_')
        __M_writer(filters.html_escape(filters.decode.utf8(element_id)))
        __M_writer(u'" class="sequence" data-id="')
        __M_writer(filters.html_escape(filters.decode.utf8(item_id)))
        __M_writer(u'" data-position="')
        __M_writer(filters.html_escape(filters.decode.utf8(position)))
        __M_writer(u'" data-ajax-url="')
        __M_writer(filters.html_escape(filters.decode.utf8(ajax_url)))
        __M_writer(u'" data-next-url="')
        __M_writer(filters.html_escape(filters.decode.utf8(next_url)))
        __M_writer(u'" data-prev-url="')
        __M_writer(filters.html_escape(filters.decode.utf8(prev_url)))
        __M_writer(u'">\n')
        if banner_text:
            __M_writer(u'    <div class="pattern-library-shim alert alert-information subsection-header" tabindex="-1">\n      <span class="pattern-library-shim icon alert-icon fa fa-info-circle" aria-hidden="true"></span>\n      <span class="sr">')
            __M_writer(filters.html_escape(filters.decode.utf8(_('Important!'))))
            __M_writer(u'&nbsp;</span>\n      <div class="pattern-library-shim alert-message">\n        <p class="pattern-library-shim alert-copy">\n          ')
            __M_writer(filters.html_escape(filters.decode.utf8(banner_text)))
            __M_writer(u'\n        </p>\n      </div>\n    </div>\n')
        __M_writer(u'\n  <div class="sequence-nav">\n    <button class="sequence-nav-button button-previous">\n      <span class="icon fa fa-chevron-prev" aria-hidden="true"></span>\n      <span class="sequence-nav-button-label">')
        __M_writer(filters.html_escape(filters.decode.utf8(_('Previous'))))
        __M_writer(u'</span>\n    </button>\n    <button class="sequence-nav-button button-next">\n      <span class="sequence-nav-button-label">')
        __M_writer(filters.html_escape(filters.decode.utf8(_('Next'))))
        __M_writer(u'</span>\n      <span class="icon fa fa-chevron-next" aria-hidden="true"></span>\n    </button>\n    <nav class="sequence-list-wrapper" aria-label="')
        __M_writer(filters.html_escape(filters.decode.utf8(_('Sequence'))))
        __M_writer(u'">\n      <ol id="sequence-list" role="tablist">\n')
        if gated_content['gated']:
            __M_writer(u'        <li>\n          <button class="active nav-item tab" title="')
            __M_writer(filters.html_escape(filters.decode.utf8(_('Content Locked'))))
            __M_writer(u'" id="tab_0" role="tab" tabindex="-1" aria-selected="true" aria-expanded="true" aria-controls="content_locked" disabled>\n            <span class="icon fa fa-lock" aria-hidden="true"></span>\n          </button>\n        </li>\n')
        else:
            for idx, item in enumerate(items):
                __M_writer(u'        <li role="presentation">\n          <button class="seq_')
                __M_writer(filters.html_escape(filters.decode.utf8(item['type'])))
                __M_writer(u' inactive nav-item tab"\n            role="tab"\n            tabindex="-1"\n            aria-selected="false"\n            aria-expanded="false"\n            aria-controls="seq_content"\n            data-index="')
                __M_writer(filters.html_escape(filters.decode.utf8(idx)))
                __M_writer(u'"\n            data-id="')
                __M_writer(filters.html_escape(filters.decode.utf8(item['id'])))
                __M_writer(u'"\n            data-element="')
                __M_writer(filters.html_escape(filters.decode.utf8(idx+1)))
                __M_writer(u'"\n            data-page-title="')
                __M_writer(filters.html_escape(filters.decode.utf8(item['page_title'])))
                __M_writer(u'"\n            data-path="')
                __M_writer(filters.html_escape(filters.decode.utf8(item['path'])))
                __M_writer(u'"\n            data-graded="')
                __M_writer(filters.html_escape(filters.decode.utf8(item['graded'])))
                __M_writer(u'"\n            id="tab_')
                __M_writer(filters.html_escape(filters.decode.utf8(idx)))
                __M_writer(u'"\n            ')
                __M_writer(filters.html_escape(filters.decode.utf8("disabled=disabled" if disable_navigation else "")))
                __M_writer(u'>\n            <span class="icon fa seq_')
                __M_writer(filters.html_escape(filters.decode.utf8(item['type'])))
                __M_writer(u'" aria-hidden="true"></span>\n')
                if 'complete' in item:
                    __M_writer(u'              <span \n                class="fa fa-check-circle check-circle ')
                    __M_writer(filters.html_escape(filters.decode.utf8("is-hidden" if not item['complete'] else "")))
                    __M_writer(u'" \n                style="color:green"\n                aria-hidden="true"\n              ></span>\n')
                __M_writer(u'            <span class="fa fa-fw fa-bookmark bookmark-icon ')
                __M_writer(filters.html_escape(filters.decode.utf8("is-hidden" if not item['bookmarked'] else "bookmarked")))
                __M_writer(u'" aria-hidden="true"></span>\n            <div class="sequence-tooltip sr"><span class="sr">')
                __M_writer(filters.html_escape(filters.decode.utf8(item['type'])))
                __M_writer(u'&nbsp;</span>')
                __M_writer(filters.html_escape(filters.decode.utf8(item['page_title'])))
                __M_writer(u'<span class="sr bookmark-icon-sr">&nbsp;')
                __M_writer(filters.html_escape(filters.decode.utf8(_("Bookmarked") if item['bookmarked'] else "")))
                __M_writer(u'</span></div>\n          </button>\n        </li>\n')
        __M_writer(u'      </ol>\n    </nav>\n  </div>\n')
        if gated_content['gated']:
            __M_writer(u'    ')
            runtime._include_file(context, u'_gated_content.html', _template_uri, prereq_url=gated_content['prereq_url'], prereq_section_name=gated_content['prereq_section_name'], gated_section_name=gated_content['gated_section_name'])
            __M_writer(u'\n')
        else:
            __M_writer(u'  <div class="sr-is-focusable" tabindex="-1"></div>\n\n')
            for idx, item in enumerate(items):
                __M_writer(u'  <div id="seq_contents_')
                __M_writer(filters.html_escape(filters.decode.utf8(idx)))
                __M_writer(u'"\n    aria-labelledby="tab_')
                __M_writer(filters.html_escape(filters.decode.utf8(idx)))
                __M_writer(u'"\n    aria-hidden="true"\n    class="seq_contents tex2jax_ignore asciimath2jax_ignore">\n    ')
                __M_writer(filters.html_escape(filters.decode.utf8(item['content'])))
                __M_writer(u'\n  </div>\n')
            __M_writer(u'  <div id="seq_content" role="tabpanel"></div>\n')
        __M_writer(u'\n  <nav class="sequence-bottom" aria-label="')
        __M_writer(filters.html_escape(filters.decode.utf8(_('Section'))))
        __M_writer(u'">\n    <button class="sequence-nav-button button-previous">\n      <span class="icon fa fa-chevron-prev" aria-hidden="true"></span>\n      <span>')
        __M_writer(filters.html_escape(filters.decode.utf8(_('Previous'))))
        __M_writer(u'</span>\n    </button>\n    <button class="sequence-nav-button button-next">\n      <span>')
        __M_writer(filters.html_escape(filters.decode.utf8(_('Next'))))
        __M_writer(u'</span>\n      <span class="icon fa fa-chevron-next" aria-hidden="true"></span>\n    </button>\n  </nav>\n</div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"16": 2, "18": 1, "34": 1, "35": 2, "36": 4, "37": 4, "38": 4, "39": 4, "40": 4, "41": 4, "42": 4, "43": 4, "44": 4, "45": 4, "46": 4, "47": 4, "48": 5, "49": 6, "50": 8, "51": 8, "52": 11, "53": 11, "54": 16, "55": 20, "56": 20, "57": 23, "58": 23, "59": 26, "60": 26, "61": 28, "62": 29, "63": 30, "64": 30, "65": 34, "66": 35, "67": 36, "68": 37, "69": 37, "70": 43, "71": 43, "72": 44, "73": 44, "74": 45, "75": 45, "76": 46, "77": 46, "78": 47, "79": 47, "80": 48, "81": 48, "82": 49, "83": 49, "84": 50, "85": 50, "86": 51, "87": 51, "88": 52, "89": 53, "90": 54, "91": 54, "92": 59, "93": 59, "94": 59, "95": 60, "96": 60, "97": 60, "98": 60, "99": 60, "100": 60, "101": 65, "102": 68, "103": 69, "104": 69, "105": 69, "106": 70, "107": 71, "108": 73, "109": 74, "110": 74, "111": 74, "112": 75, "113": 75, "114": 78, "115": 78, "116": 81, "117": 83, "118": 84, "119": 84, "120": 87, "121": 87, "122": 90, "123": 90, "129": 123}, "uri": "seq_module.html", "filename": "/home/nttlong/code/edx/apps/edx/edx-platform/xdj-gnol-lms-templates/seq_module.html"}
__M_END_METADATA
"""
