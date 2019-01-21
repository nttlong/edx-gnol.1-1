# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1548073628.49013
_enable_loop = True
_template_filename = u'/home/nttlong/code/edx/apps/edx/edx-platform/common/lib/capa/capa/templates/course_experience/course-outline-fragment.html'
_template_uri = 'course_experience/course-outline-fragment.html'
_source_encoding = 'utf-8'
_exports = []



from datetime import date

from django.utils.translation import ugettext as _

from openedx.core.djangolib.markup import HTML, Text


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace(u'static', context._clean_inheritance_tokens(), templateuri=u'../static_content.html', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, u'static')] = ns

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        user_timezone = context.get('user_timezone', UNDEFINED)
        blocks = context.get('blocks', UNDEFINED)
        self = context.get('self', UNDEFINED)
        xblock_display_names = context.get('xblock_display_names', UNDEFINED)
        static = _mako_get_namespace(context, 'static')
        user_language = context.get('user_language', UNDEFINED)
        gated_content = context.get('gated_content', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n')

        import xdj
        xdj.apply_context(self)
        
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['xdj'] if __M_key in __M_locals_builtin_stored]))
        __M_writer(u'\n')

        course_sections = blocks.get('children')
        
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['course_sections'] if __M_key in __M_locals_builtin_stored]))
        __M_writer(u'\n<main role="main" class="course-outline" id="main" tabindex="-1">\n')
        if course_sections is not None:
            __M_writer(u'        <button class="btn btn-primary"\n                id="expand-collapse-outline-all-button"\n                aria-expanded="false"\n                aria-controls="course-outline-block-tree"\n                >\n          <span class="expand-collapse-outline-all-extra-padding" id="expand-collapse-outline-all-span">')
            __M_writer(filters.html_escape(filters.decode.utf8(self.res("Expand All"))))
            __M_writer(u'</span>\n          <!-- ')
            __M_writer(filters.html_escape(filters.decode.utf8(_("Expand All"))))
            __M_writer(u' -->\n        </button>\n        <ol class="block-tree accordion"\n            id="course-outline-block-tree"\n            aria-labelledby="expand-collapse-outline-all-button">\n')
            for section in course_sections:
                __M_writer(u'            ')

                section_is_auto_opened = section.get('resume_block') is True
                
                
                __M_locals_builtin_stored = __M_locals_builtin()
                __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['section_is_auto_opened'] if __M_key in __M_locals_builtin_stored]))
                __M_writer(u'\n                <li class="outline-item section">\n                    <button class="section-name accordion-trigger"\n                            aria-expanded="')
                __M_writer(filters.html_escape(filters.decode.utf8( 'true' if section_is_auto_opened else 'false' )))
                __M_writer(u'"\n                            aria-controls="')
                __M_writer(filters.html_escape(filters.decode.utf8( section['id'] )))
                __M_writer(u'_contents"\n                            id="')
                __M_writer(filters.html_escape(filters.decode.utf8( section['id'] )))
                __M_writer(u'">\n                        <span class="fa fa-chevron-right ')
                __M_writer(filters.html_escape(filters.decode.utf8( 'fa-rotate-90' if section_is_auto_opened else '' )))
                __M_writer(u'" aria-hidden="true"></span>\n                        <h3 class="section-title">')
                __M_writer(filters.html_escape(filters.decode.utf8( section['display_name'] )))
                __M_writer(u'</h3>\n')
                if section.get('complete'):
                    __M_writer(u'                            <span class="complete-checkmark fa fa-check"></span>\n')
                __M_writer(u'                    </button>\n                    <ol class="outline-item accordion-panel ')
                __M_writer(filters.html_escape(filters.decode.utf8( '' if section_is_auto_opened else 'is-hidden' )))
                __M_writer(u'"\n                        id="')
                __M_writer(filters.html_escape(filters.decode.utf8( section['id'] )))
                __M_writer(u'_contents"\n                        aria-labelledby="')
                __M_writer(filters.html_escape(filters.decode.utf8( section['id'] )))
                __M_writer(u'">\n')
                for subsection in section.get('children', []):
                    __M_writer(u'                ')

                    gated_subsection = subsection['id'] in gated_content
                    completed_prereqs = gated_content[subsection['id']]['completed_prereqs'] if gated_subsection else False
                    subsection_is_auto_opened = subsection.get('resume_block') is True
                    
                    
                    __M_locals_builtin_stored = __M_locals_builtin()
                    __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['completed_prereqs','gated_subsection','subsection_is_auto_opened'] if __M_key in __M_locals_builtin_stored]))
                    __M_writer(u'\n                      <li class="subsection accordion ')
                    __M_writer(filters.html_escape(filters.decode.utf8( 'current' if subsection['resume_block'] else '' )))
                    __M_writer(u'">\n')
                    if gated_subsection and not completed_prereqs:
                        __M_writer(u'                                <a href="')
                        __M_writer(filters.html_escape(filters.decode.utf8( subsection['lms_web_url'] )))
                        __M_writer(u'">\n                                    <button class="subsection-text prerequisite-button"\n                                            id="')
                        __M_writer(filters.html_escape(filters.decode.utf8( subsection['id'] )))
                        __M_writer(u'">\n                                    <span class="menu-icon icon fa fa-lock"\n                                            aria-hidden="true">\n                                    </span>\n                                    <h4 class="subsection-title">\n                                        ')
                        __M_writer(filters.html_escape(filters.decode.utf8( subsection['display_name'] )))
                        __M_writer(u'\n                                    </h4>\n                                    <div class="details prerequisite">\n                                        ')
                        __M_writer(filters.html_escape(filters.decode.utf8( _("Prerequisite: ") )))
                        __M_writer(u'\n                                            ')

                        prerequisite_id = gated_content[subsection['id']]['prerequisite']
                        prerequisite_name = xblock_display_names.get(prerequisite_id)
                                                                    
                        
                        __M_locals_builtin_stored = __M_locals_builtin()
                        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['prerequisite_name','prerequisite_id'] if __M_key in __M_locals_builtin_stored]))
                        __M_writer(u'\n                                            ')
                        __M_writer(filters.html_escape(filters.decode.utf8( prerequisite_name )))
                        __M_writer(u'\n                                    </div>\n')
                    else:
                        __M_writer(u'                                    <button class="subsection-text accordion-trigger"\n                                            id="')
                        __M_writer(filters.html_escape(filters.decode.utf8( subsection['id'] )))
                        __M_writer(u'"\n                                            aria-expanded="')
                        __M_writer(filters.html_escape(filters.decode.utf8( 'true' if subsection_is_auto_opened else 'false' )))
                        __M_writer(u'"\n                                            aria-controls="')
                        __M_writer(filters.html_escape(filters.decode.utf8( subsection['id'] )))
                        __M_writer(u'_contents">\n                                        <span class="fa fa-chevron-right ')
                        __M_writer(filters.html_escape(filters.decode.utf8( 'fa-rotate-90' if subsection_is_auto_opened else '' )))
                        __M_writer(u'"\n                                              aria-hidden="true"></span>\n                                        <h4 class="subsection-title">\n                                            ')
                        __M_writer(filters.html_escape(filters.decode.utf8( subsection['display_name'] )))
                        __M_writer(u'\n                                        </h4>\n')
                        if subsection.get('complete'):
                            __M_writer(u'                                        <span class="complete-checkmark fa fa-check"></span>\n')
                    __M_writer(u'                                        <div class="details">\n\n')
                    __M_writer(u'                ')

                    if subsection.get('due') is None:
                        # examples: Homework, Lab, etc.
                        data_string = subsection.get('format')
                    else:
                        if 'special_exam_info' in subsection:
                            data_string = _('due {date}')
                        else:
                            data_string = _("{subsection_format} due {{date}}").format(subsection_format=subsection.get('format'))
                    
                    
                    __M_locals_builtin_stored = __M_locals_builtin()
                    __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['data_string'] if __M_key in __M_locals_builtin_stored]))
                    __M_writer(u'\n')
                    if subsection.get('format') or 'special_exam_info' in subsection:
                        __M_writer(u'                                            <span class="subtitle">\n')
                        if 'special_exam' in subsection:
                            __M_writer(u'                                                    <span\n                                                        class="menu-icon icon fa ')
                            __M_writer(filters.html_escape(filters.decode.utf8(subsection['special_exam_info'].get('suggested_icon', 'fa-pencil-square-o'))))
                            __M_writer(u' ')
                            __M_writer(filters.html_escape(filters.decode.utf8(subsection['special_exam_info'].get('status', 'eligible'))))
                            __M_writer(u'"\n                                                        aria-hidden="true"\n                                                    ></span>\n                                                    <span class="subtitle-name">\n                                                        ')
                            __M_writer(filters.html_escape(filters.decode.utf8(subsection['special_exam_info'].get('short_description', ''))))
                            __M_writer(u'\n                                                    </span>\n\n')
                            if not subsection['special_exam_info'].get('in_completed_state', False):
                                __M_writer(u'                                                        <span\n                                                            class="localized-datetime subtitle-name"\n                                                            data-datetime="')
                                __M_writer(filters.html_escape(filters.decode.utf8(subsection.get('due'))))
                                __M_writer(u'"\n                                                            data-string="')
                                __M_writer(filters.html_escape(filters.decode.utf8(data_string)))
                                __M_writer(u'"\n                                                            data-timezone="')
                                __M_writer(filters.html_escape(filters.decode.utf8(user_timezone)))
                                __M_writer(u'"\n                                                            data-language="')
                                __M_writer(filters.html_escape(filters.decode.utf8(user_language)))
                                __M_writer(u'"\n                                                        ></span>\n')
                        else:
                            __M_writer(u'                                                    <span\n                                                        class="localized-datetime subtitle-name"\n                                                        data-datetime="')
                            __M_writer(filters.html_escape(filters.decode.utf8(subsection.get('due'))))
                            __M_writer(u'"\n                                                        data-string="')
                            __M_writer(filters.html_escape(filters.decode.utf8(data_string)))
                            __M_writer(u'"\n                                                        data-timezone="')
                            __M_writer(filters.html_escape(filters.decode.utf8(user_timezone)))
                            __M_writer(u'"\n                                                        data-language="')
                            __M_writer(filters.html_escape(filters.decode.utf8(user_language)))
                            __M_writer(u'"\n                                                    ></span>\n\n')
                            if subsection.get('graded'):
                                __M_writer(u'                                                        <span class="sr">&nbsp;')
                                __M_writer(filters.html_escape(filters.decode.utf8(_("This content is graded"))))
                                __M_writer(u'</span>\n')
                        __M_writer(u'                                            </span>\n')
                    __M_writer(u'                                        </div> <!-- /details -->\n                                    </button> <!-- /subsection-text -->\n')
                    if gated_subsection and not completed_prereqs:
                        __M_writer(u'                                </a>\n')
                    if not gated_subsection or (gated_subsection and completed_prereqs):
                        __M_writer(u'                                <ol class="outline-item accordion-panel ')
                        __M_writer(filters.html_escape(filters.decode.utf8( '' if subsection_is_auto_opened else 'is-hidden' )))
                        __M_writer(u'"\n                                    id="')
                        __M_writer(filters.html_escape(filters.decode.utf8( subsection['id'] )))
                        __M_writer(u'_contents"\n                                    aria-labelledby="')
                        __M_writer(filters.html_escape(filters.decode.utf8( subsection['id'] )))
                        __M_writer(u'"\n                                >\n')
                        for vertical in subsection.get('children', []):
                            __M_writer(u'                                    <li class="vertical outline-item focusable">\n                                        <a class="outline-item focusable"\n                                            href="')
                            __M_writer(filters.html_escape(filters.decode.utf8( vertical['lms_web_url'] )))
                            __M_writer(u'"\n                                            id="')
                            __M_writer(filters.html_escape(filters.decode.utf8( vertical['id'] )))
                            __M_writer(u'">\n                                            <div class="vertical-details">\n                                              <div class="vertical-title">\n                                                ')
                            __M_writer(filters.html_escape(filters.decode.utf8( vertical['display_name'] )))
                            __M_writer(u'\n                                              </div>\n                                            </div>\n')
                            if vertical.get('complete'):
                                __M_writer(u'                                                <span class="complete-checkmark fa fa-check"></span>\n')
                            __M_writer(u'                                        </a>\n                                    </li>\n')
                        __M_writer(u'                                </ol>\n')
                    __M_writer(u'                            </li>\n')
                __M_writer(u'                    </ol>\n                </li>\n')
            __M_writer(u'        </ol>\n')
        __M_writer(u'</main>\n\n')
        def ccall(caller):
            def body():
                __M_writer = context.writer()
                __M_writer(u"\n    DateUtilFactory.transform('.localized-datetime');\n")
                return ''
            return [body]
        context.caller_stack.nextcaller = runtime.Namespace('caller', context, callables=ccall(__M_caller))
        try:
            __M_writer(filters.html_escape(filters.decode.utf8(static.require_module_async(class_name=u'DateUtilFactory',module_name=u'js/dateutil_factory'))))
        finally:
            context.caller_stack.nextcaller = None
        __M_writer(u'\n\n')
        def ccall(caller):
            def body():
                __M_writer = context.writer()
                __M_writer(u'\n    new CourseOutline();\n')
                return ''
            return [body]
        context.caller_stack.nextcaller = runtime.Namespace('caller', context, callables=ccall(__M_caller))
        try:
            __M_writer(filters.html_escape(filters.decode.utf8(static.webpack(entry=u'CourseOutline'))))
        finally:
            context.caller_stack.nextcaller = None
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"16": 7, "31": 5, "34": 3, "46": 2, "47": 3, "48": 5, "49": 13, "50": 14, "57": 17, "58": 18, "64": 20, "65": 22, "66": 23, "67": 28, "68": 28, "69": 29, "70": 29, "71": 34, "72": 35, "73": 35, "79": 37, "80": 40, "81": 40, "82": 41, "83": 41, "84": 42, "85": 42, "86": 43, "87": 43, "88": 44, "89": 44, "90": 45, "91": 46, "92": 48, "93": 49, "94": 49, "95": 50, "96": 50, "97": 51, "98": 51, "99": 52, "100": 53, "101": 53, "109": 57, "110": 58, "111": 58, "112": 59, "113": 60, "114": 60, "115": 60, "116": 62, "117": 62, "118": 67, "119": 67, "120": 70, "121": 70, "122": 71, "129": 74, "130": 75, "131": 75, "132": 77, "133": 78, "134": 79, "135": 79, "136": 80, "137": 80, "138": 81, "139": 81, "140": 82, "141": 82, "142": 85, "143": 85, "144": 87, "145": 88, "146": 91, "147": 97, "148": 97, "161": 106, "162": 107, "163": 108, "164": 109, "165": 111, "166": 112, "167": 112, "168": 112, "169": 112, "170": 116, "171": 116, "172": 121, "173": 122, "174": 124, "175": 124, "176": 125, "177": 125, "178": 126, "179": 126, "180": 127, "181": 127, "182": 130, "183": 133, "184": 135, "185": 135, "186": 136, "187": 136, "188": 137, "189": 137, "190": 138, "191": 138, "192": 141, "193": 142, "194": 142, "195": 142, "196": 145, "197": 147, "198": 149, "199": 150, "200": 152, "201": 153, "202": 153, "203": 153, "204": 154, "205": 154, "206": 155, "207": 155, "208": 157, "209": 158, "210": 160, "211": 160, "212": 161, "213": 161, "214": 164, "215": 164, "216": 167, "217": 168, "218": 170, "219": 173, "220": 175, "221": 177, "222": 180, "223": 182, "227": 184, "232": 184, "235": 186, "239": 188, "244": 188, "247": 190, "253": 247}, "uri": "course_experience/course-outline-fragment.html", "filename": "/home/nttlong/code/edx/apps/edx/edx-platform/common/lib/capa/capa/templates/course_experience/course-outline-fragment.html"}
__M_END_METADATA
"""
