from PyQt4 import QtGui
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
import matplotlib.animation as animation
import json
import sys
import time
from threading import Thread

config_file = open("config.json")
config_text = config_file.read()
config = json.loads(config_text)

class Window(QtGui.QDialog):
    def __init__(self, parent= None):
        super(Window, self).__init__(parent)

        self.figure1 = Figure()
        self.figure2 = Figure()
        self.canvas1 = FigureCanvas(self.figure1)
        self.canvas2 = FigureCanvas(self.figure2)
        self.toolbar1 = NavigationToolbar(self.canvas1, self)
        self.toolbar2 = NavigationToolbar(self.canvas2, self)
        self.dummyButton = QtGui.QPushButton('Plot Dummy Data')
        self.dummyButton.clicked.connect(self.plot)

        layout = QtGui.QVBoxLayout()
        layout.addWidget(self.toolbar1)
        layout.addWidget(self.canvas1)
        layout.addWidget(self.toolbar2)
        layout.addWidget(self.canvas2)
        layout.addWidget(self.dummyButton)
        self.setLayout(layout)

        self.startListening()

    def startListening(self):
        ax1 = self.figure1.add_subplot(1,1,1)
        ax2 = self.figure2.add_subplot(1,1,1)
        ax1.set_title("Altitude")
        ax2.set_title("Velocity")

        def animate(i):
            json_file = open(config["data_file"])
            json_str = json_file.read()
            try:
                json_data = json.loads(json_str)
                x = []
                y = []
                velocityX = []
                velocityY = []
                for j in json_data:
                    x.append(j["timestamp"])
                    y.append(j["altitude"])
                if len(x) > 1 and len(y) > 1:
                    for alt in range(1,len(y)):
                        velocityX.append(x[alt])
                        velocityY.append(y[alt] - y[alt - 1])
                ax1.clear()
                ax2.clear()
                ax1.plot(x, y)
                ax2.plot(velocityX, velocityY)
                json_file.close()
            except:
                pass
        ani1 = animation.FuncAnimation(self.figure1, animate, interval = 1000)
        ani2 = animation.FuncAnimation(self.figure2, animate, interval = 1000)

        self.canvas1.draw()
        self.canvas2.draw()

    def plot(self):
        def dummy():
            jsonstring = open(config["dummy_data"]).read()
            jsondata = json.loads(jsonstring)
            array = []
            for j in jsondata:
                array.append(j)
                jsonstr = json.dumps(array)
                file = open(config["data_file"], "w+")
                file.truncate()
                file.write(jsonstr)
                file.close()
                time.sleep(1)

        Thread(target = dummy).start()

if __name__ == '__main__':

    app = QtGui.QApplication(sys.argv)

    main = Window()
    main.show()

    sys.exit(app.exec_())
