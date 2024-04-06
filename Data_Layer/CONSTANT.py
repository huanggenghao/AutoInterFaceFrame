#-*- coding:utf-8 -*-#
#-------------------------------------------------------------------------
#ProjectName:       Python2020
#FileName:          CONSTANT.py
#Author:            Ben
#Date:              2020/8/1 16:35
#Description:该文件为常量文件
#--------------------------------------------------------------------------
import os
#数据层的绝对路径
DATA_PATH=os.path.abspath(os.path.dirname("__file__"))
#获取Excel文件所在的路径
EXCEL_PATH=os.path.join(DATA_PATH,"Data_Dir/InterfaceTestCase.xlsx")
#获取YAML文件所在的路径
YAML_PATH=os.path.join(DATA_PATH,"Data_Dir/RequestParams.yaml")
JSON_PATH=os.path.join(DATA_PATH,"Data_Dir/RequestParams.json")
#设置列的常量
CASE_ID="A"
CASE_NAME="B"
CASE_MODULE="C"
CASE_PRECONDITION="D"
CASE_METHOD="E"
CASE_URL="F"
CASE_PARAMS="G"
CASE_EXPECT="H"
CASE_ACTUAL="I"









