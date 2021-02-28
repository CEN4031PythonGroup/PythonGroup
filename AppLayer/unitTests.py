import Timer
import appLayerMain
import Buttons
import time
import unittest


class appLayerUnitTests(unittest.TestCase):

    def testTimerClass(self):
        t = Timer.Timer()
        t.start()
        time.sleep(2)
        t.stop()

    def testAppLayerMain(self):
        t = Timer.Timer()
        Buttons.startButton(self,t)
        time.sleep(3)
        Buttons.stopButton(self,t)

if __name__ == '__main__':
    unittest.main()