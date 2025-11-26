
import requests



def list_sub(access_token, dept_id):

    url = "https://oapi.dingtalk.com/topapi/v2/department/listsub"

    params = {"access_token": access_token}

    data = {
        "dept_id": dept_id,
        "language": "zh_CN"
    }

    try:
        resp = requests.post(url, data=data, params=params)
        # print(resp)
        return resp.json()['result']
    except Exception as e:
        print(e)


#
# # 异步批量查询部门信息
# async def async_list_sub(access_token, dept_ids):
#     """基础使用示例"""
#     url = "https://oapi.dingtalk.com/topapi/v2/department/listsub"
#     client = AsyncHTTPClient()
#
#     # # 单个请求
#     # async with aiohttp.ClientSession() as session:
#     #     result = await client.fetch(session, )
#     #     print(f"单个请求结果: {result['status']}")
#     #
#
#     data_pairs = []
#     for dept_id in dept_ids:
#         data_pairs.append({
#             "dept_id": dept_id,
#             "language": "zh_CN"
#         })
#
#     params = { "access_token": access_token }
#
#     return await client.batch_post_url(url, data_pairs, params)



def list_all_sub(access_token, dept_id):
    sub_list = list_sub(access_token, dept_id)
    all_depts = []
    if sub_list and len(sub_list) > 0:
        for dept in sub_list:
            all_depts.append(dept)
            child_depts = list_all_sub(access_token, dept['dept_id'])
            all_depts.extend(child_depts)

    return all_depts