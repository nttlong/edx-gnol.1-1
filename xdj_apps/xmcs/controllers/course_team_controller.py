from xdj_apps.xmcs.controllers.commons import CommonController
import xdj
@xdj.Controller(
    url = "^course_team/(?P<course_key_string>([^/]+/[^/]+/[^/]+|[^/:]+:[^/+]+\+[^/+]+(\+[^/]+)?))(?:/(?P<email>.+))?$",
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

