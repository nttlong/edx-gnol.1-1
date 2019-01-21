from django.contrib.auth.models import User
from django.db import models
from openedx.core.djangoapps.content.course_overviews.models import CourseOverview
from django.contrib.auth.models import User
class CoursewareChapter(models.Model):
    """
    Link One - one to CourseOverview
    """
    display_name = models.TextField(max_length=245)
    chapter_id = models.CharField(max_length=255,primary_key=True)
    created_on = models.DateField()
    creator = models.ForeignKey(to=User, related_name="created_by", to_field="username")
    modified_on = models.DateField()
    modifier= models.ForeignKey(to=User, related_name="modifier_by", to_field="username")

    class Meta:
        db_table = "courseware_chapters"