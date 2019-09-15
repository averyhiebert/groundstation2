''' The application's main file.  Perform assorted setup, and then display 
the main window and start the application.'''

from PyQt5 import QtGui, QtCore, QtWidgets
from qgis.core import QgsApplication
import sys

from mainWindow_UI import Ui_MainWindow
from data_sources.dummy_source import DummyDataSource

# The following wrapper used to be added by pyuic4 automatically, but now is
#  not, unfortunately.
class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent=parent)
        self.setupUi(self)

if __name__=="__main__":
    app = QgsApplication([],True)
    QgsApplication.setPrefixPath(u'/usr/',True)
    QgsApplication.initQgis()

    main_window = MainWindow()

    # Create temporary function for "sending" data to any widgets that need it.
    def handle_data(data):
        ''' Send a new data point to each widget that wants it.'''
        main_window.mapWidgetPlaceholder.newData.emit(data)
        main_window.altitudeGraphWidget.newData.emit(data)
        main_window.velocityGraphWidget.newData.emit(data)
        main_window.mainMapWidget.newData.emit(data)

    # Set a data source for the controls widget to control
    main_window.controlsWidgetPlaceholder.set_data_source(
        DummyDataSource(handle_data))

    # Start the application
    main_window.show()
    sys.exit(app.exec_())
