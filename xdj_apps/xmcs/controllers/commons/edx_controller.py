import xdj
class EdxController(xdj.BaseController):
    def render(self,model):
        from edxmako.shortcuts import render_to_response
        return render_to_response(self.template, model.__dict__)
    def get_course_id_from_text(self,course_key_string):
        from opaque_keys.edx.keys import CourseKey
        return CourseKey.from_string(course_key_string)
    def get_user_profile_img_url(self,user):
        from xdj_apps.xlms.bll.users import get_user_profile_img_url
        return get_user_profile_img_url(user)
    def get_user_profile_img_url_by_username(self,username):
        from django.contrib.auth.models import User
        user = User.objects.filter(username=username).get()
        if user:
            from xdj_apps.xlms.bll.users import get_user_profile_img_url
            return get_user_profile_img_url(user)
        else:
            return {}

    def apply_course_context(self,course_key_string,model):
        from opaque_keys.edx.keys import CourseKey
        from xmodule.modulestore.django import modulestore
        from student.auth import has_course_author_access
        from django.core.exceptions import PermissionDenied

        course_key = CourseKey.from_string(course_key_string)
        if not has_course_author_access(model.user, course_key):
            raise PermissionDenied()

        course_item = modulestore().get_course(course_key)

        model.context_course = course_item