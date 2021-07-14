from peewee import *
from os import path

ROOT = path.dirname(path.realpath(__file__))
db = SqliteDatabase(path.join(ROOT,"PyClass.db"))

class User(Model):
    name = CharField()
    email = CharField(unique=True)
    password = CharField()

    class Meta:
        database = db

User.create_table(fail_silently=True)