from enum import Enum


class GlobalErrors(Enum):
    WRONG_STATUS_CODE = 'Status code is different than expected!!'
    WRONG_ELEMENT_COUNT = 'Number of items not equal to expected!!'
