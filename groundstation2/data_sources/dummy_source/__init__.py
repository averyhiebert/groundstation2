''' A widget that can be used to control a dummy data source. 
This will eventually be replaced by a fully-featured control interface.'''

from PyQt5 import QtGui, QtWidgets
import sys

from .decoderControl_UI import Ui_MainForm
from .DummyDataSource import DummyDataSource

class DecoderWidget(QtWidgets.QWidget, Ui_MainForm):
    ''' An extension of the auto-generated decoder control widget, 
    with custom functionality added to allow controlling a DummyDataSource.'''

    def __init__(self,*args,data_source=None,**kwargs):
        super(DecoderWidget,self).__init__(*args,**kwargs)
        self.setupUi(self)
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
    widg = DecoderWidget(data_source=DummyDataSource(print))
    widg.show()
    app.exec_()
