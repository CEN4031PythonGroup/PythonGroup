# Sarah Gilbert
# CEN4031
# Main Code for application layer\

import Timer

#Function is triggered when user clicks the start button
class newTimer:
    def __init__(self):
        t = Timer.Timer()
    # def createNew(self):


#
class Buttons:

    def startButton(self):
        #create a new timer instance


        t = newTimer()
        # # start the time
        # Sessions.r
        t.start()

    #function for when user clicks the stop button
    def stopButton(self):
        #stop the timer
        newTimer.stop()

        #Display the total time elapsed
        total = newTimer.getTotal()
        print(total)

        #clear the timer
        t.startTimer = None
        t.stopTimer = None
