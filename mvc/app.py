#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Flask, request, render_template,session
import mysql.connector
import uuid
import json
import os
from datetime import timedelta
from flask import jsonify
app = Flask(__name__)

app.config['SECRET_KEY']=os.urandom(24)   #设置为24位的字符,每次运行服务器都是不同的，所以服务器启动一次上次的session就清除。
app.config['PERMANENT_SESSION_LIFETIME']=timedelta(days=7) #设置session的保存时间。
# site = 'http://eledim.xyz/'
#site = 'http://127.0.0.1:5000/'


@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html')


@app.route('/signin', methods=['GET'])
def signin_form():
    return render_template('signin.html')


@app.route('/signin', methods=['POST'])
def signin():
    session.permanent = True  # 默认session的时间持续31天
    username = request.form['username']
    password = request.form['password']
    session[username] = username
    session.get(username)

    conn = getConn()
    cursor = conn.cursor()
    cursor.execute('select password from user where username=%s',[username])
    values = cursor.fetchall()
    if len(values)==0:
        id = str(uuid.uuid1());
        userid = str(uuid.uuid1());
        cursor.execute('insert into user (id, userid,username,password) values (%s, %s,%s,%s)', [id, userid, username, password])
        ret = "ok add user"
    else:
        if  password==values[0][0]:
            ret = "ok"+session.get(username)
        else:
            ret = "password error"
    cursor.rowcount
    conn.commit()
    cursor.close()
    conn.close()
    return ret


@app.route('/key_page', methods=['GET'])
def key_page():
    username = request.args.get('username')
    return render_template('key_page.html', username=username)


def signin2():
    session.permanent = True  # 默认session的时间持续31天
    username = request.form['username']
    password = request.form['password']
    session[username] = username

    session.get(username)
    if username=='admin' and password=='password':
        return render_template('signin-ok.html', username=username)
    return render_template('home.html', message='Bad username or password', username=username)


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
    username = request.form['username']

    conn = getConn()
    cursor = conn.cursor()
    cursor.execute('select userid from user where username=%s',[username]) ;
    values = cursor.fetchall()
    if len(values) > 0:
        userid = values[0][0]
        cursor.execute('select userid from userkey where userid=%s', [userid]);
        values = cursor.fetchall()
        if len(values) > 0: #已有记录，更新
            cursor.execute('update userkey set level = %s,dungeon = %s where userid = %s', [ level, dungeon,userid])
            ret = "update key"
        else:
            cursor.execute('insert into userkey (id, level,dungeon,userid) values (%s, %s,%s,%s)', [id, level, dungeon, userid])
            ret = "insert key"
    else :
        ret = "user error"
    cursor.rowcount
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify(ret)


@app.route('/query_key', methods=['POST'])
def query_key():
    conn = getConn()
    cursor = conn.cursor()
    cursor.execute('select dungeon,level,username from userkey,user where userkey.userid =user.userid ')
    values = cursor.fetchall()
    json_str = json.dumps(values,ensure_ascii=False)
    cursor.close()
    conn.close()
    return jsonify(values)


if __name__ == '__main__':
    app.run()

