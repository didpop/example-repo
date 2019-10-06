from peewee import *

db = SqliteDatabase('people1')


class Person(Model)