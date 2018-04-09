#!/usr/bin/env python

# encoding: utf-8

'''

@author: SunGuoTao

@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.

@contact: GuotaoSunVipSystem@gmail.com

@software: garner

@file: mysqlTest.py

@time: 2017/12/18 下午5:20

@desc:

'''
import mysql.connector

# change root password to yours:
conn = mysql.connector.connect(host='localhost',port=3306,user='root', password='sunguotao', database='test')

cursor = conn.cursor()
# 创建user表:
cursor.execute('create table IS NOT EXISTS user (id varchar(20) primary key, name varchar(20))')
# 插入一行记录，注意MySQL的占位符是%s:
cursor.execute('insert into user (id, name) values (%s, %s)', ('1', 'Michael'))
print('rowcount =', cursor.rowcount)
# 提交事务:
conn.commit()
cursor.close()

# 运行查询:
cursor = conn.cursor()
cursor.execute('select * from user where id = %s', ('1',))
values = cursor.fetchall()
print(values)
# 关闭Cursor和Connection:
cursor.close()
conn.close()