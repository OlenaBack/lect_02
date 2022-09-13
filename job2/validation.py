import common.validation as validation
import common.common as common
from flask import request


def validate(inputs: request) -> str:
    result = validation.validate_request(inputs)
    if not result == common.EMPTY_STRING:
        return result

    result = validation.validate_property_exists(inputs, "raw_dir")
    result += validation.validate_property_exists(inputs, "stg_dir")
    return result
