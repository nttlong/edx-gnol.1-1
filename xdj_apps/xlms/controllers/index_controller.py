

import xdj
from xdj_apps.xlms.controllers.commons.edx_controller import EdxController


@xdj.Controller(
    url="",
    template="xdj-htmls/index.html",
    replace_url=r"^$"
)
class IndexControler(EdxController):
    def __init__(self):
        x=1
    def on_get(self,model):
        import branding
        model.data = xdj.dobject()
        model.data.courses = branding.get_visible_courses()
        for item in model.data.courses:
            item.key = item.id.html_id()
        return self.render(model)
    def doLoadItems(self,sender):
        """
        https://programtalk.com/python-examples-amp/student.models.anonymous_id_for_user/
        :param sender:
        :return:
        """

        import branding
        import courseware
        from xdj_models.enities import courseware as cw
        from xdj import pymqr
        from xdj import medxdb
        from django.contrib.auth.models import User
        import sysadmin
        import datetime
        from django.db.models import Q

        # courseware.models.StudentModule.objects.all()[0].student.last_name
        ret = branding.get_visible_courses()
        qr = pymqr.query(medxdb.db(), cw.modulestore_active_versions)
        for item in ret:
            # course = courseware.models.StudentModule.objects.get(course_id=item.id)
            x = qr.new().match(pymqr.filters.org==item.id.org)\
                .match(pymqr.filters.run==item.id.run)\
                .match(pymqr.filters.course==item.id.course).object

            #     .match(pymqr.funcs.expr(
            #     (pymqr.docs.org == item.id.org) &
            #     (pymqr.docs.run == item.id.run) &
            #     (pymqr.docs.course == item.id.course)
            # )).object
            from xdj_models.models import CourseAuthors
            fx=CourseAuthors()()
            item.course_id=item.id.__str__()
            if not x.is_empty():
                authors= User.objects.filter(id=x.edited_by)
                if authors.__len__()>0:
                    sql_items=CourseAuthors().objects.filter(Q(user_id=x.edited_by)&Q(course_id=item.id)).count()
                    item.author= xdj.dobject(username=authors[0].username)
                    if sql_items==0:
                        fx.user_id = x.edited_by
                        fx.course_id = item.id
                        fx.created_on = datetime.datetime.now()
                        fx.save()
            item.totalActiveStudent=courseware.models.StudentModule.objects.filter(course_id=item.id).filter(module_type="course").count()
            from xdj_models.models import CourseSubjectsLinks, CoursewareOrgs
            course_subjects_links_model = CourseSubjectsLinks()
            course_subjects_links_item = course_subjects_links_model.objects.filter(course_id=item.id).first()
            if course_subjects_links_item:
                item.subject = course_subjects_links_item.subject.SubjectName
            courseware_orgs_model = CoursewareOrgs()
            courseware_orgs_item = courseware_orgs_model.objects.filter(OrgCode=item.id.org).first()
            if courseware_orgs_item:
                item.org = courseware_orgs_item.OrgName
            item.code = item.id.run

            """calculate total activates students"""

        return ret