def getUI(pos = None, context = None, state = 'hide'):
    return TestUI(poi, context, state)

class TestUI():
    def __init__(self, pos = None, context = None, state = 'hide'):
        self.attrs = []
        if pos:
            self.pos = pos
        if context:
            self.context = context
        self.state = state

    def init(self):
        print('testUI init')

    def die(self):
        print('testUI die')

    def draw(self, screen):
        print('draw testUI')
