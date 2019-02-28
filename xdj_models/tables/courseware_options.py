from xdj_sql import table,fields
from django.db import models
from openedx.core.djangoapps.content.course_overviews.models import CourseOverview
from datetime import datetime


@table("courseware_options")
class CoursewareOptions():

    course = models.ForeignKey(CourseOverview,to_field="id",db_column="course_id")
    is_private = fields.boolean(require=True)


