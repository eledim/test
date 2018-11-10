#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Flask, request, render_template,session
import uuid
import json
import os
from mvc.util import *
from datetime import timedelta
from flask import jsonify
app = Flask(__name__)

app.config['SECRET_KEY']=os.urandom(24)   #设置为24位的字符,每次运行服务器都是不同的，所以服务器启动一次上次的session就清除。
app.config['PERMANENT_SESSION_LIFETIME']=timedelta(days=7) #设置session的保存时间。
# site = 'http://eledim.xyz/'
#site = 'http://127.0.0.1:5000/'


@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('signin.html')


@app.route('/signin', methods=['GET'])
def signin_form():
    return render_template('signin.html')


@app.route('/signin2', methods=['GET'])
def signin2():
    return render_template('home.html')


@app.route('/key_page', methods=['GET'])
def key_page():
    username = request.args.get('username')
    return render_template('key_page.html', username=username)


@app.route('/do_signin', methods=['POST'])
def signin():
    session.permanent = True  # 默认session的时间持续31天
    username = request.form['username']
    password = request.form['password']
    session[username] = username
    session.get(username)
    values = exe_sql('select password from user where username=%s',[username])
    if len(values)==0:
        id = str(uuid.uuid1());
        userid = str(uuid.uuid1());
        exe_sql('insert into user (id, userid,username,password) values (%s, %s,%s,%s)', [id, userid, username, password])
        ret = ret_json("add user success")
    else:
        if  password==values[0][0]:
            ret = ret_json(session.get(username))
        else:
            ret = ret_err_json("password error")
    return ret


def signin2():
    username = request.form['username']
    password = request.form['password']
    if username=='admin' and password=='password':
        return render_template('signin-ok.html', username=username)
    return render_template('home.html', message='Bad username or password', username=username)


@app.route('/confirm_key', methods=['POST'])
def confirm_key():
    level = request.form['level']
    dungeon = request.form['dungeon']
    id = str(uuid.uuid1());
    username = request.form['username']
    values = exe_sql('select userid from user where username = %s', [username]);
    if len(values) > 0:
        userid = values[0][0]
        values = exe_sql('select userid from userkey where userid=%s', [userid]);
        # 已有记录，更新
        if len(values) > 0:
            exe_sql('update userkey set level = %s,dungeon = %s where userid = %s', [ level, dungeon,userid])
            ret = "update key"
        else:
            exe_sql('insert into userkey (id, level,dungeon,userid) values (%s, %s,%s,%s)', [id, level, dungeon, userid])
            ret = "insert key"
    else :
        ret = "user error"
    return jsonify(ret)


@app.route('/query_key', methods=['POST'])
def query_key():
    values = exe_sql('select dungeon,level,username from userkey,user where userkey.userid =user.userid ')
    json_str = json.dumps(values, ensure_ascii=False)
    return jsonify(values)



if __name__ == '__main__':
    app.debug = True
    app.run()

