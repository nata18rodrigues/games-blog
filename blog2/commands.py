# Para testar os comandos sem as views
import click

from blog.posts import(
    get_all_consoles,
    get_console_by_slug,
    new_console,
    update_console_by_slug
)

@click.group()
def post():
    """Manage blog posts"""

@post.command()
@click.option("--name")
@click.option("--brand")
@click.option("--description")
@click.option("--value")
@click.option("--sale")
@click.option("--sold")
def new(name, brand, description, value, sale, sold):
    new = new_console(name=name, brand=brand, description=description, value=value, sale=sale, sold=sold)
    click.echo(f"New console {new} created!")

@post.command("list")
def _list():
    """List all consoles"""
    for console in get_all_consoles():
        click.echo(console)

@post.command()
@click.argument("slug")
def get(slug):
    """Get console by slug"""
    console = get_console_by_slug(slug)
    click.echo(console or "console not found!")

@post.command()
@click.argument("slug")
@click.option("--name", default=None, type=str)
@click.option("--brand", default=None, type=str)
@click.option("--description", default=None, type=str)
@click.option("--value", default=None, type=str)
@click.option("--sale", default=None, type=str)
@click.option("--sold", default=None, type=bool)
def update(slug, description):
    """Update console by slug"""
    data = {}
    if description is not None:
        data["description"] = description
    
    # if published is not None:
    #     data["published"] = published

    update_console_by_slug(slug, data)

    click.echo(f"console updated!")

    get(slug)


def configure(app):
    app.cli.add_command(post)
    