import os
import sqlalchemy as sa
from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field
from sqlalchemy.orm import (    
    DeclarativeBase,
    backref,
    relationship,
    sessionmaker,
    mapped_column,
    Mapped,
)

def create_memory_engine():
   return sa.create_engine("sqlite:///:memory:")
def create_engine():
    current_directory = os.getcwd()
    db_path = os.path.join(current_directory,"flaskdb.db")
    return sa.create_engine("sqlite:///" + db_path)

engine =  create_engine()
Session = sessionmaker(engine)
Session.configure(bind=engine)

class Base(DeclarativeBase):
    pass

# Many Books to one Author
class Author(Base):
    __tablename__ = "authors"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)

    def __repr__(self):
        return f"<Author(name={self.name!r})>"

class Book(Base):
    __tablename__ = "books"
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column()
    author_id: Mapped[int] = mapped_column(sa.ForeignKey("authors.id"))
    author: Mapped["Author"] = relationship("Author", backref=backref("books"))

