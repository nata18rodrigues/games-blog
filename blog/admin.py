from datetime import datetime
from flask_admin import Admin
from flask_admin.base import AdminIndexView
from flask_admin.contrib.pymongo import ModelView #Cria o modelo
from flask_simplelogin import login_required #Proteje a página por login
from wtforms import form, fields, validators
from blog.database import mongo


AdminIndexView._handle_view = login_required(AdminIndexView._handle_view)
ModelView._handle_view = login_required(ModelView._handle_view)

class ConsoleForm(form.Form):
    name = fields.StringField("name", [validators.data_required()])
    slug = fields.HiddenField("Slug")
    brand = fields.StringField("brand")
    description = fields.StringField("description")
    value = fields.StringField("value")
    # sale = fields.StringField("sale")
    sale = fields.StringField("sale")
    sold = fields.BooleanField("sold", default=False)
    # img = fields.StringField("Image")

class ConsolePosts(ModelView):
    column_list = ("name","slug", "brand", "description", "value", "sale", "sold")

    form = ConsoleForm

    def on_model_change(self, form, post, is_created):
        post["slug"] = post["name"].replace("_","-").replace(" ","-").lower()

        if is_created:
            post["date"] = datetime.now()

def configure(app):
    app.admin = Admin(
        app,
        name="Blog",
        template_mode=app.config.get("FLASK_ADMIN_TEMPLATE_MODE", "bootstrap3")
    )
    app.admin.add_view(ConsolePosts(mongo.db.consoles, "Consoles")
    )