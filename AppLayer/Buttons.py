# Sarah Gilbert
# CEN4031
from Controller import database_controller
# class Buttons:

def startButton(self,t):
    # Start the timer
    t.start()

def stopButton(self, t):
    # Stop the timer
    t.stop()

    # Store data in database
    # sendtoDB(start, stop, total)
    sendToDB(t.startTimer, t.stopTimer, t.totalTime):

    # Display the total time elapsed
    displayTotalTime(t)

    # Display the previous times
    # Retrieve the times from the data base and display in presentation layer
    displayPreviousTimes()

    #clear the timer
    clearTheTimer(t)

def displayTotalTime(t):
    # If a presentation layer is created, this will display the time in the box
    # for dev/test purposes this will display the time in the console, as if there is no presentation layer

    print("Total time: " + format(t.totalTime, '0.2f') + " seconds")

def clearTheTimer(t):
    t.startTimer = None
    t.stopTimer = None
    t.totalTime = None

def displayPreviousTimes():
    #reach out to database to get times
    ## JAYME* currently the queryDB() is handling the printing of this
    ## If we want it to be displayed on screen I will need the total times to be passed
    ## in something like a list so Flask can take it.
    queryDB(self)
    #format times if need
    #pass formated times to presentation layer
