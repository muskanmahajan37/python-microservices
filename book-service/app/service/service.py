import os

import requests

AUTHOR_SERVICE_URL = "http://localhost:8002/api/v1/authors/"
url = os.environ.get('AUTHOR_SERVICE_HOST_URL') or AUTHOR_SERVICE_URL


def is_author_in_database(author_id: int):
    r = requests.get(f'{url}{author_id}')
    return True if r.status_code == 200 else False
