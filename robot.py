import requests

url = "https://oapi.dingtalk.com/robot/send?access_token=05493a7395f447d8e9a477dfc07aa85c73665145bdfbf14f51a8ab4ffd64b2ef"
content = """
自动化测试结果 \n>
测试开始时间：\n>
测试执行时间：\n>
用例数：\n>
通过：**<font color=#00FF00>1</font>**\n>
失败：**<font color=#FF0000>1</font>**\n>
通过率："""
requests.post(
    url,
    json={
        "msgtype": "markdown",
        "markdown": {"title": "自动化测试结果", "text": content},
    },
)
