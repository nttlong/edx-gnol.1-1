from xdj_apps.xlms.controllers.commons.edx_controller import EdxController
import xdj

@xdj.Controller(
    template="xdj-htmls/course_search.html",
    url ="^courses/?$",
    replace_url=r"^courses/?$"
)
class CourseSearchController(EdxController):
    def get_es(self):
        from django.conf import settings
        from qres.query import qr
        return qr(settings.ELASTIC_SEARCH_CONFIG).create_index("courseware_index")

    def on_get(self,model):
        return self.render(model)
    def doSearch(self,model):
        from qres.filter import Fields
        if not hasattr(model.post_data,"value") or model.post_data.value == "":
            ret = self.get_es().search_as_objects(doc_type = "course_info",page_size=9)
            ret.items = [dict(
                start= x._source.start,
                display_name = x._source.content.display_name,
                image_url = x._source.image_url,
                org = x._source.org,
                number = x._source.number,
                id = x._source.id

            )  for x in ret.items]
            return ret
        else:
            ret = self.get_es().search_as_objects(doc_type="course_info", page_size=9,fields= Fields().display_name<<model.post_data.value)
            ret.items = [dict(
                start=x._source.start,
                display_name=x._source.content.display_name,
                image_url=x._source.image_url,
                org=x._source.org,
                number=x._source.number,
                id=x._source.id

            ) for x in ret.items]
            return ret





