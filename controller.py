    

class Controller():
    def __init__(self):
        #创建注册表
        self.map = {}

#---------------------------获取处理器--------------------------------
    def doing(self, action, prop):
        processor = self.map[action]
        processor.action(prop)
        
