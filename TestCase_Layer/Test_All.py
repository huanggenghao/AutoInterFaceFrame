#-*- coding:utf-8 -*-#
#-------------------------------------------------------------------------
#ProjectName:       Python2020
#FileName:          Test_All.py
#Author:            Ben
#Date:              2020/8/9 17:05
#Description:直接测试所有的测试用例
#--------------------------------------------------------------------------
from AutoInterFaceFrame.RunMain_Layer.Run_Main import RunMain
import pytest
from allure import dynamic
import allure
from AutoInterFaceFrame.RunMain_Layer.Read_Result import ReadResult
readresult=ReadResult()
get_all_result=readresult.get_all_result()
#self.get_request_object(self.read,sheet,row),get_method,get_url,get_params_value,get_mock,get_expect_value,get_ifpass
#参数化：数据问题：caseid、casename、caseurl.....  [(),(),()]
@pytest.mark.parametrize("requestobj,method,url,params,mock_value,expect,get_ifpass,cookies,sheet,row,get_casename",get_all_result)
def test_all(mock_request,requestobj,mock_value,expect,method,url,params,get_ifpass,cookies,sheet,row,get_casename):  #什么时候咱能够在测试用例中直接调用循环的每条用例执行？
      #在执行每条用例的时候判断依赖的情况：
      dy=dynamic()
      #声明测试用例的名称
      dy.title(get_casename)
      #取用例中的优先级
      dy.feature(url,method,params)  #完整的数据信息显示
      get_depend_value = readresult.get_response_depend(sheet, row)
      if get_depend_value:
            params.update(get_depend_value)
      #应该完成excel中的所有用例读取，并实现pytest的参数化操作
      get_actual_value=mock_request.mock_request(requestobj,mock_value,expect,method,url,params,cookies)
      #缺少，sheet，和row呀,就完成实际结果写入到excel当中
      readresult.write_actual_result(mock_request,get_actual_value,expect,sheet,row)
      print("对应的",get_actual_value)
      if mock_request.flag:
            assert get_actual_value==expect
      else:
            assert expect["text"] in get_actual_value["text"]


