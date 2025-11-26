from src.api.access_token import access_token
from src.api.dept import list_all_sub
from src.api.user import list_sample_by_dept_id
from src.api.msg_sender import send_msg
# test_simple.py
# print("刘同鑫大帅哥")

dept_id = 981231687 # 根组织机构id
agent_id = "4095306262"
access_token = access_token()

subList = list_all_sub(access_token, dept_id)

all_users = []
for dept in subList:
    users = list_sample_by_dept_id(access_token, dept['dept_id'])
    all_users.extend(users)

for user in all_users:
    print(user)


# user_id = "020116402938781404"

send_msg(access_token, agent_id, user_id, "测试消息发送")
