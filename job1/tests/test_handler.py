from unittest import TestCase, mock

# NB: avoid relative imports when you will write your code
import job1.handler as handler
import common.common as common
import common.storage as storage
import job1.tests.test_common as test_common


class HandlerFunctionTestCase(TestCase):

    @mock.patch('job1.api.get_sales')
    def test_handle_request_when_no_data(
            self,
            get_sales_mock: mock.MagicMock
    ):
        storage.save_to_disk = mock.Mock()
        get_sales_mock.return_value = common.EMPTY_STRING
        handler.handle_request(test_common.FAKE_RAW_DIR, test_common.FAKE_DATE)
        storage.save_to_disk.assert_not_called()
