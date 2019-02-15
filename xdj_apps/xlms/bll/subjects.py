from xdj_models.models import CourseSubjects

def get_all_subjects():
    course_subjects_model = CourseSubjects()
    ret = course_subjects_model.objects.all()
    return ret
