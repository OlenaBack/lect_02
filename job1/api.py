import requests
import common.common as common
API_URL = 'https://fake-api-vycpfa6oca-uc.a.run.app/'


def get_sales(date: str, page: int) -> str:
    headers = {'Authorization': common.AUTH_TOKEN}
    url = '{base_url}sales?date={date}&page={page}'.format(base_url=API_URL, date=date, page=page)
    response = requests.get(url, headers=headers)
    response_status_code = response.status_code
    if response_status_code != common.SUCCESS_STATUS_CODE:
        return common.EMPTY_STRING
    return response.text
