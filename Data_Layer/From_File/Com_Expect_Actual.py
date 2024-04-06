#-*- coding:utf-8 -*-#
#-------------------------------------------------------------------------
#ProjectName:       Python2020
#FileName:          Write_Result.py
#Author:            Ben
#Date:              2020/8/2 16:22
#Description:将请求运行运行的结果写入到Excel中
#--------------------------------------------------------------------------
from Common_Layer.PATH_CONSTANTS import EXCEL_PATH
import openpyxl
class  CompareExpectActual(object):

    #该方法用于判定是text还是json的响应结果值
    @staticmethod
    def  compare_text_json(flag,expect,actual):
        if flag==True:
           return CompareExpectActual.compare_expect_actual(expect,actual)
        else:
            #实际结果值固定text和content-type
            if expect["Content-Type"]==actual["Content-Type"] and expect["text"] in actual["text"]:
                return "预期结果与实际结果一致！"
            elif expect["Content-Type"]!=actual["Content-Type"]:
                return "预期结果：%s\n实际结果：%s"%(expect["Content-Type"],actual["Content-Type"])
            else:
                #print("得到的实际文本内容：",actual)
                return "预期的文本没有在实际结果中存在"


    #实现预期结果与实际结果的比较操作  要求实现的效果是：expect:{"reason": "用户名同名", "result": [], "error_code": 2000}
    #actual：{"reason": "用户名同名", "result": []}---->expect:{"reason": "用户名同名","error_code": 2000} actual:{"reason": "用户名同名"}
    #actual:{"reason": "用户名同名", "result": [1], "error_code": 2001} 两个字典的比较操作并取出两个字典的差异值
    @staticmethod
    def  compare_expect_actual(expect,actual):
        expect_new={}
        actual_new={}
        #求和两个字典的键的并集，然后通过键进行判定是否在并集的结果中
        union_set=set(list(expect.keys())+list(actual.keys()))
        for key in union_set:
            if key not in expect.keys():  #说明这个key在actual当中
                actual_new[key]=actual[key]
            elif key not in actual.keys():  #说明这个key在expect当中
                expect_new[key]=expect[key]
            elif expect[key]!=actual[key]:   #说明两个字典中都存在对应key，但是呢其值不同
                actual_new[key] = actual[key]
                expect_new[key] = expect[key]
                # for key,value in expect.items():
        #     if key in actual.keys():
        #         if expect[key]==actual[key]:
        #             pass
        #         else:
        #             expect_new.update({key: expect[key]})
        #             actual_new.update({key: actual[key]})
        #     else:
        #         expect_new.update({key:expect[key]})
        if not(expect_new) and not(actual_new):
            return "预期结果与实际结果一致！"
        return "预期结果：%s\n实际结果：%s"%(expect_new,actual_new)

    #声明一个方法是通过还是不通过
    @staticmethod
    def  write_pass(result):
        if result=="预期结果与实际结果一致！":
            return "通过"
        else:
            return "不通过"
if __name__ == '__main__':
    write=WriteResult()
    expect={"reason": "用户名同名", "result": [], "error_code": 2000,"test":"hello"}
    actual={"reason": "用户名同名", "result": [],"error_code": 210,"status":111}
    print(write.compare_expect_actual(expect,actual))











