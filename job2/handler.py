from common import storage
from fastavro import writer, parse_schema
import json

schema = {
    "type": "record",
    "name": "lecture_02_sales_data",
    "fields": [
        {
            "name": "client",
            "type": ["string", "null"]
        },
        {
            "name": "purchase_date",
            "type": ["string", "null"]
        },
        {
            "name": "product",
            "type": ["string", "null"]
        },
        {
            "name": "price",
            "type": ["int", "null"]
        }
    ]
}


def handle_request(source_folder: str, destination_folder: str):
    if storage.is_folder_empty(source_folder):
        return
    storage.make_folder(destination_folder)
    for file in storage.list_folder(source_folder):
        with open(storage.get_full_path_to_file_in_folder(file, source_folder), "r", encoding="utf8") as json_file:
            with open(storage.get_full_path_to_file_in_folder(f"{storage.get_file_name(file)}.avro", destination_folder), "wb") \
                    as avro_file:
                parsed_schema = parse_schema(schema)
                writer(avro_file, parsed_schema, json.loads(json_file.read()))
