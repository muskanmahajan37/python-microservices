from typing import List

from fastapi import APIRouter, HTTPException

from app.db import manage
from app.schemas.book import BookIn, BookUpdate, BookRead
from app.service.service import is_author_in_database
books = APIRouter()


@books.get("/", )
async def get_books():
    return await manage.get_all_books()



@books.post("/")
async def add_book(book_in: BookIn):
    for author_id in book_in.authors_id:
        if not is_author_in_database(author_id):
            raise HTTPException(status_code=404, detail=f"Author with {author_id} not found")
    book_id = await manage.add_book(book_in)
    response = {
        'id': book_id,
        **book_in.dict()
    }

    return response


@books.put("/{id}")
async def update_book(id: int, book_update: BookUpdate):
    book = await manage.get_book(id)
    if not book:
        raise HTTPException(status_code=404, detail="Book doesn't exist")
    update_data = book_update.dict(exclude_unset=True)

    if 'authors_id' in update_data:
        for author_id in book_update.authors_id:
            if not is_author_in_database(author_id):
                raise HTTPException(status_code=404, detail=f"Author with {id} not found")
    book_in_db = BookIn(**book)
    updated_book = book_in_db.copy(update=update_data)
    return await manage.update_book(id, updated_book)


@books.delete("/{id}")
async def delete_book(id: int):
    book = await manage.get_book(id)
    if not book:
        raise HTTPException(status_code=404, detail="Book doesn't exist")
    return await manage.delete_book(id)
