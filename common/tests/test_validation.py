import flask

import job1.tests.test_common as test_common
import common.validation as validation
import common.common as common
from flask import request
from unittest import TestCase, mock


class ValidationFunctionTestCase(TestCase):

    def test_validate_date_input_when_date_valid(self):
        result = validation.validate_date_input({'date': test_common.FAKE_DATE}, "date")
        self.assertEqual(common.EMPTY_STRING, result)

    def test_validate_date_when_no_date(self):
        result = validation.validate_date_input({'raw_dir': test_common.FAKE_RAW_DIR}, "date")
        self.assertEqual(f"Property date is missing. ", result)

    def test_validate_date_when_invalid_date(self):
        result = validation.validate_date_input({'date': 'invalid'}, "date")
        self.assertEqual(common.DATE_FORMAT_ERROR, result)

    def test_validate_request_when_invalid_json(self):
        mock_side_effect = mock.MagicMock()
        mock_side_effect.side_effect = Exception()
        request_mock = mock.patch.object(flask.request, '')
        request_mock.json = mock_side_effect
        result = validation.validate_request(request_mock)
        self.assertEqual(common.INVALID_REQUEST, result)
