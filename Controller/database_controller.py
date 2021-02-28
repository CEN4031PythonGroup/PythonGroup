from Data.base import Base, Session, engine
from Data.watch_history import WatchHistory


def sendToDB(totalTime):
    Base.metadata.create_all(engine)
    session = Session()
    timer = WatchHistory(totalTime)

    session.add(timer)
    session.commit()
    session.close()

def queryDB(self):
    session = Session()
    watchList = session.query(WatchHistory).all()

    print('\n### Past StopWatch :')
    for watch in watchList:
        print(f'{watch.sessionID}, {watch.timeLapsed} ')
    print('')

