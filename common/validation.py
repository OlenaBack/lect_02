import common.common as common
import datetime


def validate(inputs: dict) -> str:
    result = common.EMPTY_STRING

    if not ("date" in inputs.keys()):
        result += common.DATE_MISSING_ERROR_MESSAGE
    else:
        date_string = inputs["date"]
        try:
            datetime.datetime.strptime(date_string, common.DATE_FORMAT)
        except ValueError:
            result += common.DATE_FORMAT_ERROR

    if not ("raw_dir" in inputs.keys()):
        result += common.PATH_MISSING_ERROR_MESSAGE

    return result
