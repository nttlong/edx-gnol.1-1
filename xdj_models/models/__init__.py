# from . course_authors import CourseAuthors
# from . course_subjects import CourseSubjects
# from . course_subject_link import CourseSubjectsLinks
def CourseAuthors():
    from xdj_models.models.course_authors import CourseAuthors as ret
    return ret
def CourseSubjects():
    from xdj_models.models.course_subjects import CourseSubjects as ret
    return ret
def CourseSubjectsLinks():
    from xdj_models.models.course_subject_link import CourseSubjectsLinks as ret
    return ret
def CoursewareOrgs():
    from xdj_models.models.courseware_orgs import CoursewareOrgs as ret
    return ret
def CoursewareUserOrgs():
    from xdj_models.models.courseware_user_orgs import CoursewareUserOrgs as ret
    return ret
def Libraries():
    from xdj_models.models.libraries import Library as ret
    return ret
def Chapter():
    from xdj_models.models.courseware_chapter import CoursewareChapter  as ret
    return ret
def Sequential():
    from xdj_models.models.courseware_sequential import CoursewareSequential as ret
    return ret

def Vertical():
    from xdj_models.models.courseware_vertical import CoursewareVertical as ret
    return ret

def XBlock():
    from xdj_models.models.courseware_xblock import CoursewareXblock as ret
    return ret