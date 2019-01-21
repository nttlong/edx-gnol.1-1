from django.contrib.auth.models import User
from django.db import models
from openedx.core.djangoapps.content.course_overviews.models import CourseOverview
from django.contrib.auth.models import User
class CourseAuthors(models.Model):
    """
    Link One - one to CourseOverview
    """
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    # department = models.CharField(max_length=100)
    # user_id =  models.IntegerField()
    user = models.ForeignKey(User)
    course = models.ForeignKey(CourseOverview)
    # course_id = models.CharField(max_length=255)
    created_on =models.DateField()
    id=models.IntegerField()
    class Meta:
        db_table = "courseware_authors"
