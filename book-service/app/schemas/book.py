from typing import List, Optional

from pydantic import BaseModel


class BookIn(BaseModel):
    name: str
    genres: List[str]
    authors_id: List[int]
    language: str


class BookRead(BookIn):
    id: int


class BookUpdate(BookIn):
    name: Optional[str] = None
    genres: Optional[List[str]] = None
    authors_id: Optional[List[int]] = None
    language: Optional[str] = None
