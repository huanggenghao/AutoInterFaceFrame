#-*- coding:utf-8 -*-#
#-------------------------------------------------------------------------
#ProjectName:       Python2020
#FileName:          Depend_Response.py
#Author:            Ben
#Date:              2020/8/8 14:52
#Description:解决依赖响应体中的数据
#--------------------------------------------------------------------------
from Depend_Layer.Repeat_Excute import repeate_excute
from Data_Layer.From_File.Read_Yaml import ReadYaml
from Common_Layer.PATH_CONSTANTS import EXPECT_PATH,PARAMS_PATH,EXCEL_PATH
class  DependResponse(object):
    @staticmethod
    def get_depend_response(read, mock_request, sheet, row):
        # 获取到关联的cookie所对应的用例id
        get_response_case_id = read.get_case_response(sheet, row)
        get_field_case_id=read.get_case_field(sheet,row)
        get_depend_value=read.get_depend(sheet,row)
        if get_depend_value=="Y":
            #print("依赖响应体中的字段",get_response_case_id)
            if get_response_case_id:
                # 获取总行
                max_row = read.get_max_row(sheet)
                for row in range(2, max_row + 1):
                    if get_response_case_id == read.get_case_id(sheet, row):  #对应关联的caseid
                        get_ifpass=read.get_ifpass(sheet,row).value
                        get_expect = read.get_expect(sheet, row)
                        get_expect_value = ReadYaml()(EXPECT_PATH, get_expect[0], get_expect[1])
                        if get_ifpass=="通过":
                            get_field_column_value=DependResponse.get_field_value(get_field_case_id,get_expect_value)
                            if get_field_column_value:
                                return {get_field_case_id:get_field_column_value},True
                            return "指定的字段在响应体不存在",False   #依赖接口的具体结果   #如果依赖的那条接口已经执行的话
                        elif get_ifpass=="不通过":
                            return "被依赖的接口执行失败",False  #依赖接口的具体结果
                        elif get_ifpass==None:
                            #表示ifpass的单元格值是空值，那么需要先执行该用例并提取实际结果
                            get_actual_value=repeate_excute(read,mock_request,sheet,row,get_response_case_id).json()
                            return DependResponse.get_depend_response(read,mock_request,sheet,row)
            else:
                return None
    #知道一个键，需要取到该键的值,设置递归的方法进行在响应体中查找数据
    @staticmethod
    def get_field_value(field,actual_result):
        for key in actual_result.keys():
            if key == field:  #[reason,result,]
                return actual_result[key]
            elif type(actual_result[key]) == dict:
                #使用递归遍历查找
                return DependResponse.get_field_value(field,actual_result[key])

if __name__ == '__main__':
    dict1={'reason': 'sucess', 'result': {'customer_name': 'wood2', 'customer_type': 'C', 'customer_phone': '18907047890', 'customer_mail': 'fjwojefo@163.com', 'customer_address': '广州天河'}, 'error_code': 0}










