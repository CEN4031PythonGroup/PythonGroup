import Timer
import appLayerMain
import Buttons
import time
import unittest

# Timer class tests
# def main():
#
#         t = Timer.Timer()
#
#         t.start()
#         time.sleep(5)
#         t.stop()
#
#         appLayerMain.Buttons.startButton(self)
#         time.sleep(3)
#         appLayerMain.Buttons.stopButton(self)
#
#
#
# main()

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