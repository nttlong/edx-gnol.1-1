import xdj
from openedx.core.djangoapps.content.course_overviews.models import CourseOverview
from django.db.models import Q

class CommonController(xdj.BaseController):
    def __is_email__(self,txt):
        """
        Check is txtx describe an email?
        :param txt:
        :return:
        """
        import re
        match = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', txt)
        return match!=None
    def __get_user_models__(self):
        from django.contrib.auth import get_user_model
        return get_user_model().objects
    def __get_CourseOverview_Model__(self):
        from xdj_models.models.course_authors import CourseAuthors

        from openedx.core.djangoapps.content.course_overviews.models import CourseOverview
        return CourseOverview

    def __find_user_by_email__(self,email):
        users = self.__get_user_models__().filter(email=email).all()
        if users.__len__() == 0:
            return None
        else:
            return users[0]

    def __get_course_id_from_text__(self,txt):
        from opaque_keys.edx.locator import CourseLocator
        return CourseLocator.from_string(txt)

    def __check_is_creator_of_courseware__(self,txt_course_id,user):
        from xdj_models.models import CourseAuthors
        from student.models import CourseAccessRole
        course_id = self.__get_course_id_from_text__(txt_course_id)
        x = CourseAuthors().objects.filter(
            Q(course_id = course_id) &
            Q(user = user)
        ).count() + CourseAccessRole.objects.filter(
            Q(course_id=course_id) &
            Q(user = user) &
            Q(role ="staff")
        ).count()
        # x = list(CourseAuthors().objects.filter(course_id=self.__get_course_id_from_text__(txt_course_id)))+
        # CourseAccessRole.objects.filter(
        #     Q(course_id=self.__get_course_id_from_text__(txt_course_id)) & Q(user=user)).count()
        if x == 0:
            return False
        else:
            return True

    def __get_course_ware_from_str_key__(self,course_key,user):

        from xmodule.modulestore.django import modulestore
        id = self.__get_course_id_from_text__(course_key)
        with modulestore().bulk_operations(id):
            course_module = modulestore().get_course(id)
            return course_module


class StaffController(xdj.BaseController):
    def IsAllow(self,model):
        return model.user.is_staff








