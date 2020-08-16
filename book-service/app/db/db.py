from databases import Database
from sqlalchemy import (Column, Integer, MetaData, String, Table,
                        create_engine, ARRAY)

from app.core import config

DATABASE_URI = config.DATABASE_URI

engine = create_engine(DATABASE_URI)
metadata = MetaData()

books = Table(
    'books',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(100)),
    Column('authors_id', ARRAY(Integer)),
    Column('genres', ARRAY(String)),
    Column('language', String(30)),
)

database = Database(DATABASE_URI)

