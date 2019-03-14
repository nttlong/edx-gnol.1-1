#!/usr/bin/env python
# -*- coding: utf-8 -*-
import xdj
@xdj.Controller(
    url="linguistics/list",
    template="linguistics/list.html"
)
class LinguisticsListController(xdj.BaseController):

    """
    This feature allow manage Language resource: insert, update,detlete, export and import
    Tính năng này cho phép quản lý tài nguyên ngôn ngữ: chèn, cập nhật, xóa, xuất và nhập
    """

    def on_get(self,model):
        return self.render(model)

    @xdj.privilege(xdj.Privilges.VIEW)
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
    @xdj.privilege(xdj.Privilges.UPDATE)
    def DoSaveItems(self,model):
        from xdj import pymqr, medxdb, clear_language_cache
        from xdj.pymqr import docs, funcs, filters
        from django.conf import settings
        import re
        ret_data = xdj.dobject(dict(
            error=None
        ))
        qr = pymqr.query(medxdb.db(), settings.COLLECTION_LANGUAGE)
        for x in model.post_data.rows:
            mongo_entity = qr.new().where((filters.app==x['app']) &
                                (filters.view==x['view']) &
                                (filters.language==x['language']) &
                                (filters.key==x['key']))
            ret,err,result = mongo_entity.set(docs.value >> x['value']).commit()
            if err:
                if not ret_data.error:
                    ret_data.error=xdj.dobject(dict(
                        items= []
                    ))
                ret_data.error.items.append(err)

        clear_language_cache()
        return ret_data
        pass

    def do_export_to_excel(self,model):
        from django.conf import settings
        from xdj import pymqr, medxdb
        from xdj.pymqr import docs, funcs, filters  # use mongodb document and mongo db function for database filter
        from xdj_resource_download import create_new_download, get_download_info, get_download_link
        from xdj_excel import Column, save_to_file

        import re
        download_info = create_new_download("{0}.xlsx".format(model.post_data.filename))
        qr = pymqr.query(medxdb.db(), settings.COLLECTION_LANGUAGE)
        url = get_download_link(model.appUrl + "/download", download_info)
        data = list(qr.items)
        save_to_file(
            download_info.file_path,
            (
                Column("language"),
                Column("app"),
                Column("view"),
                Column("key"),
                Column("value")
            ),
            data)
        return dict(url=url)


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