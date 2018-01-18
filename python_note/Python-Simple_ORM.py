#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' Simple ORM using metaclass '
import pymysql.cursors

class Field(object):

    def __init__(self, name, column_type):
        self.name = name
        self.column_type = column_type

    def __str__(self):
        a='<%s:%s>' % (self.__class__.__name__, self.name)
        return a

class StringField(Field):

    def __init__(self, name):
        super(StringField, self).__init__(name, 'varchar(100)')

class IntegerField(Field):

    def __init__(self, name):
        super(IntegerField, self).__init__(name, 'bigint')

class ModelMetaclass(type):

    def __new__(cls, name, bases, attrs):
        if name=='Model':
            return type.__new__(cls, name, bases, attrs)
        mappings = dict()
        #v指实例
        for k, v in attrs.items():
            if isinstance(v, Field):
                #print('Found mapping: %s ==> %s' % (k, v))
                mappings[k] = v
        for k in mappings.keys():
            attrs.pop(k)
        attrs['__mappings__'] = mappings # 保存属性和列的映射关系
        attrs['__table__'] = name # 假设表名和类名一致
        return type.__new__(cls, name, bases, attrs)

class Model(dict, metaclass=ModelMetaclass):

    def __init__(self, **kw):
        super(Model, self).__init__(**kw)
        for k,v in self.items():
            if isinstance(v,int):
                self[k]=str(v)
            elif isinstance(v,str):
                self[k]="'%s'"%v
            else:
                print("can't use ")


    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Model' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value

    def save(self):
        connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='cp1193543051+', db='fuliba',
                                     charset='utf8', cursorclass=pymysql.cursors.DictCursor)
        cursor = connection.cursor()
        fields = []
        args = []
        for k, v in self.__mappings__.items():
            fields.append(v.name)
            args.append(getattr(self, k, None))
        sql = 'insert into %s (%s) values (%s)' % (self.__table__, ','.join(fields), ','.join(args))
        cursor.execute(sql)
        connection.commit()
        connection.close()
        print('SQL: %s' % sql)



class urls(Model):
    page_id = IntegerField('page_id')
    page_url = StringField('page_url')
    img_url = StringField('img_url')
    jiforjpg = StringField('jiforjpg')
    img_id = IntegerField('img_id')
    #当元类过一遍之后，id，name等都会被删除

u = urls(page_id=1245, page_url='Michael', img_url='test@orm.org', jiforjpg='jpg',img_id=4)
u.save()
