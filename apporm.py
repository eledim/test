#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Flask, request, render_template, session, Response, redirect, url_for
import uuid
import json
import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from orm import User
from util import *
from datetime import timedelta
from flask import jsonify

app = Flask(__name__)

app.config['SECRET_KEY'] = 'eyJuZXd1cmwiOiIva2V5X3BhZ2'#os.urandom(24)  # 设置为24位的字符,每次运行服务器都是不同的，所以服务器启动一次上次的session就清除。
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=7)  # 设置session的保存时间。


# site = 'http://eledim.xyz/'
# site = 'http://127.0.0.1:5000/'
# 初始化数据库连接:
engine = create_engine('mysql+mysqlconnector://{user}:{host}@{passwd}:{port}/{db}'.format(**config4))
# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)

# 拦截器
# 默认不拦截，没有session，则返回登录
@app.before_request
def before_action():
    print(request.path)
    if request.method == 'GET':
        # 资源后缀白名单
        allow_suffix = ['.ico', '.jpg', '.css', '.ttf', '.html', '.js', '.png'];
        for i in allow_suffix:
            if request.path.find(i) != -1:
                return
        # 没有session的get请求重定向
        if not request.path == '/signin' and not request.path == '/':
            if not (request.cookies.get('username') == session.get('username') \
                    and request.cookies.get('password') == session.get('password') \
                    and session.get('username') != None):
                return redirect('/signin')  # 注意return

def has_session():
    if not 'username' in session:
        print('not username in session')
        # session['newurl'] = request.path
        return False
    return True
        # return redirect(url_for('home'))

# @app.after_request
# def after_request_action(res):
#     return  res


# 以下为get请求，返回网页
@app.route('/', methods=['GET', 'POST'])
# @cache_for(hours=3)
def home():
    return render_template('signin.html')


@app.route('/signin', methods=['GET'])
# @cache(max_age=3600, public=True)
def signin_form():
    return render_template('signin.html')


@app.route('/signin2', methods=['GET'])
def signin2():
    return render_template('home.html')


@app.route('/key_page', methods=['GET'])
# @dont_cache()
def key_page():
    # username = request.args.get('username')
    # if request.cookies.get('username') ==  session.get('username') \
    #         and request.cookies.get('password') == session.get('password')\
    #         and session.get('username') != None:
    # if session.get('username') != None:
    return render_template('key_page.html', username=session.get('username'))
     #request.cookies.get('username'))
    # else :
    #     return render_template('signin.html')


# 以下为post请求
@app.route('/test', methods=['POST'])
def test():
    # username = request.form['username']
    # password = request.form['password']
    cookie = request.cookies
    username2 = cookie.get("username")
    password2 = cookie.get("password")
    resp = Response("服务器返回信息")
    #设置cookie，
    resp.set_cookie('username','derek')
    resp.delete_cookie('username')


# 登录
@app.route('/do_signin', methods=['POST'])
def signin():
    session.permanent = True  # 默认session的时间持续31天
    a = request.get_data()
    dict1 = json.loads(a)
    username = dict1["username"]
    password = dict1["password"]
    if session.get('username') == username and session.get('password') == password:
        ret = ret_ok_json("")
        add_cookie(ret, username, password)
        return ret
    values = exe_sql('select password from user where username=%s', [username])
    if len(values) == 0:
        id = str(uuid.uuid1());
        userid = str(uuid.uuid1());
        # exe_sql('insert into user (id, userid,username,password) values (%s, %s,%s,%s)',
        #         [id, userid, username, password])

        # 创建session对象:
        sql_session = DBSession()
        # 创建新User对象:
        new_user = User(id=id, username=username,userid=userid,password=password)
        # 添加到session:
        sql_session.add(new_user)
        # 提交即保存到数据库:
        sql_session.commit()
        # 关闭session:
        sql_session.close()

        ret = ret_ok_json("add user success")
        print("add user success")
        add_cookie(ret, username, password)
        add_session(username, password)
    else:
        if password == values[0][0]:
            ret = ret_ok_json(session.get('username'))
            print("password ok")
            add_cookie(ret, username, password)
            add_session(username, password)
        else:
            ret = ret_err_json("password error")
    return ret


@app.route('/logout', methods=['POST'])
def logout():
    session.clear()
    # session.pop('password');
    resp = ret_ok_json("logout")
    resp.delete_cookie('username')
    resp.delete_cookie('password')
    return resp


def add_cookie(ret, username, password):
    #设置cookie
    ret.set_cookie('username',username)
    ret.set_cookie('password', password)
    print('add_cookie username：' + username + ' password：' + password)


def add_session(username, password):
    session['username'] = username
    session['password'] = password
    print('add_session username' + username + 'password' + password)


# 提交key
@app.route('/confirm_key', methods=['POST'])
def confirm_key():
    #  猎人Hunter
    #  圣骑士Paladin
    #  德鲁伊Druid
    #  战士Warior
    #  法师Mage
    #  牧师Priest
    #  死亡骑士Death Knight
    #  术士Warlock
    #  潜行者Rogue
    #  萨满祭司Shaman
    #  武僧Monk
    #  恶魔猎手Demon Hunter
    jsonstr = request.get_data()
    dict = json.loads(jsonstr)
    level = dict["level"]
    dungeon = dict["dungeon"]
    # username = dict1["username"]
    character = dict["character"]
    username = request.cookies.get('username')
    # level = request.form['level']
    # dungeon = request.form['dungeon']
    # username = request.form['username']
    # character = request.form['character']
    talent = 0
    user_values = exe_sql('select userid from user where username = %s', [username]);
    # 检测用户是否存在
    if len(user_values) == 0:
        return ret_err_json("user qeury error")
    userid = user_values[0][0]
    character_values = exe_sql('select character_id from `character` where class = %s AND userid = %s',
                               [character, userid]);
    # 无该角色记录，添加
    if len(character_values) == 0:
        character_id = str(uuid.uuid1())
        exe_sql('insert into `character` (id, userid,character_id,class,talent) values (%s, %s,%s,%s,%s)',
                [character_id, userid, character_id, character, talent])
        ret_ok_json("insert character")
    else:
        character_id = character_values[0][0]

    key_values = exe_sql('select level from userkey where userid=%s and character_id=%s',
                         [userid, character_id]);
    # 已有key记录且等级小，更新
    if len(key_values) > 0:
        ret_level = key_values[0][0]
        if int(ret_level) < int(level):
            exe_sql('update userkey set level = %s, dungeon = %s where userid = %s and character_id = %s ',
                    [level, dungeon, userid, character_id])
            return ret_ok_json("update key")
    # 无key记录，新增
    else:
        userkey_id = str(uuid.uuid1())
        exe_sql(
            'insert into userkey (id, userkey_id,level,dungeon,userid,character_id) values (%s, %s,%s,%s,%s,%s)',
            [userkey_id, userkey_id, level, dungeon, userid, character_id])
        return ret_ok_json("insert key")
    return ret_err_json("user qeury error")


# 查询key
@app.route('/query_key', methods=['POST'])
def query_key():
    # values = exe_sql('select dungeon,level,username,class from userkey,user,`character` where userkey.userid =user.userid and userkey.character_id =`character`.character_id')
    sql = 'select dungeon,level,' \
          '(select username from user where user.userid = userkey.userid)as username,' \
          '(select class from `character` where userkey.character_id =`character`.character_id )as class ' \
          'from userkey'

    sql3 = 'SELECT a.*,`user`.username from ' \
           '(SELECT userkey.*,`character`.class FROM userkey join `character` on userkey.character_id = `character`.character_id) as a ' \
           'JOIN `user` ' \
           'on a.userid = `user`.userid';

    sql2 = 'SELECT dungeon,level,`user`.username,`character`.class ' \
           'FROM userkey join `character` on userkey.character_id = `character`.character_id ' \
           'JOIN `user` on userkey.userid = `user`.userid'

    values = exe_sql(sql2)
    json_str = json.dumps(values, ensure_ascii=False)
    return jsonify(values)



# 旧登录
def signin2():
    username = request.form['username']
    password = request.form['password']
    if username == 'admin' and password == 'password':
        return render_template('signin-ok.html', username=username)
    return render_template('home.html', message='Bad username or password', username=username)


if __name__ == '__main__':
    app.debug = True
    app.run()
