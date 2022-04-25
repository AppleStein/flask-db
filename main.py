import hashlib
import datetime
from flask import *
import string
from sqlalchemy import DATETIME, create_engine, Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session


app = Flask(__name__)
#user.dbを使う宣言
engine = create_engine('sqlite:///app.db')
#dbテーブルの親
Base = declarative_base()



#pythonではインスタンスとしてデータを使う
class User(Base):
    __tablename__ = 'users'
    #ユーザとパスワードを自動生成
    name = Column(String, primary_key = True, unique = True)
    pssw = Column(String)

    def __repr__(self):
        return "User<{}>".format(self.name)


class Content(Base):
    __tablename__ = 'contents'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    content = Column(String)
    timestamp = Column(DATETIME)

    def __repr__(self):
        return "Content<{}, {}, {}, {}>".format(self.id, self.name, self.content, self.timestamp)


#db構築する
Base.metadata.create_all(engine)
#pythonとdbの経路->作成
SessionMaker = sessionmaker(bind=engine)
session = scoped_session(SessionMaker)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port = 8888, threaded=True)