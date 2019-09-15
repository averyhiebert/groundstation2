''' The application's main file.  Perform assorted setup, and then display 
the main window and start the application.'''

from PyQt4 import QtGui
#from qgis.core import QgsApplication
import sys

from mainWindow_UI import MainWindow
from data_sources.dummy_source import DummyDataSource

if __name__=="__main__":
    app = QtGui.QApplication(sys.argv)
    #app = QgsApplication([],True)
    #QgsApplication.setPrefixPath(u'/usr/',True)
    #QgsApplication.initQgis()

    main_window = MainWindow()
    # Create temporary function for "sending" data to any widgets that need it.
    def handle_data(data):
        main_window.mapWidgetPlaceholder.newData.emit(data)
        main_window.altitudeGraphWidget.newData.emit(data)
        main_window.velocityGraphWidget.newData.emit(data)
        main_window.mainMapWidget.newData.emit(data)
    # Set a data source for the controls widget to control
    main_window.controlsWidgetPlaceholder.set_data_source(
        DummyDataSource(handle_data))
    # Start the application
    main_window.show()
    app.exec_()
