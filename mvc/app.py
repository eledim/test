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

    level = request.form['level']
    dungeon = request.form['dungeon']
    username = request.form['username']
    clas = request.form['character']
    talent = 0
    user_values = exe_sql('select userid from user where username = %s', [username]);


    if len(user_values) > 0:
        userid = user_values[0][0]
        character_values = exe_sql('select character_id from `character` where class = %s AND userid = %s', [clas,userid]);
        # 无该角色记录，添加
        if len(character_values) == 0:
            character_id = str(uuid.uuid1())
            exe_sql('insert into `character` (id, userid,character_id,class,talent) values (%s, %s,%s,%s,%s)',
                    [character_id, userid, character_id, clas, talent])
            ret = ret_json("insert character")
        else:
            character_id =  character_values[0][0]

        key_values = exe_sql('select userid from userkey where userid=%s and character_id=%s', [userid,character_id]);
        # 已有key记录，更新
        if len(key_values) > 0:
            exe_sql('update userkey set level = %s,dungeon = %s where userid = %s and character_id = %s', [ level, dungeon,userid,character_id])
            ret = ret_json("update key")
        else:
            userkey_id = str(uuid.uuid1())
            exe_sql('insert into userkey (id, level,dungeon,userid,character_id) values (%s, %s,%s,%s,%s)', [userkey_id, level, dungeon, userid,character_id])
            ret = ret_json("insert key")
    else :
        ret = ret_err_json("user qeury error")
    return ret


@app.route('/query_key', methods=['POST'])
def query_key():
    #values = exe_sql('select dungeon,level,username,class from userkey,user,`character` where userkey.userid =user.userid and userkey.character_id =`character`.character_id')
    sql = 'select dungeon,level,'\
          '(select username from user where user.userid = userkey.userid)as username,'\
          '(select class from `character` where userkey.character_id =`character`.character_id )as class '\
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



if __name__ == '__main__':
    app.debug = True
    app.run()

