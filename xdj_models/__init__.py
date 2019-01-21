from . import models
from . import enities
class db():
    @staticmethod
    @property
    def CourseAuthors():
        from . models import CourseAuthors
        return CourseAuthors