import xdj
@xdj.Controller(
    url="system/subjects",
    template="system/subjects.html"
)
class SystemSubjectsController(xdj.BaseController):
    def on_get(self,model):
        return self.render(model)

    def DoLoadItems(self,model):
        from xdj_models.models import CourseSubjects
        return list(CourseSubjects().objects.all())

    def do_export_to_excel(self,model):
        if isinstance(model,xdj.Model):
            from xdj_resource_download import create_new_download, get_download_info, get_download_link
            from xdj_excel import Column, save_to_file
            from xdj_models.models import CourseSubjects
            from xdj_sql import qr
            from django.conf import settings
            import os
            download_info = create_new_download( "{0}.xlsx".format(model.post_data.filename))
            url = get_download_link(model.appUrl+"/download",download_info)

            data = list(qr(CourseSubjects()).all())
            save_to_file(
                download_info.file_path,
                (
                    Column("id", "id",is_lock=True),
                    Column("SubjectCode"),
                    Column("SubjectName"),
                    Column("SubjectFName"),
                    Column("CreatedOn",format = "dd/MM/yyyy",is_lock=True),
                    Column("CreatedBy",is_lock=True)
                 ),
                data)
            return dict(url=url)
    @xdj.Page(
        url="subject",
        template="system/subject.html"
    )

    class subject(object):

        def DoSaveItem(self,model):
            try:
                from django.db.utils import IntegrityError
                from xdj_models.models import CourseSubjects
                from xdj_models.models import CourseSubjectsLinks
                if isinstance(model,xdj.Model):
                    if model.post_data.__dict__.get("SubjectCode","") == "":
                        return dict(
                            errorType="missingField",
                            field="SubjectCode"
                        )
                    if model.post_data.__dict__.get("SubjectName","") == "":
                        return dict(
                            errorType="missingField",
                            field="SubjectName"
                        )
                    from datetime import datetime
                    item = None

                    if CourseSubjects().objects.filter(id=model.post_data.id).count() == 0:
                        item = CourseSubjects().objects.create(SubjectCode=model.post_data.SubjectCode)
                        item.CreatedOn = datetime.utcnow()
                        item.CreatedBy = model.user.username
                    else:
                        item = CourseSubjects().objects.get(id=model.post_data.id)
                        CourseSubjectsLinks().objects.filter(subject_id=item.SubjectCode).update(subject_id= model.post_data.SubjectCode)
                        item.ModifiedOn = datetime.utcnow()
                        item.ModifiedBy = model.user.username
                    item.SubjectCode = model.post_data.SubjectCode
                    item.SubjectName = model.post_data.SubjectName
                    item.SubjectFName = model.post_data.__dict__.get("SubjectFName",item.SubjectName)
                    item.SubjectDescription = model.post_data.__dict__.get("SubjectDescription", None)

                    item.save()
                return dict(
                    data = item
                )
            except IntegrityError as ex:
                return dict(
                    error=ex.args[1],
                    data = model.post_data
                )
            except Exception as ex:
                return dict(
                    data=model.post_data,
                    error=ex.message
                )

        def DoLoadItem(self,model):
            from xdj_models.models import CourseSubjects
            if CourseSubjects().objects.filter(id=model.post_data.id).count()>0:
                item = CourseSubjects().objects.get(id=model.post_data.id)
                return item
            else:
                return {"id":-1}
