import os
from datetime import datetime

import pytest

data = {"passed":0,"failed":0,}

def pytest_runtest_logreport(report:pytest.TestReport):
    if report.when=='call':
        data[report.outcome]+=1

def pytest_collection_finish(session:pytest.Session):
    data["tatal"]=len(session.items)

def pytest_configure():
    """用例开始前执行"""
    data["start_time"]=datetime.now()
    print(f"{datetime.now()} pytest开始执行")


def pytest_unconfigure():
    """用例结束后执行"""
    data["end_time"]=datetime.now()
    print(f"{datetime.now()} pytest结束执行")
    data["run_time"]=data["end_time"]-data["start_time"]
    data['pass_radio']=data['passed']/data['total']*100
    data['pass_radio']=f"{data['pass_radio']:.2f}%"
