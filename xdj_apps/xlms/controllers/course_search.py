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
        from contentstore.courseware_index import CourseAboutSearchIndexer
        return qr(settings.ELASTIC_SEARCH_CONFIG).create_index(CourseAboutSearchIndexer.INDEX_NAME)

    def on_get(self,model):
        return self.render(model)
    def doSearch(self,model):
        from contentstore.courseware_index import CourseAboutSearchIndexer
        from qres.filter import Fields
        if not hasattr(model.post_data,"value") or model.post_data.value == "":
            ret = self.get_es().search_as_objects(doc_type = CourseAboutSearchIndexer.DISCOVERY_DOCUMENT_TYPE,page_size=9)
            for x in ret.items:
                ret.items = [dict(
                    start= x._source.start,
                    display_name = x._source.content.display_name,
                    image_url = x._source.image_url,
                    org = x._source.org,
                    number = x._source.number,
                    id = x._source.id ,
                    organization=x._source.organization,
                    author=x._source.author,
                    subject=x._source.subject

                )  for x in ret.items]
            return ret
        else:
            ret = self.get_es().search_as_objects(
                doc_type="course_info",
                page_size=9,
                fields= (Fields().display_name << model.post_data.value)|
                        (Fields().subject.name << model.post_data.value)|
                        (Fields().organization.name << model.post_data.value) |
                        (Fields().author.username << model.post_data.value))
            ret.items = [dict(
                start=x._source.start,
                display_name=x._source.content.display_name,
                image_url=x._source.image_url,
                org=x._source.org,
                number=x._source.number,
                id=x._source.id,
                organization = x._source.organization,
                author = x._source.author,
                subject = x._source.subject

            ) for x in ret.items]
            return ret





