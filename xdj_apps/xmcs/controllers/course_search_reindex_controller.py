import xdj
@xdj.Controller(
    url="course/(?P<course_key_string>[^/+]+(/|\+)[^/+]+(/|\+)[^/?]+)/search_reindex?",
    template="course_search_reindex.html",
    check_url=r"^course/(?P<course_key_string>[^/+]+(/|\+)[^/+]+(/|\+)[^/?]+)/search_reindex?$"
)
class CourseSearchReindex(xdj.BaseController):
    def on_get(self,model):
        pass