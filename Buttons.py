# Sarah Gilbert
# CEN4031
import Timer
import time
# class Buttons:

def startButton(self,t):
    #start the timer
    t.start()

def stopButton(self, t):
    # stop the timer
    t.stop()

    #Display the total time elapsed
    displayTotalTime(t)

    #Display the previous times
    # Add a function that will retrieve the times from the data base and display in presentation layer
    # displayPreviousTimes()
    #clear the timer
    clearTheTimer(t)
    print(t.totalTime, " ", t.startTimer, t.stopTimer)

def displayTotalTime(t):
    # If a presentation layer is created, this will display the time in the box
    # for dev/test purposes this will display the time in the console, as if there is no presentation layer

    print("Total time: " + format(t.totalTime, '0.2f') + " seconds")

def clearTheTimer(t):
    t.startTimer = None
    t.stopTimer = None
    t.totalTime = None


# def displayPreviousTimes():
    #reach out to database to get times
    #format times if need
    #pass formated times to presentation layer
