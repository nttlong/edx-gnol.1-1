from xdj_apps.xlms.controllers.commons.edx_controller import EdxController
import xdj

@xdj.Controller(
    template="xdj-htmls/course_subjects.html",
    url="subjects/(?P<subject>.*)"
)
class CourseSubjects(EdxController):
    def on_get(self,model):
        import branding
        return self.render(model)
    def doLoadItems(self,model):
        from xdj import dobject
        from xdj_models.models import CourseSubjectsLinks, CourseAuthors, CoursewareOrgs
        from django.contrib.auth.models import User
        course_subjects_links_model = CourseSubjectsLinks()
        course_authors_model = CourseAuthors()
        courseware_orgs = CoursewareOrgs()
        ret = []
        lst = course_subjects_links_model.objects.filter(subject_id=model.params.subject).all()
        for x in lst:
            item = dobject()
            item.course_id = x.course.id.__str__()
            item.display_name = x.course.display_name
            item.course_image_url = x.course.course_image_url
            item.org = x.course.org
            item.code = x.course.id.run

            course_author_item = course_authors_model.objects.filter(course_id=x.course.id).first()
            courseware_orgs_item = courseware_orgs.objects.filter(OrgCode=x.course.org).first()
            if courseware_orgs_item:
                item.org = courseware_orgs_item.OrgName

            if course_author_item:
                author = User.objects.filter(id=course_author_item.user_id).first()
                if author:
                    item.author = author.username

            ret.append(item)
        return ret



