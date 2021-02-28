# coding=utf-8
# Class representation of the database structure. Table stores the time lapsed for each run of the stopwatch.
from sqlalchemy import Column, Float, Integer
from base import Base


class WatchHistory(Base):
    __tablename__ = 'WatchHistory'

    sessionID = Column(Integer, primary_key=True)  # Should auto increment
    timeLapsed = Column(Float)

    def __init__(self, time_lapsed):
        self.timeLapsed = time_lapsed

    def __str__(self):
        return f'WatchHistory({self.sessionID},{self.timeLapsed})'


