# Sarah Gilbert
# CEN4031
# Timer class for application layer
import time

class Timer:
    def __init__(self):
        self.startTimer = None
        self.stopTimer = None
        self.totalTime = None

    def start(self):
       #Check that the timer is not already running
        if self.startTimer is not None:
            print("The Timer is already running, if you wish to stop it press Stop")

        # Get the starting time
        self.startTimer = time.time()

    def stop(self):

        #check that the Timer is running
        if self.startTimer is None:
            print("The Timer is not running, if you wish to start it press Start")

        #Calculate the total time and set the stop time
        self.stopTimer = time.time()
        self.totalTime = self.stopTimer - self.startTimer

    def getTotal(self):
        return self.totalTime
