import xdj
@xdj.Controller(
    url="resource/import/excel",
    template = "upload.html"
)
class ExcelUploadController(xdj.BaseController):
    def on_get(self,model):
        return self.render(model)