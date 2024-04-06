#-*- coding:utf-8 -*-#
#-------------------------------------------------------------------------
#ProjectName:       Python2020
#FileName:          Write_Result.py
#Author:            Ben
#Date:              2020/8/2 16:22
#Description:将请求运行运行的结果写入到Excel中
#--------------------------------------------------------------------------
from AutoInterFaceFrame.Common_Layer.PATH_CONSTANTS import EXCEL_PATH
import openpyxl
class  WriteResult(object):
    def __init__(self):
        self.work=openpyxl.load_workbook(EXCEL_PATH)
        self.work["Sheet1"]["I2"]=10
        self.work.save(EXCEL_PATH)



if __name__ == '__main__':
    write=WriteResult()








