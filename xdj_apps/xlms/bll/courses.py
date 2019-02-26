def get_author(course_key):
    from xdj_models.models import CourseAuthors
    from opaque_keys.edx.keys import CourseKey
    course_id = CourseKey.from_string(course_key)
    course_author = CourseAuthors().objects.filter(course_id=course_id).get()
    if course_author:
        return course_author.user