from starlette.config import Config

config = Config(".env")

DEBUG = config("DEBUG", default=True)

PROJECT_NAME = config("PROJECT_NAME", default="author-service")
OPENAPI_URL = "/api/v1/authors/openapi.json"
DOCS_URL = "/api/v1/authors/docs"
API_PREFIX = "/api/v1/authors"
VERSION = "0.0.1"
