#-*- coding:utf-8 -*-#
#-------------------------------------------------------------------------
#ProjectName:       Python2020
#FileName:          Depend_Cookie.py
#Author:            Ben
#Date:              2020/8/6 22:15
#Description:解决cookie的依赖
#--------------------------------------------------------------------------
from Data_Layer.From_File.Read_TestCase import ReadTestCase
from Data_Layer.From_File.Read_Yaml import ReadYaml
from Common_Layer.PATH_CONSTANTS import EXPECT_PATH,PARAMS_PATH,EXCEL_PATH
from Depend_Layer.Repeat_Excute import repeate_excute
class DependCookie(object):

    #获取到依赖的cookie类型后，需要获取到cookie的结果值，如果是json格式文件直接读取操作即可，如果不是，则需要先运行指定关联的接口用例所产生的cookie
    #信息然后传入到下面的接口中
    @staticmethod
    def  get_cookie_value(read,mock_request,sheet,row):
        # 获取到关联的cookie所对应的用例id
        get_public_case_id = read.get_cookie(sheet, row)
        print(get_public_case_id)
        #print("依赖cookie的字段：",get_public_case_id)
        if get_public_case_id:
            if get_public_case_id.endswith(".json"):
                pass   #pass部分你们添加
            else:
                return repeate_excute(read,mock_request,sheet,row,get_public_case_id).cookies













