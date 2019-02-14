from django.core.files.storage import FileSystemStorage
from proxy_storage.storages.base import ProxyStorageBase
from proxy_storage.meta_backends.mongo import MongoMetaBackend
from medxdb import db

class FileSystemProxyStorage(ProxyStorageBase):
    original_storage = FileSystemStorage(location='/tmp/')
    meta_backend = MongoMetaBackend(
        database=db(),
        collection='meta_backend_collection'
    )