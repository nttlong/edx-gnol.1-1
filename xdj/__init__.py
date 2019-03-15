#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Package này dùng để mở rộng open edx app (dạng micro app)
xdj: Extension of django framework including:
    1- MVC support
    2- Automatic controller loader:
        You just create a package in xdj_apps with directory struct like bellow:
        ├── <app dir name>
                ├── <controller>(contains your controller files here)
                │        ├── <controller 1>.py
                │        ├── <controller 2>.py
                │        ...
                │        ├── <controller n>.py
                │
                ├── static (all static file serve for your web site here)
                ├── views (all html view files here)

"""


from . dynamic_object import dobject
from django.conf import settings
import sys
import os
from .controller_privileges import Privilges,privilege
try:
    sys.path.append(os.sep.join([settings.REPO_ROOT,"cms/djangoapps"]))
except Exception as ex:
    pass

__apps__ = {} # micro app setting cache
__register_apps__ = {}
__controllers__ = []
__pages__ = []
__build_cached__ = None
__controllert_url_build_cache__ = None
__controlers_hash__ = None
__controlers_hash_vert__ = None
from . controllers import Model


def help():
    """
    Show help for this package
    :return:
    """
    print "xdj: Extension of django framework including: \n" \
          "1- MVC support \n" \
          "2- Automatic controller loader: \n" \
          "      You just create a package in xdj_apps with directories looks like bellow: \n" \
          "        ├── <app dir name> \n" \
          "        │         ├── <controller>(contains your controller files here) \n" \
          "        │         │        ├── <controller 1>.py \n" \
          "        │         │        ├── <controller 2>.py \n" \
          "        │         │        ...\n" \
          "        │         │        ├── <controller n>.py \n" \
          "        │         │ \n"\
          "        │         ├── static (all static file serve for your web site here)  \n" \
          "        │         ├── views (all html view files here)\n" \
          "3- Create controller file:\n" \
          "  3-1: In controller dir of app create file <controller name>.py\n" \
          "  3-2: import xdj\n" \
          "  3-4: add bellow declare:\n" \
          "         @xdj.Controller(url='...',template='...')\n" \
          "         class <Controller name>(xdj.BaseController):\n" \
          "             def on_get(self,model):\n" \
          "                 return self.render(model)\n"


def get_info_of_apps():
    """
    Get all apps info and return dictionary with key of each item is the name of app.
    Lấy thông tin của tất cả các apps là một dictionary với khóa của mỗi item chính là tên của app
    :return:
    """
    return __apps__


def __create__(urls):
    """
    Tạo app
    The method will load all apps in xdj_apps and extract information in each app of apps folder the build urls for all apps.
    Hàm này sẽ tải tất cả các app trong thư mục xdj_apps (mỗi package trong thư mục này là một app).
    Sau đó, sẽ tiến hành xây dựng lại thông tin url cho django settings
    :param name:
    :param host_dir:
    :return:
    """
    global __controlers_hash__
    if not __controlers_hash__:
        __controlers_hash__ = {}
    global __controlers_hash_vert__
    if not __controlers_hash_vert__:
        __controlers_hash_vert__ = {}
    import uuid
    from . private_services import __find_url_by_pattern__
    urlpatterns = ()
    global __build_cached__
    if __build_cached__ == None:
        __build_cached__ = {}

    from django.conf.urls import url
    import django
    replace_urls = []
    check_urls = []
    for item in __controllers__:
        hash_path = item.instance.__class__.__module__ + "/" + item.instance.__class__.__name__
        controller_id = uuid.uuid4().__str__()
        __controlers_hash__.update({
            controller_id: dict(instance = item,
                                hash_path = hash_path)
        })
        __controlers_hash_vert__.update({
            hash_path:dict(
                instance  = item,
                controller_id = controller_id
            )
        })



        if item.instance.replace_url:
            replace_urls.append(item.instance)
        if item.instance.check_url:
            check_urls.append(item.instance)

        if not __apps__.has_key(item.instance.app_name):
            import os
            try:
                if item.instance.app_dir != None:
                    server_static_path = os.sep.join([
                        item.instance.app_dir,"static"
                    ])
                    urlpatterns+=(
                        url(r'^' + item.instance.host_dir + '/static/(?P<path>.*)$', django.views.static.serve,
                            {'document_root': server_static_path, 'show_indexes': True}),
                    )
            except Exception as ex:
                raise ex
            __apps__.update({
                item.instance.app_name:item.instance.app_name
            })
        if not __build_cached__.has_key(item.instance.on_get.im_func.func_code.co_filename):
            if item.url=="":
                print item.instance.on_get.im_func.func_code.co_filename
                urlpatterns +=(
                    url(r"^"+item.instance.host_dir + "$", item.instance.__view_exec__),
                    url(r"^"+item.instance.host_dir + "/$", item.instance.__view_exec__)
                )
            else:
                urlpatterns += (
                    url(r"^"+item.instance.host_dir +"/"+item.url+"$", item.instance.__view_exec__),
                    url(r"^"+item.instance.host_dir +"/"+item.url+"/$", item.instance.__view_exec__)
                )
            for sub_page in item.instance.sub_pages:
                if item.url == "":
                    urlpatterns += (
                        url(r"^" + item.instance.host_dir+"/"+sub_page.url + "$", sub_page.exec_request_get),
                        url(r"^" + item.instance.host_dir +"/"+sub_page.url+ "/$", sub_page.exec_request_get)
                    )
                else:
                    urlpatterns += (
                        url(r"^" + item.instance.host_dir + "/" + item.url+"/"+sub_page.url + "$", sub_page.exec_request_get),
                        url(r"^" + item.instance.host_dir + "/" + item.url+"/"+sub_page.url + "/$", sub_page.exec_request_get)
                    )
            __build_cached__.update({
                item.instance.on_get.im_func.func_code.co_filename:item.instance.on_get
            })
        # urlpatterns += (
        #     url(r'config/self_paced', ConfigurationModelCurrentAPIView.as_view(model=SelfPacedConfiguration)),
        #     url(r'config/programs', ConfigurationModelCurrentAPIView.as_view(model=ProgramsApiConfig)),
        #     url(r'config/catalog', ConfigurationModelCurrentAPIView.as_view(model=CatalogIntegration)),
        #     url(r'config/forums', ConfigurationModelCurrentAPIView.as_view(model=ForumsConfig)),
        # )
    if isinstance(urls,tuple):
        urls += urlpatterns
    for item in replace_urls:
        class cls_replacer():
            def __init__(self,obj):
                self.obj=obj
            def exec_url(self,request,*args,**kwargs):
                return self.obj.__view_exec__(request,*args,**kwargs)
        print "will replace with {0}".format(item.replace_url)
        match_url = __find_url_by_pattern__(urls, item.replace_url)
        if not match_url:
            print "{0} can not find replacer, will run under {1}".format(item.replace_url,item.url)
        else:
            import inspect
            print "{0} can not find replacer, will run by controller {1} in {2}".format(match_url.regex.pattern , item,inspect.getfile(item.__class__))
            x= cls_replacer(item)
            match_url.callback = x.exec_url
    for item in check_urls:
        print "{0} will be check".format(item.check_url)
        match_url = match_url = __find_url_by_pattern__(urls, item.check_url)
        if not match_url:
            print "{0} can not find checker, will run under {1}".format(item.check_url,item.url)
        else:
            import inspect
            print "{0} will be check by controller {1} in {2}".format(match_url.regex.pattern , item,inspect.getfile(item.__class__))

            class obj_check_url():
                def __init__(self,obj,origin_callback):
                    self.obj = obj
                    self.__origin_callback__ = origin_callback

                def check_request(self,request,*args,**kwargs):
                    ret = self.obj.__view_exec__(request, *args, **kwargs)
                    if ret:
                        if issubclass(type(ret),Handler):
                            _ret = ret.OnBeforeHandler(ret.model)
                            if _ret==None:
                                _ret = self.__origin_callback__(request,*args,**kwargs)
                                ret.model.origin_result= _ret
                                _ret = ret.OnAfterHandler(ret.model)
                                if _ret == None:
                                    return ret.model.origin_result
                                else:
                                    return _ret
                        return ret
                    else:
                        return self.__origin_callback__(request, *args, **kwargs)

            x_obj = obj_check_url(item,match_url.callback)

            match_url.callback = x_obj.check_request
    if isinstance(urls, list):
        urls.extend(list(urlpatterns))

    # x = [x for x in urls if x._regex == r"^static\/(?P<path>.*)$"]
    # u = x[0]
    # print x[0].default_args["document_root"]
    return urls
from . controllers import BaseController,Controller
from .page import Page


def register_INSTALLED_APPS(for_lms):
    """
    This method just serve for Openedx nothing more.
    The method will be call at {source}/apps/edx/edx_platform/cms/startup.py
    and {source}/apps/edx/edx_platform/lms/startup.py

    Chức năng này chỉ phục vụ cho Openedx không có gì khác.
     Phương thức này sẽ được gọi tại {source} /apps/edx/edx_pl platform / cms / startup.py
     và {source} /apps/edx/edx_pl platform / lms / startup.py
    :param for_lms:
    :return:
    """
    from . import private_services as ps
    try:
        ps.__load_middle_ware__()
        ps.__load_models__()
        ps.__load_settings__(for_lms)
        ps.__load_config__()

        ps.__load_email_settings__()
        ps.__load_feature_settings__()
        ps.__load_elastic_search_config__()
        ps.__load_forum_config__()
        ps.__load_installed_apps__()
        # settings.MIDDLEWARE_CLASSES.append("xdj.middle_ware.GlobalRequestMiddleware")
    except Exception as ex:
        raise Exception(ex)


def load_apps(urlpatterns=None):
    """
    Load all apps and rebuild urlpattern app info can get by get_info_of_apps
    Tải tất cả các ứng dụng và xây dựng lại thông tin ứng dụng Mẫu Url có thể nhận được bằng get_info_of_apps
    :param urlpatterns:
    :return:
    """
    from exceptions import IOError
    import os
    from django.conf import settings
    from . import private_services as ps
    _path = os.sep.join([settings.REPO_ROOT.__str__(), "xdj_apps"])
    if settings.INSTALLED_APPS.count("xdj_models.models") == 0:
        raise Exception("it look like you forgot call xdj.register_INSTALLED_APPS() at manage.py , cms/bitnami_wsgi.py or lms/bitnami_wsgi.py before startup.run()\n"
                        "How to use xdj?\n"
                        "At before startup.run() for dev mode or for deploy mode bottom of '{edx source}/apps/edx/edx-platform/lms/envs/bitnami.py' put follow code:\n"
                        "import sys\n"
                        "sys.path.append(path to parent of xdj package)\n"
                        "import xdj"
                        "xdj.register_INSTALLED_APPS()\n"
                        "")

    if urlpatterns==None:
        urlpatterns=()
    import os
    import sys
    import imp
    import xdj
    global __controllert_url_build_cache__
    if __controllert_url_build_cache__ == None:
        __controllert_url_build_cache__ = {}
    sys.path.append(_path)
    ps.__apply_settings__()
    path_to_app_dir = _path

    def get_all_sub_dir():
        lst=[x for x in os.walk(path_to_app_dir).next()[1] if x.find(".")==-1]
        return lst
    lst_sub_dirs = get_all_sub_dir()
    for item in lst_sub_dirs:
        full_path_to_app = os.sep.join([path_to_app_dir,item])
        sys.path.append(full_path_to_app)
        controller_dir = os.sep.join([path_to_app_dir,item,"controllers"])
        if not hasattr(xdj, "apps"):
            setattr(xdj, "apps", imp.new_module("xdj.apps"))
        if not hasattr(xdj.apps, item):
            setattr(xdj.apps, item, imp.new_module("xdj.apps.{0}".format(item)))
        try:
            app_settings = imp.load_source("xdj.apps.{0}.settings".format(item),os.sep.join([path_to_app_dir,item,"settings.py"]))
        except IOError as ex:
            raise Exception("{0} was not found ".format(item),os.sep.join([path_to_app_dir,item,"settings.py"]))
        except Exception as ex:
            raise ex
        if not hasattr(app_settings,"app_name"):
            raise Exception("'{0}' was not found in '{1}'".format(
                "app_name",
                os.sep.join([path_to_app_dir, item, "settings.py"])
            ))
        if not hasattr(app_settings,"on_authenticate"):
            raise Exception("'{0}' was not found in '{1}'".format(
                "on_authenticate",
                os.sep.join([path_to_app_dir, item, "settings.py"])
            ))
        if not callable(app_settings.on_authenticate):
            raise Exception("{0} in {1} must be a function with one param".format(
                "on_authenticate",
                os.sep.join([path_to_app_dir, item, "settings.py"])
            ))
        if not hasattr(app_settings,"host_dir"):
            raise Exception("'{0}' was not found in '{1}'".format(
                "host_dir",
                os.sep.join([path_to_app_dir, item, "settings.py"])
            ))
        if not type(app_settings.host_dir) in [str,unicode]:
            raise Exception(
                "{0} in {3} mut be in {1}, not is {2}".format(
                    "host_dir",
                    [str,unicode],
                    app_settings.host_dir,
                    os.sep.join([path_to_app_dir, item, "settings.py"])
                )
            )
        if not hasattr(app_settings,"on_get_language_resource_item"):
            raise Exception("'{0}' was not found in '{1}'".format(
                "on_get_language_resource_item",
                os.sep.join([path_to_app_dir, item, "settings.py"])
            ))
        if not callable(app_settings.on_get_language_resource_item):
            raise Exception("'{0}' in '{1}' must be a function like bellow\n"
                            "on_get_language_resource_item(language,appname,view,key,value)".format(
                "on_get_language_resource_item",
                os.sep.join([path_to_app_dir, item, "settings.py"])
            ))
        if not hasattr(app_settings,"rel_login_url"):
            raise Exception("'{0}' was not found in '{1}'".format(
                "rel_login_url",
                os.sep.join([path_to_app_dir, item, "settings.py"])
            ))
        import inspect
        if inspect.getargspec(app_settings.on_get_language_resource_item).args.__len__()<4:
            raise Exception("'{0}' in '{1}' must be a function like bellow\n"
                            "on_get_language_resource_item(language,appname,view,key,value)".format(
                "on_get_language_resource_item",
                os.sep.join([path_to_app_dir, item, "settings.py"])
            ))

        _app=getattr(xdj.apps, item)
        if not hasattr(_app,"settings"):
            setattr(_app,"settings",app_settings)

        sys.path.append(controller_dir)
        files = os.listdir(controller_dir)
        for file in files:

            import inspect
            controller_file = os.sep.join([controller_dir,file])
            extension = os.path.splitext(controller_file)[1][1:]
            if (not __controllert_url_build_cache__.has_key(controller_file)) and extension == "py":
                m = None
                try:
                    m = imp.load_source("{0}.{1}".format(item,file.split('.')[0]),controller_file)
                except SyntaxError as ex:
                    raise ex
                except Exception as ex:
                    from xdj.errors import LoadControllerError
                    raise LoadControllerError(ex.message,file,ex.args)

                if __controllers__.__len__()>0:
                    controller_instance=__controllers__[__controllers__.__len__()-1].instance
                    class_file = inspect.getfile(controller_instance.__class__)
                    extension_class = os.path.splitext(class_file)[1][1:]
                    class_file = class_file[0:class_file.__len__() - extension_class.__len__()]
                    controller_file_class = controller_file[0:controller_file.__len__() - extension.__len__()]
                    if class_file == controller_file_class:
                        __controllers__[__controllers__.__len__() - 1].app_dir = os.sep.join([path_to_app_dir,item])
                        controller_instance.app_dir = os.sep.join([path_to_app_dir,item])
                        controller_instance.host_dir = app_settings.host_dir
                        controller_instance.app_name = app_settings.app_name
                        controller_instance.on_authenticate = app_settings.on_authenticate
                        controller_instance.rel_login_url = app_settings.rel_login_url
                        controller_instance.settings = app_settings
                        controller_instance.param_names = __controllers__[__controllers__.__len__()-1].params
                        print controller_instance.url
                        print inspect.getfile(controller_instance.__class__)

                        from . controllers import Res
                        controller_instance.res = Res(app_settings.on_get_language_resource_item,controller_instance.app_name,controller_instance.template)
                    else:
                        print "uncontroller file {0}".format(
                            controller_file
                        )
                    __controllert_url_build_cache__.update({
                        controller_file:controller_instance
                    })

            """
            # self.controllerClass()
            if self.instance.app_name==None:
                raise Exception("{0} do not have 'app_name'".format(self.controllerClass))
            if self.instance.app_dir==None:
                raise Exception("{0} do not have 'app_dir'".format(self.controllerClass))
            """
            # x=1
    ret_url_patterns = __create__(urlpatterns)
    return ret_url_patterns


def debugTemplate(x):
    from xdj.middle_ware import GlobalRequestMiddleware
    request = GlobalRequestMiddleware.get_current_request()
    pass


def apply_context(context):
    from xdj.middle_ware import GlobalRequestMiddleware
    from django.shortcuts import redirect
    from django.template.context_processors import csrf
    from django.conf import settings


    def res(key,value=None):
        if value == None:
            value = key
        request = GlobalRequestMiddleware.get_current_request()
        from xdj import languages
        return languages.get_item(request.LANGUAGE_CODE, "_", "_", key, value)

    # context._data.update({"res": res})
    # context.res = res
    context.res = res
    context.request = GlobalRequestMiddleware.get_current_request()
    if not context.request:
        context.request = context.context._data.get('request')
    request = context.request

    context.currentUrl = request.build_absolute_uri().split("?")[0]
    context.absUrl = context.currentUrl[0:context.currentUrl.__len__() - request.path.__len__()]
    context.appUrl = context.absUrl
    context.static = context.appUrl + "/static"
    context.redirect = redirect

    context.user = request.user
    context.csrf_token = csrf(request)["csrf_token"]
    context.settings = settings
    # context._data["res"] = res
    # context["self"].context._data["res"] = res


class Handler(object):

    def from_json(self,txt):
        from xdj import JSON
        return JSON.from_json(txt)

    def __init__(self,model):
        self.model = model
    def OnBeforeHandler(self,model):
        pass
    def OnAfterHandler(self,model):
        pass


def clear_language_cache():
    from xdj.controllers import clear_language_cache
    clear_language_cache()


def find_controller_by_path(path_to_find):
    global __controlers_hash_vert__
    if not __controlers_hash_vert__:
        __controlers_hash_vert__ = {}
    return [k for k,v in __controlers_hash_vert__.items() if k.lower().count(path_to_find.lower())>0]


def get_hash_controller(controller_path):
    global __controlers_hash_vert__
    if not __controlers_hash_vert__:
        __controlers_hash_vert__ = {}
    ret = __controlers_hash_vert__.get(controller_path,None)
    if ret:
        return ret.get('controller_id',None)


def get_controller_by_id(controller_id):
    global __controlers_hash__
    if not __controlers_hash__:
        __controlers_hash__ = {}
    ret = __controlers_hash__.get(controller_id,None)
    if not ret:
        return  None
    else:
        return ret.get('instance',None)





