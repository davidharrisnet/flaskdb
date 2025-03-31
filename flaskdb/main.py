from .schemas import AuthorSchema, BookSchema, HobbySchema, PersonSchema
from .db import Base, engine, Session, Author, Book, Hobby, Person

Base.metadata.create_all(engine)

author = Author(name="Chuck Paluhniuk")
author_schema = AuthorSchema()
book = Book(title="Fight Club", author=author)

"""
with Session() as session:
    session.add(author)
    session.add(book)
    session.commit()

    dump_data = author_schema.dump(author)
    print(dump_data)
    # {'id': 1, 'name': 'Chuck Paluhniuk', 'books': [1]}

with Session() as session:
    load_data = author_schema.load(dump_data, session=session)
    print(load_data)
"""

person1 = Person(name="Jack")
person2 = Person(name="Jon")
person_schema = PersonSchema()

hobby1 = Hobby(name="cards")
hobby2 = Hobby(name="darts")
hobby_schema = HobbySchema()


person1.hobbies = [hobby1, hobby2]
person1.add(hobby2)
person2.add(hobby1)
person2.add(hobby2)

with Session() as session:
    session.add(person1)
    session.add(person2)
    session.add(hobby1)
    session.add(hobby2)
    session.commit()

