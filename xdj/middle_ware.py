import thread
from django.conf import settings
class GlobalRequestMiddleware(object):
    _threadmap = {}

    @classmethod
    def get_current_request(cls):
        import threading
        if hasattr(threading.current_thread(),"request"):
            return threading.current_thread().request
        else:
            return None

    def process_request(self, request):
        import threading
        threading.current_thread().request = request

        if request.path.find("/static/")>-1:
            return None

        class RES(object):
            def __rshift__(self, other):
                return  other
            def res(key, value=None):
                if value == None:
                    value = key
                request = GlobalRequestMiddleware.get_current_request()
                from xdj import languages
                return languages.get_item(request.LANGUAGE_CODE, "_", "_", key, value)
        request.xdj_res = RES()
        request.TEST="XXXXX"

    def process_exception(self, request, exception):
        try:
            del self._threadmap[thread.get_ident()]
        except KeyError:
            pass

    def process_response(self, request, response):
        try:
            del self._threadmap[thread.get_ident()]
        except KeyError:
            pass
        return response