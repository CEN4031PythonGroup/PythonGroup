# coding=utf-8
# Class representation of the database structure. Table stores the time lapsed for each run of the stopwatch.
from sqlalchemy import Column, Float, Integer
from Data.base import Base

# This class maps its properties to match the structure of the postgres DB
class WatchHistory(Base):
    __tablename__ = 'WatchHistory'

    sessionID = Column(Integer, primary_key=True)  # Should auto increment
    timeLapsed = Column(Float)
    startTime = Column(Float)
    stopTime = Column(Float)


    def __init__(self, start, stop, lapsed):
        self.startTime = start
        self.stopTime = stop
        self.timeLapsed = lapsed


    def __str__(self):
        return f'WatchHistory [Start:({self.startTime}), Stop:({self.stopTime}), Lapsed:({self.timeLapsed})'


