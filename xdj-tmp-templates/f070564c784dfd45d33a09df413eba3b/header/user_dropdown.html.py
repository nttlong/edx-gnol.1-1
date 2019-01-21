# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1548073578.805847
_enable_loop = True
_template_filename = u'/home/nttlong/code/edx/apps/edx/edx-platform/xdj-gnol-lms-templates/header/user_dropdown.html'
_template_uri = u'/header/user_dropdown.html'
_source_encoding = 'utf-8'
_exports = []



from django.urls import reverse
from django.utils.translation import ugettext as _

from openedx.core.djangoapps.user_api.accounts.image_helpers import get_profile_image_urls_for_user
from openedx.core.djangoapps.user_api.accounts.utils import retrieve_last_sitewide_block_completed
from openedx.features.enterprise_support.utils import get_enterprise_learner_generic_name


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
        getattr = context.get('getattr', UNDEFINED)
        request = context.get('request', UNDEFINED)
        user = context.get('user', UNDEFINED)
        self = context.get('self', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')

## This template should not use the target student's details when masquerading, see TNL-4895
        self.real_user = getattr(user, 'real_user', user)
        profile_image_url = get_profile_image_urls_for_user(self.real_user)['medium']
        username = self.real_user.username
        resume_block = retrieve_last_sitewide_block_completed(username)
        displayname = get_enterprise_learner_generic_name(request) or username
        
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['username','resume_block','displayname','profile_image_url'] if __M_key in __M_locals_builtin_stored]))
        __M_writer(u'\n\n<div class="nav-item hidden-mobile">\n    <a href="')
        __M_writer(filters.html_escape(filters.decode.utf8(reverse('dashboard'))))
        __M_writer(u'" class="menu-title">\n        <img class="user-image-frame" src="')
        __M_writer(filters.html_escape(filters.decode.utf8(profile_image_url)))
        __M_writer(u'" alt="">\n        <span class="sr-only">')
        __M_writer(filters.html_escape(filters.decode.utf8(_("Dashboard for:"))))
        __M_writer(u'</span>\n        <span class="username">')
        __M_writer(filters.html_escape(filters.decode.utf8(displayname)))
        __M_writer(u'</span>\n    </a>\n</div>\n<div class="nav-item hidden-mobile nav-item-dropdown" tabindex="-1">\n    <div class="toggle-user-dropdown" role="button" aria-label=')
        __M_writer(filters.html_escape(filters.decode.utf8(_("Options Menu"))))
        __M_writer(u' aria-expanded="false" tabindex="0" aria-controls="user-menu">\n        <span class="fa fa-caret-down" aria-hidden="true"></span>\n    </div>\n    <div class="dropdown-user-menu hidden" aria-label=')
        __M_writer(filters.html_escape(filters.decode.utf8(_("More Options"))))
        __M_writer(u' role="menu" id="user-menu" tabindex="-1">\n')
        if resume_block:
            __M_writer(u'            <div class="mobile-nav-item dropdown-item dropdown-nav-item"><a href="')
            __M_writer(filters.html_escape(filters.decode.utf8(resume_block)))
            __M_writer(u'" role="menuitem">')
            __M_writer(filters.html_escape(filters.decode.utf8(_("Resume your last course"))))
            __M_writer(u'</a></div>\n')
        __M_writer(u'        <div class="mobile-nav-item dropdown-item dropdown-nav-item"><a href="')
        __M_writer(filters.html_escape(filters.decode.utf8(reverse('dashboard'))))
        __M_writer(u'" role="menuitem">')
        __M_writer(filters.html_escape(filters.decode.utf8(_("Dashboard"))))
        __M_writer(u'</a></div>\n        <div class="mobile-nav-item dropdown-item dropdown-nav-item"><a href="')
        __M_writer(filters.html_escape(filters.decode.utf8(reverse('learner_profile', kwargs={'username': username}))))
        __M_writer(u'" role="menuitem">')
        __M_writer(filters.html_escape(filters.decode.utf8(_("Profile"))))
        __M_writer(u'</a></div>\n        <div class="mobile-nav-item dropdown-item dropdown-nav-item"><a href="')
        __M_writer(filters.html_escape(filters.decode.utf8(reverse('account_settings'))))
        __M_writer(u'" role="menuitem">')
        __M_writer(filters.html_escape(filters.decode.utf8(_("Account"))))
        __M_writer(u'</a></div>\n        <div class="mobile-nav-item dropdown-item dropdown-nav-item"><a href="')
        __M_writer(filters.html_escape(filters.decode.utf8(reverse('logout'))))
        __M_writer(u'" role="menuitem">')
        __M_writer(filters.html_escape(filters.decode.utf8(_("Sign Out"))))
        __M_writer(u'</a></div>\n    </div>\n</div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"16": 5, "32": 3, "35": 2, "44": 2, "45": 3, "46": 12, "47": 14, "58": 21, "59": 24, "60": 24, "61": 25, "62": 25, "63": 26, "64": 26, "65": 27, "66": 27, "67": 31, "68": 31, "69": 34, "70": 34, "71": 35, "72": 36, "73": 36, "74": 36, "75": 36, "76": 36, "77": 38, "78": 38, "79": 38, "80": 38, "81": 38, "82": 39, "83": 39, "84": 39, "85": 39, "86": 40, "87": 40, "88": 40, "89": 40, "90": 41, "91": 41, "92": 41, "93": 41, "99": 93}, "uri": "/header/user_dropdown.html", "filename": "/home/nttlong/code/edx/apps/edx/edx-platform/xdj-gnol-lms-templates/header/user_dropdown.html"}
__M_END_METADATA
"""
