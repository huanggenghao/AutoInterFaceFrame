#-*- coding:utf-8 -*-#
#-------------------------------------------------------------------------
#ProjectName:       Python2020
#FileName:          PATH_CONSTANTS.py
#Author:            Ben
#Date:              2020/8/2 15:28
#Description:
#--------------------------------------------------------------------------
import os
from Data_Layer.From_File.Data_Dir.PATH import FROM_FILE_BASE_DIR
from Common_Layer.Read_Data_Ini import ReadDataIni
#获取Excel文件所在的路径
EXCEL_PATH=os.path.join(FROM_FILE_BASE_DIR,ReadDataIni()("excelpath","excelpath"))
#获取YAML文件所在的路径
PARAMS_PATH=os.path.join(FROM_FILE_BASE_DIR,ReadDataIni()("yamlpath","paramspath"))
EXPECT_PATH=os.path.join(FROM_FILE_BASE_DIR,ReadDataIni()("yamlpath","expectpath"))

# print(EXCEL_PATH)