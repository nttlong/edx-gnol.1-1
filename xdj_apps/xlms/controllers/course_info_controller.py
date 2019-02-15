from xdj_apps.xlms.controllers.commons import edx_controller
import xdj
@xdj.Controller(
    url="course_info",
    template="course_info.html",
    check_url=r"^courses/(?P<course_id>[^/+]+(/|\+)[^/+]+(/|\+)[^/?]+)/course/"
)
class CourseInfoCopntroller(xdj.BaseController):
    def on_get(self,model):
        pass