import job1.api as api
import common.common as common
import common.storage as storage
import re


def handle_request(path: str, date: str):
    page = common.START_PAGE
    content = common.EMPTY_STRING
    while True:
        response = api.get_sales(date, page)
        if response == common.EMPTY_STRING:
            break
        else:
            content_without_brackets = re.search("\\[(.*)\\]", response).group(1)
            content += f"{content_without_brackets}, "
            page += 1
    if content != common.EMPTY_STRING:
        file_name = f"{date}.json"
        storage.save_to_disk(f"[{content.rstrip(', ')}]", path, file_name)
