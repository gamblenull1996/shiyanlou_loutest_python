#!/usr/bin/python
#-*- coding:utf-8 -*-

"""
1.删除先前存在的数据库，重新创建用户，课程，学习记录三张表
2.插入一个用户
3.插入一个课程
4.插入用户学习课程10分钟的学习记录
5.输出用户学习记录

"""
from sqlalchemy import create_engine
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
 
Base = declarative_base()
engine = create_engine('sqlite:///shiyanlou.db', echo=True)
 
class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(64), nullable=False, unique=True)
    usercourses = relationship('UserCourse', backref='user')
 
class Course(Base):
    __tablename__ = 'course'
    id = Column(Integer, primary_key=True)
    name = Column(String(256), unique=True)
    usercourses = relationship('UserCourse', backref='course')
 
class UserCourse(Base):
    __tablename__ = 'usercourse'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    # user = relationship('User', backref='usercourses')
    course_id = Column(Integer, ForeignKey('course.id'))
    # course = relationship('Course', backref='usercourses')
    study_time = Column(Integer)

Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()
 
new_user = User(id = 1, name='louuser1')
session.add(new_user)
 
new_course = Course(id = 2, name='loucourse1')
session.add(new_course)

new_usercourse = UserCourse(user_id=new_user.id,
                            course_id=new_course.id,
                            study_time=10)
session.add(new_usercourse)
session.commit()

print '%s - %s - %d minutes' \
      % (new_user.name, new_course.name, new_usercourse.study_time)

session.close()
