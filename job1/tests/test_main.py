from unittest import TestCase, mock

# NB: avoid relative imports when you will write your code
import job1.main as main
import job1.handler as handler
import common.validation as validation
import job1.tests.test_common as test_common
import common.common as common


class MainFunctionTestCase(TestCase):
    handler.handle_request = mock.Mock()

    @classmethod
    def setUpClass(cls) -> None:
        main.app.testing = True
        cls.client = main.app.test_client()

    @mock.patch('common.validation.validate')
    def test_return_400(self,
                        mock_validate: mock.MagicMock
                        ):
        mock_validate.return_value = common.DATE_FORMAT_ERROR
        resp = self.client.post(
            '/',
            json={
                'raw_dir': test_common.FAKE_RAW_DIR,
                # no 'date' set!
            },
        )
        self.assertEqual(400, resp.status_code)

    @mock.patch('common.validation.validate')
    def test_api_get_sales_called(self,
                                  mock_validate
                                  ):
        mock_validate.return_value = common.EMPTY_STRING
        self.client.post(
            '/',
            json={
                'date': test_common.FAKE_DATE,
                'raw_dir': test_common.FAKE_RAW_DIR,
            },
        )

        handler.handle_request.assert_called_with(test_common.FAKE_RAW_DIR, test_common.FAKE_DATE)

    @mock.patch.object(validation, 'validate')
    def test_return_201_when_all_is_ok(self,
                                       mock_validate
                                       ):
        mock_validate.return_value = common.EMPTY_STRING
        response = self.client.post(
            '/',
            json={
                'date': test_common.FAKE_DATE,
                'raw_dir': '/foo/bar/',
            },
        )

        self.assertEqual(201, response.status_code)
