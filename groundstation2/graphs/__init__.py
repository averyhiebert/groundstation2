import pyqtgraph as pg
from PyQt5 import QtGui, QtCore
import sys

class altitudeGraphDisplayWidget(QtGui.QGraphicsView):
    newData = QtCore.pyqtSignal(object)

    def __init__(self, parent = None):
        super(altitudeGraphDisplayWidget, self).__init__(parent)

        pg.setConfigOption('background', 'k')
        pg.setConfigOption('foreground', 'w')

        self.view = pg.GraphicsView()
        self.graphpaper = pg.PlotItem()
        self.view.setCentralWidget(self.graphpaper)
        self.PenStyle = {'width': 3, 'color':(255,255,255)}
        layout = QtGui.QVBoxLayout()
        layout.addWidget(self.view)
        self.setLayout(layout)
        self.show()
        self.TimeData = []
        self.AltitudeData = []
        self.VelocityData = []
        self.alt = 0
        self.t = 0
        self.newData.connect(self.update)

    def update(self, new_data):
        self.TimeData.append(new_data["timestamp"])
        self.AltitudeData.append(new_data["altitude"])
        self.graphpaper.plot(self.TimeData, self.AltitudeData, pen = self.PenStyle)

class velocityGraphDisplayWidget(QtGui.QGraphicsView):
    newData = QtCore.pyqtSignal(object)

    def __init__(self, parent = None):
        super(velocityGraphDisplayWidget, self).__init__(parent)

        pg.setConfigOption('background', 'k')
        pg.setConfigOption('foreground', 'w')

        self.view = pg.GraphicsView()
        self.graphpaper = pg.PlotItem()
        self.view.setCentralWidget(self.graphpaper)
        self.PenStyle = {'width': 3, 'color':(255,255,255)}
        layout = QtGui.QVBoxLayout()
        layout.addWidget(self.view)
        self.setLayout(layout)
        self.show()
        self.TimeData = []
        self.AltitudeData = []
        self.VelocityData = []
        self.alt = 0
        self.t = 0
        self.newData.connect(self.update)

    def update(self, new_data):
        self.TimeData.append(new_data["timestamp"])
        self.AltitudeData.append(new_data["altitude"])
        if new_data["timestamp"] != 0:
            alt_difference = new_data["altitude"] - self.alt
            t_difference = new_data["timestamp"] - self.t
            vel = alt_difference/t_difference
            self.VelocityData.append(vel)
        else:
            self.VelocityData.append(0)
        self.graphpaper.plot(self.TimeData, self.VelocityData, pen = self.PenStyle)
        self.alt =  new_data["altitude"]
        self.t = new_data["timestamp"]

if __name__ == "__main__":

    app = QtGui.QApplication(sys.argv)
    widg1 = altitudeGraphDisplayWidget()
    widg2 = velocityGraphDisplayWidget()
    timer = pg.QtCore.QTimer()
    def alt():
        alt = 1
        while True:
            yield alt
            if alt <= 100:
                alt += alt
            elif alt > 100:
                alt = 1
    def time():
        time = 0
        while True:
            yield time
            time += 1
    a = alt()
    t = time()
    timer.timeout.connect(lambda: widg1.newData.emit({"altitude": next(a), "timestamp": next(t)}))
    timer.timeout.connect(lambda: widg2.newData.emit({"altitude": next(a), "timestamp": next(t)}))
    timer.start(1000)
    app.exec_()
