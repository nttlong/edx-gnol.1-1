from xdj_apps.xmcs.controllers.commons import CommonController
import xdj
@xdj.Controller(
    url="courseware/list",
    template="courseware_list.html"
)
class CoursewareListController(CommonController):
    def on_get(self,model):
        return self.render(model)
    def LoadItems(self,model):
        from xdj_models.tables.course_overviews import CourseoverView
        from xdj_models.tables.courseware_options import CoursewareOptions
        from xdj_models.tables.courseware_authors import CoursewareAuthors
        from xdj_models.tables.auth_user import AuthUser
        from xdj_sql import qr, builder
        sql = builder.query(CourseoverView).left_outer_join(
            to=CoursewareAuthors,
            local_fields=CourseoverView.id,
            foreign_fields = CoursewareAuthors.course_id
        ).select_related(builder.outer(CoursewareAuthors)).join(
            to = AuthUser,
            local_fields = builder.outer(CoursewareAuthors).user_id,
            foreign_fields = AuthUser.id
        ).select(
            CourseoverView.id,
            CourseoverView.course_image_url,
            CourseoverView.org,
            CourseoverView.display_name,
            CourseoverView.language,
            builder.outer(CoursewareAuthors).user_id >> builder.fields.user_id,
            builder.outer(CoursewareAuthors).user_id >> builder.fields.user_id
        )



        fx = sql.execute()


        ret = []


        for item in self.__get_CourseOverview_Model__().objects.prefetch_related("courseauthors_set").filter(courseauthors__user=model.user):
            ret.append(dict(
                display_name=item.display_name,
                id=item.id.html_id(),
                image_urls=item.image_urls,
                short_description = item.short_description,
                start = item.start,
                end = item.end,
                enrollment_start=item.enrollment_start,
                enrollment_end=item.enrollment_end,

            ))


        return ret
