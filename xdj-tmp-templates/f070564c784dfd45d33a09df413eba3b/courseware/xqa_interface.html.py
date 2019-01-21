# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1548073579.27028
_enable_loop = True
_template_filename = u'/home/nttlong/code/edx/apps/edx/edx-platform/xdj-gnol-lms-templates/courseware/xqa_interface.html'
_template_uri = u'courseware/xqa_interface.html'
_source_encoding = 'utf-8'
_exports = []


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
        course = context.get('course', UNDEFINED)
        xqa_server = context.get('xqa_server', UNDEFINED)
        static = _mako_get_namespace(context, 'static')
        unicode = context.get('unicode', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n\n<script type="text/javascript" src="')
        __M_writer(filters.decode.utf8(static.url('js/vendor/jquery.leanModal.js')))
        __M_writer(u'"></script>\n<script type="text/javascript" src="')
        __M_writer(filters.decode.utf8(static.url('js/staff_debug_actions.js')))
        __M_writer(u'"></script>\n<script type="text/javascript">\n\nfunction setup_debug(element_id, edit_link, staff_context){\n    var staffDebugTrigger = $(\'#\' + element_id + \'_trig\'),\n        xqaLogTrigger = $(\'#\' + element_id + \'_xqa_log\'),\n        historyTrigger = $("#" + element_id + "_history_trig"),\n        debugModalSelector = \'#\' + element_id + \'_debug\',\n        historyModalSelector = \'#\' + element_id + \'_history\',\n        xqaModalSelector = \'#\' + element_id + \'_xqa-modal\',\n        leanOverlaySelector = $(\'#lean_overlay\');\n\n    staffDebugTrigger.leanModal();\n    xqaLogTrigger.leanModal();\n    $(\'#\' + element_id + \'_xqa_form\').submit(function () {sendlog(element_id, edit_link, staff_context);});\n\n    historyTrigger.leanModal();\n\n    $(\'#\' + element_id + \'_history_form\').submit(\n        function () {\n            var username = $("#" + element_id + "_history_student_username").val();\n            var location = $("#" + element_id + "_history_location").val();\n\n            $("#" + element_id + "_history_text").load(\'/courses/\' + "')
        __M_writer(filters.url_escape(filters.decode.utf8(unicode(course.id) )))
        __M_writer(u'" +\n                "/submission_history/" + username + "/" + location);\n            return false;\n        }\n    );\n\n    DialogTabControls.setKeydownListener($(debugModalSelector), leanOverlaySelector);\n    DialogTabControls.setKeydownListener($(historyModalSelector), leanOverlaySelector);\n    DialogTabControls.setKeydownListener($(xqaModalSelector), leanOverlaySelector);\n\n    staffDebugTrigger.on(\'click\', function() {\n        DialogTabControls.initializeTabKeyValues(debugModalSelector);\n        $(debugModalSelector).attr("aria-hidden", "false");\n    });\n\n    historyTrigger.on(\'click\', function() {\n        DialogTabControls.initializeTabKeyValues(historyModalSelector);\n        $(historyModalSelector).attr("aria-hidden", "false");\n    });\n\n    xqaLogTrigger.on(\'click\', function() {\n        DialogTabControls.initializeTabKeyValues(xqaModalSelector);\n        $(xqaModalSelector).attr("aria-hidden", "false");\n    });\n\n    leanOverlaySelector.click(function () {\n        $(xqaModalSelector).attr("aria-hidden", "true");\n        $(historyModalSelector).attr("aria-hidden", "true");\n        $(debugModalSelector).attr("aria-hidden", "true");\n      })\n}\n\nfunction sendlog(element_id, edit_link, staff_context){\n\n    var xqaLog = {\n            authkey: staff_context.xqa_key,\n            location: staff_context.location,\n            category : staff_context.category,\n            \'username\' : staff_context.user.username,\n            \'return\' : \'query\',\n            format : \'html\',\n            email : staff_context.user.email,\n            tag:$(\'#\' + element_id + \'_xqa_tag\').val(),\n            entry: $(\'#\' + element_id + \'_xqa_entry\').val()\n        };\n\n    $.ajax({\n        url: \'')
        __M_writer(filters.decode.utf8(xqa_server))
        __M_writer(u'/log\',\n        type: \'GET\',\n        contentType: \'application/json\',\n        data: JSON.stringify(xqaLog),\n        crossDomain: true,\n        dataType: \'jsonp\',\n        beforeSend: function (xhr) {\n            xhr.setRequestHeader ("Authorization", "Basic eHFhOmFnYXJ3YWw="); },\n        timeout : 1000,\n        success: function(result) {\n                $(\'#\' + element_id + \'_xqa_log_data\').html(result);\n        },\n        error: function() {\n            alert(\'Error: cannot connect to XQA server. Check the value of the XQA_SERVER setting.\');\n            console.log(\'error!\');\n        }\n    });\n    return false;\n};\n\nfunction getlog(element_id, staff_context){\n\n    var xqaQuery = {\n        authkey: staff_context.xqa_key,\n        location: staff_context.location,\n        format: \'html\'\n    };\n\n    $.ajax({\n        url: \'')
        __M_writer(filters.decode.utf8(xqa_server))
        __M_writer(u"/query',\n        type: 'GET',\n        contentType: 'application/json',\n        data: JSON.stringify(xqaQuery),\n        crossDomain: true,\n        dataType: 'jsonp',\n        timeout : 1000,\n        success: function(result) {\n            $('#' + element_id + '_xqa_log_data').html(result);\n        },\n        error: function() {\n            alert('Error: cannot connect to XQA server. Check the value of the XQA_SERVER setting.');\n        }\n    });\n\n\n};\n</script>\n")
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"35": 1, "36": 3, "37": 3, "38": 4, "39": 4, "40": 27, "41": 27, "42": 74, "43": 74, "44": 103, "45": 103, "51": 45, "23": 1, "26": 0}, "uri": "courseware/xqa_interface.html", "filename": "/home/nttlong/code/edx/apps/edx/edx-platform/xdj-gnol-lms-templates/courseware/xqa_interface.html"}
__M_END_METADATA
"""
