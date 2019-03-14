app_name = "resource_manager"
host_dir = "resource_manager"
rel_login_url = ""
def on_authenticate(sender):
    return True
def on_get_language_resource_item(language,appname,view,key,value):
    from xdj import languages
    return languages.get_item(language,appname,view,key,value)
