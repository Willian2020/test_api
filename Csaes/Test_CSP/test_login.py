# !/usr/bin/python3
# _*_ coding:utf-8 _*_
# Author : william - xwj
# Github: https://githun.com/
# CreatDate : 2020/9/4-9:54
# Description : PyCharm
# 项目名称：test_api
# 当前用户/文件名： Administrator /test_login
import requests
from ddt import  ddt,data,file_data,unpack
import unittest
from Config import path_configuration
from common import base_api
from common.readexcel import ExcelUtil
@ddt
class Test_LogIn(unittest.TestCase):
    filename = path_configuration.CSP_data_path + r"\test_login.xlsx"
    report_filename =  path_configuration.CSP__report_path + r"\result.xlsx"
    list_data = ExcelUtil(filename).dict_data()
    @data(*list_data)
    def test_login(self,list_data):
        s = requests.session()
        res= base_api.send_requests(s,list_data)
        return res

if __name__ == '__main__':
    unittest.main()