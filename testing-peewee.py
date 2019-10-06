from peewee import *
from datetime import date

db = SqliteDatabase('people.db')


class Person(Model):
    id = PrimaryKeyField('id')
    name = CharField()
    birthday = CharField()

    class Meta:
        database = db # This model uses default database "people.db"


class Pet(Model):
    owner = ForeignKeyField(Person, backref='pets')
    name = CharField()
    animal_type = CharField()

    class Meta:
        database = db

db.connect()
# db.create_tables([Person, Pet])

#uncle_bob = Person(name='Bob',birthday=date(1960,1, 15))
#uncle_bob.save()

#grandma = Person.create(name='Grandma', birthday=date(1948,3,22))
#herb = Person.create(name='Herb', birthday=date(1968,7,20))

#grandma.name = 'Grandma L.'
#grandma.save()

#bob_kitty = Pet.create(owner=uncle_bob, name='Kitty', animal_type='cat')
#herb_fido = Pet.create(owner=herb, name='Fido', animal_type='dog')
#herb_mittens = Pet.create(owner=herb, name='Mittens', animal_type='cat')
#herb_mittens_jr = Pet.create(owner=herb, name='Mittens Jr', animal_type='cat')

grandma = Person.get(Person.name == 'Grandma L.')

for person in Person.select():
    print(person.name)

print("")

query = (Pet
         .select(Pet, Person)
         .join(Person)
         .where(Pet.animal_type == 'cat'))

for pet in query:
    print(pet.name, pet.animal_type, pet.owner.name)

print()
query = Pet.select().order_by(Pet.name.desc())
for pet in query:
    print(pet.name, pet.animal_type)

