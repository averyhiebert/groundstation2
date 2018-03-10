''' A widget which will eventually be replaced by a map display.'''

from PyQt4 import QtGui, QtCore
import sys

from dataDisplay_UI import MainForm

class DataDisplayWidget(MainForm):
    ''' An extension of the auto-generated data display widget, 
    with custom functionality added to allow updating the display.'''

    # Use a signal to receive new data points from the application
    newData = QtCore.pyqtSignal(object)

    def __init__(self,parent=None):
        super(DataDisplayWidget,self).__init__(parent)
        self.newData.connect(self.on_newData)

    @QtCore.pyqtSlot(object)
    def on_newData(self,new_data):
        ''' Handle incoming data by displaying latitude and longitude. '''
        self.lat_display.setText(str(new_data["latitude"]))
        self.lon_display.setText(str(new_data["longitude"]))
        self.alt_display.setText(str(new_data["altitude"]))


if __name__=="__main__":
    # Run the widget on its own for testing purposes
    app = QtGui.QApplication(sys.argv)
    widg = DataDisplayWidget()
    widg.show()
    widg.newData.emit({"latitude":13.233,"longitude":12, "altitude":14})
    app.exec_()
