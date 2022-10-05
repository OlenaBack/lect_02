from flask import Flask, request
from flask import typing as flask_typing
from common import common
from job2 import validation, handler

app = Flask(__name__)


@app.route('/', methods=['POST'])
def main() -> flask_typing.ResponseReturnValue:
    validation_result = validation.validate(request)
    if validation_result != common.EMPTY_STRING:
        return {
                   "message": validation_result,
               }, 400

    input_data: dict = request.json

    handler.handle_request(input_data["raw_dir"], input_data["stg_dir"])
    return {
               "message": "Data converted successfully",
           }, 201


if __name__ == "__main__":
    app.run(debug=True, host="localhost", port=8082)