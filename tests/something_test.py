import requests
from src.enums.global_enums import GlobalErrors
from jsonschema import validate
from src.schemas.post import POST_SCHEMA
from src.baseclasses.response import Response
from configuration import *


def test_url():
    request_ = requests.get(url=SERVICE_URL)
    response = Response(request_)
    response.assert_status_code(200).validate_(POST_SCHEMA)
