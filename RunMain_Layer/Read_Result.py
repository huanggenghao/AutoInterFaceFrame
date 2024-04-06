#-*- coding:utf-8 -*-#
#-------------------------------------------------------------------------
#ProjectName:       Python2020
#FileName:          Read_Result.py
#Author:            Ben
#Date:              2020/8/11 20:40
#Description:
#--------------------------------------------------------------------------
#需要获取到excel中的所有数据
from Data_Layer.From_File.Read_TestCase import ReadTestCase
from Request_Layer.Mock_RequestOperation import MockRequestOperation
from Data_Layer.From_File.Read_Yaml import ReadYaml
from Data_Layer.From_File.Read_TestCase import ReadTestCase
from Common_Layer.PATH_CONSTANTS import EXPECT_PATH,PARAMS_PATH,EXCEL_PATH
from Data_Layer.From_File.Com_Expect_Actual import CompareExpectActual
from openpyxl.styles.fonts import Font
from openpyxl.styles import Alignment
from openpyxl.styles import Color
from Depend_Layer.Depend_Cookie import DependCookie
from Depend_Layer.Depend_Response import DependResponse
from Request_Layer.Session_RequestOperation import SessionRequestOperation
import requests
import re
class  ReadResult(object):
        def __init__(self):
            self.read=ReadTestCase()
            self.session=SessionRequestOperation().session
            self.flag_depend = True

        #获取所有的sheet
        # def get_all_sheet(self):

        #cookie的依赖
        def  get_cookie_value(self,sheet,row):
            get_depend_value = self.read.get_depend(sheet, row)
            if get_depend_value == "Y":
                #print("获取到的cookie值",get_cookie_value)
                return DependCookie.get_cookie_value(self.read, MockRequestOperation(), sheet, row)


        #响应体的依赖
        def  get_response_depend(self,sheet,row):
            get_depend_response_value = DependResponse.get_depend_response(self.read,MockRequestOperation(), sheet, row)
            #print(get_depend_response_value)
            # print("响应的依赖结果值",get_depend_response_value)
            # 更新依赖的数据
            if get_depend_response_value:
                self.flag_depend = get_depend_response_value[1]
                if type(get_depend_response_value[0]) == dict:
                    return get_depend_response_value[0]
            return None

        # 判定session的值
        def depend_session(self, sheet, row):
            dict_session = {}
            get_request_value = self.read.get_request(sheet, row)
            get_session = self.read.get_session(sheet, row)
            if get_request_value:
                get_value_list = get_request_value.split(",")
                for value in get_value_list:
                    get_value = value.split(":", maxsplit=1)
                    dict_session[get_value[0]] = get_value[1]
                get_session_value = get_session.split(":")
                return dict_session, {get_session_value[0]: get_session_value[1]}
            return None



        #判断第一个参数是什么对象，如果是session的话则返回session的对象，如果是空值则返回requests对象
        def  get_request_object(self,sheet,row,get_params_value):
            get_depend_session_value = self.depend_session(sheet, row)
            if get_depend_session_value:
                dict_session_response = {}
                get_depend_session_value = self.depend_session( sheet, row)
                if get_depend_session_value:
                    for request_key, request_value in get_depend_session_value[0].items():
                        dict_session_response[request_key] = MockRequestOperation().send_request(self.session, request_value,
                                                                                      "GET").text
                    get_key = list(get_depend_session_value[1].keys())[0]
                    get_session = re.findall(get_depend_session_value[1][get_key], dict_session_response[get_key])
                    get_params_value.update({"userSession": get_session[0]})
                return self.session
            else:
                return requests

        #一条请求所需要的所有数据  sheet1  [{},{},{}]  sheet2 [{} {} {}] sheet3 。。。。
        def get_all_result(self):
            list_result=[]
            for sheet in self.read.get_sheets:
                for row in range(2, self.read.get_max_row(sheet) + 1):
                    get_casename=self.read.get_case_name(sheet,row)
                    get_params = self.read.get_params(sheet, row)
                    get_params_value = ReadYaml()(PARAMS_PATH, get_params[0], get_params[1])
                    get_method = self.read.get_method(sheet, row)
                    get_url = self.read.get_url(sheet, row)
                    get_mock = self.read.get_ismock(sheet, row)
                    get_expect = self.read.get_expect(sheet, row)
                    get_expect_value = ReadYaml()(EXPECT_PATH, get_expect[0], get_expect[1])
                    get_ifpass = self.read.get_ifpass(sheet, row)
                    #固定好顺序，不能够在此句调用实际结果写入，没有实际结果
                    list_result.append([self.get_request_object(sheet,row,get_params_value),get_method,get_url,get_params_value,get_mock,get_expect_value,get_ifpass,self.get_cookie_value(sheet,row),sheet,row,get_casename])
            return list_result

        #声明一个方法，完成实际结果值的写入保存操作
        def  write_actual_result(self,mock_request,get_actual_value,get_expect_value,sheet,row):
            get_actual_cell = self.read.get_actual(sheet, row)
            get_compare_value = CompareExpectActual.compare_text_json(mock_request.flag,get_expect_value,
                                                                      get_actual_value)
            get_actual_cell.value=get_compare_value
            # 写是否通过
            self.read.get_ifpass(sheet, row).value = CompareExpectActual.write_pass(get_actual_cell.value)

            self.read.read_excel.save(EXCEL_PATH)


if __name__ == '__main__':
    read=ReadResult()
    #print(read.get_all_result())
    for row in range(2,8):
        print(read.get_cookie_value("Sheet2",row))











