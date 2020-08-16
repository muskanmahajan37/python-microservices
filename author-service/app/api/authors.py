from app.db import manage
from app.schemas.author import AuthorIn, AuthorRead
from fastapi import APIRouter, HTTPException

authors = APIRouter()


@authors.post("/", response_model=AuthorRead, status_code=201)
async def create_author(author_in: AuthorIn):
    author_id = await manage.create_author(author_in=author_in)
    response = {
        "id": author_id,
        **author_in.dict()
    }

    return response


@authors.get("/{id}/", response_model=AuthorRead)
async def get_author(id: int):
    author = await manage.get_author(id)
    if not author:
        raise HTTPException(status_code=404, detail="Author not found")
    return author
