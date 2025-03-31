import os

from sqlalchemy import (MetaData, 
                        Table, 
                        Column, 
                        Integer, 
                        String,                          
                        ForeignKey,
                        create_engine)

def engine():
    current_directory = os.getcwd()
    db_path = os.path.join(current_directory,"sa.db")
    return create_engine("sqlite:///" + db_path)

engine = engine()
metadata = MetaData()

user_table = Table(
    "user",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String(30))
)

address_table = Table(
    "address",
    metadata,
    Column("id", Integer,primary_key=True),
    Column("user_id", ForeignKey("user.id")),
    Column("address", String, nullable=False)    
)

metadata.create_all(engine)