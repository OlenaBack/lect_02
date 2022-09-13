import common.common as common
import datetime
from flask import request


def validate_request(payload: request) -> str:
    try:
        payload.json
        return common.EMPTY_STRING
    except:
        return common.INVALID_REQUEST


def validate_property_exists(inputs: dict, key: str) -> str:
    result = common.EMPTY_STRING

    if (not (key in inputs.keys())) or (inputs[key] == common.EMPTY_STRING):
        result += f"Property {key} is missing. "

    return result


def validate_date_input(inputs: dict, date_key: str) -> str:
    result = validate_property_exists(inputs, date_key)
    if result == common.EMPTY_STRING:
        date_string = inputs[date_key]
        try:
            datetime.datetime.strptime(date_string, common.DATE_FORMAT)
        except ValueError:
            result = common.DATE_FORMAT_ERROR
    return result
