#-*- coding:utf-8 -*-#
#-------------------------------------------------------------------------
#ProjectName:       Python2020
#FileName:          Repeat_Excute.py
#Author:            Ben
#Date:              2020/8/8 15:43
#Description:表示的是需要重复执行测试用例的操作
#--------------------------------------------------------------------------
from Data_Layer.From_File.Read_TestCase import ReadTestCase
from Data_Layer.From_File.Read_Yaml import ReadYaml
from Common_Layer.PATH_CONSTANTS import EXPECT_PATH,PARAMS_PATH,EXCEL_PATH
import requests
def repeate_excute(read, mock_request, sheet, row,get_public_case_id):
    # 获取总行
    max_row = read.get_max_row(sheet)
    for row in range(2, max_row + 1):
        if get_public_case_id == read.get_case_id(sheet, row):
            get_params = read.get_params(sheet, row)
            get_params_value = ReadYaml()(PARAMS_PATH, get_params[0], get_params[1])
            get_method = read.get_method(sheet, row)
            get_url = read.get_url(sheet, row)
            get_response = mock_request.send_request(requests,get_url,get_method, get_params_value)
            return get_response
