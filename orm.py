# 导入:
from sqlalchemy import Sequence, Integer
from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# 创建对象的基类:
Base = declarative_base()

# 定义User对象:
class Userkey(Base):
    # 表的名字:
    __tablename__ = 'userkey'

    # 表的结构:
    id = Column(String(20), primary_key=True)
    userkey_id = Column(String(20))
    userid = Column(String(20))
    level = Column(String(20))
    dungeon = Column(String(20))
    character_id = Column(String(20))


# 定义User对象:
class User(Base):
    # 表的名字:
    __tablename__ = 'user'
    id = Column(String(20), primary_key=True)
    userid = Column(String(20))
    username = Column(String(20))
    gamename = Column(String(20))
    password = Column(String(20))
    phone = Column(String(20))
    email = Column(String(20))
    birthday = Column(String(20))
    sinnup_ipv4 = Column(String(20))
    signup_time = Column(String(20))
    last_signin_time = Column(String(20))
    last_signin_ipv4 = Column(String(20))


# 定义User对象:
class Character(Base):
    # 表的名字:
    __tablename__ = 'character'
    id = Column(String(20), primary_key=True)
    character_id = Column(String(20))
    talent = Column(String(20))
    clazz = Column(String(20))
    item_level = Column(String(20))
    userid = Column(String(20))


class Article(Base):
    # 表的名字:
    __tablename__ = 'article'
    id = Column(Integer, autoincrement=True,primary_key=True)
    title = Column(String(200))
    create_time = Column(Integer)
    modify_time = Column(Integer)
    read_times = Column(Integer)
    content = Column(String(200))
    user = Column(Integer)