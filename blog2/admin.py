from datetime import datetime
from flask_admin import Admin
from flask_admin.base import AdminIndexView
from flask_admin.contrib.pymongo import ModelView
from flask_simplelogin import login_required
from wtforms import form, fields, validators
from blog.database import mongo

AdminIndexView._handle_view = login_required(AdminIndexView._handle_view)
ModelView._handle_view = login_required(ModelView._handle_view)

class ConsolesForm(form.Form):
    name = fields.StringField("name", [validators.data_required()])
    brand = fields.StringField("brand", [validators.data_required()])
    description = fields.StringField("description", [validators.data_required()])
    value = fields.StringField("value", [validators.data_required()])
    sale = fields.StringField("sale", [validators.data_required()])
    sold = fields.BooleanField("sold", default=False)
    slug = fields.HiddenField("Slug")

class Admin_consoles(ModelView):
    column_list = ("name", "brand", "description", "value", "sale", "sold" )
    form = ConsolesForm

    def on_model_change(self, form, console, is_created):
        console["slug"] = console["name"].replace("_","-").replace("_","-").lower()

        if is_created:
            console["date"] = datetime.now()


def configure(app):
    app.admin = Admin(
        app,
        name="Blog",
        template_mode=app.config.get("FLASK_ADMIN_TEMPLATE_MODE", "bootstrap3")
    )
    app.admin.add_view(Admin_consoles(mongo.db.consoles, "Console"))
