import pyqtgraph as pg
from PyQt4 import QtGui
from PyQt4 import QtCore
import sys
import time

class GraphDisplayWidget(QtGui.QDialog):
    newData = QtCore.pyqtSignal(object)

    def __init__(self, parent = None):
        super(GraphDisplayWidget, self).__init__(parent)

        pg.setConfigOption('background', 'w')
        pg.setConfigOption('foreground', 'k')

        self.view = pg.GraphicsView()
        self.graphpaper = pg.PlotItem()
        self.view.setCentralWidget(self.graphpaper)
        self.PenStyle = {'width': 1.5, 'color':(0,0,0)}
        layout = QtGui.QVBoxLayout()
        layout.addWidget(self.view)
        self.setLayout(layout)
        self.show()
        self.TimeData = []
        self.AltitudeData = []
        self.newData.connect(self.update)

    def update(self, new_data):
        self.TimeData.append(new_data["timestamp"])
        self.AltitudeData.append(new_data["altitude"])
        self.graphpaper.plot(self.TimeData, self.AltitudeData, pen = self.PenStyle)

if __name__ == "__main__":

    app = QtGui.QApplication(sys.argv)
    widg = GraphDisplayWidget()
    timer = pg.QtCore.QTimer()
    def sendData():
        yield lambda: widg.newData.emit({"altitude": 0, "timestamp": 0})
        yield lambda: widg.newData.emit({"altitude": 1, "timestamp": 1})
        yield lambda: widg.newData.emit({"altitude": 2, "timestamp": 2})
        yield lambda: widg.newData.emit({"altitude": 3, "timestamp": 3})
        yield lambda: widg.newData.emit({"altitude": 4, "timestamp": 4})
    a = sendData()
    timer.timeout.connect(next(a))
    timer.start(2000)
    app.exec_()
