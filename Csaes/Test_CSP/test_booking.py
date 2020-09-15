# !/usr/bin/python3
# _*_ coding:utf-8 _*_
# Author : william - xwj
# Github: https://githun.com/
# CreatDate : 2020/8/27-20:25
# Description : PyCharm
# 项目名称：test_cityocean_api
# 当前用户/文件名： Administrator /test_booking
from ddt import ddt,data,file_data,unpack
import unittest
import requests
from Config import path_configuration
from common import base_api
from common.readexcel import ExcelUtil
@ddt
class Test_Booking(unittest.TestCase):
    filename = path_configuration.CSP_data_path + r"\creat_booking.xlsx"
    report_filename = path_configuration.CSP__report_path + r"\result.xlsx"
    list_data = ExcelUtil(filename).dict_data()
    @data(*list_data)
    def test_booking(self,data):
        s = requests.session()
        res = base_api.send_requests(s,data)
        return res
if __name__ == '__main__':
    unittest.main()