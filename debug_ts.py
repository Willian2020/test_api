# !/usr/bin/python3
# _*_ coding:utf-8 _*_
# Author : william - xwj
# Github: https://githun.com/
# CreatDate : 2020/9/4-14:40
# Description : PyCharm
# 项目名称：test_api
# 当前用户/文件名： Administrator /debug_ts
import requests

url = "https://test-api.cityocean.com:10001/CSP/Booking/Create?timestamp=1594629881000"

payload = "{\r\n\"cargoReadyDate\": \"2020-07-07T10:20:01.379Z\",\r\n\"consigneeCustomerId\": \"32809880-4fc3-447a-b19e-decaacbe8b37\",\r\n\"containerType\": \"[{'value':1,'name':'20GP'}]\",\r\n\"destinationIsRequireTruck\": false,\r\n\"destinationPortId\": \"72528faf-4006-4b47-b16f-0dc3b6ae7158\",\r\n\"dimensionsUnitId\": 1,\r\n\"freightMethodType\": 1,\r\n\"incotermsId\": \"d952c54f-5b36-438d-8695-4c2f9edf77d2\",\r\n\"name\": \"\",\r\n\"originPortId\": \"b3df90cb-c0cc-4ee1-a6dd-2dcf7624dee0\",\r\n\"quantityUnitCode\": \"ctn\",\r\n\"shipmentType\": 0,\r\n\"shipperCustomerId\": \"89796121-32f7-466d-898b-f212674d3571\",\r\n\"shipperPartnerId\": \"1049d705-1d0a-4aa5-fad0-08d81bd78e3d\",\r\n\"specialInstructions\": \"\",\r\n\"status\": 4,\r\n\"tradeType\": 1,\r\n\"unitConvertType\": 0,\r\n\"volumeUnitCode\": \"TJDWCBM\",\r\n\"volumeUnitString\": \"cbm\",\r\n\"weightUnitCode\": \"ZLDWKGS\",\r\n\"weightUnitString\": \"kg\"\r\n}"
headers = {
  'Content-Type': 'application/json, text/plain, */*',
  'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsImtpZCI6IjVhMjUwNmQ0Y2IwNWJiMzk4YTgxMmZiYjRiZjUyZmY5IiwidHlwIjoiSldUIn0.eyJuYmYiOjE1OTk0Njk5NDUsImV4cCI6MTU5OTQ3NzE0NSwiaXNzIjoiaHR0cDovLzE5Mi4xNjguMS42OjgwMDEvIiwiYXVkIjpbImh0dHA6Ly8xOTIuMTY4LjEuNjo4MDAxL3Jlc291cmNlcyIsImlkczQtYXBpIiwiUGxhdGZvcm1BcGkiXSwiY2xpZW50X2lkIjoiY2l0eU9jZWFuIiwic3ViIjoiMjQwODAiLCJhdXRoX3RpbWUiOjE1OTk0Njk5NDUsImlkcCI6ImxvY2FsIiwiaHR0cDovL3d3dy5hc3BuZXRib2lsZXJwbGF0ZS5jb20vaWRlbnRpdHkvY2xhaW1zL3RlbmFudElkIjoiMSIsInJvbGUiOiIxMCIsInJvbGVfbmFtZXMiOiJCaWxsaW5nIiwidGVuYW5jeV9uYW1lIjoiQ2l0eSBPY2VhbiIsIm5hbWUiOiJBbWVyaWNhbiIsInN1cl9uYW1lIjoi5rWL6K-VIiwicGxhdGZvcm0iOiIiLCJwYXJlbnRfdXNlcmlkIjoiMjQwNzkiLCJjcmVhdG9yX3VzZXJJZCI6IjE1NyIsImF1dGhvcml6YXRpb25fdHlwZSI6IkV4dGVybmFsIiwiaWNwX3VzZXJpZCI6IiIsImN1c3RvbWVyX2lkIjoiNDg3MWExYTMtNzE3OS00ZWE0LWExNzAtOGE5MTMzZjU3M2YwIiwic2NvcGUiOlsiaWRzNC1hcGkiLCJQbGF0Zm9ybUFwaSIsIm9mZmxpbmVfYWNjZXNzIl0sImFtciI6WyJwd2QiXX0.34y9SufxGbpAk7V4fEHUHUOawQMLUI9vCHoC4tPlqtcTqCi23rfBWQhSMVNIwfGGf4w42VKX8zbxhUIAt5jW6aiLGvefOlgik_Pua46P9a93qnOMJtpCrIDwJDztpC7XFIRR_Nwz8zsMjfNLmetipOUF-08OCMzMdx1edCY3Yh6FGRbskEvKljm-ZSBzrPIBoqc4yN_BBItMaiQILPndjPtMFWaMUmKTopsb5bqZnATi4MFIQwOuDIxAV8btuICbW3bCjCHcG8uWHLjx2erbZPwJeiB_LQcPqUtEJC_bQ8MQ4AXRwTLtqIA1hIRYXMFo-hCYfEDem2YK0iHvQEDNbQ'
}

response = requests.request("POST", url, headers=headers, data = payload)
res = response.content.decode('utf-8')
print(response.text.encode('utf8'))
print(res)
print(response.status_code)
