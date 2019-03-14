import xdj
@xdj.Controller(
    url="resource/import/excel",
    template="resource/upload_excel.html"
)
class ResourceUploadExcelController(xdj.BaseController):

    def on_get(self,model):
        from xdj_resource_upload import create_upload
        ret = create_upload()
        model.token = ret.token
        return self.render(model)

    def doUploadChunk(self,model):
        from xdj_resource_upload import save_upload
        import binascii
        bff = model.post_data.info['result']
        try:
            bff = bytearray(binascii.a2b_base64(bff.split(';base64,')[1]))
            save_upload(model.post_data.token, model.post_data.info['originFileName'], bff)
        except Exception as ex:
            return dict(
                error=dict(
                    message = ex.message
                )
            )


        return {}