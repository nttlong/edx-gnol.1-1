def search(field,value):
    from qres.filter import Fields
    if isinstance(field,Fields):
        field.__expr__ = {
            "match": {
                field.__name__: {
                    "query": value
                }
            }
        }
    return field

def seach_all(field,value):
    from qres.filter import Fields
    if isinstance(field, Fields):
        field.__expr__ = {
            "match": {
                field.__name__+"._all": {
                    "query": value
                }
            }
        }
    return field
