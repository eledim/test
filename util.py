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
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from properties import *

def main():
    pass

# 初始化数据库连接:
engine = create_engine('mysql+mysqlconnector://{user}:{passwd}@{host}:{port}/{db}'.format(**config4))
# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)

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

def add(dto):
    # 创建session对象:
    sql_session = DBSession()
    # 创建新User对象:
    # 添加到session:
    sql_session.add(dto)
    # 提交即保存到数据库:
    sql_session.commit()
    # 关闭session:
    sql_session.close()

def query(dto,id):
    sql_session = DBSession()
    ret = sql_session.query(dto).filter(dto.id == id).one()
    sql_session.close()
    return ret


def query_all(dto):
    sql_session = DBSession()
    ret = sql_session.query(dto).all()
    sql_session.close()
    return ret


def ret_err_json(str):
    return jsonify({"stat": "err", "response": str});


def ret_ok_json(str):
    return jsonify({"stat": "ok", "response": str});


if __name__ == "__main__":
    main()
