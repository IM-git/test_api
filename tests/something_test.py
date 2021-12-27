import requests
from src.enums.global_enums import GlobalErrors
from jsonschema import validate
from src.schemas.post import POST_SCHEMA
from src.baseclasses.response import Response
from src.pydantic_shemas.post import Post
from src.schemas.user import User
from configuration import *


def test_url(get_users):
    Response(get_users)
    # request_ = requests.get(url=SERVICE_URL)
    # test_object = Response(request_)
    # test_object.assert_status_code(200).validate_(User)
