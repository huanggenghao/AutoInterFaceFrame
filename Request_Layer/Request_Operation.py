#-*- coding:utf-8 -*-#
#-------------------------------------------------------------------------
#ProjectName:       Python2020
#FileName:          Request_Operation.py
#Author:            Ben
#Date:              2020/8/2 15:51
#Description:
#--------------------------------------------------------------------------
#请求操作的代码封装
import requests
from AutoInterFaceFrame.Data_Layer.From_File.Read_Yaml import ReadYaml
from AutoInterFaceFrame.Data_Layer.From_File.Read_TestCase import ReadTestCase
from AutoInterFaceFrame.Common_Layer.PATH_CONSTANTS import EXPECT_PATH,PARAMS_PATH
from unittest import mock
class  RequestOperation(object):

    def __init__(self):
        self.flag=True  #用于进行判定结果是text还是json的

    def send_request(self,requestobj,url,method=None,params=None,cookies=None):
        if method=="GET":
           return requestobj.get(url,params=params,cookies=cookies)
        elif method=="POST":
           return requestobj.post(url,data=params,cookies=cookies)
        else:
            return "其他请求方法还未实现"

    #声明一个方法获取响应体
    def get_response(self,requestobj,url,method=None,params=None,cookies=None):
        self.get_resp=self.send_request(requestobj,url, method, params,cookies)
        if type(self.get_resp)==str:
            pass
        else:
            try:
                self.flag=True
                return self.get_resp.json()  #响应体可以调用json格式也可以调用text
            except:
                self.flag=False
                return {"text":self.get_resp.text,"Content-Type":self.get_resp.headers["Content-Type"]}   #处理返回一个html所对应的dict格式


    def mock_request(self,requestobj,mock_value,expect,method,url,params,cookies=None):
            if mock_value=="Y":
                get_mock=mock.Mock(return_value=expect)
                #将mock对象赋值给需要mock的python对象
                #self.get_response=get_mock    #如果你将get_mock对象赋值给self.get_response的话，实际表示的是完成当前对象中添加一个get_response属性，将get_mock的值赋值给该属性
                self.repsonse=get_mock
            elif mock_value=="N":
                get_mock=mock.Mock(side_effect=self.get_response)   #那么side_effect中调用的也是之前mock的属性结果值
                self.repsonse=get_mock
                #self.get_response=get_mock
            return self.repsonse(requestobj,method,url,params,cookies)


if __name__ == '__main__':
    read = ReadTestCase()
    mock_requst=RequestOperation()
    for row in range(2, read.get_max_row("Sheet1") + 1):
        get_params = read.get_params("Sheet1", row)
        get_params_value=ReadYaml()(PARAMS_PATH, get_params[0], get_params[1])
        get_method=read.get_method("Sheet1",row)
        get_url=read.get_url("Sheet1",row)
        get_mock=read.get_ismock("Sheet1",row)
        get_expect = read.get_expect("Sheet1", row)
        get_expect_value = ReadYaml()(EXPECT_PATH, get_expect[0], get_expect[1])
        #print(get_method,get_url,get_params_value)
        print(mock_requst.mock_request(get_mock,get_expect_value,get_method,get_url,get_params_value))