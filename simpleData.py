import sqlite3
from utils.connectionPool import ConnectionPool
import importlib

def get_table_name(obj):
    table_name = ''
    if hasattr(obj, 'table_name'):
        table_name = getattr(obj, 'table_name')
        return table_name
    else:
        return None

def get_attrs(obj):
    attrs = None
    if hasattr(obj, 'attrs'):
        attrs = getattr(obj, 'attrs')
        return attrs
    else:
        return None

def get_attrStr(attrs):
    attrKey = ''
    attrVal = ''
    if len(attrs) > 0:
        for attr in attrs:
            attrKey += attr + ','
            attrVal += '?,'
        attrKey = attrKey[:len(attrKey)-1]
        attrVal = attrVal[:len(attrVal)-1]
        return (attrKey, attrVal)
    else:
        return None

def get_prop(obj, attrs):
    prop = []
    if len(attrs) > 0:
        for attr in attrs:
            if hasattr(obj, attr):
                prop.append(getattr(obj, attr))
            else:
                prop.append('')
        return prop
    else:
        return None

def get_obj_id(obj):
    if hasattr(obj, 'id'):
        return getattr(obj, 'id')
    else:
        return None

def update_attr(attrs):
    updateStr = ''
    if len(attrs) > 0:
        for attr in attrs:
            updateStr += attr + '=?,'
        updateStr = updateStr[:len(updateStr)-1]
        return updateStr
    else:
        return None

def get_table_list(data):
    tablelist = []
    if data:
        for row in data:
            tablelist.append(row[0])
        return tablelist
    else:
        return None

def get_attr_types(obj, attrs):
    attrTypes = []
    if len(attrs) > 0:
        for attr in attrs:
            if hasattr(obj, attr + '__type'):
                attrTypes.append(getattr(obj, attr + '__type'))
        return attrTypes
    else:
        return None

def list_to_obj(obj, data):
    newobj = importlib.import_module(getattr(obj, 'model_name')).getPojo()
    attrs = get_attrs(obj)
    for index in range(len(attrs)):
        setattr(newobj, attrs[index], data[index])
    return newobj

class SimpleData():
    
    def __init__(self):
        self.list = []
        self.pool = ConnectionPool()

    def execute(self, sql, prop = None):
        data = None
        conn = self.pool.getConnection()
        if not prop:
            data = conn.execute(sql)
        else:
            data = conn.execute(sql, prop)
        conn.commit()
        self.pool.reConnection(conn)
        return data

    def add(self, obj):
        table_name = get_table_name(obj)
        attrs = get_attrs(obj)
        attrStr = get_attrStr(attrs)
        prop = get_prop(obj, attrs)
        if table_name and attrs and attrStr and prop:
            sql = 'insert into ' + table_name + ' (' + attrStr[0] + ') values (' + attrStr[1] +');'
            self.execute(sql, prop)
            return 1
        else:
            return None

        
    def delete(self, obj):
        table_name = get_table_name(obj)
        id = get_obj_id(obj)
        if table_name and id:
            sql = 'delete from ' + table_name + ' where id = ?;'
            self.execute(sql, str(id))
            return 1
        else:
            return None

    def update(self, obj):
        table_name = get_table_name(obj)
        attrs = get_attrs(obj)
        attrUpdate = update_attr(attrs)
        prop = get_prop(obj, attrs)
        if table_name and attrs and attrUpdate and prop:
            sql = 'update ' + table_name + ' set ' + attrUpdate + 'where id = ' + str(prop[0])
            self.execute(sql, prop)
            return 1
        else:
            return None

    def findById(self, obj, id):
        table_name = get_table_name(obj)
        attrs = get_attrs(obj)
        attrStr = get_attrStr(attrs)
        if table_name and attrs and attrStr:
            sql = 'select ' + attrStr[0] + ' from ' + table_name + ' where id = ?;'
            datas = self.execute(sql, str(id))
            objList = []
            for data in datas:
                objList.append(list_to_obj(obj, data))
            return objList
        else:
            return None

    def findAll(self, obj):
        table_name = get_table_name(obj)
        attrs = get_attrs(obj)
        attrStr = get_attrStr(attrs)
        if table_name and attrs and attrStr:
            sql = 'select ' + attrStr[0] + ' from ' + table_name + ';'
            datas = self.execute(sql)
            objList = []
            for data in datas:
                objList.append(list_to_obj(obj, data))
            return objList
        else:
            return None
    
    def initialization(self):
        sql = "SELECT name FROM sqlite_master WHERE type='table' ORDER BY name;"
        data = self.execute(sql)
        tableNameList = get_table_list(data)
        for obj in self.list:
            if not(get_table_name(obj) in tableNameList):
                self.createTable(obj)

    def createTable(self, obj):
        sql = 'create table '
        table_name = get_table_name(obj)
        attrs = get_attrs(obj)
        attrTypes = get_attr_types(obj, attrs)
        if table_name and attrs and attrTypes:
            sql += table_name + ' ('
            for index in range(len(attrs)):
                sql += attrs[index] + ' ' + attrTypes[index][0]
                if len(attrTypes[index]) > 1:
                    sql += ' ' + attrTypes[index][1]
                sql += ','
            sql = sql[:len(sql)-1]
            sql += ');'
            
        self.execute(sql)
            
