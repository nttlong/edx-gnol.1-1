# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1548073946.112939
_enable_loop = True
_template_filename = u'/home/nttlong/code/edx/apps/edx/edx-platform/xdj-gnol-lms-templates/wiki/includes/article_menu.html'
_template_uri = u'wiki/includes/article_menu.html'
_source_encoding = 'utf-8'
_exports = []



from django.urls import reverse
from django.utils.translation import ugettext as _
from openedx.core.djangolib.markup import HTML, Text
from wiki.core.permissions import can_change_permissions


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        selected_tab = context.get('selected_tab', UNDEFINED)
        urlpath = context.get('urlpath', UNDEFINED)
        user = context.get('user', UNDEFINED)
        article_tabs = context.get('article_tabs', UNDEFINED)
        article = context.get('article', UNDEFINED)
        hasattr = context.get('hasattr', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n')
        __M_writer(u'\n\n<li class="')
        __M_writer(filters.html_escape(filters.decode.utf8("active" if selected_tab == "view" else "")))
        __M_writer(u'">\n  <a href="')
        __M_writer(filters.html_escape(filters.decode.utf8(reverse('wiki:get', kwargs={'article_id' : article.id, 'path' : urlpath.path}))))
        __M_writer(u'">\n    <span class="icon fa fa-eye" aria-hidden="true"></span>\n    ')
        __M_writer(filters.html_escape(filters.decode.utf8(_("View"))))
        __M_writer(u'\n    ')
        __M_writer(filters.html_escape(filters.decode.utf8(Text(_("{span_start}(active){span_end}")).format(span_start=HTML("<span class='sr'>"), span_end=HTML("</span>")) if selected_tab == "view" else "")))
        __M_writer(u'\n  </a>\n</li>\n\n')
        if article.can_write(user):
            __M_writer(u'  <li class="')
            __M_writer(filters.html_escape(filters.decode.utf8("active" if selected_tab == "edit" else "")))
            __M_writer(u'">\n    <a href="')
            __M_writer(filters.html_escape(filters.decode.utf8(reverse('wiki:edit', kwargs={'article_id' : article.id, 'path' : urlpath.path}))))
            __M_writer(u'">\n      <span class="icon fa fa-pencil" aria-hidden="true"></span>\n      ')
            __M_writer(filters.html_escape(filters.decode.utf8(_("Edit"))))
            __M_writer(u'\n      ')
            __M_writer(filters.html_escape(filters.decode.utf8(Text(_("{span_start}(active){span_end}")).format(span_start=HTML("<span class='sr'>"), span_end=HTML("</span>")) if selected_tab == "edit" else "")))
            __M_writer(u'\n    </a>\n  </li>\n')
        __M_writer(u'\n<li class="')
        __M_writer(filters.html_escape(filters.decode.utf8("active" if selected_tab == "history" else "")))
        __M_writer(u'">\n  <a href="')
        __M_writer(filters.html_escape(filters.decode.utf8(reverse('wiki:history', kwargs={'article_id' : article.id, 'path' : urlpath.path}))))
        __M_writer(u'">\n    <span class="icon fa fa-clock-o" aria-hidden="true"></span>\n    ')
        __M_writer(filters.html_escape(filters.decode.utf8(_("Changes"))))
        __M_writer(u'\n    ')
        __M_writer(filters.html_escape(filters.decode.utf8(Text(_("{span_start}(active){span_end}")).format(span_start=HTML("<span class='sr'>"), span_end=HTML("</span>")) if selected_tab == "history" else "")))
        __M_writer(u'\n  </a>\n</li>\n\n')
        for plugin in article_tabs:
            if hasattr(plugin, "article_tab"):
                __M_writer(u'    <li class="')
                __M_writer(filters.html_escape(filters.decode.utf8("active" if selected_tab == plugin.slug else "")))
                __M_writer(u'">\n      <a href="')
                __M_writer(filters.html_escape(filters.decode.utf8(reverse('wiki:plugin', kwargs={'slug' : plugin.slug, 'article_id' : article.id, 'path' : urlpath.path}) )))
                __M_writer(u'">\n        <span class="icon fa fa-file ')
                __M_writer(filters.html_escape(filters.decode.utf8(plugin.article_tab[1])))
                __M_writer(u'" aria-hidden="true"></span>\n        ')
                __M_writer(filters.html_escape(filters.decode.utf8(plugin.article_tab[0])))
                __M_writer(u'\n        ')
                __M_writer(filters.html_escape(filters.decode.utf8(Text(_("{span_start}(active){span_end}")).format(span_start=HTML("<span class='sr'>"), span_end=HTML("</span>")) if selected_tab == plugin.slug else "")))
                __M_writer(u'\n      </a>\n    </li>\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')
        if can_change_permissions(article,user):
            __M_writer(u'<li class="')
            __M_writer(filters.html_escape(filters.decode.utf8("active" if selected_tab == "settings" else "")))
            __M_writer(u'">\n  <a href="')
            __M_writer(filters.html_escape(filters.decode.utf8(reverse('wiki:settings', kwargs={'article_id' : article.id, 'path' : urlpath.path}))))
            __M_writer(u'">\n    <span class="icon fa fa-cog" aria-hidden="true"></span>\n    ')
            __M_writer(filters.html_escape(filters.decode.utf8(_("Settings"))))
            __M_writer(u'\n    ')
            __M_writer(filters.html_escape(filters.decode.utf8(Text(_("{span_start}active{span_end}")).format(span_start=HTML("<span class='sr'>"), span_end=HTML("</span>")) if selected_tab == "settings" else "")))
            __M_writer(u'\n  </a>\n</li>\n')
        __M_writer(u'\n\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"16": 3, "23": 2, "34": 2, "35": 8, "36": 10, "37": 10, "38": 11, "39": 11, "40": 13, "41": 13, "42": 14, "43": 14, "44": 18, "45": 19, "46": 19, "47": 19, "48": 20, "49": 20, "50": 22, "51": 22, "52": 23, "53": 23, "54": 27, "55": 28, "56": 28, "57": 29, "58": 29, "59": 31, "60": 31, "61": 32, "62": 32, "63": 36, "64": 37, "65": 38, "66": 38, "67": 38, "68": 39, "69": 39, "70": 40, "71": 40, "72": 41, "73": 41, "74": 42, "75": 42, "76": 47, "77": 51, "78": 53, "79": 54, "80": 54, "81": 54, "82": 55, "83": 55, "84": 57, "85": 57, "86": 58, "87": 58, "88": 62, "94": 88}, "uri": "wiki/includes/article_menu.html", "filename": "/home/nttlong/code/edx/apps/edx/edx-platform/xdj-gnol-lms-templates/wiki/includes/article_menu.html"}
__M_END_METADATA
"""
