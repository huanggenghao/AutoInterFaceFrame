#-*- coding:utf-8 -*-#
#-------------------------------------------------------------------------
#ProjectName:       Python2020
#FileName:          Read_Json.py
#Author:            Ben
#Date:              2020/10/28 11:28
#Description:
#--------------------------------------------------------------------------
from Data_Layer.CONSTANT import JSON_PATH
import json
class  ReadParams:
     def __init__(self):
         with open(JSON_PATH) as fp:
             self.get_param_object=json.load(fp)
     #获取指定excel中所映射的具体数据
     def get_param_value(self,get_param):
         if get_param:
            return self.get_param_object[get_param]



if __name__ == '__main__':
    read=ReadParams()