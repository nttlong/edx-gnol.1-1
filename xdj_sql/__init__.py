#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
This package is django model queryable. By according django model the package will help us build a readable query like bellow:
    qr(model).select(fields.fullname << fields.code+" "+fields.name, fields.age)
    .where(fields.age>23)

"""

from . import utils
Fields = utils.Fields
from  . singeton import single, get_join_table
from . import funcs as Funcs


class __alias_field__(object):

    def __init__(self, expr):
        self.__expr__ = expr



class __express_field__(object):

    def __init__(self,name, expr):
        self.__expr__ = expr
        self.__f_name__ = name


class qr(object):

    def __init__(self, model = None):
        from django.db.models import Model
        from . models import Base as B
        self.__xdj_model__ = None
        if isinstance(model, B):
            self.__model__ = model.__model__
            self.__xdj_model__ = model
        elif issubclass(model, Model):
            self.__model__ = model
        else:
            raise Exception("'model' is invalid. The model must be {0} or {1}".format(
                Model,B
            ))
        self.__fields__ = {}
        self.__where__ = None
        self.__select_related__ = []
        self.__sort__ = []

    def select(self,*args,**kwargs):
        from django.db.models.fields import DeferredAttribute
        from . utils import __field__, check_is_str
        from . import __express_field__

        if args.__len__()>0:
            for x in args:
                if isinstance(x,DeferredAttribute):
                    self.__fields__.update({
                        x.field_name: 1
                    })
                elif check_is_str(x):
                    self.__fields__.update({
                        x:1
                    })
                elif isinstance(x,__express_field__):
                    self.__fields__.update({
                        x.__f_name__: x
                    })
                elif isinstance(x, __field__):
                    if x.__alias__:
                        if not x.__expr__:
                            self.__fields__.update({
                                x.__f_name__: __alias_field__(x.__alias__)
                            })
                        else:
                            self.__fields__.update({
                                x.__f_name__: __express_field__(x.__f_name__,x.__expr__)
                            })
                    else:
                        self.__fields__.update({
                            x.__f_name__: 1
                        })
        return self

    def select_related(self,*args,**kwargs):
        from django.db.models import Model
        from xdj_sql.utils import __field__
        if args.__len__()>0:
            for x in args:
                try:
                    if type(x) in [str,unicode]:
                        self.__select_related__.append(
                            x
                        )
                    elif issubclass(x,Model):
                        self.__select_related__.append(
                            x.__name__
                        )


                except TypeError as ex:
                    self.__select_related__.append(
                        x.__f_name__
                    )
        # self.__model__ = self.__model__.objects.get_queryset()

        return self

    def execute(self,model =None):
        from django.db.models import Model,F
        from xdj_sql import __express_field__
        from xdj_sql.utils import __field__

        if model and not issubclass(model,Model):
            raise Exception("Invalid model. The model must be inherit from {0}".format(
                Model
            ))
        if not model and not self.__model__:
            raise Exception("'model' must be set at __init__ or execute")
        if model:
            self.__model__ = model
        qr_set = self.__model__.objects
        if self.__select_related__.__len__()>0:
            for x in self.__select_related__:
                qr_set.select_related(x)
        if self.__where__:
            qr_set = qr_set.filter(self.__where__)

        selected_fields = []
        alias_fields = []
        for k, v in self.__fields__.items():
            if isinstance(v, __alias_field__):
                alias_fields.append((v.__expr__,F(k)))
                # selected_fields.append(k)
            elif isinstance(v, __express_field__):
                alias_fields.append((k, v.__expr__))
            elif isinstance(v, __field__):
                if not v.__expr__:
                    selected_fields.append(k)
                else:
                    alias_fields.append((k, v.__expr__))
            else:
                selected_fields.append(k)

        # selected_fields = [k for k, v in self.__fields__.items()]

        if selected_fields.__len__() > 0:
            qr_set = qr_set.values(*selected_fields)
        if alias_fields.__len__() > 0:
            _annotate = {}
            for x in alias_fields:
                _annotate.update({
                    x[0]: x[1]
                })
            qr_set = qr_set.annotate(**_annotate)
            __selected_fields__ = [x[0] for x in alias_fields]
            __selected_fields__.extend(selected_fields)
            qr_set = qr_set.values(*__selected_fields__)
        if self.__sort__.__len__() > 0:
            _sort_ = []
            for x in self.__sort__:
                if x["asc"]:
                    _sort_.append(x["field"])
                    # qr_set = qr_set.order_by(x["field"])
                else:
                    _sort_.append("-" + x["field"])
                    # qr_set = qr_set.order_by("-"+x["field"])
            qr_set = qr_set.order_by(*_sort_)
        return qr_set.all()

    def count(self):
        return self.execute().count()

    def limit(self,num):
        return self.execute()[:num]

    def skip(self,num):
        return self.execute()[num:]

    def sort(self,*args,**kwargs):
        from xdj_sql.utils import __field__
        if args.__len__()>0:
            for x in args:
                if isinstance(x,__field__):
                    if x.__sort__ == "desc":
                        self.__sort__.append(dict(
                            field=x.__f_name__,
                            asc = False
                        ))
                    else:
                        self.__sort__.append(dict(
                            field=x.__f_name__,
                            asc= True
                        ))
        return self

    def get_page(self,page_size,page_index):

        total = self.execute().count()
        pages = int(total/page_size)
        if total % page_size >0:
            pages = pages + 1
        items = list(self.execute()[page_size * page_index: page_size])
        return obj_data(dict(
            total=total,
            pages = pages,
            items = items,
            size =page_size,
            index =page_index
        ))

    def first(self):
        return self.execute().first()
    def __iter__(self):
        return self.execute().all()

    def all(self):
        return self.execute().all()

    def where(self, expr):
        from .utils import __field__
        if isinstance(expr, __field__):
            self.__where__ = expr.__expr__
        else:
            raise Exception("Invalid data type of argument one\n"
                            "Example:\n"
                            "from xdj_sql import Fields\n"
                            "qr.where(Fields.Code=='aaa')")
        return self

    def insert(self,*args,**kwargs):
        from xdj_sql.utils import __field__
        data = {}
        for x in args:
            if isinstance(x,dict):
                for k,v in x.items():
                    data.update({
                        k: v
                    })
        try:
            x = self.__model__.objects.create(**data)
            return x
        except Exception as ex:
            from xdj_sql.error_description import get_error
            ret = get_error(self.__model__._meta.db_table,ex)
            return None, ret

    def update(self,*args,**kwargs):
        from xdj_sql.utils import __field__
        if self.__where__:
            items = self.__model__.objects.filter(self.__where__).all()
            if items.__len__()>0:
                item = items[0]
                for x in args:
                    if isinstance(x,dict):
                        for k,v in x.items():
                            setattr(item, k, v)
                try:
                    item.save()
                except Exception as ex:
                    from xdj_sql.error_description import get_error
                    ret = get_error(self.__model__._meta.db_table, ex)
                    return None, ret
        return item, None

    def join(self,to,local_fields, foreign_fields,null= False, alias=None):
        """
        :param to:
        :param local_fields:
        :param foreign_fields:
        :return:
        """

        """
        Search is existing
        """
        from . import utils
        _to = to
        _foreign_fields = foreign_fields
        _local_fields = local_fields

        if isinstance(local_fields,utils.__field__):
            _local_fields = local_fields.__f_name__
        if isinstance(_foreign_fields,utils.__field__):
            _foreign_fields = _foreign_fields.__f_name__

        if issubclass(type(to),models.Base):
            _to = to.__model__
            if not alias:
                alias = to.__origin_class__.__name__
        if not alias:
            alias = _to.__model__._meta.db_table
        if null:
            alias = "_outer_"+alias
        from django.db.models.base import ModelBase
        if issubclass(type(self.__model__),ModelBase):
            related_models = [x for x in  self.__model__._meta.fields if x.name == alias]
            if related_models.__len__()>0:
                return self


        from django.db import models as dj_models

        fx = dj_models.ForeignKey(
            to=_to,
            to_field=_foreign_fields,
            related_name=_local_fields,
            null= null
        )
        fx.model = self.__model__
        fx.name = alias
        fx.concrete = True
        fx.attname = _local_fields
        fx.column = _local_fields
        if issubclass(type(self.__model__), ModelBase):
            self.__model__._meta.add_field(fx)
        else:
            self.__model__.model._meta.add_field(fx)
        return self

    def left_outer_join(self, to, local_fields,foreign_fields, alias=None):
        return self.join(
            to,local_fields,foreign_fields,True,alias
        )




class obj_data(object):
    def __init__(self,data):
        self.__dict__.update(data)








from . models import table
from . models import fields


class builder():
    @staticmethod
    def query(model):
        return qr(model)
    fields = utils.Fields
    funcs = Funcs
    @staticmethod
    def outer(model):
        if issubclass(type(model),models.Base):
            return getattr(utils.Fields,"_outer_"+model.__origin_class__.__name__)

        return model


