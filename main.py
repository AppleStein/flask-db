from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#user.dbを使う宣言
engine = create_engine('sqlite:///qpp.db')
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

#db構築する
Base.metadata.create_all(engine)
#pythonとdbの経路->作成
SessionMaker = sessionmaker(bind=engine)
session = SessionMaker()

#idは自動
user1 = User(email="thisisme@test.com", name="Python")
#user1をdbに入れる準備->格納
session.add(user1)
session.commit()