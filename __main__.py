from src.api.access_token import access_token
from src.input.excel_reader import ExcelReader

# test_simple.py
# print("刘同鑫大帅哥")

# dept_id = 981231687 # 根组织机构id
agent_id = "4095306262"
access_token = access_token()
#
# subList = list_all_sub(access_token, dept_id)
#
# all_users = []
# for dept in subList:
#     users = list_sample_by_dept_id(access_token, dept['dept_id'])
#     all_users.extend(users)
#
# for user in all_users:
#     print(user)
#
#
user_input_path = input()
# user_input_path = '/Users/mac/Documents/学校行政/钉钉/薪酬发放/教职工工资表-工资汇总—学校定稿_dev.xlsx'
# user_input_path = '/Users/mac/Documents/学校行政/钉钉/薪酬发放/教职工工资表-工资汇总_---明博.xlsx'

excel_reader = ExcelReader(access_token, agent_id, user_input_path)
excel_reader.read_write()
# xls = pd.read_excel(user_input_path, sheet_name=None)

# user_id = "020116402938781404" # 马恩方
# user_id = "011154680423979976" # 石涛

# send_msg(access_token, agent_id, user_id, "石涛老师，把老师的工资条信息发到这里怎么样？[大笑]")
