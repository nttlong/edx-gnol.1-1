import xdj
@xdj.Controller(
    url="/",
    template="index.html"
)
class IndexController(xdj.BaseController):
    def on_get(self, model):
        return self.render(model)
