def model(*args,**kwargs):
    def wrapper(*args,**kwargs):
        from qres.filter import Fields
        return Fields()
    return wrapper