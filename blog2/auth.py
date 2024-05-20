
import click
from blog.database import mongo
from werkzeug.security import check_password_hash, generate_password_hash
from flask_simplelogin import SimpleLogin

def create_user(**data): #data é dicionário, ** descompacta todo dicionário
    print("entrei 1")
    """
    Creates user with encripted password.
    """
    if "username" not in data or "password" not in data:
        raise ValueError("username e password são requeridos.")
    
    data["password"] = generate_password_hash(
        data.pop("password"), 
        method="pbkdf2:sha256" #camada de segurança
    )

    #TODO: Verificar se o user já existe
    mongo.db.users.insert_one(data)
    return data

def validate_login(data):
    #TODO: Checa se o user existe
    print("oi man")
    if "username" not in data or "password" not in data:
        raise ValueError("username e password são requeridos.")
    
    user = mongo.db.users.find_one(
        {"username": data["username"]}
    )

    if user and check_password_hash(user["password"], data["password"]):
        return True
    return False

def configure(app):
    SimpleLogin(app, login_checker=validate_login)
    @app.cli.command()
    @click.argument("username")
    @click.password_option()
    def add_user(username, password):
        """Creates  new user."""
        user = create_user(username=username, password=password)
        click.echo("User created!")