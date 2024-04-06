#-*- coding:utf-8 -*-#
#-------------------------------------------------------------------------
#ProjectName:       Python2020
#FileName:          Mock_RequestOperation.py
#Author:            Ben
#Date:              2020/8/2 16:05
#Description:
#--------------------------------------------------------------------------
from AutoInterFaceFrame.Request_Layer.Request_Operation import RequestOperation
from AutoInterFaceFrame.Data_Layer.From_File.Read_Yaml import ReadYaml
from AutoInterFaceFrame.Data_Layer.From_File.Read_TestCase import ReadTestCase
from AutoInterFaceFrame.Common_Layer.PATH_CONSTANTS import EXPECT_PATH,PARAMS_PATH
from unittest import mock
class MockRequestOperation(RequestOperation):

    def __init__(self):
        super().__init__()
        self.repsonse=RequestOperation().get_response

    #如果测试接口过程中某些用例需要实现mock的话，那么如何实现
    def mock_request(self,requestobj,mock_value,expect,method,url,params,cookies=None):
        if mock_value=="Y":
            get_mock=mock.Mock(return_value=expect)
            self.repsonse=get_mock
        elif mock_value=="N":
            get_mock=mock.Mock(side_effect=self.get_response)
            self.repsonse=get_mock
        return self.repsonse(requestobj,url,method,params,cookies)


if __name__ == '__main__':
    read = ReadTestCase()
    mock_requst=MockRequestOperation()
    for row in range(2, read.get_max_row("Sheet2") + 1):
        get_params = read.get_params("Sheet2", row)
        get_params_value=ReadYaml()(PARAMS_PATH, get_params[0], get_params[1])
        get_method=read.get_method("Sheet2",row)
        get_url=read.get_url("Sheet2",row)
        get_mock=read.get_ismock("Sheet2",row)
        get_expect = read.get_expect("Sheet2", row)
        get_expect_value = ReadYaml()(EXPECT_PATH, get_expect[0], get_expect[1])
        #print(get_method,get_url,get_params_value)
        print(mock_requst.mock_request(get_mock,get_expect_value,get_method,get_url,get_params_value))