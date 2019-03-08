__download_info_cache__ = None


def create_new_download(filename):
    from django.conf import settings
    from . download_info import DownloadInfo
    import os
    from uuid import uuid4
    dirname = uuid4().__str__()
    folderpath = os.sep.join([settings.TEMP_DOWNLOAD_DIR,dirname])
    if not os.path.exists(folderpath):
        os.makedirs(folderpath)
    filepath = os.sep.join([folderpath,filename])
    return DownloadInfo(
        dir_path = folderpath,
        file_path = filepath,
        file_name = filename,
        token = dirname
    )


def get_download_link(url,info):
    global  __download_info_cache__
    if not __download_info_cache__:
        __download_info_cache__ = {}
    from .download_info import DownloadInfo
    if not isinstance(info, DownloadInfo):
        raise Exception("parameter must be {0}".format(DownloadInfo))
    __download_info_cache__.update({
        info.token:info
    })
    return url + "/" + info.token


def get_download_info(token):
    global __download_info_cache__
    if not __download_info_cache__:
        __download_info_cache__ = {}
    return __download_info_cache__.get(token, None)