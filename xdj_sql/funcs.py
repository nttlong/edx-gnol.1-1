def concat(*args,**kwargs):
    from . utils import __field__

    from django.db.models import Value
    from django.db.models.functions import Concat
    params = []
    if args.__len__()>0:
        for x in args:
            if isinstance(x, __field__):
                params.append(x.__f_name__)
            elif type(x) in [str, unicode]:
                params.append(Value(x))
    return Concat(*params)

def call(fn,*args,**kwargs):
    from .utils import __field__
    from django.db.models import Value,F
    x = []
    for item in args:
        if isinstance(item,__field__):
            x.append(F( item.__f_name__))
        elif type(item).__module__ == "django.db.models.functions.base":
            x.append(item)
        else:
            x.append(Value(item))
    return fn(*x)