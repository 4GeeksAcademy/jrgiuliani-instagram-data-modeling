import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    user_name = Column(String(50), unique=True)
    first_name = Column(String(50))
    last_name = Column(String(50))
    email = Column(String(50), unique=True)
    password = Column(String(32))

class Follower(Base):
    __tablename__ = 'follower'
    user_from_id = Column(Integer, ForeignKey('user.id'), primary_key=True)
    user_from_id_relationship = relationship(User)
    user_to_id = Column(Integer, ForeignKey('user.id'))
    user_to_id_relationship = relationship(User)

class Comment(Base):
    __tablename__ = 'comment'
    id = Column(Integer, primary_key=True)
    comment_text = Column(String(100))
    author_id = Column(Integer, ForeignKey('user.id'))
    author_id_relationship = relationship(User)
    post_id = Column(Integer)

class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, ForeignKey('comment.post_id'), primary_key=True)
    id_relationship = relationship(Comment)
    user_id = Column(Integer, ForeignKey('user.id'))
    user_id_relationship = relationship(User)

class Media(Base):
    __tablename__ = 'media'
    id = Column(Integer, primary_key=True)
    type = Column(String) #aca debe ir dato del tipo enum pero da error, preguntar.
    url = Column(String)
    post_id = Column(Integer, ForeignKey('post.id'))
    post_id_relationship = relationship(Post)





## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
