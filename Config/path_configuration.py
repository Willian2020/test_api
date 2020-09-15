# !/usr/bin/python3
# _*_ coding:utf-8 _*_
# Author : william - xwj
# Github: https://githun.com/
# CreatDate : 2020/9/8-19:54
# Description : PyCharm
# 项目名称：test_api
# 当前用户/文件名： Administrator /path_configuration
import os
home_path = os.path.dirname(os.path.dirname(__file__))# 获取当前项目的根目录路径
# print(home_path)
#1、CSP测试数据地址
CSP_data_path = home_path + r"\APi_Data\CSP"
# print(CSP_data_path)
#2、FCM测试数据地址
FCM_data_path = home_path + r"\APi_Data\FCM"
# print(FCM_data_path)
#3、FRM测试数据地址
FRM_data_path = home_path + r"\APi_Data\FRM"
# print(FRM_data_path)
#4、CRM测试数据地址
CRM_data_path = home_path + r"\APi_Data\CRM"
# print(CRM_data_path)
#5、CSP测试报告地址
CSP__report_path = home_path + r"\reports\CSP_test_report"
# print(CSP__report_path)
#4、FCM测试报告地址
FCM__report_path = home_path + r"\reports\FCM_test_report"
# print(FCM__report_path)
#4、FRM测试报告地址
FRM_report_path = home_path + r"\reports\FRM_test_report"
# print(FRM_report_path)
#4、CRM测试报告地址
CRM__report_path = home_path + r"\reports\CRM_test_report"
# print(CRM__report_path)
