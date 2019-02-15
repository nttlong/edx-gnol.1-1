import xdj
@xdj.Controller(
    template="xdj-htmls/course_jump.html",
    url="jump",
    check_url=r"^courses/(?P<course_id>[^/+]+(/|\+)[^/+]+(/|\+)[^/?]+)/jump_to/(?P<location>.*)$"
)
class CourseJumpController(xdj.BaseController):
    def on_get(self,model):
        pass