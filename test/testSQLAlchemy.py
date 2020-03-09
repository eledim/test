# 导入:
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
    userkey_id  = Column(String(20))
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
    PASSWORD = Column(String(20))
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
    character_id  = Column(String(20))
    talent = Column(String(20))
    clazz = Column(String(20))
    item_level = Column(String(20))
    userid = Column(String(20))

# 初始化数据库连接:
engine = create_engine('mysql+mysqlconnector://root:Diablo!9234@101.37.116.142:3306/wow_key')
# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)

# 创建session对象:
session = DBSession()
# 创建新User对象:
new_user = Userkey(id='52')
# 添加到session:
session.add(new_user)
# 提交即保存到数据库:
session.commit()
# 关闭session:
session.close()

# 创建Session:
session = DBSession()
# 创建Query查询，filter是where条件，最后调用one()返回唯一行，如果调用all()则返回所有行:
user = session.query(Userkey).filter(Userkey.id=='2b8eef1a-5ef6-11ea-8dda-00163e0e3cc0').one()
# 打印类型和对象的name属性:
print('type:', type(user))
print('name:', user.userkey_id)
# 关闭Session:
session.close()