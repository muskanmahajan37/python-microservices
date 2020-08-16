from app.db.db import books, database
from app.schemas.book import BookIn


async def add_book(book_in: BookIn):
    query = books.insert().values(**book_in.dict())

    return await database.execute(query=query)


async def get_all_books():
    query = books.select()
    return await database.fetch_all(query=query)


async def get_book(id):
    query = books.select(books.c.id == id)
    return await database.fetch_one(query=query)


async def delete_book(id):
    query = books.delete().where(books.c.id == id)
    return await database.execute(query=query)


async def update_book(id: int, book_update: BookIn):
    query = (
        books.update().where(books.c.id == id).
            values(**book_update.dict())
    )
    return await database.execute(query=query)
