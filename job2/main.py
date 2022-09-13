"""
This file contains the controller that accepts command via HTTP
and trigger business logic layer
"""

from flask import Flask, request
from flask import typing as flask_typing

import comon.common as common
import comon.validation as validation
import job2.handler as handler

app = Flask(__name__)


@app.route('/', methods=['POST'])
def main() -> flask_typing.ResponseReturnValue:

    input_data: dict = request.json

    handler.handle_request(input_data["raw_dir"], input_data["stg_dir"])
    return {
               "message": "Data converted successfully",
           }, 201


if __name__ == "__main__":
    app.run(debug=True, host="localhost", port=8082)