''' A widget that can be used to control a dummy data source. 
This will eventually be replaced by a fully-featured control interface.'''

from PyQt4 import QtGui
import sys

from decoderControl_UI import MainForm
from DummyDataSource import DummyDataSource

class DecoderWidget(MainForm):
    ''' An extension of the auto-generated decoder control widget, 
    with custom functionality added to allow controlling a DummyDataSource.'''

    def __init__(self,parent=None,data_source=None):
        super(DecoderWidget,self).__init__(parent)
        self.data_source = data_source
        self.add_button_actions()

    def set_data_source(self,data_source):
        ''' Change the data source that the widget controls. '''
        self.data_source = data_source

    def add_button_actions(self):
        ''' Make clicking the buttons actually control the data source. '''
        self.startButton.clicked.connect(
            lambda _:self.data_source.start_stream())
        self.stopButton.clicked.connect(
            lambda _:self.data_source.stop_stream())


if __name__=="__main__":
    # Run the widget on its own for testing purposes
    app = QtGui.QApplication(sys.argv)
    def pr(x):
        print x
    widg = DecoderWidget(data_source=DummyDataSource(pr))
    widg.show()
    app.exec_()
