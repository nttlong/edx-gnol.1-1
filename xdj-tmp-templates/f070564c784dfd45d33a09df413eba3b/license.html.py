# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1548073579.163228
_enable_loop = True
_template_filename = u'/home/nttlong/code/edx/apps/edx/edx-platform/openedx/core/lib/license/templates/license.html'
_template_uri = u'license.html'
_source_encoding = 'utf-8'
_exports = []



from django.utils.translation import ugettext as _

def parse_license(lic):
    """
    Returns a two-tuple: license type, and options.
    """
    if not lic:
        return None, {}
    if ":" not in lic:
        # no options, so the entire thing is the license type
        return lic, {}

    ltype, option_str = lic.split(":", 1)
    options = {}
    for part in option_str.split():
        if "=" in part:
            key, value = part.split("=", 1)
            options[key] = value
        else:
            options[part] = True
    return ltype, options


def render_body(context,license,button=False,button_size='88x31',**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(button=button,button_size=button_size,pageargs=pageargs,license=license)
        len = context.get('len', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n')
        __M_writer(u'\n')
        license_type, license_options = parse_license(license) 
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['license_type','license_options'] if __M_key in __M_locals_builtin_stored]))
        __M_writer(u'\n')
        if license_type == "all-rights-reserved":
            __M_writer(u'    \xa9 <span class="license-text">')
            __M_writer(filters.decode.utf8(_("All Rights Reserved")))
            __M_writer(u'</span>\n')
        elif license_type == "creative-commons":
            __M_writer(u'    ')

            possible = ["by", "nc", "nd", "sa"]
            names = {
               "by": _("Attribution"), "nc": _("Noncommercial"),
               "nd": _("No Derivatives"), "sa": _("Share Alike")
            }
            enabled = [opt for opt in possible
                       if license_options.get(opt) or license_options.get(opt.upper())]
            version = license_options.get("ver", "4.0")
            if len(enabled) == 0:
                enabled = ["zero"]
                version = license_options.get("ver", "1.0")
            
            
            __M_locals_builtin_stored = __M_locals_builtin()
            __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['opt','version','enabled','possible','names'] if __M_key in __M_locals_builtin_stored]))
            __M_writer(u'\n    <a rel="license" href="https://creativecommons.org/licenses/')
            __M_writer(filters.decode.utf8('-'.join(enabled)))
            __M_writer(u'/')
            __M_writer(filters.decode.utf8(version))
            __M_writer(u'/" target="_blank">\n')
            if button:
                __M_writer(u'        <img src="https://licensebuttons.net/l/')
                __M_writer(filters.decode.utf8('-'.join(enabled)))
                __M_writer(u'/')
                __M_writer(filters.decode.utf8(version))
                __M_writer(u'/')
                __M_writer(filters.decode.utf8(button_size))
                __M_writer(u'.png"\n             alt="')
                __M_writer(filters.decode.utf8(license))
                __M_writer(u'"\n             />\n        </a>\n')
            else:
                __M_writer(u'        <span class="sr">')
                __M_writer(filters.decode.utf8(_("Creative Commons licensed content, with terms as follow:")))
                __M_writer(u'&nbsp;</span><span aria-hidden="true" class="icon-cc"></span>\n')
                for option in enabled:
                    __M_writer(u'            <span class="sr">')
                    __M_writer(filters.decode.utf8(names[option]))
                    __M_writer(u'&nbsp;</span><span aria-hidden="true" class="icon-cc-')
                    __M_writer(filters.decode.utf8(option))
                    __M_writer(u'"></span>\n')
                __M_writer(u'        <span class="license-text">')
                __M_writer(filters.decode.utf8(_("Some Rights Reserved")))
                __M_writer(u'</span>\n')
            __M_writer(u'    </a>\n')
        else:
            __M_writer(u'    ')
            __M_writer(filters.decode.utf8(license))
            __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"16": 3, "40": 1, "46": 1, "47": 25, "48": 26, "52": 26, "53": 27, "54": 28, "55": 28, "56": 28, "57": 29, "58": 30, "59": 30, "75": 42, "76": 43, "77": 43, "78": 43, "79": 43, "80": 44, "81": 45, "82": 45, "83": 45, "84": 45, "85": 45, "86": 45, "87": 45, "88": 46, "89": 46, "90": 49, "91": 51, "92": 51, "93": 51, "94": 52, "95": 53, "96": 53, "97": 53, "98": 53, "99": 53, "100": 55, "101": 55, "102": 55, "103": 57, "104": 58, "105": 59, "106": 59, "107": 59, "113": 107}, "uri": "license.html", "filename": "/home/nttlong/code/edx/apps/edx/edx-platform/openedx/core/lib/license/templates/license.html"}
__M_END_METADATA
"""
