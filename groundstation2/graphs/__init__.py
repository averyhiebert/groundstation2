import pyqtgraph as pg
from PyQt4 import QtGui
from PyQt4 import QtCore
import sys

class GraphDisplayWidget(QtGui.QDialog):
    newData = QtCore.pyqtSignal(object)

    def __init__(self, parent = None):
        super(GraphDisplayWidget, self).__init__(parent)

        pg.setConfigOption('background', 'w')
        pg.setConfigOption('foreground', 'k')

        self.view1 = pg.GraphicsView()
        self.view2 = pg.GraphicsView()
        self.graphpaper1 = pg.PlotItem()
        self.graphpaper2 = pg.PlotItem()
        self.view1.setCentralWidget(self.graphpaper1)
        self.view2.setCentralWidget(self.graphpaper2)
        self.PenStyle = {'width': 1.5, 'color':(0,0,0)}
        layout = QtGui.QVBoxLayout()
        layout.addWidget(self.view1)
        layout.addWidget(self.view2)
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
        self.graphpaper1.plot(self.TimeData, self.AltitudeData, pen = self.PenStyle)
        if new_data["timestamp"] != 0:
            alt_difference = new_data["altitude"] - self.alt
            t_difference = new_data["timestamp"] - self.t
            vel = alt_difference/t_difference
            self.VelocityData.append(vel)
            self.graphpaper2.plot(self.TimeData, self.VelocityData, pen = self.PenStyle)
        else:
            self.VelocityData.append(0)
        self.alt =  new_data["altitude"]
        self.t = new_data["timestamp"]
if __name__ == "__main__":

    app = QtGui.QApplication(sys.argv)
    widg = GraphDisplayWidget()
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
    timer.timeout.connect(lambda: widg.newData.emit({"altitude": next(a), "timestamp": next(t)}))
    timer.start(1000)
    app.exec_()
