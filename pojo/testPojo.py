def getPojo():
    return TestPojo()

class TestPojo():
    def __init__(self, id=None, name=None):
        self.model_name = 'pojo.testPojo'
        if id:
            self.id = id
        self.id__type = ('INT PRIMARY KEY', 'NOT NULL')
        if name:
            self.name = name
        self.name__type = ('TEXT', 'NOT NULL')
        self.table_name = 'test'
        self.attrs = ['id', 'name']
        
