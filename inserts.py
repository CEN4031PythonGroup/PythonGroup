from Data.base import Session, engine, Base
from Data.watch_history import WatchHistory

Base.metadata.create_all(engine)

session = Session()

sw1 = WatchHistory(60)
sw2 = WatchHistory(30)

session.add(sw1)
session.add(sw2)

session.commit()
session.close()
