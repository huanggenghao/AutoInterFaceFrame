#-*- coding:utf-8 -*-#
#-------------------------------------------------------------------------
#ProjectName:       Python2020
#FileName:          conftest.py
#Author:            Ben
#Date:              2020/7/28 20:49
#Description:这是所有包都共享的conftest中的固件对象
#--------------------------------------------------------------------------
import pytest
from RunMain_Layer.Run_Main import RunMain
from Request_Layer.Mock_RequestOperation import MockRequestOperation
from Request_Layer.Session_RequestOperation import SessionRequestOperation
import time
#声明数据库的固件对象
# @pytest.fixture(scope='class')
# def  runmain():
#      runmain=RunMain()
#      return runmain

@pytest.fixture(scope='class')
def  mock_request():
     mock_request=MockRequestOperation()
     return mock_request


#声明session对象
@pytest.fixture(scope='class')
def  session_request():
     session_request=SessionRequestOperation().session
     return session_request


from datetime import datetime
from py.xml import html
import pytest
import time
#声明报告表格的表头定义
def pytest_html_results_table_header(cells):
    cells.insert(2, html.th('Description'))
    cells.insert(1, html.th('Time', class_='sortable time', col='time'))
    cells.insert(3, html.th('Y OR N'))
    cells.pop()
#实现对应表头的行的值的操作，description、实际就是我们声明的每个方法对应docstring值
def pytest_html_results_table_row(report, cells):
    cells.insert(2, html.td(report.description))
    cells.insert(1, html.td(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()), class_='col-time'))
    cells.insert(3,html.td("Y"))
    cells.pop()

#
# import pytest
# import time
# from CrmTest.Business_Object.Login.Login_Business import LoginBusiness
# login=None
# @pytest.fixture()
# def get_login():
#     global login
#     login=LoginBusiness("http://123.57.71.195:7878/index.php/login")
#     # print("这是setup方法")
#     #return login
#     yield login   #如果针对被测试模块中的测试用例需要实现调用teardown方法的话，那么自定义固件对象中可以通过yield的关键字替代return语句以完成teardown的操作
#     # print("这是teardown方法")
#     time.sleep(2)
#     login.get_driver.quit()
#
# #缺少驱动器对象
# def get_image(filename):
#     print("这是外面的conftest的驱动器对象",get_login)
#     login.get_driver.save_screenshot(filename)

# from CrmTest.GET_PATH import GETPATH
# import os
# from PIL import ImageGrab
# import allure
# #真正完成扩展模块扩展内容写入到报告中的主方法
# @pytest.hookimpl(hookwrapper=True)
# def pytest_runtest_makereport(item, call):
#     pytest_html = item.config.pluginmanager.getplugin('html')
#     outcome = yield
#     report = outcome.get_result()
#     extra = getattr(report, 'extra', [])
#     if report.when == 'call' or report.when == "setup":    #判定需要获取失败的状态，如果运行失败的话则进行页面截图并写入报告操作,内置方法__call__如果被显式声明的话则对象可以直接通过方法调用
#         xfail = hasattr(report, 'wasxfail')
#         if (report.skipped and xfail) or (report.failed and not xfail):
#             #需要实现截图操作;图片宽和高的大小的单位是像素,如果点击图片则可以实现显示当前图片
#             #可以专门设定一个目录完成报告以及图片的存放
#             get_dir=os.path.join(GETPATH,"Report_Object/ErrorImage")
#             if not(os.path.exists(get_dir)):
#                 os.mkdir(get_dir)
#             #图片的名字不能够固定，如果固定，如果多个失败则只有一张图片，图片的名字如何定义，最好图片能够对应测试用例的名字，用例的名字是可以取到的
#               #获取每个测试用例具体名字，但是文件命名不能够存在::特殊符号
#             get_testcase_name=report.nodeid.split("::")[-1]
#             get_index=get_testcase_name.find("[")
#             get_last_index=get_testcase_name.find("]")
#             get_name=get_testcase_name[get_index+1:get_last_index]
#             get_name=get_name.split("-")[:4]
#             print("测试用例的前四个构成的用例名：",get_name)
#             get_new_name=""
#             for value in get_name:
#                 if "\\" in value:
#                     value=value.encode("utf-8").decode("unicode_escape")
#                 get_new_name+=value+"_"
#             print("分割数据名称",get_new_name)   #"_".join(get_name)
#             filename=get_new_name+".png"
#             print("图片的文件名",filename)
#             filepath=os.path.join(get_dir,filename)
#             #get_image(filepath)
#             im=ImageGrab.grab(bbox=(760, 0, 1160, 1080))
#             im.save(filepath)  #相当于键盘上的截图的案件    因为完美的解决了父包下的conftest与子包下的conftest之间的依赖问题
#             print(im.size)
#             #extra.append(pytest_html.extras.html('<div><img src="../Report_Object/ErrorImage/%s" style="width:400px;height:400px;" onclick="window.open(this.src)" align="right" ></div>'%filename))
#             #直接将上面的代码转换成allure的代码即可实现python+pytest+pytest-html+allure
#             allure.attach.file(filepath,name=filename,attachment_type=allure.attachment_type.PNG)
#         report.extra = extra
#     report.description = str(item.function.__doc__)





