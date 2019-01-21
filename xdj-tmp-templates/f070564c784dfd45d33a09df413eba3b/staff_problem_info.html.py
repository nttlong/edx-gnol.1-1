# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1548073575.55018
_enable_loop = True
_template_filename = u'/home/nttlong/code/edx/apps/edx/edx-platform/xdj-gnol-lms-templates/staff_problem_info.html'
_template_uri = 'staff_problem_info.html'
_source_encoding = 'utf-8'
_exports = []



from django.utils.translation import ugettext as _
from django.template.defaultfilters import escapejs
from six import text_type


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace(u'static', context._clean_inheritance_tokens(), templateuri=u'/x-static-content.html', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, u'static')] = ns

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        category = context.get('category', UNDEFINED)
        block_content = context.get('block_content', UNDEFINED)
        xml_attributes = context.get('xml_attributes', UNDEFINED)
        disable_staff_debug_info = context.get('disable_staff_debug_info', UNDEFINED)
        settings = context.get('settings', UNDEFINED)
        xqa_key = context.get('xqa_key', UNDEFINED)
        tags = context.get('tags', UNDEFINED)
        can_override_problem_score = context.get('can_override_problem_score', UNDEFINED)
        histogram = context.get('histogram', UNDEFINED)
        is_released = context.get('is_released', UNDEFINED)
        render_histogram = context.get('render_histogram', UNDEFINED)
        dict = context.get('dict', UNDEFINED)
        user = context.get('user', UNDEFINED)
        fields = context.get('fields', UNDEFINED)
        max_problem_score = context.get('max_problem_score', UNDEFINED)
        can_reset_attempts = context.get('can_reset_attempts', UNDEFINED)
        element_id = context.get('element_id', UNDEFINED)
        can_rescore_problem = context.get('can_rescore_problem', UNDEFINED)
        edit_link = context.get('edit_link', UNDEFINED)
        location = context.get('location', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n')
        __M_writer(u'\n\n')
        __M_writer(filters.decode.utf8(block_content))
        __M_writer(u'\n')
        if 'detached' not in tags:
            if edit_link:
                __M_writer(u'  <div>\n      <a href="')
                __M_writer(filters.decode.utf8(edit_link))
                __M_writer(u'">Edit</a>\n')
                if xqa_key:
                    __M_writer(u'          / <a href="#')
                    __M_writer(filters.decode.utf8(element_id))
                    __M_writer(u'_xqa-modal" onclick="javascript:getlog(\'')
                    __M_writer(filters.decode.utf8(element_id))
                    __M_writer(u"', {\n          'location': '")
                    __M_writer(filters.html_escape(filters.decode.utf8(location )))
                    __M_writer(u"',\n          'xqa_key': '")
                    __M_writer(filters.html_escape(filters.decode.utf8(xqa_key )))
                    __M_writer(u"',\n          'category': '")
                    __M_writer(filters.html_escape(filters.decode.utf8(category )))
                    __M_writer(u"',\n          'user': '")
                    __M_writer(filters.html_escape(filters.decode.utf8(user )))
                    __M_writer(u'\'\n       })" id="')
                    __M_writer(filters.decode.utf8(element_id))
                    __M_writer(u'_xqa_log">QA</a>\n')
                __M_writer(u'  </div>\n')
            if not disable_staff_debug_info:
                __M_writer(u'<div class="wrap-instructor-info">\n  <a class="instructor-info-action" href="#')
                __M_writer(filters.decode.utf8(element_id))
                __M_writer(u'_debug" id="')
                __M_writer(filters.decode.utf8(element_id))
                __M_writer(u'_trig">')
                __M_writer(filters.decode.utf8(_("Staff Debug Info")))
                __M_writer(u'</a>\n\n')
                if settings.FEATURES.get('ENABLE_STUDENT_HISTORY_VIEW') and \
    location.block_type == 'problem':
                    __M_writer(u'    <a class="instructor-info-action" href="#')
                    __M_writer(filters.decode.utf8(element_id))
                    __M_writer(u'_history" id="')
                    __M_writer(filters.decode.utf8(element_id))
                    __M_writer(u'_history_trig">')
                    __M_writer(filters.decode.utf8(_("Submission history")))
                    __M_writer(u'</a>\n')
                __M_writer(u'</div>\n')
            __M_writer(u'\n<div aria-hidden="true" role="dialog" tabindex="-1" id="')
            __M_writer(filters.decode.utf8(element_id))
            __M_writer(u'_xqa-modal" class="modal xqa-modal">\n  <div class="inner-wrapper">\n    <header>\n      <h2>')
            __M_writer(filters.decode.utf8(_("{platform_name} Content Quality Assessment").format(platform_name=settings.PLATFORM_NAME)))
            __M_writer(u'</h2>\n    </header>\n\n    <form id="')
            __M_writer(filters.decode.utf8(element_id))
            __M_writer(u'_xqa_form" class="xqa_form">\n      <label for="')
            __M_writer(filters.decode.utf8(element_id))
            __M_writer(u'_xqa_entry">')
            __M_writer(filters.decode.utf8(_("Comment")))
            __M_writer(u'</label>\n      <input tabindex="0" id="')
            __M_writer(filters.decode.utf8(element_id))
            __M_writer(u'_xqa_entry" type="text" placeholder="')
            __M_writer(filters.decode.utf8(_('comment')))
            __M_writer(u'">\n      <label for="')
            __M_writer(filters.decode.utf8(element_id))
            __M_writer(u'_xqa_tag">')
            __M_writer(filters.decode.utf8(_("Tag")))
            __M_writer(u'</label>\n      <span style="color:black;vertical-align: -10pt">')
            __M_writer(filters.decode.utf8(_('Optional tag (eg "done" or "broken"):') + '&nbsp; '))
            __M_writer(u'      </span>\n      <input id="')
            __M_writer(filters.decode.utf8(element_id))
            __M_writer(u'_xqa_tag" type="text" placeholder="')
            __M_writer(filters.decode.utf8(_('tag')))
            __M_writer(u'" style="width:80px;display:inline">\n      <div class="submit">\n        <button name="submit" type="submit">')
            __M_writer(filters.decode.utf8(_('Add comment')))
            __M_writer(u'</button>\n      </div>\n      <hr>\n      <div id="')
            __M_writer(filters.decode.utf8(element_id))
            __M_writer(u'_xqa_log_data"></div>\n    </form>\n\n  </div>\n</div>\n\n<div aria-hidden="true" role="dialog" tabindex="-1" class="modal staff-modal" id="')
            __M_writer(filters.decode.utf8(element_id))
            __M_writer(u'_debug" >\n  <div class="inner-wrapper">\n    <header>\n      <h2>')
            __M_writer(filters.decode.utf8(_('Staff Debug:')))
            __M_writer(u' ')
            __M_writer(filters.decode.utf8(dict(fields)['display_name']))
            __M_writer(u'</h2>\n    </header>\n\n    <hr />\n    <div class="staff_actions">\n      <h3>')
            __M_writer(filters.decode.utf8(_('Actions')))
            __M_writer(u'</h3>\n      <div>\n        <label for="sd_fu_')
            __M_writer(filters.html_escape(filters.decode.utf8(location.block_id )))
            __M_writer(u'">')
            __M_writer(filters.decode.utf8(_('Username')))
            __M_writer(u':</label>\n        <input type="text" tabindex="0" id="sd_fu_')
            __M_writer(filters.html_escape(filters.decode.utf8(location.block_id )))
            __M_writer(u'" placeholder="')
            __M_writer(filters.decode.utf8(user.username))
            __M_writer(u'"/>\n      </div>\n')
            if can_override_problem_score:
                __M_writer(u'      <div>\n        <label for="sd_fs_')
                __M_writer(filters.html_escape(filters.decode.utf8(location.block_id )))
                __M_writer(u'">')
                __M_writer(filters.decode.utf8(_('Score (for override only)')))
                __M_writer(u':</label>\n        <input type="text" tabindex="0" id="sd_fs_')
                __M_writer(filters.html_escape(filters.decode.utf8(location.block_id )))
                __M_writer(u'" placeholder="0"/>\n        <label for="sd_fs_')
                __M_writer(filters.html_escape(filters.decode.utf8(location.block_id )))
                __M_writer(u'"> / ')
                __M_writer(filters.decode.utf8(max_problem_score))
                __M_writer(u'</label>\n      </div>\n')
            __M_writer(u'      <div data-location="')
            __M_writer(filters.html_escape(filters.decode.utf8(location )))
            __M_writer(u'" data-location-name="')
            __M_writer(filters.html_escape(filters.decode.utf8(location.block_id )))
            __M_writer(u'">\n        [\n')
            if can_reset_attempts:
                __M_writer(u'        <button type="button" class="btn-link staff-debug-reset">')
                __M_writer(filters.decode.utf8(_('Reset Learner\'s Attempts to Zero')))
                __M_writer(u'</button>\n        |\n')
            __M_writer(u'        <button type="button" class="btn-link staff-debug-sdelete">')
            __M_writer(filters.decode.utf8(_('Delete Learner\'s State')))
            __M_writer(u'</button>\n')
            if can_rescore_problem:
                __M_writer(u'        |\n        <button type="button" class="btn-link staff-debug-rescore">')
                __M_writer(filters.decode.utf8(_('Rescore Learner\'s Submission')))
                __M_writer(u'</button>\n        |\n        <button type="button" class="btn-link staff-debug-rescore-if-higher">')
                __M_writer(filters.decode.utf8(_('Rescore Only If Score Improves')))
                __M_writer(u'</button>\n        |\n')
            if can_override_problem_score:
                __M_writer(u'        <button type="button" class="btn-link staff-debug-override-score">')
                __M_writer(filters.decode.utf8(_('Override Score')))
                __M_writer(u'</button>\n')
            __M_writer(u'        ]\n      </div>\n      <div id="result_')
            __M_writer(filters.html_escape(filters.decode.utf8(location.block_id )))
            __M_writer(u'"></div>\n    </div>\n\n    <div class="staff_info" style="display:block">\n      is_released = ')
            __M_writer(filters.decode.utf8(is_released))
            __M_writer(u'\n      location = ')
            __M_writer(filters.html_escape(filters.decode.utf8(text_type(location) )))
            __M_writer(u'\n\n      <table summary="')
            __M_writer(filters.decode.utf8(_('Module Fields')))
            __M_writer(u'">\n        <tr><th>')
            __M_writer(filters.decode.utf8(_('Module Fields')))
            __M_writer(u'</th></tr>\n')
            for name, field in fields:
                __M_writer(u'        <tr><td style="width:25%">')
                __M_writer(filters.decode.utf8(name))
                __M_writer(u'</td><td><pre style="display:inline-block; margin: 0;">')
                __M_writer(filters.html_escape(filters.decode.utf8(field )))
                __M_writer(u'</pre></td></tr>\n')
            __M_writer(u'      </table>\n      <table>\n        <tr><th>')
            __M_writer(filters.decode.utf8(_('XML attributes')))
            __M_writer(u'</th></tr>\n')
            for name, field in xml_attributes.items():
                __M_writer(u'        <tr><td style="width:25%">')
                __M_writer(filters.decode.utf8(name))
                __M_writer(u'</td><td><pre style="display:inline-block; margin: 0;">')
                __M_writer(filters.html_escape(filters.decode.utf8(field )))
                __M_writer(u'</pre></td></tr>\n')
            __M_writer(u'      </table>\n      category = ')
            __M_writer(filters.html_escape(filters.decode.utf8(category )))
            __M_writer(u'\n    </div>\n')
            if render_histogram:
                __M_writer(u'    <div id="histogram_')
                __M_writer(filters.decode.utf8(element_id))
                __M_writer(u'" class="histogram" data-histogram="')
                __M_writer(filters.decode.utf8(histogram))
                __M_writer(u'"></div>\n')
            __M_writer(u'  </div>\n</div>\n\n<div aria-hidden="true" role="dialog" tabindex="-1" class="modal history-modal" id="')
            __M_writer(filters.decode.utf8(element_id))
            __M_writer(u'_history">\n  <div class="inner-wrapper">\n    <header>\n      <h2>')
            __M_writer(filters.decode.utf8(_("Submission History Viewer")))
            __M_writer(u'</h2>\n    </header>\n    <form id="')
            __M_writer(filters.decode.utf8(element_id))
            __M_writer(u'_history_form">\n      <label for="')
            __M_writer(filters.decode.utf8(element_id))
            __M_writer(u'_history_student_username">')
            __M_writer(filters.decode.utf8(_("User:")))
            __M_writer(u'</label>\n      <input tabindex="0" id="')
            __M_writer(filters.decode.utf8(element_id))
            __M_writer(u'_history_student_username" type="text" placeholder=""/>\n      <input type="hidden" id="')
            __M_writer(filters.decode.utf8(element_id))
            __M_writer(u'_history_location" value="')
            __M_writer(filters.html_escape(filters.decode.utf8(location )))
            __M_writer(u'"/>\n      <div class="submit">\n        <button name="submit" type="submit">')
            __M_writer(filters.decode.utf8(_("View History")))
            __M_writer(u'</button>\n      </div>\n    </form>\n\n    <div id="')
            __M_writer(filters.decode.utf8(element_id))
            __M_writer(u'_history_text" class="staff_info" style="display:block">\n    </div>\n  </div>\n</div>\n\n<div id="')
            __M_writer(filters.decode.utf8(element_id))
            __M_writer(u'_setup"></div>\n\n<script type="text/javascript">\n// assumes courseware.html\'s loaded this method.\n$(function () {\n    setup_debug(\'')
            __M_writer(filters.decode.utf8(element_id))
            __M_writer(u"',\n")
            if edit_link:
                __M_writer(u"        '")
                __M_writer(filters.decode.utf8(edit_link))
                __M_writer(u"',\n")
            else:
                __M_writer(u'        null,\n')
            __M_writer(u"        {\n            'location': '")
            __M_writer(escapejs(filters.decode.utf8(location )))
            __M_writer(u"',\n            'xqa_key': '")
            __M_writer(filters.decode.utf8(xqa_key))
            __M_writer(u"',\n            'category': '")
            __M_writer(filters.decode.utf8(category))
            __M_writer(u"',\n            'user': '")
            __M_writer(filters.decode.utf8(user))
            __M_writer(u"'\n        }\n    );\n});\n</script>\n")
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"16": 2, "29": 1, "32": 0, "57": 1, "58": 6, "59": 9, "60": 9, "61": 10, "62": 11, "63": 12, "64": 13, "65": 13, "66": 14, "67": 15, "68": 15, "69": 15, "70": 15, "71": 15, "72": 16, "73": 16, "74": 17, "75": 17, "76": 18, "77": 18, "78": 19, "79": 19, "80": 20, "81": 20, "82": 22, "83": 24, "84": 25, "85": 26, "86": 26, "87": 26, "88": 26, "89": 26, "90": 26, "91": 28, "93": 30, "94": 30, "95": 30, "96": 30, "97": 30, "98": 30, "99": 30, "100": 32, "101": 34, "102": 35, "103": 35, "104": 38, "105": 38, "106": 41, "107": 41, "108": 42, "109": 42, "110": 42, "111": 42, "112": 43, "113": 43, "114": 43, "115": 43, "116": 44, "117": 44, "118": 44, "119": 44, "120": 45, "121": 45, "122": 46, "123": 46, "124": 46, "125": 46, "126": 48, "127": 48, "128": 51, "129": 51, "130": 57, "131": 57, "132": 60, "133": 60, "134": 60, "135": 60, "136": 65, "137": 65, "138": 67, "139": 67, "140": 67, "141": 67, "142": 68, "143": 68, "144": 68, "145": 68, "146": 70, "147": 71, "148": 72, "149": 72, "150": 72, "151": 72, "152": 73, "153": 73, "154": 74, "155": 74, "156": 74, "157": 74, "158": 77, "159": 77, "160": 77, "161": 77, "162": 77, "163": 79, "164": 80, "165": 80, "166": 80, "167": 83, "168": 83, "169": 83, "170": 84, "171": 85, "172": 86, "173": 86, "174": 88, "175": 88, "176": 91, "177": 92, "178": 92, "179": 92, "180": 94, "181": 96, "182": 96, "183": 100, "184": 100, "185": 101, "186": 101, "187": 103, "188": 103, "189": 104, "190": 104, "191": 105, "192": 106, "193": 106, "194": 106, "195": 106, "196": 106, "197": 108, "198": 110, "199": 110, "200": 111, "201": 112, "202": 112, "203": 112, "204": 112, "205": 112, "206": 114, "207": 115, "208": 115, "209": 117, "210": 118, "211": 118, "212": 118, "213": 118, "214": 118, "215": 120, "216": 123, "217": 123, "218": 126, "219": 126, "220": 128, "221": 128, "222": 129, "223": 129, "224": 129, "225": 129, "226": 130, "227": 130, "228": 131, "229": 131, "230": 131, "231": 131, "232": 133, "233": 133, "234": 137, "235": 137, "236": 142, "237": 142, "238": 147, "239": 147, "240": 148, "241": 149, "242": 149, "243": 149, "244": 150, "245": 151, "246": 153, "247": 154, "248": 154, "249": 155, "250": 155, "251": 156, "252": 156, "253": 157, "254": 157, "260": 254}, "uri": "staff_problem_info.html", "filename": "/home/nttlong/code/edx/apps/edx/edx-platform/xdj-gnol-lms-templates/staff_problem_info.html"}
__M_END_METADATA
"""
