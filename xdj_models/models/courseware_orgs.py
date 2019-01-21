from django.contrib.auth.models import User
from django.db import models
from openedx.core.djangoapps.content.course_overviews.models import CourseOverview
from django.contrib.auth.models import User
class CoursewareOrgs(models.Model):
    """
    Link One - one to CourseOverview
    """
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    # department = models.CharField(max_length=100)
    # user_id =  models.IntegerField()
    # user = models.ForeignKey(User)
    # course = models.ForeignKey(CourseOverview)
    # course_id = models.CharField(max_length=255)
    OrgCode = models.TextField(50)
    OrgName = models.TextField(250)
    OrgFName = models.TextField(250)
    OrgDescription = models.TextField(2000)
    OrgAddress = models.TextField(200)
    OrgWebSite = models.TextField(2000)
    CreatedOn = models.DateField()
    CreatedBy = models.TextField(150)
    ModifiedOn = models.DateField()
    ModifiedBy = models.TextField(150)
    id=models.AutoField(primary_key=True)
    RegisteredBy = models.ForeignKey(User,to_field="id",db_column="RegisteredBy")
    RegisteredOn = models.DateField()

    class Meta:
        db_table = "courseware_orgs"
