import time
import math
from Controller.database_controller import sendToDB, queryDB


input('Press Enter to start')
start_time = math.trunc(time.time())
input('Press Enter to stop')
end_time = math.trunc(time.time())
time_lapsed = math.trunc(end_time - start_time)

sendToDB(start_time, end_time, time_lapsed)
print('Total time: ' + format(time_lapsed, '0.2f') + ' seconds')
print('')

queryDB()

