from django.contrib.auth.models import User
from django.db import models
from openedx.core.djangoapps.content.course_overviews.models import CourseOverview
from django.contrib.auth.models import User
from xdj_models.models import courseware_sequential
class CoursewareXblock(models.Model):
    xblock_id=models.TextField(max_length=255,primary_key=True)
    vertical_id = models.TextField(max_length=255)
    xblock_type = models.TextField(max_length=255)
    course = models.ForeignKey(CourseOverview)
    display_name = models.TextField(max_length=455)
    created_on = models.DateField()
    creator = models.ForeignKey(to=User, related_name="created_by", to_field="username")
    modified_on = models.DateField()
    modifier = models.ForeignKey(to=User, related_name="modifier_by", to_field="username")
    class Meta:
        db_table = "courseware_xblocks"