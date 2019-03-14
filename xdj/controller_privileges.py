#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Each action in Xdj controller require a privileges such as : insert, update,delete, import, export or something else
if the method in controller combine with action the client can invoke it
The code file declare method decorator to manage action in controller
------------------------------------------------------
Mỗi action trong controller Xdj yêu cầu một đặc quyền như: chèn, cập nhật, xóa, nhập, xuất hoặc một cái gì đó khác
nếu phương thức trong controller kết hợp với action thì máy khách có thể gọi nó
Tệp mã khai báo decorator cho phương thức để quản lý hành động trong controller
"""


class Action(object):
    def __init__(self,name,fn):
        self.name = name
        self.fn = fn

class Privilges:

    INSERT = "INSERT"
    UPDATE = "UPDATE"
    DELETE = "DELETE"
    IMPORT = "IMPORT"
    EXPORT = "EXPORT"
    VIEW = "VIEW"


def privilege(name):
    def wrapper(*args,**kwargs):
        return Action(name,args[0])
    return wrapper