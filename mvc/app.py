#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Flask, request, render_template
import mysql.connector
import uuid
import json

from flask import jsonify
app = Flask(__name__)
# site = 'http://eledim.xyz/'
#site = 'http://127.0.0.1:5000/'
@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html')

@app.route('/signin', methods=['GET'])
def signin_form():
    return render_template('form.html')

@app.route('/signin', methods=['POST'])
def signin():
    username = request.form['username']
    password = request.form['password']
    if username=='admin' and password=='password':
        return render_template('signin-ok.html', username=username)
    return render_template('form.html', message='Bad username or password', username=username)
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

@app.route('/confirm_key', methods=['POST'])
def confirm_key():
    level = request.form['level']
    dungeon = request.form['dungeon']
    id = str(uuid.uuid1());
    conn = getConn()
    cursor = conn.cursor()
    cursor.execute('insert into userkey (id, level,dungeon) values (%s, %s,%s)', [id, level, dungeon])
    cursor.rowcount
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify("")

@app.route('/query_key', methods=['POST'])
def query_key():
    conn = getConn()
    cursor = conn.cursor()
    cursor.execute('select dungeon,level,userid from userkey')
    values = cursor.fetchall()
    json_str = json.dumps(values,ensure_ascii=False)
    cursor.close()
    conn.close()
    return jsonify(values)
if __name__ == '__main__':
    app.run()

