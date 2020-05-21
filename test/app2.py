#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from flask import Flask
from flask import request
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    return '<h1>Home</h1>'

@app.route('/signin', methods=['GET'])
def signin_form():
    return '''<form action="/signin" method="post">
              <p><input name="username"></p>
              <p><input name="password" type="password"></p>
              <p><button type="submit">Sign In</button></p>
              </form>'''

@app.route('/signin', methods=['POST'])
def signin():
    # 需要从request对象读取表单内容：
    if request.form['username']=='admin' and request.form['password']=='password':
        return '<h3>Hello, admin!</h3>'
    return '<h3>Bad username or password.</h3>'


# 大新闻排行榜
@app.route('/big_news', methods=['POST'])
def big_news():
    conn = redis.Redis(host="101.37.116.142", port=193)
    conn = redis.Redis(**config_redis)
    conn.set("x1", "hello", ex=1000)  # ex代表seconds，px代表ms
    val = conn.get("x1")
    print(val)
    for i in range(10):
        conn.lpush('names_list1', *['把几个'+str(i), '鲁宁'+str(i)])  #
        conn.rpush('names_list1', *['r把几个'+str(i), 'r鲁宁'+str(i)])  #
    v = conn.llen('names_list')
    #
    list = []
    for i in range(100):
        val = conn.rpop('names_list')
        # 从右边第一条开始pop数据
        # val = conn.lpop('names_list')
        # 从左边第一条开始pop数据
        # print(val.decode('utf-8'))
        list.append(val.decode('utf-8'))
    v = conn.llen('names_list')
    # list = [{'a':4},{"a":5}]
    # list = [4,5]
    print(v)

    # pool = redis.ConnectionPool(host="192.168.23.166", port=6379, password="123456", max_connections=1024)
    pool = redis.ConnectionPool(**config_redis_pool)
    conn = redis.Redis(connection_pool=pool)
    print(conn.get("x1"))

    return jsonify({"a":list})
    # ret_ok_json(list)


if __name__ == '__main__':
    app.debug = True
    app.run()