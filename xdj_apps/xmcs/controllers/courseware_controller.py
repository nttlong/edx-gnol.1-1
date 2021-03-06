import xdj
from datetime import datetime
@xdj.Controller(
    url="courseware",
    template="courseware.html"
)
class CoursewareController(xdj.BaseController):
    def on_get(self,model):
        return self.render(model)
    def DoCreateCourseWare(self,model):
        import cms.djangoapps.contentstore.views.course
        data = xdj.JSON.from_json(model.request.body)
        if data.get("subject","") == "":
            return dict(
                error="missing",
                field="subject"
            )
        if not data.has_key("name"):
            return dict(
                error="missing",
                field="name"
            )
        if not data.has_key("number"):
            return dict(
                error="missing",
                field="number"
            )
        if not data.has_key("run"):
            return dict(
                error="missing",
                field="run"
            )
        from xdj_models.models import CoursewareUserOrgs
        user_org = CoursewareUserOrgs().objects.get(User=model.user)
        from xdj_models.models import CoursewareOrgs
        org = CoursewareOrgs().objects.get(id=user_org.Org_id)

        model.request.json =data
        model.request._body = xdj.JSON.to_json(dict(
            display_name =data["name"],
            org = org.OrgCode,
            number = data["number"],
            run = data["run"]
        ))
        ret = cms.djangoapps.contentstore.views.course._create_or_rerun_course(model.request)
        if hasattr(ret,"getvalue"):
            ret_json = xdj.JSON.from_json(ret.getvalue())
            if ret_json.has_key("ErrMsg"):
                return dict(error_msg=ret_json["ErrMsg"])
        from opaque_keys.edx.locator import CourseLocator
        course_id = CourseLocator(org=org.OrgCode, course=data["number"], run=data["run"])
        from xdj_models.models import CourseAuthors, CourseSubjectsLinks, CourseSubjects
        ca = CourseAuthors().objects.create(user=model.user,created_on= datetime.utcnow(),course_id=course_id)
        ca.user = model.user

        ca.created_on = datetime.utcnow()
        ca.course_id = course_id
        ca.save()
        subject_model = CourseSubjects()
        subject_item = subject_model.objects.filter(id=data["subject"]).first()
        course_subjects_links_model = CourseSubjectsLinks()
        course_subjects_links_model = course_subjects_links_model.objects.create(subject_id=subject_item.SubjectCode, course_id=course_id)
        course_subjects_links_model.save()

        return ret
    def DoInit(self,model):
        if isinstance(model,xdj.Model):

            pass
    def DoLoadSubjects(self,model):
        from xdj_models.models import CourseSubjects
        return list(CourseSubjects().objects.all())
    def DoLoadItem(self,model):
        from xdj_models.models import CoursewareUserOrgs
        if CoursewareUserOrgs().objects.filter(User=model.user).count()==0:
            return dict(
                error="org_was_not_found"
            )
        from xdj_models.models import CoursewareOrgs
        from xdj_models.models import CoursewareUserOrgs
        u_org = CoursewareUserOrgs().objects.get(User=model.user)
        org = CoursewareOrgs().objects.get(id=u_org.Org_id)
        return dict(
            data=dict(
                Org=org.OrgCode
            )
        )
        pass