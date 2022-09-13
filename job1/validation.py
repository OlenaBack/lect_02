from common import common, validation
from flask import request


def validate(request_input: request) -> str:
    result = validation.validate_request(request_input)
    if not result == common.EMPTY_STRING:
        return result

    inputs = request_input.json
    result = validation.validate_date_input(inputs, "date")
    result += validation.validate_property_exists(inputs, "raw_dir")
    return result
