# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1548073937.790159
_enable_loop = True
_template_filename = u'/home/nttlong/code/edx/apps/edx/edx-platform/xdj-gnol-lms-templates/wiki/includes/breadcrumbs.html'
_template_uri = u'wiki/includes/breadcrumbs.html'
_source_encoding = 'utf-8'
_exports = []



from django.urls import reverse
from django.utils.translation import ugettext as _


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        urlpath = context.get('urlpath', UNDEFINED)
        article = context.get('article', UNDEFINED)
        Undefined = context.get('Undefined', UNDEFINED)
        user = context.get('user', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n')
        __M_writer(u'\n\n')
        if urlpath is not Undefined and urlpath:
            __M_writer(u'<header class="breadcrumbs-header">\n  <h2 class="sr">')
            __M_writer(filters.html_escape(filters.decode.utf8(_("Course Wiki"))))
            __M_writer(u'</h2>\n  <ul class="breadcrumb pull-left" class="">\n    ')

      # The create button links to the highest ancestor we have edit priveleges to
            create_article_root = None
                
            
            __M_locals_builtin_stored = __M_locals_builtin()
            __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['create_article_root'] if __M_key in __M_locals_builtin_stored]))
            __M_writer(u'\n')
            for ancestor in urlpath.cached_ancestors:
                __M_writer(u'      <li><a href="')
                __M_writer(filters.html_escape(filters.decode.utf8(reverse('wiki:get', kwargs={'path' : ancestor.path}))))
                __M_writer(u'">')
                __M_writer(filters.html_escape(filters.decode.utf8(ancestor.article.current_revision.title)))
                __M_writer(u'</a></li>\n      ')

                if not create_article_root and ancestor.article.can_write(user):
                  create_article_root = ancestor
                      
                
                __M_locals_builtin_stored = __M_locals_builtin()
                __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['create_article_root'] if __M_key in __M_locals_builtin_stored]))
                __M_writer(u'\n')
            __M_writer(u'    <li class="active"><a href="')
            __M_writer(filters.html_escape(filters.decode.utf8(reverse('wiki:get', kwargs={'path' : urlpath.path}))))
            __M_writer(u'">')
            __M_writer(filters.html_escape(filters.decode.utf8(article.current_revision.title)))
            __M_writer(u'</a></li>\n    ')

            if not create_article_root and urlpath.article.can_write(user):
              create_article_root = urlpath
                
            
            __M_locals_builtin_stored = __M_locals_builtin()
            __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['create_article_root'] if __M_key in __M_locals_builtin_stored]))
            __M_writer(u'\n  </ul>\n\n  <div class="global-functions pull-right">\n    <!-- <form class="search-wiki pull-left">\n      <input type="search" placeholder="search wiki" />\n    </form> -->\n')
            if create_article_root:
                __M_writer(u'    <a class="add-article-btn btn pull-left" href="')
                __M_writer(filters.html_escape(filters.decode.utf8(reverse('wiki:create', kwargs={'path' : create_article_root.path}))))
                __M_writer(u'" style="padding: 7px;">\n      <span class="icon fa fa-plus" aria-hidden="true"></span>\n      ')
                __M_writer(filters.html_escape(filters.decode.utf8(_("Add article"))))
                __M_writer(u'\n    </a>\n')
            __M_writer(u'  </div>\n</header>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"16": 3, "21": 2, "30": 2, "31": 6, "32": 8, "33": 9, "34": 10, "35": 10, "36": 12, "43": 15, "44": 16, "45": 17, "46": 17, "47": 17, "48": 17, "49": 17, "50": 18, "57": 21, "58": 23, "59": 23, "60": 23, "61": 23, "62": 23, "63": 24, "70": 27, "71": 34, "72": 35, "73": 35, "74": 35, "75": 37, "76": 37, "77": 40, "83": 77}, "uri": "wiki/includes/breadcrumbs.html", "filename": "/home/nttlong/code/edx/apps/edx/edx-platform/xdj-gnol-lms-templates/wiki/includes/breadcrumbs.html"}
__M_END_METADATA
"""
