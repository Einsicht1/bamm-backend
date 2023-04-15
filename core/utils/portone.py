import os

import requests


def get_portone_access_token() -> str:
    portone_token_url = "https://api.iamport.kr/users/getToken"
    data = {
        "imp_key": os.environ.get("imp_key"),
        "imp_secret": os.environ.get("imp_secret"),
    }
    res = requests.post(portone_token_url, data=data)
    res_json = res.json()
    access_token = res_json["response"]["access_token"]
    return access_token
