import string
from sqlalchemy import DATETIME, create_engine, Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session

#user.dbを使う宣言
engine = create_engine('sqlite:///user.db')
#dbテーブルの親
Base = declarative_base()



#pythonではインスタンスとしてデータを使う
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, unique=True)
    email = Column(String)
    name = Column(String)

    def __repr__(self):
        return "User<{}, {}, {}>".format(self.id, self.email, self.name)


class Content(Base):
    __tablename__ = 'contents'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    content = Column(string)
    timestamp = Column(DATETIME)

    def __repr__(self):
        return "Content<{}, {}, {}>".format(self.id, self.name, self.content, self.timestamp)


#db構築する
Base.metadata.create_all(engine)
#pythonとdbの経路->作成
SessionMaker = sessionmaker(bind=engine)
session = scoped_session(SessionMaker)