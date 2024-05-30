import os
from datetime import datetime


def pytest_configure():
    """用例开始前执行"""
    print(f"{datetime.now()} pytest开始执行")


def pytest_unconfigure():
    """用例结束后执行"""
    print(f"{datetime.now()} pytest结束执行")
