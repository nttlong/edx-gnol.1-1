import xdj
@xdj.Controller(
    url="password_reset",
    template="password_reset.html",
    check_url=r'^password_reset/$'
)
class PasswordResetController(xdj.BaseController):
    def on_get(self,model):
        pass
    def on_post(self,model):
        pass