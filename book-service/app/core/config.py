from starlette.config import Config

config = Config(".env")
DEBUG = config("DEBUG",default="ABC")
DATABASE_URI = config("DATABASE_URI")
PROJECT_NAME = config("PROJECT_NAME", default="book-service")
OPENAPI_URL = "/api/v1/books/openapi.json"
DOCS_URL = "/api/v1/books/docs"
API_PREFIX = "/api/v1/books"
VERSION = "0.1.1"

