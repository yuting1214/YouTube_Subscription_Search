import json
import os
from langchain.docstore.document import Document

def load_json_from_file(file_path, default_value=None):
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except Exception as e:
        print(f"No such file or directory; Creating a new one.")
        return default_value

def process_and_append_to_json(new_data, file_path):
    # Check if the file exists
    if os.path.isfile(file_path):
        with open(file_path, 'r') as file:
            existing_data = json.load(file)
    else:
        existing_data = {}

    # Update only the keys that are not present in existing_data
    for key in new_data:
        if key not in existing_data:
            existing_data[key] = new_data[key]

    with open(file_path, 'w') as file:
        json.dump(existing_data, file, indent=4)

# Transform json format into langchain doc format
def json_documentify(channel_video_list):
    docs = []
    for channel_id, value in channel_video_list.items():
        metadata = dict(channel_id=channel_id)
        docs.append(Document(page_content=str(value['video']['video_title'][:50]), metadata=metadata))
    return docs