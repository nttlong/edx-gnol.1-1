from xdj_apps.xmcs.controllers.commons.edx_controller import EdxController
import xdj
@xdj.Controller(
    url="course_students/(?P<course_key_string>[^/+]+(/|\+)[^/+]+(/|\+)[^/?]+)",
    replace_url=r"^course_info/(?P<course_key_string>[^/+]+(/|\+)[^/+]+(/|\+)[^/?]+)$",
    template="xdj-htmls/course_students.html"
)
class CourseStudentsController(EdxController):
    def on_get(self,model):
        self.apply_course_context(model.params.course_key_string,model)
        return self.render(model)
    def loadStudents(self,model):
        from xdj_sql import Fields, qr
        from student.models import CourseEnrollment
        course_id = self.get_course_id_from_text(model.params.course_key_string)
        x = qr(CourseEnrollment).where((Fields.course_id == course_id) & (Fields.user_id!=model.user.id))
        x.select_related(Fields.user)
        x.select(
            Fields.user.username >> Fields.username,
            Fields.user.email >> Fields.email,
            Fields.user.first_name >> Fields.first_name,
            Fields.user.last_name >> Fields.last_name
        )
        x.select(Fields.created)
        x.sort(-Fields.created)
        ret = x.get_page(50,0)
        for x in ret.items:
            x["img"] = self.get_user_profile_img_url_by_username(x["username"])
        return ret

