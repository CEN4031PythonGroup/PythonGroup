from Controller.database_controller import sendToDB, queryDB, query
from Data.watch_history import WatchHistory
'''
class TestTimer:
    def __init__(self, lapsed):
        self.timeLapsed = lapsed'''

timer = WatchHistory(10, 40, 30)

sendToDB(timer.startTime, timer.stopTime, timer.timeLapsed)
watches = query()
for i in watches:
    print(i.timeLapsed)
    print()
