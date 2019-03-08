class dobject(object):
    def __init__(self,*args,**kwargs):
        def feed_data(data):
            if isinstance(data,dobject):
                data =data.__dict__
            for k,v in data.items():
                    if isinstance(v,dict):
                        self.__dict__.update({
                            k:dobject(v)
                        })
                    elif isinstance(v,dobject):
                        self.__dict__.update({
                            k: v
                        })

                    elif isinstance(v,list):
                        lst =[]
                        for item in v:
                            lst.append(dobject(item))
                        self.__dict__.update({
                            k:lst
                        })
                    else:
                        self.__dict__.update({
                            k:v
                        })
        if args.__len__()==0:
            feed_data(kwargs)
        else:
            feed_data(args[0])


