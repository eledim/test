#!/usr/bin/python  
# coding:utf-8

""" 
@author: Ele 
@contact: xx@xx.com 
@software: PyCharm 
@file: util.py 
@time: 2018/11/10 16:29 
"""
import mysql.connector
from flask import jsonify
from properties import *

def main():
    pass


def getConn():
    # conn = mysql.connector.connect(user='root', password='1234][po', database='forum')
    # 也可以使用字典进行连接参数的管理

    # conn = mysql.connector.connect(host = '108.61.220.188', user="root", passwd="a498211713", database="wow_key", use_unicode=True)
    conn = mysql.connector.connect(**config4)
    return conn


def exe_sql(sql_str, params=(), is_query=()):
    conn = getConn()
    cursor = conn.cursor()
    cursor.execute(sql_str, params)
    ret = 0;
    if sql_str.find("se", 0, 3) >= 0 or sql_str.find("S", 0, 3) >= 0:
        ret = cursor.fetchall()
        cursor.rowcount
    conn.commit()
    cursor.close()
    conn.close()
    return ret


def ret_err_json(str):
    return jsonify({"stat": "err", "response": str});


def ret_ok_json(str):
    return jsonify({"stat": "ok", "response": str});


if __name__ == "__main__":
    main()
