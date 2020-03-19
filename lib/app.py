from peewee import *
from datetime import date
db = PostgresqlDatabase('contacts', user='postgres', password='',
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
    phone_number = '249-943-0303', email = 'levani@mail.com', birthday = 11/11/1984)
Levani.save()
Charlie = Person(first_name = 'Charlie', last_name='Smith',
    phone_number = '555-555-2524', email = 'charliedo@gmail.com', birthday = 3/9/85 )
Charlie.save()
Sara = Person(first_name = 'Sara', last_name ='Ross',
    phone_number = '434-023-2313', email = 'saralalal@yahoo.com', birthday = 4/22/75)
person = Person.get(Person.first_name == 'Levani')
print(person.first_name)
print(person.last_name)
print(person.birthday)