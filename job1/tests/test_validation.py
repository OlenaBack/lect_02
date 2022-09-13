from unittest import TestCase
import job1.tests.test_common as test_common
import common.validation as validation
import common.common as common


class ValidationFunctionTestCase(TestCase):

    def test_validate_when_data_valid(self):
        result = validation.validate({'date': test_common.FAKE_DATE, 'raw_dir': test_common.FAKE_RAW_DIR})
        self.assertEqual(result, common.EMPTY_STRING)

    def test_validate_when_no_date(self):
        result = validation.validate({'raw_dir': test_common.FAKE_RAW_DIR})
        self.assertNotEqual(result, common.EMPTY_STRING)

    def test_validate_when_invalid_date(self):
        result = validation.validate({'date': 'invalid', 'raw_dir': test_common.FAKE_RAW_DIR})
        self.assertNotEqual(result, common.EMPTY_STRING)

    def test_validate_when_no_raw_dir(self):
        result = validation.validate({'date': test_common.FAKE_DATE})
        self.assertNotEqual(result, common.EMPTY_STRING)
