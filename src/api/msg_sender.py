import json

import requests

def send_msg(access_token, agent_id, user_id, message):
    url = "https://oapi.dingtalk.com/topapi/message/corpconversation/asyncsend_v2"

    params = { "access_token": access_token }
    headers = { 'Content-Type': 'application/json' }

    data = {
        "agent_id": agent_id,
        "userid_list": user_id,
        "msg": {
            "msgtype": "text",
            "text": {
                "content": message
            }
        }
    }

    print(f"发送消息给用户: {user_id}，内容: {message }")
    return requests.post(url, headers=headers, data=json.dumps(data), params=params)

