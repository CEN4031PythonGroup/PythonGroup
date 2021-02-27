from base import Session
from watch_history import WatchHistory


session = Session()
watchList = session.query(WatchHistory).all()

print('\n### Past StopWatch :')
for watch in watchList:
    print(f'{watch.timeLapsed} ')
print('')