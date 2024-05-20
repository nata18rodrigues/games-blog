from datetime import datetime
from blog.database import mongo


def get_all_posts():
    """ Pegar todos os consoless  """
    consoles = mongo.db.consoles.find()
    return consoles


def get_console_by_slug(slug: str):
    console = mongo.db.consoles.find_one({"slug":slug})
    return console

def delete_console_by_slug(slug: str):
    console = mongo.db.consoles.delete_one({"slug":slug})
    return console

def update_console_by_slug(slug: str, data:dict): # data = dado a ser atualizado
    """ Atualiza o console """
    return mongo.db.consoles.find_one_and_update(
        {
            "slug": slug
        },
        {
            "$set": data
        }
    )


def new_console(name:str, brand:str, description:str, value:str, sale:str, sold: bool = False) -> str:
    # TODO: Refatorar a criação do Slug removendo acentos
    # TODO: Verificar se já existe algum console com esse slog
    slug = name.replace(" ","-").replace("_","-").lower()

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
