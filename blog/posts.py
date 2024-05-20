from datetime import datetime
from blog.database import mongo
# from slugify import slugify

def get_all_posts():
    """ Pegar todos os consoless  """
    consoles = mongo.db.consoles.find()
    return consoles


def get_post_by_slug(slug: str):
    """Seleciona apenas pelo slug"""
    console = mongo.db.consoles.find_one({"slug":slug})
    return console


def update_post_by_slug(slug: str, data:dict): # data = dado a ser atualizado
    """ Atualiza o console por slug"""
    return mongo.db.consoles.find_one_and_update(
        {
            "slug": slug
        },
        {
            "$set": data
        }
    )

def delete_post_by_slug(slug: str):
    """ Deleta um novo console por slug """
    console = mongo.db.consoles.delete_one({"slug":slug})
    return console

def new_post(title: str, content: str, img: str, published: bool = True) -> str:
    """ Cria um novo console """
    # TODO: Refatorar a criação do Slug removendo acentos
    # TODO: Verificar se já existe algum console com esse slog
    slug = name.replace(" ","-").replace("_","-").lower()
    # slug = slugify(name)

    mongo.db.consoles.insert_one(
        {
            "name": name,
            "brand": brand,
            "description": description,
            "value": value,
            "sale": sale,
            "sold": sold,
            "slug": slug,
            "date": datetime.now()
        }
    )

    return slug
    