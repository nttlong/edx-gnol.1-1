from xdj_apps.xmcs.controllers.commons import CommonController
from student.models import CourseAccessRole
from django.contrib.auth.models import User
from openedx.core.djangoapps.user_api.accounts.image_helpers import get_profile_image_urls_for_user
from django.db.models import Q,F
import xdj
@xdj.Controller(
    url = "settings/course_team",
    check_url = r'^course_team/(?P<course_key_string>([^/]+/[^/]+/[^/]+|[^/:]+:[^/+]+\+[^/+]+(\+[^/]+)?))(?:/(?P<email>.+))?$',
    template = "settings/course_team.html",
    replace_url = r'^course_team/(?P<course_key_string>([^/]+/[^/]+/[^/]+|[^/:]+:[^/+]+\+[^/+]+(\+[^/]+)?))(?:/(?P<email>.+))?$'
)
class CourseTeamController(CommonController):

    def on_get(self,model):
        if not self.__check_is_creator_of_courseware__(model.params.course_key_string,model.user):
            return model.redirect(model.absUrl+"/signin?next={0}".format(
                model.escape(model.absUrl+ model.request.get_full_path())
            ))
        course = self.__get_course_ware_from_str_key__(model.params.course_key_string, model.user)
        model.course = course
        return self.render(model)

    def on_post(self,model):
        pass

    def DoLoadItems(self,model):
        if not self.__check_is_creator_of_courseware__(model.params.course_key_string,model.user):
            return {}
        course_id = self.__get_course_id_from_text__(model.params.course_key_string)
        ret = []
        for item in CourseAccessRole.objects.filter(
                course_id=course_id
        ).select_related("user"):
            if model.user != item.user:
                ret.append(dict(
                    username=item.user.username,
                    email = item.user.email,
                    first_name = item.user.first_name,
                    last_name = item.user.last_name

                ))
        return ret

    @xdj.Page(
        url="editor",
        template="settings/course_team_editor.html"
    )
    class editor(object):

        def DoLoadItems(self,model):
            from xdj_sql import Fields,qr,Funcs
            from django.db.models.functions import Upper


            from xdj_models.models import CoursewareUserOrgs
            from django.db.models import F,Q

            fx = qr(CoursewareUserOrgs()).where(Fields.User==model.user).first()

            x=qr(CoursewareUserOrgs())
            x.select_related(User)
            x.where(
                (Fields.Org == fx.Org) &
                (Fields.User.is_staff == True) &
                (Fields.User != model.user)
            )
            # x.select(
            #     Fields.User.username,
            #     Fields.User.email,
            #     Fields.User.first_name,
            #     Fields.User.last_name
            # )
            x.select(
                Fields.xxxx << (Fields.User.id + Fields.id)*12,
                # Fields.username << Fields.User.username,
                # Fields.email << Fields.User.email,
                # Fields.FName << Fields.User.first_name,
                # Fields.LName << Fields.User.last_name,
                Fields.FullName << Funcs.call(Upper,Funcs.concat(Fields.User.first_name," ",Fields.User.last_name))
            )
            print x.execute().query
            d= x.all()





            item = CoursewareUserOrgs().objects.filter(User=model.user).first()
            ret = CoursewareUserOrgs().objects.filter(
                Org=item.Org
            ).select_related("User").filter(
                Q(User__is_staff=True) &
                (~Q(User=model.user))).all()
            ret = ret.values(
                "User__username",
                "User__email",
                "User__first_name",
                "User__last_name"
            ).annotate(
                username=F("User__username"),
                email=F("User__email"),
                first_name=F("User__first_name"),
                last_name=F("User__last_name")
            )
            ret_list = list(ret)
            ret_data =[]
            for x in ret_list:
                x["img"]= get_profile_image_urls_for_user(User.objects.get(username=x["username"]))

            return ret_list

        def DoAddItems(self,model):
            id = self.owner.__get_course_id_from_text__(model.post_data.course_id)
            for x in model.post_data.data:
                user = user=User.objects.get(
                        username=x["username"]
                    )
                if CourseAccessRole.objects.filter(Q(course_id=id) & Q(user=user)).count() == 0:
                    item = CourseAccessRole.objects.create(
                        course_id=id,
                        user=user,
                        role="staff"
                    )
                    item.save()
            pass




