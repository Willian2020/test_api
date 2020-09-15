# !/usr/bin/python3
# _*_ coding:utf-8 _*_
# Author : william - xwj
# Github: https://githun.com/
# CreatDate : 2020/9/3-19:58
# Description : PyCharm
# 项目名称：test_api
# 当前用户/文件名： Administrator /run_csp

import unittest
import time
from BeautifulReport import BeautifulReport

def run():
    test_dir = r'./Csaes/Test_CSP'
    report_dir1 = "./reports/CSP_test_report"
    now = time.strftime("%Y-%m-%d %H_%M_%S", time.localtime(time.time()))
    report_name = now + "report.html"
    discovery = unittest.defaultTestLoader.discover(start_dir=test_dir, pattern="test*.py")
    runner =BeautifulReport(discovery)
    runner.report( filename= report_name,description="CityOcean自动化测试报告",
                   report_dir =report_dir1
                    )
if __name__ == '__main__':
    run()