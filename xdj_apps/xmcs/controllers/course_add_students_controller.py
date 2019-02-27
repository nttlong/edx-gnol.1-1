import xdj
@xdj.Controller(
    url="course_add_students/(?P<course_key_string>[^/+]+(/|\+)[^/+]+(/|\+)[^/?]+)",
    template="course_invitation.html"
)
class CourseInvitationController(xdj.BaseController):
    def on_get(self,model):
        model.for_inviation =False
        return self.render(model)
    def doSearch(self,model):
        from django.contrib.auth.models import User
        from xdj_apps.xlms.bll.users import get_user_profile_img_url
        from django.db.models.query import Q
        total = 0
        page_size = model.post_data.__dict__.get("pageSize",50)
        page_index = model.post_data.__dict__.get("pageIndex", 0)
        items  = []
        if not hasattr(model.post_data,"value") or model.post_data.value == "":
            total = User.objects.filter(~Q(username=model.user.username)).count()
            users = User.objects.filter(~Q(username=model.user.username)).all()[page_size*page_index:page_size]

        else:
            filter = (Q(username__icontains=model.post_data.value)|Q(email__icontains=model.post_data.value))&(~Q(username=model.user.username))
            total = User.objects.filter(filter).count()
            users = User.objects.filter(filter)[page_size * page_index:page_size]

        for user in users:
            items.append(dict(
                username=user.username,
                email=user.email,
                first_name=user.first_name,
                last_name=user.last_name,
                img_url=get_user_profile_img_url(user)
            ))

        return dict(
            total= total,
            items = items
        )

    def doAddStudents(self,model):
        from student.models import CourseEnrollment
        from opaque_keys.edx.keys import CourseKey
        from django.contrib.auth.models import User
        from datetime import datetime

        course_id = CourseKey.from_string(model.params.course_key_string)
        if hasattr(model.post_data,"students"):
            for student in model.post_data.students:
                user = User.objects.filter(username=student["username"]).get()
                if user:
                    if CourseEnrollment.objects.filter(course_id=course_id, user_id=user.id).count()==0:
                        course_enrollment = CourseEnrollment.objects.create(
                            course_id=course_id,
                            user_id=user.id,
                            mode="audit",
                            is_active=True,
                            created=datetime.utcnow())
                        course_enrollment.save()





