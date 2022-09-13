from unittest import TestCase, mock
import common.common as common
import requests
import job1.api as api
import test_common as test_common


class GetSalesTestCase(TestCase):
    @mock.patch.object(requests, 'get')
    def test_get_sales_with_404_in_response(
            self,
            mock_get
    ):
        mock_response = mock.Mock()
        mock_get.return_value = mock_response
        mock_response.status_code = 404
        result = api.get_sales(test_common.FAKE_DATE, test_common.FAKE_RAW_DIR)
        self.assertEqual(common.EMPTY_STRING, result)

    @mock.patch.object(requests, 'get')
    def test_get_sales_with_200_in_response(
            self,
            mock_get
    ):
        mock_response = mock.Mock()
        mock_get.return_value = mock_response
        mock_response.status_code = common.SUCCESS_STATUS_CODE
        mock_response.text = '[{"p1":"v1"}]'
        result = api.get_sales(test_common.FAKE_DATE, test_common.FAKE_RAW_DIR)
        self.assertEqual(mock_response.text, result)


