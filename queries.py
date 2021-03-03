from Data.base import Session
from Data.watch_history import WatchHistory


session = Session()
watchList = session.query(WatchHistory).all()

print('\n### Past StopWatch Runs:'
      '\nID\tStart Time\tStop Time\tTimeLapsed')
for watch in watchList:
    print(f'{watch.sessionID}\t {watch.startTime}\t\t{watch.stopTime}\t\t{watch.timeLapsed}')
print('')