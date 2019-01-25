
class __fields__(object):

    def __getattr__(self, item):
        return __field__(item)

    def get(self, x):
        from django.db.models.fields import DeferredAttribute
        if isinstance(x,DeferredAttribute):
            return __fields__(x.field_name)



class __field__(object):

    def __getattr__(self, item):
        return __field__(self.__f_name__+ "__" + item)

    def __init__(self, name):
        self.__f_name__ = name
        self.__alias__ = None
        self.__expr__ = None

    def __eq__(self, other):
        from django.db.models import Q
        expr = {
            self.__f_name__:other
        }
        self.__expr__= Q(**expr)
        return self

    def __ne__(self, other):
        from django.db.models import Q
        expr = {
            self.__f_name__: other
        }
        self.__expr__ = ~Q(**expr)
        return self

    def __and__(self, other):
        from django.db.models import Q
        if isinstance(other,__field__):
            self.__expr__ = self.__expr__ & other.__expr__
        else:
            raise Exception("This operator just support with {0}".format(type(other)))
        return self

    def __invert__(self):
        from django.db.models import Q
        self.__expr__ = ~ (self.__expr__)
        return self

    def __gt__(self, other):
        from django.db.models import Q
        expr = {
            "{0}__gt".format(self.__f_name__): other
        }
        self.__expr__ = Q(**expr)
        return self

    def __ge__(self, other):
        from django.db.models import Q
        expr = {
            "{0}__gte".format(self.__f_name__): other
        }
        self.__expr__ = Q(**expr)
        return self

    def __lt__(self, other):
        from django.db.models import Q
        expr = {
            "{0}__lt".format(self.__f_name__): other
        }
        self.__expr__ = Q(**expr)
        return self

    def __le__(self, other):
        from django.db.models import Q
        expr = {
            "{0}__lte".format(self.__f_name__): other
        }
        self.__expr__ = Q(**expr)
        return self

    def __lshift__(self, other):
        from django.db.models.functions import Concat
        from . import __express_field__
        if isinstance(other,__field__):
            other.__alias__ = self.__f_name__
            return other
        elif isinstance(other,Concat):
            return __express_field__(self.__f_name__,other)
        elif type(other).__module__ == "django.db.models.functions.base":
            return __express_field__(self.__f_name__, other)
        else:
            raise Exception("Can not set alias with {0}".format(type(other)))

    def __add__(self, other):
        from django.db.models import Value
        from django.db.models import F
        if isinstance(other, __field__):
            if not self.__expr__:
                self.__expr__ = F(self.__f_name__) + F(other.__f_name__)
                return self
            else:
                self.__expr__ = self.__expr__ + F(other.__f_name__)
                return self
        else:
            if not self.__expr__:
                self.__expr__ = F(self.__f_name__) + Value(other)
                return self
            else:
                self.__expr__ = self.__expr__ + Value(other)
                return self

    def __mul__(self, other):
        from django.db.models import Value
        from django.db.models import F
        if isinstance(other, __field__):
            if not self.__expr__:
                self.__expr__ = F(self.__f_name__) * F(other.__f_name__)
                return self
            else:
                self.__expr__ = self.__expr__ * F(other.__f_name__)
                return self
        else:
            if not self.__expr__:
                self.__expr__ = F(self.__f_name__) * Value(other)
                return self
            else:
                self.__expr__ = self.__expr__ * Value(other)
                return self

    def __div__(self, other):
        from django.db.models import Value
        from django.db.models import F
        if isinstance(other, __field__):
            if not self.__expr__:
                self.__expr__ = F(self.__f_name__) / F(other.__f_name__)
                return self
            else:
                self.__expr__ = self.__expr__ / F(other.__f_name__)
                return self
        else:
            if not self.__expr__:
                self.__expr__ = F(self.__f_name__) / Value(other)
                return self
            else:
                self.__expr__ = self.__expr__ / Value(other)
                return self

    def __mod__(self, other):
        from django.db.models import Value
        from django.db.models import F
        if isinstance(other, __field__):
            if not self.__expr__:
                self.__expr__ = F(self.__f_name__) % F(other.__f_name__)
                return self
            else:
                self.__expr__ = self.__expr__ % F(other.__f_name__)
                return self
        else:
            if not self.__expr__:
                self.__expr__ = F(self.__f_name__) % Value(other)
                return self
            else:
                self.__expr__ = self.__expr__ % Value(other)
                return self


Fields = __fields__()



