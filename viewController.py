import importlib

class ViewController():
    def __init__(self, interface):
        self.uiNames = []
        self.uiDict = {}
        self.interface = interface

    def getUI(self, uiModels):
        for uiModel in uiModels:
            if uiModel['name'] in self.uiNames:
                ui = self.uiDict[uiModel['name']]
                self.setUiAttr(ui, uiModel)
            else:
                ui = importlib.import_module(uiModel['moudle_name']).getUI()
                self.uiDict.setdefault(uiModel['name'], ui)
                self.setUiAttr(ui, uiModel)

    def setUiAttr(self, ui, uiModel):
        if hasattr(ui, 'attrs'):
            attrs = getattr(ui, 'attrs')
            for attr in attrs:
                setattr(ui, attr, uiModel[attr])
        if ui.state == 'show' and not(ui in self.interface):
            ui.init()
            print(ui)
            self.interface.append(ui)
        elif ui.state == 'hide' and ui in self.interface:
            ui.die()
            print(ui)
            self.interface.remove(ui)

    
