#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
 ____     _  ____  _      _____ ____
/  _ \   / |/  _ \/ \  /|/  __//  _ \
| | \|   | || / \|| |\ ||| |  _| / \|
| |_/|/\_| || |-||| | \||| |_//| \_/|
\____/\____/\_/ \|\_/  \|\____\\____/


"""
__lang_cache__ = None
__build_cached__ = None
import threading
lock = threading.Lock()
def clear_language_cache():
    global __lang_cache__
    __lang_cache__ = {}


class Res(object):
    """
    This class serve for language resource item getter with three level
    1- Global:The item apply at global could be access for all application
    2- Application:The item apply at application could be access for all view in application
    3- View:The item apply at view could be access for specific view in application

    Lớp này phục vụ cho trình thu thập mục tài nguyên ngôn ngữ với ba cấp độ
     1- Toàn cục: Mục áp dụng tại toàn cầu có thể được truy cập cho tất cả các ứng dụng
     2- Ứng dụng: Mục áp dụng tại ứng dụng có thể được truy cập cho tất cả các chế độ xem trong ứng dụng
     3- Chế độ tính năng: Mục áp dụng tại chế độ xem có thể được truy cập để xem cụ thể trong ứng dụng
    """
    def __init__(self,on_get_lang_item,app_name,view_name):
        if app_name==None:
            raise Exception("app_name can not be None")
        self.app_name=app_name
        self.view_name=view_name
        self.on_get_lang_item=on_get_lang_item

    def g(self,key,value=None):
        """
        Get global language item resource
        :param key:
        :param value:
        :return:
        """
        global __lang_cache__
        if __lang_cache__ == None:
            __lang_cache__ = {}
        from django.utils import translation

        if value==None:
            key = key.rstrip(" ").lstrip(" ")
            value=key
        key=key.lower()
        _key="lang={0};app={1};view={2};key={3}".format(
            translation.get_language(),
            "-",
            "-",
            key
        )
        if not __lang_cache__.has_key(_key):
            try:
                lock.acquire()
                __lang_cache__.update({_key:self.on_get_lang_item(translation.get_language(),"-","-",key,value)})
                if type(__lang_cache__[_key]) not in [str,unicode]:
                    raise Exception("{0} in {1} must return 'str' or 'unicode' value".format(
                        "on_get_language_resource_item",
                        self.on_get_lang_item.func_code.co_filename
                    ))
                lock.release()
                return __lang_cache__[_key]
            except Exception as ex:
                lock.release()
                raise ex
        else:
            return __lang_cache__[_key]

    def a(self,key,value=None):
        """
        Get application language resource
        :param key:
        :param value:
        :return:
        """

        global __lang_cache__
        if __lang_cache__ == None:
            __lang_cache__ = {}
        from django.utils import translation

        if value == None:
            key = key.rstrip(" ").lstrip(" ")
            value = key
        key = key.lower()
        _key = "lang={0};app={1};view={2};key={3}".format(
            translation.get_language(),
            self.app_name,
            "-",
            key
        )
        if not __lang_cache__.has_key(_key):
            try:
                lock.acquire()
                __lang_cache__.update({_key: self.on_get_lang_item(translation.get_language(), self.app_name, "-", key, value)})
                if type(__lang_cache__[_key]) not in [str,unicode]:
                    raise Exception("{0} in {1} must return 'str' or 'unicode' value".format(
                        "on_get_language_resource_item",
                        self.on_get_lang_item.func_code.co_filename
                    ))
                lock.release()
                return __lang_cache__[_key]
            except Exception as ex:
                lock.release()
                raise ex
        else:
            return __lang_cache__[_key]

    def v(self,key,value=None):
        """
        Get View Item reources
        :param key:
        :param value:
        :return:
        """

        global __lang_cache__
        if __lang_cache__ == None:
            __lang_cache__ = {}

        from django.utils import translation
        if value == None:
            key = key.rstrip(" ").lstrip(" ")
            value = key
        key = key.lower()
        _key = "lang={0};app={1};view={2};key={3}".format(
            translation.get_language(),
            self.app_name,
            self.view_name,
            key
        )
        if not __lang_cache__.has_key(_key):
            try:
                lock.acquire()
                __lang_cache__.update({_key:self.on_get_lang_item(translation.get_language(), self.app_name, self.view_name, key, value)})
                if type(__lang_cache__[_key]) not in [str,unicode]:
                    raise Exception("{0} in {1} must return 'str' or 'unicode' value".format(
                        "on_get_language_resource_item",
                        self.on_get_lang_item.func_code.co_filename
                    ))

                lock.release()
                return __lang_cache__[_key]
            except Exception as ex:
                lock.release()
                raise ex
        else:
            return __lang_cache__[_key]

    def __floordiv__(self, other):
        """
        Get global application resource at html template can be use _//"My label"
        :param other:
        :return:
        """
        if isinstance(other,tuple):
            if other.__len__()>1:
                return self.g(other[0],other[1])
            elif other.__len__()>0:
                return self.g(other[0])
        elif type(other) in [str,unicode]:
            return  self.g(other)

    def __gt__(self, other):
        """
        Get Language resource at view at html template can be use _>"My Lable"
        :param other:
        :return:
        """
        if isinstance(other,tuple):
            if other.__len__()>1:
                return self.v(other[0],other[1])
            elif other.__len__()>0:
                return self.v(other[0])
        elif type(other) in [str,unicode]:
            return  self.v(other)

    def __rshift__(self, other):
        """
        Get application resource at template can be use _>>"My lable"
        :param other:
        :return:
        """
        if isinstance(other,tuple):
            if other.__len__()>1:
                return self.a(other[0],other[1])
            elif other.__len__()>0:
                return self.a(other[0])
        elif type(other) in [str,unicode]:
            return  self.a(other)


class PostData(object):
    pass


class ModelUser(object):
    def __init__(self):
        self.username=""
        self.is_staff= False
        self.is_superuser= False
        self.is_active= False

    def is_anonymous(self):
        return


def to_json(data):
    import xdj.JSON
    return xdj.JSON.to_json(data)


class Model(object):
    """
    The model definition for all template rendering
    Định nghĩa mô hình cho tất cả kết xuất mẫu
    """
    def __init__(self):
        from django.utils.translation import ugettext
        from xdj import get_hash_controller
        import urllib
        self.request = None
        self.response = None
        self.absUrl = None
        self.appUrl = None
        self.static = None
        self.redirect = None
        self.user= ModelUser()
        self.csrf_token = None
        self.post_data= PostData()
        self.settings=None
        self.to_json= to_json
        self.escape = urllib.quote_plus
        self.djRes = ugettext
        self.get_hash_controller=get_hash_controller

    def debugger(self):
        print "debugger"


class __controller_wrapper__(object):
    """
    Controller wrapper class. Wrap and return single instance of Controller
    Controller wrapper class. Gói và trả lại một thể hiện của Bộ điều khiển
    """
    def __init__(self,*args,**kwargs):
        self.url=kwargs["url"]
        self.template=kwargs["template"]
        self.controllerClass=None
        self.params = kwargs.get("params",[])
        self.replace_url = kwargs.get("replace_url",None)
        self.check_url = kwargs.get("check_url", None)

    def wrapper(self,*args,**kwargs):
        import xdj
        if issubclass(args[0],BaseController):
            self.controllerClass=args[0]
            self.instance = self.controllerClass.__new__(self.controllerClass)
            # self.instance =BaseController.__new__(self.controllerClass)
            super(self.controllerClass, self.instance).__init__()
            self.instance.__init__()
            self.instance.url=self.url
            self.instance.template = self.template
            self.instance.sub_pages = [v for k, v in self.controllerClass.__dict__.items() if hasattr(v, "is_sub_page")]
            self.instance.replace_url = self.replace_url
            self.instance.check_url = self.check_url
            for item in self.instance.sub_pages:
                item.owner=self.instance
                class cls_exec_request(object):
                    def __init__(self,obj):
                        self.obj=obj
                    def exec_request_get(self,request,*args,**kwargs):
                        model = self.obj.owner.create_client_model(request)
                        model.params = xdj.dobject(kwargs)
                        def do_rendert(model):
                            return self.obj.owner.render_with_template(model, self.obj.template)
                        self.obj.render = do_rendert
                        if request.method == "GET":
                            if hasattr(self.obj,"on_get"):
                                return  self.obj.on_get(model)
                            else:
                                return self.obj.owner.render_with_template(model,self.obj.template)
                        else:
                            if request.META.has_key("HTTP_AJAX_POST"):
                                exec_method = request.META["HTTP_AJAX_POST"]
                                try:
                                    from xdj import JSON
                                    from django.http import HttpResponse
                                    from exceptions import ValueError
                                    try:
                                        model.post_data.__dict__.update(JSON.from_json(request.body))
                                    except ValueError as ex:
                                        pass
                                    method = getattr(self.obj, exec_method)
                                    ret = method(model)
                                    json_data = JSON.to_json(ret)
                                    return HttpResponse(json_data, content_type="application/json")
                                except AttributeError as ex:
                                    if not hasattr(self.obj,exec_method):
                                        import inspect
                                        code_file = inspect.getfile(self.obj.__class__)
                                        raise Exception("{0} was not found in {1}".format(
                                            exec_method,
                                            code_file
                                        ))
                                    else:
                                        raise ex



                item.exec_request_get=cls_exec_request(item).exec_request_get


            xdj.__controllers__.append(self)
        else:
            raise Exception("{0} mus be inherit from {1}".format(self.controllerClass,BaseController))


def __create_model_from_request__(request, rel_login_url, res,host_dir, on_authenticate, settings):
    """
    Create basic model before process a request in controller
    Tạo mô hình cơ bản trước khi xử lý yêu cầu trong bộ điều khiển
    :param request:
    :param rel_login_url:
    :param res:
    :param host_dir:
    :param on_authenticate:
    :param settings:
    :return:
    """


    from django.shortcuts import redirect
    from django.template.context_processors import csrf

    model = Model()
    model.request = request
    model.currentUrl = request.build_absolute_uri().split("?")[0]
    model.absUrl = model.currentUrl[0:model.currentUrl.__len__() - request.path.__len__()]
    model.appUrl = model.absUrl + "/" + host_dir
    model.static = model.appUrl + "/static"
    model.redirect = redirect
    model._ = res
    model.user = request.user
    model.csrf_token = csrf(request)["csrf_token"]
    model.settings = settings

    return model


def Controller(*args, **kwargs):
    """
    Create an controller from class
    :param args:
    :param kwargs:
    :return:
    """
    ret = __controller_wrapper__(*args, **kwargs)
    return ret.wrapper


class BaseController(object):
    """
    Every controller class in xdj must inherit from this class
    Mỗi lớp trình điều khiển trong xdj phải kế thừa từ lớp này
    """
    def __init__(self):
        self.app_name = None
        self.app_dir = None
        self.url = None
        self.template = None
        self.on_get_language_resource_item=None
        self.on_authenticate = None
        self.rel_login_url = None
        self.params = None

    def create_client_model(self, request):
        model = __create_model_from_request__(
            request, self.rel_login_url, self.res, self.host_dir, self.on_authenticate, self.settings
        )
        return model

    def __view_exec__(self,request,*args,**kwargs):
        import xdj
        from django.http import HttpResponse
        from django.shortcuts import redirect
        model = self.create_client_model(request)
        model.params = xdj.dobject(*args, **kwargs)
        if request.build_absolute_uri(self.rel_login_url).lower() != model.currentUrl.lower():
            if not self.on_authenticate(model):
                return redirect(model.appUrl + "/" + self.rel_login_url)
        if request.method == 'GET':
            return self.on_get(model)
        else:
            if not request.META.has_key("HTTP_AJAX_POST"):
                if request._get_post()!={}:
                    model.post_data.__dict__.update(
                        request._get_post()
                    )
                elif request.body and request.body != "":
                    from xdj import JSON
                    model.post_data.__dict__.update(
                        JSON.from_json(request.body)
                    )


                return self.on_post(model)
            else:
                try:
                    from xdj import JSON
                    if request.body.__len__()>0:
                        client_data = JSON.from_json(request.body)
                        if isinstance(client_data,list):
                            model.post_data.__dict__.update({
                                "items":client_data
                            })
                        else:
                            model.post_data.__dict__.update(client_data)
                    method_name = request.META["HTTP_AJAX_POST"]
                    method_items = method_name.split('.')
                    obj= self
                    for i in range(0,method_items.__len__()-1):
                        obj=getattr(obj,method_items[i])
                    method_exec = getattr(obj,method_items[method_items.__len__()-1])
                    from xdj.controller_privileges import Action
                    ret = None
                    if isinstance(method_exec, Action):
                        ret = method_exec.fn(obj,model)
                    else:
                        # from django.http import HttpResponseForbidden
                        # return HttpResponseForbidden()
                        ret = method_exec(model)
                    from util.json_request import JsonResponse
                    if type(ret) == JsonResponse:
                        return ret
                    json_data = JSON.to_json(ret)


                    return HttpResponse(json_data, content_type="application/json")
                except AttributeError as ex:
                    if not hasattr(obj,method_items[method_items.__len__()-1]):
                        raise Exception("{0} was not found in {1} or error '{2}'".format(
                            request.META["HTTP_AJAX_POST"],
                            self.on_get.im_func.func_code.co_filename,
                            ex.message
                        ))
                    else:
                        raise ex

    def render_with_template(self,model,template):
        if isinstance(model,Model):
            from django.http import HttpResponse
            import os
            from mako.lookup import TemplateLookup
            viewpath=os.sep.join([self.app_dir,"views"])

            ret_res = None
            mylookup = TemplateLookup(directories=[viewpath],
                                      default_filters=['decode.utf8'],
                                      input_encoding='utf-8',
                                      output_encoding='utf-8',
                                      encoding_errors='replace',

                                      )
            d=model.__dict__
            ret_res = mylookup.get_template(template).render(**d)
            return HttpResponse(ret_res)
        else:
            raise Exception("{0} is not instance of {1}".format(
                type(model),
                Model
            ))

    def render(self, model):
        """
        Get html content by render tempate and a model
        :param model:
        :return:
        """
        return self.render_with_template(model,self.template)

