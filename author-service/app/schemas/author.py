from typing import Optional

from pydantic import BaseModel


class AuthorIn(BaseModel):
    name: str
    country: Optional[str] = None


class AuthorRead(AuthorIn):
    id: int


class AuthorUpdate(AuthorIn):
    name: Optional[str] = None
