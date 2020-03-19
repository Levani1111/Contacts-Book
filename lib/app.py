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
    bithday = '11/11/1999'
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
person = Person.get(Person.first_name == 'Levani')
print(person.first_name)
print(person.last_name)
print(person.birthday)