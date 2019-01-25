def table(table_name):
    ret = __table_wrapper__(table_name)
    return ret.wrapper

class __table_wrapper__(object):
    def __init__(self,table_name):
        self.__table_name__ = table_name
    def wrapper(self,*args,**kwargs):
        from django.db import models as dj_models
        if not issubclass(args[0],Base):
            raise Exception("{0} is not sub class of {1}".format(
                args[0],
                Base
            ))
        _fields = {}
        for x in args[0].__dict__.items():
            if x[0].__len__() > 2 and x[0][0:2] != "__" and x[0][x[0].__len__()-2:x[0].__len__()]:
                _fields.update({
                    x[0]:x[1]
                })
            else:
                _fields.update({
                    x[0]: x[1]
                })
        from .utils import create_model
        model = create_model(self.__table_name__, _fields, app_label="")
        super(type(args[0]), args[0]).__init__()



class Base(object):
    def __init__(self):
        pass


class BaseField(object):
    def __init__(self,name=None,unique=False,max_len=255):
        self.name = name
        self.unique = unique
        self.max_len = max_len


class TextField(BaseField):
    def __init__(self,name=None,max_len=45,unique=False):
        super(TextField,self).__init__(name,unique,max_len)
class fields():
    @staticmethod
    def text(name=None,max_len=45,unique=False):
        return TextField(name,max_len,unique)


