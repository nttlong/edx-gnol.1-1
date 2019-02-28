def single(*args,**kwargs):
    def wrapper(*args1,**kwargsk):
        return args1[0]()
    return wrapper
def get_join_table(*args,**kwargs):
    def wrapper(*args1,**kwargsk):
        return args1[0]()
    return wrapper
