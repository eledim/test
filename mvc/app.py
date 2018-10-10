#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Flask, request, render_template
import mysql.connector

app = Flask(__name__)
# site = 'http://eledim.xyz/'
site = 'http://127.0.0.1:5000/'
@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html',site=site)

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

@app.route('/confirm_key', methods=['POST'])
def confirm_key():
    key = request.form['key']
    dungeon = request.form['dungeon']
    # conn = mysql.connector.connect(user='root', password='1234][po', database='forum')
    # 也可以使用字典进行连接参数的管理
    config = {
        'host': '127.0.0.1',
        'port': 3306,
        'user': 'root',
        'passwd': '1234][po',
        'db': 'forum',
        'charset': 'utf8'
    }
    conn = mysql.connector.connect(**config)

    cursor = conn.cursor()
    cursor.execute('insert into user (id, key,username) values (%s, %s,%s)', ['2', '2', 'chen'])
    cursor.rowcount
    conn.commit()
    cursor.close()

if __name__ == '__main__':
    app.run()
