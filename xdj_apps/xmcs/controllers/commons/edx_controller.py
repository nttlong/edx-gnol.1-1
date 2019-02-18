import xdj
class EdxController(xdj.BaseController):
    def render(self,model):
        from edxmako.shortcuts import render_to_response
        return render_to_response(self.template, model.__dict__)