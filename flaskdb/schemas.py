from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field
from .db import Author, Book, Person, Hobby, PersonsHobbies

class AuthorSchema(SQLAlchemySchema):
    class Meta:
        model = Author
        load_instance = True  # Optional: deserialize to model instances

    id = auto_field()
    name = auto_field()
    books = auto_field()


class BookSchema(SQLAlchemySchema):
    class Meta:
        model = Book
        load_instance = True

    id = auto_field()
    title = auto_field()
    author_id = auto_field()
    


class PersonSchema(SQLAlchemySchema):
    class Meta:
        model = Person
        load_instance = True  # Optional: deserialize to model instances

    id = auto_field()
    name = auto_field()
    hobbies = auto_field()

class HobbySchema(SQLAlchemySchema):
    
    class Meta:
        model = Hobby
        load_instance = True
    
    id = auto_field()
    name = auto_field()
    persons = auto_field()

class PersonsHobbiesSchema(SQLAlchemySchema):
    class Meta:
        model = PersonsHobbies
        load_instance = True
    id = auto_field()
    person_id  = auto_field()
    hobby_id  = auto_field()