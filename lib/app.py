from peewee import PostgresqlDatabase, Model, CharField, DateField
import psycopg2
from datetime import date


db = PostgresqlDatabase('contact_book', user='postgres', password='',
                       host='localhost', port=5432)
class BaseModel(Model):
    class Meta:
        database = db
class Person(BaseModel):    
    first_name = CharField()
    last_name = CharField()
    phone_number = CharField()
    email  = CharField
    birthday = DateField()
db.connect()
db.drop_tables([Person])
db.create_tables([Person])

##
Levani = Person(first_name = 'Levani', last_name = 'Papashvili',
    phone_number = '249-943-0303', email = 'levani@mail.com', birthday = '11/11/1984')
Levani.save()
Charlie = Person(first_name = 'Charlie', last_name='Smith',
    phone_number = '555-555-2524', email = 'charliedo@gmail.com', birthday = '03/09/85' )
Charlie.save()
Sara = Person(first_name = 'Sara', last_name ='Ross',
    phone_number = '434-023-2313', email = 'saralalal@yahoo.com', birthday = '04/22/75')
Sara.save()
Lilly = Person(
    first_name = 'Lilly',
    last_name = 'Johnson',
    phone_number = '555-555-5053',
    email = 'princess@gmail.com',
    birthday = '11/13/1999'
)
Lilly.save()
Bailey = Person(
    first_name = 'Bailey',
    last_name = 'Johnson',
    phone_number = '555-240-0443',
    email = 'bobbyb@mail.com',
    birthday = '10/30/2002'
)
Bailey.save()
Jeremy = Person(
    first_name = 'Jeremy',
    last_name = 'Johnson',
    phone_number = '555-980-6578',
    email = 'jeremypa@mail.com',
    birthday = '09/24/1982'
)
Jeremy.save()
Gio = Person(
    first_name = 'Gio',
    last_name = 'Niparishvili',
    phone_number = '987-340-1429',
    email = 'gionb@mail.com',
    birthday = '06/07/1986'
)
Gio.save()
Lia = Person(
    first_name = 'Lia',
    last_name = 'Rusishvili',
    phone_number = '545-340-9842',
    email = 'liarus@mail.com',
    birthday = '11/04/1785'
)
Lia.save()
Omari = Person(
    first_name = 'Omari',
    last_name = 'Ninoshvili',
    phone_number = '986-120-1236',
    email = 'omargs@mail.com',
    birthday = '10/30/200'
)
Omari.save()
Patta = Person(
    first_name = 'Patta',
    last_name = 'Borjomi',
    phone_number = '678-340-9876',
    email = 'pattalab@mail.com',
    birthday = '09/30/2001'
)
Patta.save()
Anna = Person(
    first_name = 'Anna',
    last_name = 'Mamodze',
    phone_number = '571-897-3452',
    email = 'annatya@mail.com',
    birthday = '11/02/2009'
)
Anna.save()
Giorgi = Person(
    first_name = 'Giorgi',
    last_name = 'Nonoiashvil',
    phone_number = '555-876-0093',
    email = 'Giorginan@mail.com',
    birthday = '03/30/1982'
)
Giorgi.save()
Natela = Person(
    first_name = 'Natela',
    last_name = 'Baliako',
    phone_number = '555-120-1643',
    email = 'natelabsd@mail.com',
    birthday = '03/05/2008'
)
Natela.save()
Dato = Person(
    first_name = 'Dato',
    last_name = 'Guraspashvili',
    phone_number = '555-987-0964',
    email = 'datojgf@mail.com',
    birthday = '01/06/2010'
)
Dato.save()
Nika = Person(
    first_name = 'Nika',
    last_name = 'Sakashvili',
    phone_number = '555-090-1283',
    email = 'nikaso@mail.com',
    birthday = '07/30/1783'
)
Nika.save()
Papuna = Person(
    first_name = 'Papauna',
    last_name = 'Papaskiri',
    phone_number = '555-449-0089',
    email = 'papunaeee@mail.com',
    birthday = '10/01/2007'
)
Papuna.save()
Maka = Person(
    first_name = 'Maka',
    last_name = 'Blaxamishvili',
    phone_number = '555-298-0983',
    email = 'makaiut@mail.com',
    birthday = '10/03/2000'
)
Maka.save()
Jabo = Person(
    first_name = 'Jabo',
    last_name = 'Rosiko',
    phone_number = '555-987-9873',
    email = 'noklass@mail.com',
    birthday = '04/11/1975'
)
Jabo.save()
Scoot = Person(
    first_name = 'Scoot',
    last_name = 'Dior',
    phone_number = '155-654-9543',
    email = 'scootri@mail.com',
    birthday = '10/03/1891'
)
Scoot.save()
Wako = Person(
    first_name = 'Wako',
    last_name = 'Mamuashvili',
    phone_number = '555-876-1543',
    email = 'mamunsk@mail.com',
    birthday = '01/15/2000'
)
Wako.save()
Mariami = Person(
    first_name = 'Mariami',
    last_name = 'Berianidze',
    phone_number = '555-140-1643',
    email = 'mariamioyb@mail.com',
    birthday = '08/09/2008'
)
Mariami.save()
Soso = Person(
    first_name = 'Soso',
    last_name = 'Bodare',
    phone_number = '557-220-2643',
    email = 'soson@mail.com',
    birthday = '07/08/1988'
)
Soso.save()
Datuna = Person(
    first_name = 'Datuna',
    last_name = 'Lkaon',
    phone_number = '667-829-5658',
    email = 'datunammm@mail.com',
    birthday = '09/10/1989'
)
Datuna.save()

Nodo = Person(
    first_name = 'Nodo',
    last_name = 'Noniashvili',
    phone_number = '222-429-5018',
    email = 'nodoppp@mail.com',
    birthday = '07/01/1980'
)
Nodo.save()


person = Person.get(Person.first_name == 'Levani')
print(person.first_name)
print(person.last_name)
print(person.birthday)