import xdj
@xdj.Controller(
    url="courseware/team/(?P<course_key_string>([^/]+/[^/]+/[^/]+|[^/:]+:[^/+]+\+[^/+]+(\+[^/]+)?))(?:/(?P<email>.+))?",
    template="courseware_team.html"
)
class CoursewareTeamController(xdj.BaseController):
    def on_get(self,model):
        return self.render(model)

    def loadStaffs(self,model):
        from django.db.models import Q
        from student.models import CourseAccessRole
        from opaque_keys.edx.keys import CourseKey
        course_id = CourseKey.from_string(model.params.course_key_string)
        filter = Q(course_id=course_id) & (~Q(user_id=model.user.id))
        staffs = CourseAccessRole.objects.filter(filter).all()
        total = CourseAccessRole.objects.filter(filter).count()

        items = []

        for staff in staffs:
            items.append(dict(
                username = staff.user.username
            ))


        return dict(
            items = items,
            total =total
        )
