# !/usr/bin/python3
# _*_ coding:utf-8 _*_
# Author : william - xwj
# Github: https://githun.com/
# CreatDate : 2020/9/3-9:54
# Description : PyCharm
# 项目名称：test_api
# 当前用户/文件名： Administrator /base_api
import json
import requests
import unittest
from common.readexcel import ExcelUtil
from common.writeexcel import copy_excel, Write_excel
# @unittest.skipIf(testdata['perform']  == "yes","测试用例不执行")
def send_requests(s, testdata):
    '''封装requests请求'''
    method = testdata["method"]
    url = testdata["url"]
    # url后面的params参数
    try:
        params = eval(testdata["params"])
    except:
        params = None
    # 请求头部headers
    try:
        headers = eval(testdata["headers"])
        # print("请求头部：%s" % headers +'\n')
    except:
        headers = None
    # post请求body类型
    type = testdata["type"]

    test_nub = testdata['id']
    print("*******正在执行用例：-----  %s  ----**********" % test_nub+'\n')
    print("请求方式：%s, 请求url:%s" % (method, url)+'\n')
    print("请求params：%s" % params+'\n')

    # post请求body内容
    try:
        bodydata = eval(testdata["body"])
    except:
        bodydata = {}

    # 判断传data数据还是json
    if type == "data":
        body = bodydata
        #body = "{\r\n\"cargoReadyDate\": \"2020-07-07T10:20:01.379Z\",\r\n\"consigneeCustomerId\": \"32809880-4fc3-447a-b19e-decaacbe8b37\",\r\n\"containerType\": \"[{'value':1,'name':'20GP'}]\",\r\n\"destinationIsRequireTruck\": false,\r\n\"destinationPortId\": \"72528faf-4006-4b47-b16f-0dc3b6ae7158\",\r\n\"dimensionsUnitId\": 1,\r\n\"freightMethodType\": 1,\r\n\"incotermsId\": \"d952c54f-5b36-438d-8695-4c2f9edf77d2\",\r\n\"name\": \"\",\r\n\"originPortId\": \"b3df90cb-c0cc-4ee1-a6dd-2dcf7624dee0\",\r\n\"quantityUnitCode\": \"ctn\",\r\n\"shipmentType\": 0,\r\n\"shipperCustomerId\": \"89796121-32f7-466d-898b-f212674d3571\",\r\n\"shipperPartnerId\": \"1049d705-1d0a-4aa5-fad0-08d81bd78e3d\",\r\n\"specialInstructions\": \"\",\r\n\"status\": 4,\r\n\"tradeType\": 1,\r\n\"unitConvertType\": 0,\r\n\"volumeUnitCode\": \"TJDWCBM\",\r\n\"volumeUnitString\": \"cbm\",\r\n\"weightUnitCode\": \"ZLDWKGS\",\r\n\"weightUnitString\": \"kg\"\r\n}"
    elif type == "json":
        body = json.dumps(bodydata)
        #body = "{\r\n\"cargoReadyDate\": \"2020-07-07T10:20:01.379Z\",\r\n\"consigneeCustomerId\": \"32809880-4fc3-447a-b19e-decaacbe8b37\",\r\n\"containerType\": \"[{'value':1,'name':'20GP'}]\",\r\n\"destinationIsRequireTruck\": false,\r\n\"destinationPortId\": \"72528faf-4006-4b47-b16f-0dc3b6ae7158\",\r\n\"dimensionsUnitId\": 1,\r\n\"freightMethodType\": 1,\r\n\"incotermsId\": \"d952c54f-5b36-438d-8695-4c2f9edf77d2\",\r\n\"name\": \"\",\r\n\"originPortId\": \"b3df90cb-c0cc-4ee1-a6dd-2dcf7624dee0\",\r\n\"quantityUnitCode\": \"ctn\",\r\n\"shipmentType\": 0,\r\n\"shipperCustomerId\": \"89796121-32f7-466d-898b-f212674d3571\",\r\n\"shipperPartnerId\": \"1049d705-1d0a-4aa5-fad0-08d81bd78e3d\",\r\n\"specialInstructions\": \"\",\r\n\"status\": 4,\r\n\"tradeType\": 1,\r\n\"unitConvertType\": 0,\r\n\"volumeUnitCode\": \"TJDWCBM\",\r\n\"volumeUnitString\": \"cbm\",\r\n\"weightUnitCode\": \"ZLDWKGS\",\r\n\"weightUnitString\": \"kg\"\r\n}"

    else:
        body = bodydata
    if method == "post":
        print("post请求body类型为：%s ,body内容为：%s" % (type, body))
        # print("\n")

    verify = False
    res = {}   # 接受返回数据

    try:
        r = s.request(method=method,
                      url=url,
                      params=params,
                      headers=headers,
                      data=body,
                      verify=verify
                       )
        print("页面返回信息：%s" % r.content.decode("utf-8"))
        res['id'] = testdata['id']
        res['rowNum'] = testdata['rowNum']
        res["statuscode"] = str(r.status_code)  # 状态码转成str
        res["text"] = r.content.decode("utf-8")
        res["times"] = str(r.elapsed.total_seconds())   # 接口请求时间转str
        if res["statuscode"] != "200":
            res["error"] = res["text"]
        else:
            res["error"] = ""
        res["msg"] = ""
        if testdata["checkpoint"] in res["text"]:
            res["result"] = "pass"
            print("用例测试结果:   %s---->%s" % (test_nub, res["result"]))
        else:
            res["result"] = "fail"
        return res
    except Exception as msg:
        res["msg"] = str(msg)
        return res

def wirte_result(result, filename="result.xlsx"):
    # 返回结果的行数row_nub
    row_nub = result['rowNum']
    # 写入statuscode
    wt = Write_excel(filename)
    wt.write(row_nub, 8, result['statuscode'])           # 写入返回状态码statuscode,第8列
    wt.write(row_nub, 9, result['times'])                # 耗时
    wt.write(row_nub, 10, result['error'])               # 状态码非200时的返回信息
    wt.write(row_nub, 12, result['result'])              # 测试结果 pass 还是fail
    wt.write(row_nub, 13, result['msg'])                 # 抛异常

if __name__ == "__main__":
    filename = get_path()+r"\test_login.xlsx"
    report_filename = repot_path() + r"\result.xlsx"
    data = ExcelUtil(filename).dict_data()
    s = requests.session()
    res = send_requests(s,data[0])
    print(type(data[0]['headers']))
    # copy_excel(filename, report_filename)
    # wirte_result(res, filename=report_filename)