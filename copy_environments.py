'''
RUN:
    - python copy_environments.py
Requirements:
    - Source API Key
    - Destination API Key
'''

import json
import requests

TOKEN_SOURCE = 'xxxxx'  # Source API Key
TOKEN_DEST = 'xxxxxx'  # Destination API Key

BASE_URL_SOURCE = "https://api.bigpanda.io"
BASE_URL_DEST = "https://api.bigpanda.io"

headers_SOURCE = {
    "Authorization": f"Bearer {TOKEN_SOURCE}",
    "Content-Type": "application/json"
}
headers_DEST = {
    "Authorization": f"Bearer {TOKEN_DEST}",
    "Content-Type": "application/json"
}

url = f'{BASE_URL_SOURCE}/resources/v2.0/environments/'
source_req = requests.get(url, headers=headers_SOURCE)
source_tags = source_req.json()

dest_url = f'{BASE_URL_DEST}/resources/v2.0/environments/'

for payload in source_tags:

    # All doesn't have all the fields.
    if payload["name"] != "All":
        payload.pop("id")
        payload.pop("created_at")
        payload.pop("updated_at")
        payload.pop("updated_by")
        payload.pop("created_by")

        sanitized_filter = (str(payload["filter"]).replace('\'', '\"'))
        payload['filter'] = sanitized_filter

        json_payload = json.dumps(payload)

        req = requests.post(dest_url, data=json_payload, headers=headers_DEST)
        print(f'HTTP: {req.status_code} - {json_payload}')
