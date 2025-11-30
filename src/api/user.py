import requests




def list_sample_by_dept_id(access_token, dept_id):
    url = "https://oapi.dingtalk.com/topapi/user/listsimple"

    params = {"access_token": access_token}

    data = {
        "dept_id": dept_id,
        "cursor": 0,
        "size": 500,
        "order_field": "modify_desc",
        # "contain_access_limit": True,
        "language": "zh_CN"
    }

    try:
        resp = requests.post(url, data=data, params=params)
        if resp.status_code != 200:
            print(f"Error: Received status code {resp.status_code}, errmsg: {resp.text}")
            return None
        # print(resp)
        return resp.json()['result']['list']
    except Exception as e:
        print(e)
def get_by_user_id(access_token, user_id):
    url = "https://oapi.dingtalk.com/topapi/v2/user/get"

    params = {"access_token": access_token}

    data = {
        "userid": user_id,
        "language": "zh_CN"
    }

    try:
        resp = requests.post(url, data=data, params=params)
        if resp.status_code != 200:
            print(f"Error: Received status code {resp.status_code}, errmsg: {resp.text}")
            return None
        # print(resp)
        return resp.json()['result']
    except Exception as e:
        print(e)

