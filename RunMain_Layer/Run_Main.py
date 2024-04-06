#-*- coding:utf-8 -*-#
#-------------------------------------------------------------------------
#ProjectName:       Python2020
#FileName:          Run_Main.py
#Author:            Ben
#Date:              2020/8/4 21:36
#Description:程序主入口
#--------------------------------------------------------------------------
from AutoInterFaceFrame.Request_Layer.Mock_RequestOperation import MockRequestOperation
from AutoInterFaceFrame.Data_Layer.From_File.Read_Yaml import ReadYaml
from AutoInterFaceFrame.Data_Layer.From_File.Read_TestCase import ReadTestCase
from AutoInterFaceFrame.Common_Layer.PATH_CONSTANTS import EXPECT_PATH,PARAMS_PATH,EXCEL_PATH
from AutoInterFaceFrame.Data_Layer.From_File.Com_Expect_Actual import CompareExpectActual
from  openpyxl.styles.fonts import Font
from openpyxl.styles import Alignment
from openpyxl.styles import Color
from AutoInterFaceFrame.Depend_Layer.Depend_Cookie import DependCookie
from AutoInterFaceFrame.Depend_Layer.Depend_Response import DependResponse
from AutoInterFaceFrame.Request_Layer.Session_RequestOperation import SessionRequestOperation
import re
import requests
class RunMain(object):
    def __init__(self):
        self.flag_depend=True
        self.get_cookie_value=None
        self.get_expect_value=None
        self.get_actual_value=None
        #self.read = ReadTestCase()


    #判定session的值
    def  depend_session(self,read,sheet,row):
        dict_session={}
        get_request_value=read.get_request(sheet,row)
        get_session=read.get_session(sheet,row)
        if get_request_value:
            get_value_list=get_request_value.split(",")
            for value in  get_value_list :
                get_value=value.split(":",maxsplit=1)
                dict_session[get_value[0]]=get_value[1]
            get_session_value=get_session.split(":")
            return dict_session,{get_session_value[0]:get_session_value[1]}
        return None

    #声明一个主方法
    def  runmain(self):
        #声明一个变量
        read = ReadTestCase()
        mock_requst = MockRequestOperation()
        session_request=SessionRequestOperation().session
        for sheet in read.get_sheets:
            for row in range(2, read.get_max_row(sheet) + 1):
                get_params = read.get_params(sheet, row)
                get_params_value = ReadYaml()(PARAMS_PATH, get_params[0], get_params[1])
                get_method = read.get_method(sheet, row)
                get_url = read.get_url(sheet, row)
                get_mock = read.get_ismock(sheet, row)
                get_expect = read.get_expect(sheet, row)
                self.get_expect_value = ReadYaml()(EXPECT_PATH, get_expect[0], get_expect[1])
                get_ifpass = read.get_ifpass(sheet, row)
                # print(get_method,get_url,get_params_value)
                dict_session_response={}
                get_depend_session_value=self.depend_session(read,sheet,row)
                if get_depend_session_value:
                    for request_key,request_value in get_depend_session_value[0].items():
                        dict_session_response[request_key]=mock_requst.send_request(session_request,request_value,"GET").text
                        #dict_session_response[request_key] = session.get(request_value).text
                    #完成映射取出完整的响应文本
                    get_key=list(get_depend_session_value[1].keys())[0]
                    print("两个结果值：",get_depend_session_value[1][get_key],dict_session_response[get_key])
                    get_session=re.findall(get_depend_session_value[1][get_key],dict_session_response[get_key])
                    print("之前的值",get_params_value)
                    get_params_value.update({"userSession":get_session[0]})
                    print("之前的值", get_session[0])
                    print(get_params_value,get_url,get_method,self.get_expect_value,get_mock)
                    get_response=mock_requst.get_response(session_request,get_url,method=get_method, params=get_params_value,cookies=self.get_cookie_value)
                    #get_response=session.post(get_url,data=get_params_value)
                    print("Webtours的响应结果",get_response)
                else:
                    #判断是否存在cookie依赖
                    get_depend_value = read.get_depend(sheet, row)
                    if get_depend_value == "Y":
                        self.get_cookie_value = DependCookie.get_cookie_value(read, mock_requst, sheet, row)
                        #print("获取到的cookie值",get_cookie_value)
                        get_depend_response_value=DependResponse.get_depend_response(read,mock_requst,sheet,row)
                        #print("响应的依赖结果值",get_depend_response_value)
                        #更新依赖的数据
                        if get_depend_response_value:
                            self.flag_depend=get_depend_response_value[1]
                            if type(get_depend_response_value[0])==dict:
                                get_params_value.update(get_depend_response_value[0])
                    get_cell = read.get_actual(sheet, row)
                    #如果被依赖的那条接口本身就运行失败了，那么依赖的这条接口就没有必要执行了
                    if self.flag_depend:
                        self.get_actual_value=mock_requst.mock_request(requests,get_mock, self.get_expect_value, get_method, get_url, get_params_value,cookies=self.get_cookie_value)
                        print(self.get_actual_value)
                       # print(get_params_value,get_method,get_url,get_expect_value)
                        #将实际与预期比较的结果值写入到excel中
                        #font = Font(name="微软雅黑", size=11, bold=True)
                        align=Alignment(horizontal="left",wrap_text=True)
                        #比较后返回一个元组，第一个值是需要写入到excel中，第二个值是用于进行依赖取关联数据
                        get_compare_value=CompareExpectActual.compare_text_json(mock_requst.flag,self.get_expect_value,self.get_actual_value)
                        get_cell.value=get_compare_value
                        #get_cell.font=font
                        get_cell.alignment=align
                        #写是否通过
                        read.get_ifpass(sheet,row).value=CompareExpectActual.write_pass(get_cell.value)
                        read.read_excel.save(EXCEL_PATH)
                    else:
                        get_cell.value=get_depend_response_value[0]
                        get_ifpass.value="不通过"
                        read.read_excel.save(EXCEL_PATH)
                        self.flag_depend=True
                # 每执行完一条之后，其cookie的变量变为None值，可以获取到新的cookie值
            self.get_cookie_value=None



if __name__ == '__main__':
    run=RunMain()
    run.runmain()







