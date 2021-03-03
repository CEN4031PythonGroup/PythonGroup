from Data.base import Session, engine, Base
from Data.watch_history import WatchHistory

Base.metadata.create_all(engine)

session = Session()

sw1 = WatchHistory(86.03, 96.03, 10)
sw2 = WatchHistory(12, 36, 24)

session.add(sw1)
session.add(sw2)

session.commit()
session.close()
