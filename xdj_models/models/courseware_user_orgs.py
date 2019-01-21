from django.db import models
from django.contrib.auth.models import User
from . courseware_orgs import CoursewareOrgs

class CoursewareUserOrgs(models.Model):
    id = models.AutoField(primary_key=True)
    User = models.ForeignKey(User)
    Org = models.ForeignKey(CoursewareOrgs)
    class Meta:
        db_table ="courseware_user_orgs"
