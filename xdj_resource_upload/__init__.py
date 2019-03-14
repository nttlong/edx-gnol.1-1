__upload_info__ = None


class UploadInfo(object):

    def __init__(self):
        from uuid import uuid4
        from django.conf import settings
        import os
        self.token = uuid4().__str__()
        self.dir_name = self.token
        self.folder_path = os.sep.join([settings.TEMP_UPLOAD_DIR, self.dir_name])
        self.origin_file_name = None




def get_upload_info(token):
    global __upload_info__
    if not __upload_info__:
        __upload_info__ = {}
    return __upload_info__.get(token,None)

def create_upload():
    import os
    global __upload_info__
    if not __upload_info__:
        __upload_info__ = {}
    ret = UploadInfo()
    from django.conf import settings
    # import os
    # from uuid import uuid4
    # dir_name = uuid4().__str__()
    # folder_path = os.sep.join([settings.TEMP_UPLOAD_DIR, dir_name])
    if not os.path.exists(settings.TEMP_UPLOAD_DIR):
        os.makedirs(settings.TEMP_UPLOAD_DIR)
    #
    # ret = UploadInfo(dir_name, folder_path)
    __upload_info__.update({
        ret.token: ret
    })
    return ret


def save_upload(token,origin_file_name,buffer):
    upload_info = get_upload_info(token)
    import os
    if not isinstance(upload_info,UploadInfo):
        raise Exception("upload_info must be {0}".format(UploadInfo))
    if not os.path.exists(upload_info.folder_path):
        os.makedirs(upload_info.folder_path)
    dir_name = upload_info.token

    file_path = os.sep.join([upload_info.folder_path, origin_file_name])
    if not os.path.exists(file_path):
        with open(file_path, 'wb') as f:
            f.write(buffer)
    else:
        with open(file_path, 'ab') as f:
            f.write(buffer)
