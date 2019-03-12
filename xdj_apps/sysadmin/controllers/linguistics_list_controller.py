import xdj
@xdj.Controller(
    url="linguistics/list",
    template="linguistics/list.html"
)
class LinguisticsListController(xdj.BaseController):

    def on_get(self,model):
        return self.render(model)

    def DoLoadItems(self,model):
        if not hasattr(model.post_data,"pageSize"):
            return  {}
        from django.conf import settings
        from xdj import pymqr, medxdb
        from xdj.pymqr import docs, funcs, filters # use mongodb document and mongo db function for database filter


        import re
        qr = pymqr.query(medxdb.db(), settings.COLLECTION_LANGUAGE)
        for k,v in model.post_data.filter.items():
            if v.get('operator',None):
                m=1
            if v.get('type') == 'contains':
                qr.pipeline.append({"$match": {k: re.compile(v.get("filter"), re.IGNORECASE)}})
            if v.get('type') == 'equals':
                qr.pipeline.append({"$match": {k: re.compile("^" + v.get("filter") + "$", re.IGNORECASE)}})
            if v.get('type') == 'notEqual':
                qr.match(getattr(filters, k) != v.get("filter"))

        for x in model.post_data.sort:
            """
            if end user would like sort data by fieldname
            """
            field = getattr(docs,x['colId']) # get field from mongodb document
            if x['sort'] == 'desc': 
                qr.sort(field.desc())
            else:
                qr.sort(field.asc())
        ret = qr.get_page(model.post_data.pageSize,model.post_data.pageIndex)
        return ret
        pass
    @xdj.Page(
        template="linguistics/editor.html",
        url="editor"
    )
    class editor(object):
        def DoLoadItem(self,model):
            from django.conf import settings
            from xdj import pymqr, medxdb
            from bson import ObjectId
            qr = pymqr.query(medxdb.db(), settings.COLLECTION_LANGUAGE)
            x = qr.new().where(pymqr.filters._id == ObjectId(model.post_data.id)).object
            return x
        def DoSaveItem(self,model):
            from django.conf import settings
            from xdj import pymqr, medxdb,clear_language_cache
            from bson import ObjectId
            qr = pymqr.query(medxdb.db(), settings.COLLECTION_LANGUAGE)
            x= qr.new().where(pymqr.filters._id == ObjectId(model.post_data._id))
            x.set(value = model.post_data.value)
            x.commit()
            clear_language_cache()
            return model.post_data