'''
RUN:
    - python update_alert_enrichment_sources.py
'''

import json
import requests

API_TOKEN = 'INSERT_API_TOKEN'
TARGET_SOURCE = 'INSERT_TARGET_SOURCE'
REPLACEMENT_SOURCE = 'INSERT_REPLACEMENT_SOURCE'

# True = output will signify what will change, but no action taken.
# False = will outline and execute changes.

SAFETY_ON = True


def http_patch(url, payload):
    request_headers = {"Authorization": f"Bearer {API_TOKEN}",
                       "Content-Type": "application/json"}

    source_req = requests.patch(f'https://api.bigpanda.io{url}', data=payload, headers=request_headers)
    if source_req.status_code == 200:
        print('UPDATING : HTTP 200 Successfully replaced source')


def http_get(url):
    request_headers = {"Authorization": f"Bearer {API_TOKEN}",
                       "Content-Type": "application/json"}

    source_req = requests.get(f'https://api.bigpanda.io{url}', headers=request_headers)

    return source_req.json()


alert_enrichments = http_get('/resources/v2.0/enrichments-config/tags')

for enrichment in alert_enrichments['data']:
    for i in enrichment['enrichments']:

        if i["when"]:
            if TARGET_SOURCE in str(i['when']):
                pre_when = (i["when"])
                id = i['id']
                new_when = str(pre_when).replace(TARGET_SOURCE, REPLACEMENT_SOURCE)
                new_when = new_when.replace("'", "\"")

                payload = '{"when":' + new_when + '}'
                print(f'UPDATING - Tag Name: {enrichment["name"]}')
                print(f'\tUPDATING - Existing WHEN: {pre_when}')
                print(f'\tUPDATING - Target WHEN: {TARGET_SOURCE}')
                print(f'\tUPDATING - Replacement Source: {REPLACEMENT_SOURCE}')
                print(f'\tUPDATING - Payload: {payload}')
                if SAFETY_ON:
                    print('SAFETY_ON = TRUE - Set to false in order to execute. ')
                else:
                    http_patch(f'/resources/v2.0/alert-enrichments/{id}', payload)
            else:
                print(f'NO CHANGE - Tag Name: {enrichment["name"]} - No source to modify')
