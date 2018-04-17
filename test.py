import controller
from processors import processorRegist
from utils import connectionPool
import simpleData
from pojo import testPojo
from pojo import pojoRegist
import importlib
import viewController

pool = connectionPool.ConnectionPool()
connection = pool.getConnection()
print(connection)

#connection.execute("INSERT INTO test (ID,NAME) \
#      VALUES (1, 'Paul');")
#cursor = connection.execute("SELECT id, name from test;")
#for row in cursor:
#    print(row[1])
#connection.execute("insert into test (ID, NAME) values (?,?)", [4, 'red'])
#connection.commit()

def create():
    connection.execute('''CREATE TABLE test2
       (ID INT PRIMARY KEY     NOT NULL,
       NAME           TEXT    NOT NULL);''')

def select():
    cursor = connection.execute("SELECT id, name from test;")
    for row in cursor:
        print(row)

def test2(dataDao):
    obj = testPojo.TestPojo(7,'Aria')
    data = dataDao.add(obj)
    print(data)

def test3(dataDao):
    obj = testPojo.TestPojo(7,'Aria')
    data = dataDao.delete(obj)
    print(data)

def test4(data):
    obj = testPojo.TestPojo(5, 'pand')
    data = dataDao.update(obj)
    print(data)

def test5(dataDao):
    obj = testPojo.TestPojo(3, '')
    data = dataDao.findById(obj, 3)
    for row in data:
        print(row.name)

def test6(dataDao):
    obj = testPojo.TestPojo(3,'')
    data = dataDao.findAll(obj)
    for row in data:
        print(row.name)

def test7():
    data = connection.execute("SELECT name FROM sqlite_master WHERE type='table' ORDER BY name;")
    for row in data:
        print(row[0])

def test8(dataDao):
    dataDao.list = pojoRegist.regist()
    dataDao.initialization()

def test9():
    moudle_name = 'ui.testUi'
    testUi = importlib.import_module(moudle_name).getUI('100,100', '测试', 'hide')
    print(testUi)
    return testUi

def test10(ui):
    interface = []
    view = viewController.ViewController(interface)
    uiModel = {'name':'test1','poi':'50,50', 'context':'打开', 'state':'show'}
    view.setUiAttr(ui, uiModel)
    uiModel = {'name':'test2','poi':'50,50', 'context':'关闭', 'state':'hide'}
    view.setUiAttr(ui, uiModel)

def test11():
    uiModels = [{'name':'test1','poi':'50,50', 'context':'打开', 'state':'show', 'moudle_name':'ui.testUi'},
                {'name':'test2','poi':'50,50', 'context':'打开', 'state':'show', 'moudle_name':'ui.testUi'}]
    interface = []
    view = viewController.ViewController(interface)
    view.getUI(uiModels)
    
dataDao = simpleData.SimpleData()

#--------------------------------数据库-----------------------------
#test2(dataDao)
#test3(dataDao)
#test4(dataDao)
#test5(dataDao)
test6(dataDao)
#create()

#test8(dataDao)
#test7()

#select()

#--------------------------------视图控制器---------------------------

#ui = test9()
#test10(ui)

#test11()

