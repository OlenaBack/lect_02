"""
This file contains the controller that accepts command via HTTP
and trigger business logic layer
"""

from flask import Flask, request
from flask import typing as flask_typing
from common import common
from job1 import validation, handler

if not common.AUTH_TOKEN:
    print("AUTH_TOKEN environment variable must be set")

app = Flask(__name__)


@app.route('/', methods=['POST'])
def main() -> flask_typing.ResponseReturnValue:
    validation_result = validation.validate(request)
    if validation_result != common.EMPTY_STRING:
        return {
                   "message": validation_result,
               }, 400

    input_data: dict = request.json
    handler.handle_request(input_data["raw_dir"], input_data["date"])
    return {
               "message": "Data retrieved successfully from API",
           }, 201


if __name__ == "__main__":
    app.run(debug=True, host="localhost", port=8081)