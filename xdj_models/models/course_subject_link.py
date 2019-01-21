from django.db import models
from openedx.core.djangoapps.content.course_overviews.models import CourseOverview
from django.contrib.auth.models import User
from . import course_subjects
class CourseSubjectsLinks(models.Model):
    # course = models.ForeignKey(CourseOverview)
    id = models.AutoField(primary_key=True)
    subject_id = models.OneToOneField(
        to= course_subjects,
        to_field=course_subjects.SubjectCode,
    )
    course = models.ForeignKey(CourseOverview)
    class Meta:
        db_table="courseware_subjects_links"
