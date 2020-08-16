from app.db.db import authors, database
from app.schemas.author import AuthorIn


async def create_author(author_in: AuthorIn):
    query = authors.insert().values(**author_in.dict())
    return await database.execute(query=query)


async def get_author(id: int):
    query = authors.select(authors.c.id == id)
    return await database.fetch_one(query=query)
