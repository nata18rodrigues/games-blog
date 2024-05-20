from setuptools import setup

setup(
    name="flask_blog",
    versions="0.1.0",
    packages=["blog"],
    install_requires=[
        "flask",
        "Flask-PyMongo",
        "dynaconf",
        "Flask-Bootstrap",
        "mistune",
        "flask-simplelogin",
        "python-slugify[unidecode]",
        "Flask-Admin"
    ]
)