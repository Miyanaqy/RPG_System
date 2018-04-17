from processors.testProcessor import *

def regist(controller):
    controller.map['testProcessor'] = TestProcessor()
