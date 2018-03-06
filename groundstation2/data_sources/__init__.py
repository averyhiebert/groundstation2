class AbstractDataSource():
    ''' An abstract class enforcing an interface for 
    data source objects to be used by the main application. '''

    def start_stream(self):
        ''' Start a stream of data, calling the callback for
        each new data point. '''
        raise NotImplementedError("start_stream should be implemented")

    def stop_stream(self):
        ''' Stop streaming data '''
        raise NotImplementedError("stop_stream should be implemented")

    def set_callback(self,callback):
        ''' Set the function to call on each new data point '''
        self.callback = callback
