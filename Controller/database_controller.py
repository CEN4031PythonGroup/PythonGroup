from Data.base import Base, Session, engine
from Data.watch_history import WatchHistory
'''
Methods which send and retrieve data from the database.
'''

def sendToDB(start, stop, total):
    Base.metadata.create_all(engine)
    session = Session()
    timer = WatchHistory(start, stop, total)

    session.add(timer)
    session.commit()
    session.close()

def queryDB(self):
    session = Session()
    watchList = session.query(WatchHistory).all()

    print('\n### Past StopWatch :'
          '\n ID\t\tTimeLapsed\tStart Time\tEnd Time')
    for watch in watchList:
        print(f'{watch.sessionID},\t {watch.timeLapsed}, \t{watch.startTime}, \t{watch.stopTime}')
    print('')

