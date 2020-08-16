from fastapi import FastAPI

from app.api.authors import authors
from app.core import config
from app.db.db import database, engine, metadata

app = FastAPI(openapi_url=config.OPENAPI_URL,
              docs_url=config.DOCS_URL,
              debug=config.DEBUG,
              title=config.PROJECT_NAME,
              version=config.VERSION)
app.include_router(authors, prefix=config.API_PREFIX, tags=['authors'])
metadata.create_all(engine)


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()
