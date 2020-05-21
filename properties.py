#!/usr/bin/python
# coding:utf-8

"""
@author: Ele
@contact: xx@xx.com
@software: PyCharm
@file: util.py
@time: 2020/2/20 16:29
"""
import mysql.connector
from flask import jsonify


def main():
    pass


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



config_redis = {
    'host': '101.37.116.142',
    'port': 193
    # 'password': 'a498211713'
}
config_redis_pool ={
    'host': '101.37.116.142',
    'port': 193,
    "max_connections":1024
}