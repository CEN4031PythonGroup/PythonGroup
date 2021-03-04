from flask import Flask, render_template
import time
from AppLayer import Buttons
from AppLayer import Timer

app = Flask(__name__)
app.debug = True


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start')
def start():
    t = Timer.Timer()
    Buttons.startButton(self, t)
    # time.sleep(3)
    return render_template('started.html')

@app.route('/stop')
def stop():
    Buttons.stopButton(self, t)
    return render_template('index.html')
if __name__ == '__main__':
    app.run()
