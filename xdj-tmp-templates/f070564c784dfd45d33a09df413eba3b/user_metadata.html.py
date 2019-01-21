# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1548073578.040755
_enable_loop = True
_template_filename = u'/home/nttlong/code/edx/apps/edx/edx-platform/xdj-gnol-lms-templates/user_metadata.html'
_template_uri = u'/user_metadata.html'
_source_encoding = 'utf-8'
_exports = []



from openedx.core.djangolib.js_utils import dump_js_escaped_json
from eventtracking import tracker
from opaque_keys.edx.keys import CourseKey


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        basestring = context.get('basestring', UNDEFINED)
        course = context.get('course', UNDEFINED)
        user = context.get('user', UNDEFINED)
        unicode = context.get('unicode', UNDEFINED)
        course_id = context.get('course_id', UNDEFINED)
        isinstance = context.get('isinstance', UNDEFINED)
        hasattr = context.get('hasattr', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n')
        __M_writer(u'\n')

        user_metadata = {
            key: context.get(key)
            for key in (
                'username',
                'user_id',
                'course_id',
                'enrollment_mode',
                'upgrade_link',
                'upgrade_price',
                'pacing_type',
                'has_staff_access',
                'forum_roles'
            )
        }
        
        if user:
            user_metadata['username'] = user.username
            user_metadata['user_id'] = user.id
            if hasattr(user, 'email'):
                user_metadata['email'] = user.email
        
        for datekey in (
                'schedule_start',
                'enrollment_time',
                'course_start',
                'course_end',
                'upgrade_deadline'
        ):
            user_metadata[datekey] = (
                context.get(datekey).isoformat() if context.get(datekey) else None
            )
        
        course_key = context.get('course_key')
        if course and not course_key:
            course_key = course.id
        
        if course_key:
            if isinstance(course_key, CourseKey):
                user_metadata['course_key_fields'] = {
                    'org': course_key.org,
                    'course': course_key.course,
                    'run': course_key.run,
                }
        
                if not course_id:
                    user_metadata['course_id'] = unicode(course_key)
            elif isinstance(course_key, basestring):
                user_metadata['course_id'] = course_key
        
        
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['datekey','user_metadata','key','course_key'] if __M_key in __M_locals_builtin_stored]))
        __M_writer(u'\n<script type="application/json" id="user-metadata">\n    ')
        __M_writer(dump_js_escaped_json(user_metadata ))
        __M_writer(u'\n</script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"34": 1, "35": 6, "36": 7, "98": 92, "16": 2, "22": 1, "90": 57, "91": 59, "92": 59}, "uri": "/user_metadata.html", "filename": "/home/nttlong/code/edx/apps/edx/edx-platform/xdj-gnol-lms-templates/user_metadata.html"}
__M_END_METADATA
"""
