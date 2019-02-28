from xdj_sql import table,fields

@table("courseware_authors")
class CoursewareAuthors():
    user_id = fields.integer()
    course_id = fields.text()
    created_on = fields.date()

