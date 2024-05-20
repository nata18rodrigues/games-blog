from flask import(
    Flask,
    Blueprint,
    render_template,
    abort,
    request,
    session,
    url_for,
    redirect
)

from flask_simplelogin import login_required

from blog.posts import(
    get_all_consoles,
    get_console_by_slug,
    delete_console_by_slug,
    update_console_by_slug,
    new_console
    #TODO: criar update e delete
)

bp = Blueprint("view_console", __name__, template_folder="templates")

@bp.route("/")
def index():
    consoles = get_all_consoles()
    teste = []
    for console in consoles:
        teste.insert(1, console)
    return render_template("index.html.j2",consoles=teste)


@bp.route("/show/<string:slug>")
def detail(slug):

    console = get_console_by_slug(slug)

    if not console:
        return abort(404, "console not found")
    
    return render_template("console.html.j2", console=console)


@bp.route("/delete/<string:slug>")
@login_required
def delete(slug):
    print("oi man",slug)
    console = delete_console_by_slug(slug)
    print("sou",console)
    if not console:
        return abort(404, "console not found")
    
    return render_template("console.html.j2", console=console)


@bp.route("/update/<string:slug>", methods=["GET", "POST"])
@login_required
def update(slug):
    if request.method == "POST":
        name = request.form.get("name")
        brand = request.form.get("brand")
        description = request.form.get("description")
        value = request.form.get("value")
        sale = request.form.get("sale")

        console = update_console_by_slug(slug ,{ "description" : description })

        return redirect(url_for("view_console.detail", slug=slug))

    console = get_console_by_slug(slug)
    console["url"] = "/update/"+slug
    return render_template("form.html.j2", console=console)


@bp.route("/add-product", methods=["GET", "POST"])
@login_required
def newProduct():
    if request.method == "POST":

        name = request.form.get("name")
        brand = request.form.get("brand")
        description = request.form.get("description")
        value = request.form.get("value")
        sale = request.form.get("sale")
        slug = new_console(name, brand, description, value, sale)

        return redirect(url_for("view_console.detail", slug=slug))

    console = { "url" : "/add-product"}
    return render_template("form.html.j2", console=console)


def configure(app:Flask):
    app.register_blueprint(bp)