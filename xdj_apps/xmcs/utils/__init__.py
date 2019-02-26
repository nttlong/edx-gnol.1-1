def add_extra_search(data):
    from opaque_keys.edx.keys import CourseKey
    from xdj_models.models import CoursewareOrgs, CourseSubjectsLinks, CourseAuthors
    course_id = CourseKey.from_string(data[0]["id"])
    org_item = CoursewareOrgs().objects.filter(OrgCode=data[0]["org"]).get()
    course_subjects_link = CourseSubjectsLinks().objects.filter(course_id=course_id).get()
    course_authors_item = CourseAuthors().objects.filter(course_id=course_id).get()

    if isinstance(data, list):
        for x in data:
            if course_authors_item:
                x["author"] = dict(
                    first_name=course_authors_item.user.first_name,
                    last_name=course_authors_item.user.last_name,
                    username=course_authors_item.user.username,
                    email=course_authors_item.user.email,

                )
            if course_subjects_link:
                x["subject"] = dict(
                    name=course_subjects_link.subject.SubjectName,
                    fname=course_subjects_link.subject.SubjectFName,
                    code=course_subjects_link.subject.SubjectCode
                )
            if org_item:
                x["organization"] = dict(
                    code=org_item.OrgCode,
                    name=org_item.OrgName,
                    fname= org_item.OrgFName,
                )
