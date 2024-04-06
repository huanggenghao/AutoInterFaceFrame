#-*- coding:utf-8 -*-#
#-------------------------------------------------------------------------
#ProjectName:       Python2020
#FileName:          Session_RequestOperation.py
#Author:            Ben
#Date:              2020/8/9 14:57
#Description:如果是session请求的话则需要创建该对象进行完成请求的发送
#--------------------------------------------------------------------------
from Request_Layer.Mock_RequestOperation import MockRequestOperation
from requests import Session
import requests
class  SessionRequestOperation(MockRequestOperation):
    def __init__(self):
        super().__init__()
        self.session=Session()




