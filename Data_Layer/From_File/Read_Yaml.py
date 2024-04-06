#-*- coding:utf-8 -*-#
#-------------------------------------------------------------------------
#ProjectName:       Python2020
#FileName:          Read_RequestParams.py
#Author:            Ben
#Date:              2020/8/1 16:31
#Description:主要完成的是接口所需要的参数提取的代码封装
#--------------------------------------------------------------------------
import yaml
from Common_Layer.PATH_CONSTANTS import PARAMS_PATH,EXPECT_PATH
class  ReadYaml(object):
     def __call__(self,yamlpath,parent,child):
         #请求参数会存储到的yaml中，如果预期结果也是使用yaml存储的话，那么该模块不能够单纯的只能够操作参数的形式，就必须合并一个模块操作
         #如果说将预期结果存储到json中那就没关系
         with open(yamlpath,encoding="utf-8") as fp:
             self.read_yaml=yaml.safe_load(fp)
         for value in self.read_yaml[parent]:
             for key, value in value.items():
                 if key == child:
                    return value


if __name__ == '__main__':
    read=ReadYaml()
    print(read(PARAMS_PATH))
    #print(read(EXPECT_PATH))




