from datetime import datetime

import pytest
import requests

data = {
    "passed": 0,
    "failed": 0,
}


def pytest_addoption(parser):
    parser.addini("send_when", help="在如何时候都发送")
    parser.addini("send_url", help="发送地址")


def pytest_runtest_logreport(report: pytest.TestReport):
    """记录运行结果"""
    if report.when == "call":
        data[report.outcome] += 1


def pytest_collection_finish(session: pytest.Session):
    """用例加载完成之后执行，包含全部用例"""
    data["total"] = len(session.items)


def pytest_configure(config: pytest.Config):
    """用例开始前执行"""
    data["start_time"] = datetime.now()
    print(f"{datetime.now()} pytest开始执行")
    data["send_when"] = config.getini("send_when")
    data["send_url"] = config.getini("send_url")


def pytest_unconfigure():
    """用例结束后执行"""
    data["end_time"] = datetime.now()
    print(f"{datetime.now()} pytest结束执行")
    data["run_time"] = data["end_time"] - data["start_time"]
    data["pass_radio"] = data["passed"] / data["total"] * 100
    data["pass_radio"] = f"{data['pass_radio']:.2f}%"
    # assert data['total']==2
    send_resuld()


def send_resuld():
    if not data["send_url"]:
        return
    if data["send_when"] != "every":
        return
    url = data["send_url"]
    content = f"""
    自动化测试结果 \n>
    测试开始时间：{data["start_time"]}\n>
    测试执行时间：{data["run_time"]}\n>
    用例数：{data['total']}\n>
    通过：{data['passed']}\n>
    失败：{data['failed']}\n>
    通过率：{data['pass_radio']}"""
    try:
        requests.post(
            url,
            json={
                "msgtype": "markdown",
                "markdown": {"title": "自动化测试结果", "text": content},
            },
        )
    except Exception:
        pass
    data["send_done"] = 1  # 发送成功
