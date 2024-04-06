#-*- coding:utf-8 -*-#
#-------------------------------------------------------------------------
#ProjectName:       Python2020
#FileName:          Read_Data_Ini.py
#Author:            Ben
#Date:              2020/8/2 15:25
#Description:
#--------------------------------------------------------------------------
#完成Ini的配置文件操作
import os
import configparser
BASE_DIR=os.path.dirname(os.path.abspath(__file__))
class  ReadDataIni(object):
    def __init__(self):
        self.config=configparser.ConfigParser()
        with open(os.path.join(BASE_DIR,"data.ini")) as fp:
            self.config.read_file(fp)

    def __call__(self,section,option):
        return self.config.get(section,option)


if __name__ == '__main__':
    read=ReadDataIni()
    print(read("excelpath","excelpath"))