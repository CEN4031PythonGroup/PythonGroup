from Controller.database_controller import sendToDB, queryDB
from Data.watch_history import WatchHistory
'''
class TestTimer:
    def __init__(self, lapsed):
        self.timeLapsed = lapsed'''

timer = WatchHistory(10, 40, 30)

sendToDB(timer.startTime, timer.stopTime, timer.timeLapsed)
queryDB()
