import xdj
@xdj.Controller(
    url="resource/download/excel",
    template="resource/download_excel.html"
)
class ResourceDownloadExcel(xdj.BaseController):
    def on_get(self,model):
        from uuid import uuid4
        model.filename = uuid4().__str__()
        return self.render(model)
