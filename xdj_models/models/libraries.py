from django.contrib.auth.models import User
from django.db import models
from openedx.core.djangoapps.content.course_overviews.models import CourseOverview
from django.contrib.auth.models import User
class Library(models.Model):
    """
    Link One - one to CourseOverview
    """
    id  = models.AutoField(primary_key=True)
    key = models.TextField(max_length=450)
    user = models.ForeignKey(User)
    name = models.TextField(max_length=500)
    description = models.TextField(max_length=2000)
    created_on =models.DateField()
    class Meta:
        db_table = "libraries"