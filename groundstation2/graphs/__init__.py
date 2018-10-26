from PyQt4 import QtGui, QtCore
import sys
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
import matplotlib.animation as animation
import time
from threading import Thread

class GraphDisplayWidget(QtGui.QDialog):
    newData = QtCore.pyqtSignal(object)

    def __init__(self, parent = None):

        super(GraphDisplayWidget, self).__init__(parent)

        self.figure1 = Figure()
        #self.figure2 = Figure()
        self.canvas1 = FigureCanvas(self.figure1)
        #self.canvas2 = FigureCanvas(self.figure2)
        self.toolbar1 = NavigationToolbar(self.canvas1, self)
        #self.toolbar2 = NavigationToolbar(self.canvas2, self)
        self.altitude_data = []
        self.time_data = []

        layout = QtGui.QVBoxLayout()
        layout.addWidget(self.toolbar1)
        layout.addWidget(self.canvas1)
        #layout.addWidget(self.toolbar2)
        #layout.addWidget(self.canvas2)
        self.setLayout(layout)
        self.newData.connect(self.on_newData)
        self.startListening()
        self.sendData()

    def startListening(self):
        self.ax1 = self.figure1.add_subplot(1,1,1)
        #ax2 = self.figure2.add_subplot(1,1,1)
        self.ax1.set_title("Altitude")
        #ax2.set_title("Velocity")

        ani1 = animation.FuncAnimation(self.figure1, self.on_newData, interval = 1000)
        #ani2 = animation.FuncAnimation(self.figure2, animate, interval = 1000)

        self.canvas1.draw()
        #self.canvas2.draw()

    def on_newData(self, new_data):
        if new_data["timestamp"] not in self.time_data:
            self.altitude_data.append(new_data["altitude"])
            self.time_data.append(new_data["timestamp"])
            print("New Data Signal!")
        self.ax1.clear()
        self.ax1.plot(self.time_data, self.altitude_data)

    def sendData(self):
        self.newData.emit({"latitude":13.233,"longitude":12, "altitude":14, "timestamp":0})
        time.sleep(1)
        self.newData.emit({"latitude":13.233,"longitude":12, "altitude":17, "timestamp":1000})
        time.sleep(1)
        self.newData.emit({"latitude":13.233,"longitude":12, "altitude":17, "timestamp":2000})
        time.sleep(1)
        self.newData.emit({"latitude":13.233,"longitude":12, "altitude":17, "timestamp":3000})
        time.sleep(1)
        self.newData.emit({"latitude":13.233,"longitude":12, "altitude":17, "timestamp":4000})
        time.sleep(1)
        self.newData.emit({"latitude":13.233,"longitude":12, "altitude":17, "timestamp":5000})

if __name__=="__main__":
    # Run the widget on its own for testing purposes
    app = QtGui.QApplication(sys.argv)
    widg = GraphDisplayWidget()
    widg.show()
    app.exec_()
