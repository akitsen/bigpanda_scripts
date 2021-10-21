'''
RUN:
    - python update_environment_sources.py
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


def http_put(url, payload):
    request_headers = {"Authorization": f"Bearer {API_TOKEN}",
                       "Content-Type": "application/json"}

    source_req = requests.put(f'https://api.bigpanda.io{url}', data=payload, headers=request_headers)
    print(source_req.status_code)
    print(source_req)


def http_get(url):
    request_headers = {"Authorization": f"Bearer {API_TOKEN}",
                       "Content-Type": "application/json"}

    source_req = requests.get(f'https://api.bigpanda.io{url}', headers=request_headers)

    return source_req.json()


environments = http_get('/web/environments')
print(environments)
for env in environments["item"]:
    if TARGET_SOURCE in str(env):
        data = {}
        data["name"] = env["name"]
        data["_id"] = env["_id"]
        data["filter"] = str(env["filter"]).replace("'", "\"").replace("True", "true")
        data["filter"] = data["filter"].replace(TARGET_SOURCE, REPLACEMENT_SOURCE)

        json_data = json.dumps(data)
        print(json_data)

        print(f'UPDATING - Environment: {env["name"]}')
        print(f'\tEXISTING FILTER {env["filter"]}')
        print(f'\tNEW FILTER {data["filter"]}')
        print(f'\tTARGET SOURCE {TARGET_SOURCE}')
        print(f'\tREPLACEMENT SOURCE {REPLACEMENT_SOURCE}')

        if SAFETY_ON:
            print('SAFETY_ON = TRUE - Set to false in order to execute. ')
        else:
            http_put(f'/web/environments/{env["_id"]}?_roles=skip', json_data)
    else:
        print(f'NO CHANGE - Environment: {env["name"]} - No source to modify')
