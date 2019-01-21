# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1548073575.417889
_enable_loop = True
_template_filename = u'/home/nttlong/code/edx/apps/edx/edx-platform/xdj-gnol-lms-templates/problem.html'
_template_uri = 'problem.html'
_source_encoding = 'utf-8'
_exports = []



from django.utils.translation import ungettext, ugettext as _
from openedx.core.djangolib.markup import HTML


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace(u'static', context._clean_inheritance_tokens(), templateuri=u'static_content.html', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, u'static')] = ns

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        submit_button_submitting = context.get('submit_button_submitting', UNDEFINED)
        save_message = context.get('save_message', UNDEFINED)
        short_id = context.get('short_id', UNDEFINED)
        answer_notification_message = context.get('answer_notification_message', UNDEFINED)
        should_enable_next_hint = context.get('should_enable_next_hint', UNDEFINED)
        id = context.get('id', UNDEFINED)
        reset_button = context.get('reset_button', UNDEFINED)
        has_saved_answers = context.get('has_saved_answers', UNDEFINED)
        demand_hint_possible = context.get('demand_hint_possible', UNDEFINED)
        should_enable_submit_button = context.get('should_enable_submit_button', UNDEFINED)
        submit_button = context.get('submit_button', UNDEFINED)
        attempts_allowed = context.get('attempts_allowed', UNDEFINED)
        save_button = context.get('save_button', UNDEFINED)
        problem = context.get('problem', UNDEFINED)
        attempts_used = context.get('attempts_used', UNDEFINED)
        answer_available = context.get('answer_available', UNDEFINED)
        answer_notification_type = context.get('answer_notification_type', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n<h3 class="hd hd-3 problem-header" id="')
        __M_writer(filters.html_escape(filters.decode.utf8( short_id )))
        __M_writer(u'-problem-title" aria-describedby="')
        __M_writer(filters.html_escape(filters.decode.utf8( id )))
        __M_writer(u'-problem-progress" tabindex="-1">\n  ')
        __M_writer(filters.html_escape(filters.decode.utf8( problem['name'] )))
        __M_writer(u'\n</h3>\n\n<div class="problem-progress" id="')
        __M_writer(filters.html_escape(filters.decode.utf8( id )))
        __M_writer(u'-problem-progress"></div>\n\n<div class="problem">\n  ')
        __M_writer(filters.html_escape(filters.decode.utf8( HTML(problem['html']) )))
        __M_writer(u'\n  <div class="action">\n    <input type="hidden" name="problem_id" value="')
        __M_writer(filters.html_escape(filters.decode.utf8( problem['name'] )))
        __M_writer(u'" />\n')
        if demand_hint_possible:
            __M_writer(u'      <div class="problem-hint">\n        ')
            runtime._include_file(context, u'problem_notifications.html', _template_uri, 
         notification_name='hint',
         notification_type='problem-hint',
         notification_icon='fa-question',
         notification_message='')
            __M_writer(u'\n      </div>\n')
        __M_writer(u'\n    <div class="submit-attempt-container">\n      <button type="button" class="submit btn-brand" data-submitting="')
        __M_writer(filters.html_escape(filters.decode.utf8( submit_button_submitting )))
        __M_writer(u'" data-value="')
        __M_writer(filters.html_escape(filters.decode.utf8( submit_button )))
        __M_writer(u'" data-should-enable-submit-button="')
        __M_writer(filters.html_escape(filters.decode.utf8( should_enable_submit_button )))
        __M_writer(u'" aria-describedby="submission_feedback_')
        __M_writer(filters.html_escape(filters.decode.utf8(short_id)))
        __M_writer(u'" ')
        __M_writer(filters.html_escape(filters.decode.utf8('' if should_enable_submit_button else 'disabled')))
        __M_writer(u'>\n          <span class="submit-label">')
        __M_writer(filters.html_escape(filters.decode.utf8( submit_button )))
        __M_writer(u'</span>\n      </button>\n      <div class="submission-feedback" id="submission_feedback_')
        __M_writer(filters.html_escape(filters.decode.utf8(short_id)))
        __M_writer(u'">\n')
        if attempts_allowed:
            __M_writer(u'          ')
            __M_writer(filters.html_escape(filters.decode.utf8(ungettext("You have used {num_used} of {num_total} attempt", "You have used {num_used} of {num_total} attempts", attempts_allowed).format(num_used=attempts_used, num_total=attempts_allowed))))
            __M_writer(u'\n')
        __M_writer(u'        <span class="sr">')
        __M_writer(filters.html_escape(filters.decode.utf8(_("Some problems have options such as save, reset, hints, or show answer. These options follow the Submit button."))))
        __M_writer(u'</span>\n      </div>\n    </div>\n    <div class="problem-action-buttons-wrapper">\n')
        if demand_hint_possible:
            __M_writer(u'      <span class="problem-action-button-wrapper">\n          <button type="button" class="hint-button problem-action-btn btn-default btn-small" data-value="')
            __M_writer(filters.html_escape(filters.decode.utf8(_('Hint'))))
            __M_writer(u'" ')
            __M_writer(filters.html_escape(filters.decode.utf8('' if should_enable_next_hint else 'disabled')))
            __M_writer(u'><span class="icon fa fa-question" aria-hidden="true"></span>')
            __M_writer(filters.html_escape(filters.decode.utf8(_('Hint'))))
            __M_writer(u'</button>\n      </span>\n')
        if save_button:
            __M_writer(u'      <span class="problem-action-button-wrapper">\n          <button type="button" class="save problem-action-btn btn-default btn-small" data-value="')
            __M_writer(filters.html_escape(filters.decode.utf8(_('Save'))))
            __M_writer(u'">\n              <span class="icon fa fa-floppy-o" aria-hidden="true"></span>\n              <span aria-hidden="true">')
            __M_writer(filters.html_escape(filters.decode.utf8(_('Save'))))
            __M_writer(u'</span>\n              <span class="sr">')
            __M_writer(filters.html_escape(filters.decode.utf8(_("Save your answer"))))
            __M_writer(u'</span>\n          </button>\n      </span>\n')
        if reset_button:
            __M_writer(u'      <span class="problem-action-button-wrapper">\n          <button type="button" class="reset problem-action-btn btn-default btn-small" data-value="')
            __M_writer(filters.html_escape(filters.decode.utf8(_('Reset'))))
            __M_writer(u'"><span class="icon fa fa-refresh" aria-hidden="true"></span><span aria-hidden="true">')
            __M_writer(filters.html_escape(filters.decode.utf8(_('Reset'))))
            __M_writer(u'</span><span class="sr">')
            __M_writer(filters.html_escape(filters.decode.utf8(_("Reset your answer"))))
            __M_writer(u'</span></button>\n      </span>\n')
        if answer_available:
            __M_writer(u'      <span class="problem-action-button-wrapper">\n          <button type="button" class="show problem-action-btn btn-default btn-small" aria-describedby="')
            __M_writer(filters.html_escape(filters.decode.utf8( short_id )))
            __M_writer(u'-problem-title"><span class="icon fa fa-info-circle" aria-hidden="true"></span><span class="show-label">')
            __M_writer(filters.html_escape(filters.decode.utf8(_('Show Answer'))))
            __M_writer(u'</span></button>\n      </span>\n')
        __M_writer(u'    </div>\n  </div>\n    ')
        runtime._include_file(context, u'problem_notifications.html', _template_uri, 
      notification_type='warning',
      notification_icon='fa-exclamation-circle',
      notification_name='gentle-alert',
      notification_message='')
        __M_writer(u'\n')
        if answer_notification_type:
            if 'correct' == answer_notification_type:
                __M_writer(u'            ')
                runtime._include_file(context, u'problem_notifications.html', _template_uri, 
                notification_type='success',
                notification_icon='fa-check',
                notification_name='submit',
                is_hidden=False,
                notification_message=answer_notification_message)
                __M_writer(u'\n')
            if 'incorrect' == answer_notification_type:
                __M_writer(u'            ')
                runtime._include_file(context, u'problem_notifications.html', _template_uri, 
                notification_type='error',
                notification_icon='fa-close',
                notification_name='submit',
                is_hidden=False,
                notification_message=answer_notification_message)
                __M_writer(u'\n')
            if 'partially-correct' == answer_notification_type:
                __M_writer(u'            ')
                runtime._include_file(context, u'problem_notifications.html', _template_uri, 
                notification_type='success',
                notification_icon='fa-asterisk',
                notification_name='submit',
                is_hidden=False,
                notification_message=answer_notification_message)
                __M_writer(u'\n')
            if 'submitted' == answer_notification_type:
                __M_writer(u'            ')
                runtime._include_file(context, u'problem_notifications.html', _template_uri, 
                notification_type='general',
                notification_icon='fa-info-circle',
                notification_name='submit',
                is_hidden=False,
                notification_message=answer_notification_message)
                __M_writer(u'\n')
        __M_writer(u'    ')
        runtime._include_file(context, u'problem_notifications.html', _template_uri, 
      notification_type='warning',
      notification_icon='fa-save',
      notification_name='save',
      notification_message=save_message,
      is_hidden=not has_saved_answers)
        __M_writer(u'\n    ')
        runtime._include_file(context, u'problem_notifications.html', _template_uri, 
      notification_type='general',
      notification_icon='fa-info-circle',
      notification_name='show-answer',
      notification_message=_('Answers are displayed within the problem'),
      is_hidden=True)
        __M_writer(u'\n</div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"16": 2, "28": 7, "31": 1, "53": 1, "54": 5, "55": 7, "56": 8, "57": 8, "58": 8, "59": 8, "60": 9, "61": 9, "62": 12, "63": 12, "64": 15, "65": 15, "66": 17, "67": 17, "68": 18, "69": 19, "70": 20, "75": 25, "76": 28, "77": 30, "78": 30, "79": 30, "80": 30, "81": 30, "82": 30, "83": 30, "84": 30, "85": 30, "86": 30, "87": 31, "88": 31, "89": 33, "90": 33, "91": 34, "92": 35, "93": 35, "94": 35, "95": 37, "96": 37, "97": 37, "98": 41, "99": 42, "100": 43, "101": 43, "102": 43, "103": 43, "104": 43, "105": 43, "106": 46, "107": 47, "108": 48, "109": 48, "110": 50, "111": 50, "112": 51, "113": 51, "114": 55, "115": 56, "116": 57, "117": 57, "118": 57, "119": 57, "120": 57, "121": 57, "122": 60, "123": 61, "124": 62, "125": 62, "126": 62, "127": 62, "128": 65, "129": 67, "134": 72, "135": 73, "136": 74, "137": 75, "138": 75, "144": 81, "145": 83, "146": 84, "147": 84, "153": 90, "154": 92, "155": 93, "156": 93, "162": 99, "163": 101, "164": 102, "165": 102, "171": 108, "172": 111, "173": 111, "179": 117, "180": 118, "186": 124, "192": 186}, "uri": "problem.html", "filename": "/home/nttlong/code/edx/apps/edx/edx-platform/xdj-gnol-lms-templates/problem.html"}
__M_END_METADATA
"""
