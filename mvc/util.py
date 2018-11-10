#!/usr/bin/python  
#coding:utf-8  

""" 
@author: Ele 
@contact: xx@xx.com 
@software: PyCharm 
@file: util.py 
@time: 2018/11/10 16:29 
"""
import mysql.connector
from flask import jsonify


def main():
    pass


def getConn():
    # conn = mysql.connector.connect(user='root', password='1234][po', database='forum')
    # 也可以使用字典进行连接参数的管理
    config = {
        'host': '127.0.0.1',  # '108.61.220.188',
        'port': 3306,
        'user': 'root',
        'passwd': '1234][po',
        'db': 'wow_key',
        'charset': 'utf8'
    }
    config2 = {
        'host': '108.61.220.188',
        'port': 3306,
        'user': 'root',
        'passwd': 'a498211713',
        'db': 'wow_key',
        'charset': 'utf8'
    }
    config3 = {
        'host': '192.168.43.135',
        'port': 3306,
        'user': 'root',
        'passwd': '1234][Po',
        'db': 'wow_key',
        'charset': 'utf8'
    }
    # conn = mysql.connector.connect(host = '108.61.220.188', user="root", passwd="a498211713", database="wow_key", use_unicode=True)

    conn = mysql.connector.connect(**config3)
    return conn


def exe_sql(sql_str,params=(),is_query=()):
    conn = getConn()
    cursor = conn.cursor()
    cursor.execute(sql_str, params)
    values = 0;
    if sql_str.find("se", 0, 3) >= 0:
        values = cursor.fetchall()
        cursor.rowcount
    conn.commit()
    cursor.close()
    conn.close()
    return values


def ret_err_json(str):
    return jsonify({"stat":"err", "response":str});


def ret_json(str):
    return jsonify({"stat":"ok", "response":str});

if __name__ == "__main__":
    main() 