'''
RUN:
    - python copy_alert_enrichment.py
Requirements:
    - Source API Key
    - Destination API Key
'''

import requests

TOKEN_SOURCE = 'xxxxx'  # Source API Key
TOKEN_DEST = 'xxxxxx'  # Destination API Key

BASE_URL_SOURCE = "https://api.bigpanda.io"
BASE_URL_DEST = "https://api.bigpanda.io"

# List of tags to copy from source into destination
TAGS_LIST = ["atm_status",
             "eventid_extract"]

headers_SOURCE = {
    "Authorization": f"Bearer {TOKEN_SOURCE}",
    "Content-Type": "application/json"
}
headers_DEST = {
    "Authorization": f"Bearer {TOKEN_DEST}",
    "Content-Type": "application/json"
}

for tag in TAGS_LIST:
    url = f'{BASE_URL_SOURCE}/resources/v2.0/enrichments-config/tags/{tag}'
    source_req = requests.get(url, headers=headers_SOURCE)
    source_tags = source_req.json()

    dest_url = f'{BASE_URL_DEST}/resources/v2.0/alert-enrichments/'
    for payload in source_tags["data"][0]["enrichments"]:
        dest_req = str(payload).replace("'", '"')
        dest_req = dest_req.replace("True", "true")
        dest_req = dest_req.replace("False", "false")
        dest_req = dest_req.replace("None", "null")

        req = requests.post(dest_url, data=dest_req, headers=headers_DEST)
        print(f'Tag: {tag} - HTTP RESPONSE : {req.status_code}')
