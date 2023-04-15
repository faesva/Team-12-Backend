from sqlalchemy import Column, Integer, String, Boolean, Date
from Config import Base

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    is_admin = Column(Boolean)
    username = Column(String(30))
    name = Column(String(255))
    email = Column(String(255))
    password = Column(String(455))


class Movie(Base):
    __tablename__ = 'movies'
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer)
    category_id = Column(Integer)
    title = Column(String(255))
    sipnosis = Column(String(1000))
    director = Column(String(60))
    release_date = Column(Date())