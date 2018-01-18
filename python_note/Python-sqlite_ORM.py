#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sqlite3
import logging

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s: %(message)s',
                    filename='log.txt',
                    filemode='a')


def log(sql):
    # print(sql)
    logging.info(sql)


class Field(object):
    def __init__(self, name, column_type, primary_key, can_be_null, default):
        self.name = name
        self.column_type = column_type
        self.primary_key = primary_key
        self.can_be_NULL = can_be_null
        self.default = default


class IntegerField(Field):
    def __init__(self, name=None, primary_key=False, default=None):
        super(IntegerField, self).__init__(name, 'bigint', primary_key, None, default)


class FloatField(Field):
    def __init__(self, name=None, primary_key=False, default=None):
        super(FloatField, self).__init__(name, 'real', primary_key, None, default)


class StringField(Field):
    def __init__(self, name=None, column_type='varchar(100)', primary_key=False, default=None):
        super(StringField, self).__init__(name, column_type, primary_key, None, default)


class TextField(Field):
    def __init__(self, name=None, default=None):
        super(TextField, self).__init__(name, 'mediumtext', False, None, default)


class BoolField(Field):
    def __init__(self, name=None, default=None):
        super(BoolField, self).__init__(name, 'boolean', False, None, default)


class PrimaryKey_Error(Exception):
    pass


class ModleMetaclass(type):
    def __new__(cls, name, bases, attrs):
        if name == 'Model':
            return type.__new__(cls, name, bases, attrs)
        tablename = attrs.get('__table__', None) or name
        mappings = dict()
        fields = []
        primarykey = None
        for key, value in attrs.items():
            if isinstance(value, Field):
                mappings[key] = value
                # mapings装入name：intgerfield类
                if value.primary_key:
                    # 找到主键，然后判重，有且只有一个主键
                    if primarykey:
                        raise PrimaryKey_Error('too many primary key for field: %s' % key)
                    primarykey = key
                else:
                    fields.append(key)
        if not primarykey:
            raise PrimaryKey_Error('have no primary key')

        for key in mappings.keys():
            attrs.pop(key)
        # 删除类的属性，只使用__mappings__存储映射关系

        attrs['__mappings__'] = mappings
        attrs['__table__'] = tablename
        attrs['__primary_key__'] = primarykey
        attrs['__fields__'] = fields
        return type.__new__(cls, name, bases, attrs)


class Model(metaclass=ModleMetaclass):
    def __init__(self):
        self.connection = sqlite3.connect('proxy')

    def select(self, sql, size=None):
        log(sql)
        with self.connection as connection:
            cursor = connection.cursor()
            cursor.execute(sql)
            if size:
                result = cursor.fetchmany(size)
            else:
                result = cursor.fetchall()
        return result

    def execute(self, sql):
        log(sql)
        with self.connection as connection:
            try:
                cursor = connection.cursor()
                cursor.execute(sql)
                connection.commit()
                affected = cursor.rowcount
            except Exception:
                logging.warning(sql)
                raise
            return affected

    def find_many(self, where=None, size=None, **kw):
        # size满足条件的形式下取多少
        # where 接收第一个条件如a>100，kw接收其余的条件，但是需要以连接符加条件的方式配合
        # 如 and:b>10 ,limit:2,like:'c%',每个条件限用一次
        # 条件比较复杂建议直接在where里面写全
        select_sql = "select %s from %s" % (','.join(self.__mappings__.keys()), self.__table__)
        sql = [select_sql]
        if where:
            sql.append(' where ')
            sql.append(where)
            if kw is not None:
                for key, value in kw.items():
                    sql.append(' %s ' % key)
                    sql.append(str(value))
        sql = ''.join(sql)
        result = self.select(sql, size)
        return result

    def find_one(self, **kw):
        # kw接收键值对来作筛选
        select_sql = "select %s from %s where " % (','.join(self.__mappings__.keys()), self.__table__)
        sql = [select_sql]
        for key, value in kw.items():
            if not key in self.__mappings__.keys():
                raise Exception('%s is Invalid' % key)
            sql.append('%s=%s' % (key, value))
        sql = sql[0] + ' and '.join(sql[1:])
        result = self.select(sql)
        if len(result) != 1:
            raise Exception('please use primary key')
        return result

    def insert(self, **kw):
        values = []
        for key, value in kw.items():
            if not key in self.__mappings__.keys():
                raise Exception('%s is Invalid' % key)
        for key, value in self.__mappings__.items():
            get_value = kw.get(key, None) or value.default
            values.append("'%s'" % str(get_value))
        columns = ','.join(self.__mappings__.keys())
        values = ','.join(values)
        sql = 'insert into %s(%s) values(%s)' % (self.__table__, columns, values)
        affect_row = self.execute(sql)
        return affect_row

    def delete(self, primarykey):
        # 只需传入主键值
        sql = "DELETE FROM %s WHERE %s='%s'" % (self.__table__, self.__primary_key__, primarykey)
        affect_row = self.execute(sql)
        return affect_row

    def update(self, primarykey, **kw):
        values = []
        for key, value in kw.items():
            if not key in self.__mappings__.keys():
                raise Exception('%s is Invalid' % key)
            get_value = "%s='%s'" % (key, value)
            values.append(get_value)
        set_values = ','.join(values)
        sql = "UPDATE %s SET %s WHERE %s='%s'" % (self.__table__, set_values, self.__primary_key__, primarykey)
        affect_row = self.execute(sql)
        return affect_row

    def __del__(self):
        self.connection.close()