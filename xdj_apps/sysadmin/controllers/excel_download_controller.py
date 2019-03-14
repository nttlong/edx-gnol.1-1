# import xdj
# @xdj.Controller(
#     url="download/(?P<token>.*)",
#     template = "resource/download_excel.html"
# )
# class ExcelDownloadController(xdj.BaseController):
#     def on_get(self,model):
#         from xdj_resource_download import get_download_info
#         from django.http import HttpResponse
#
#         x = get_download_info(model.params.token)
#         with open(x.file_path, "r") as excel:
#             data = excel.read()
#         response = HttpResponse(data, content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
#         response['Content-Disposition'] = 'attachment; filename=%s' % x.file_name
#         return response
#         return self.render(model)
