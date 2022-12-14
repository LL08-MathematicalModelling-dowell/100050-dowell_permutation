import json
import requests
import pprint

from datetime import datetime


def get_event_id():
    dd = datetime.now()
    time = dd.strftime("%d:%m:%Y,%H:%M:%S")
    url = "https://100003.pythonanywhere.com/event_creation"

    data = {
        "platformcode": "FB",
        "citycode": "101",
        "daycode": "0",
        "dbcode": "pfm",
        "ip_address": "192.168.0.41",
        "login_id": "lav",
        "session_id": "new",
        "processcode": "1",
        "regional_time": time,
        "dowell_time": time,
        "location": "22446576",
        "objectcode": "1",
        "instancecode": "100051",
        "context": "afdafa ",
        "document_id": "3004",
        "rules": "some rules",
        "status": "work",
        "data_type": "learn",
        "purpose_of_usage": "add",
        "colour": "color value",
        "hashtags": "hash tag alue",
        "mentions": "mentions value",
        "emojis": "emojis",
    }

    r = requests.post(url, json=data)
    return r.text


url = "http://100002.pythonanywhere.com/"

payload = json.dumps(
    {
        "cluster": "Documents",
        "database": "Documentation",
        "collection": "permutation",
        "document": "permutation",
        "team_member_ID": "100084007",
        "function_ID": "ABCDE",
        "command": "insert",
        "field": {"eventId": get_event_id(), "name": "manish"},
        "update_field": {"int_wf_position": 8},
        "platform": "bangalore",
    }
)
headers = {"Content-Type": "application/json"}

response = requests.request("POST", url, headers=headers, data=payload)
print(response.text)
