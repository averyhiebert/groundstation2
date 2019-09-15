import json
import threading
import time

from .. import AbstractDataSource
#from data_sources import AbstractDataSource

class DummyDataThread(threading.Thread):
    ''' A thread which calls a callback on a new piece of data every second '''
    def __init__(self, callback):
        super(DummyDataThread,self).__init__()
        self.callback = callback
        with open("data_sources/dummy_source/data.json","r") as f:
            file_contents = f.read()
            self.data = json.loads(file_contents)
        self.index = 0    # Index used to iterate through data list
        self.stop_flag = False

    def run(self):
        ''' Start the thread '''
        self.stop_flag = False
        while(not self.stop_flag):
            self.callback(self.data[self.index])
            self.index = (self.index + 1) % len(self.data)
            time.sleep(1)
    
    def stop(self):
        ''' Stop the thread '''
        self.stop_flag = True
        

class DummyDataSource(AbstractDataSource):
    ''' Provides as stream of prerecorded data from a .json file'''

    def __init__(self, callback = (lambda x: True)):
        self.callback = callback   # function to call on each new data point
        self.data_thread = DummyDataThread(self.callback)
        self.running = False

    def start_stream(self):
        ''' Start a stream of data, calling the callback for
        each new data point. '''
        if not self.running:
            self.data_thread = DummyDataThread(self.callback)
            self.data_thread.start()
            self.running = True

    def stop_stream(self):
        ''' Stop streaming data '''
        if self.running:
            self.data_thread.stop()
            self.running = False

    def set_callback(self,callback):
        ''' Set the function to call on each new data point '''
        self.callback = callback

def main():
    ''' Useful for testing. '''
    DDS = DummyDataSource(print)
    DDS.start_stream()
    time.sleep(5)
    DDS.stop_stream()
    DDS.start_stream()
    time.sleep(5)
    DDS.stop_stream()

