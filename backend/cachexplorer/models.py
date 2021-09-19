from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, DateTime, Boolean, Interval, ForeignKey, PrimaryKeyConstraint, Integer
from sqlalchemy.types import DATE
from sqlalchemy.dialects.postgresql import UUID
import datetime
from werkzeug.security import generate_password_hash
from flask_login import UserMixin

Base = declarative_base()

 
class authentication(Base):

    __tablename__ = 'authentication'
    userid = Column(UUID, primary_key=True)
    username = Column(String)
    password = Column(String)


    def __repr__(self):
        return "<authentication(userid='{0}', username='{1}', password='{2}')>".format(
            self.userid, self.username, self.password)


class userinfo(Base):

    __tablename__ = 'userinfo'
    cum_id = Column(UUID, primary_key=True)
    goldstars = Column(Integer)
    totaldistance= Column(Integer)
    true_id = Column(UUID, ForeignKey('authentication.id'))

    def __repr__(self):
        return "<userinfo(true_id='{0}', goldstars='{1}', totaldistance='{2}', cum_id='{3}')>".format(
            self.true_id, self.goldstars, self.totaldistance, self.cum_id)

class currenttaskinfo(Base):

    __tablename__ = 'rides'
    curr_id = Column(UUID, primary_key=True)
    recentstartpoint = Column(String)
    length = Column(Integer)
    target = Column(String)
    true_id = Column(UUID, ForeignKey('authentication.id'))

    def __repr__(self):
        return "<currenttaskinfo(true_id='{0}', recentstartpoint='{1}', length='{2}', target='{3}', curr_id='{4}')>".format(
            self.true_id, self.recentstartpoint, self.length, self.target, self.curr_id)