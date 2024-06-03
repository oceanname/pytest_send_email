import requests
url=""
content='''
测试结果：<br>
测试开始时间：<br>
测试结束时间：<br>
测试执行时间：<br>
用例数：<br>
通过：<font color='gree'>1</font><br>
失败：<font color='red'>1</font><br>
通过率：'''
requests.post(url,
              json={content:content},)