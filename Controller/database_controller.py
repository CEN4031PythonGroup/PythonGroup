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

# Query the Postgres DB and print the results to console
def queryDB():
    session = Session()
    watchList = session.query(WatchHistory).all()

    print('\n### Past StopWatch Runs:'
          '\nID\tStart Time\tStop Time\tTimeLapsed')
    for watch in watchList:
        print(f'{watch.sessionID}\t{watch.startTime}\t\t{watch.stopTime}\t\t{watch.timeLapsed}')
    print('')

# Query the database and return it as a list
def query():
    session = Session()
    watchList = session.query(WatchHistory).all()

    return watchList

