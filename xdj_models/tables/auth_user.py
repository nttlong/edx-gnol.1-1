from xdj_sql import table, fields


@table("auth_user")
class AuthUser():
    id = fields.integer()
    last_login = fields.date()
    is_superuser = fields.boolean()
    username = fields.text()
    first_name = fields.text()
    last_name = fields.text()
    email = fields.text()
    is_staff = fields.boolean()
    is_active = fields.boolean()
    date_joined = fields.date()