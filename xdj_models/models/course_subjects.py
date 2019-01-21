from django.db import models
from openedx.core.djangoapps.content.course_overviews.models import CourseOverview
from django.contrib.auth.models import User
class CourseSubjects(models.Model):
    # course = models.ForeignKey(CourseOverview)
    id = models.AutoField(primary_key=True)
    SubjectCode = models.TextField(max_length=50, primary_key=True)
    SubjectName = models.TextField(300)
    SubjectFName = models.TextField(300)
    SubjectDescription = models.TextField(2000)
    CreatedBy = models.TextField(200)
    CreatedOn = models.DateField()
    ModifiedBy = models.TextField(200)
    ModifiedOn = models.DateField()
    class Meta:
        db_table="courseware_subjects"
