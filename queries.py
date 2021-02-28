from Data.base import Session
from Data.watch_history import WatchHistory


session = Session()
watchList = session.query(WatchHistory).all()

print('\n### Past StopWatch :')
for watch in watchList:
    print(f'{watch.sessionID}, {watch.timeLapsed} ')
print('')
