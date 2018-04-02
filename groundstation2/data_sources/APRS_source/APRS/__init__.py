import subprocess
import sys
import threading
import time

#from .. import AbstractDataSource

class APRSSubprocessThread(threading.Thread):
    ''' Thread for starting and stopping the rtl_fm and
    direwolf subprocesses.'''

    def __init__(self,callback,sdr_args,direwolf_args):
        super(APRSSubprocessThread,self).__init__()
        self.callback = callback
        self.stop_flag = True
        self.sdr_args = sdr_args
        self.direwolf_args = direwolf_args

    def run(self):
        ''' Start the demodulator and decoder as subprocesses, and repeatedly
        call the callback on the output until the thread is stopped. '''
        self.stop_flag = False
        sdr_process = subprocess.Popen(
            self.sdr_args,
            stdout=subprocess.PIPE)
        direwolf_process = subprocess.Popen(
            self.direwolf_args,
            stdin=sdr_process.stdout,
            stdout=subprocess.PIPE)
        for line in iter(direwolf_process.stdout.readline,''):
            self.callback(line)
            if self.stop_flag:
                sdr_process.terminate()
                direwolf_process.terminate()
                break

    def stop(self):
        ''' Stop the thread and all subprocesses. '''
        self.stop_flag = True


class APRSDataSource():
    ''' Provide a stream of decoded APRS data using rtl_fm and Direwolf. '''

    def __init__(self, callback = (lambda x: True),
            frequency="144.39M", gain="auto", ppm="0", do_test=True):
        self.callback = callback
        self.data_thread = None
        self.running = False
       
        # Set up radio options:
        self.frequency = frequency
        self.gain = gain
        self.ppm = ppm
        self.test_mode = do_test
    
    def start_stream(self):
        ''' Start receiving APRS data from the software defined radio '''
        if self.running:
            return

        # Set appropriate subprocess arguments, based on settings:
        sdr_args = ["bash","dummy_rtlfm/run.sh"]
        if not self.test_mode:
            sdr_args = ["rtl_fm", "-f", self.frequency, 
                "-p", self.ppm, "-s","260k", "-r", "48k"]
            if self.gain != "auto":
                sdr_args += ["-g", self.gain]
        direwolf_args = ["direwolf", "-n", "1", "-r", "48000",
            "-b", "16", "-t", "0", "-"]

        self.data_thread = APRSSubprocessThread(callback=self.callback, 
            sdr_args=sdr_args, direwolf_args=direwolf_args)
        self.data_thread.start()
        self.running = True

    def stop_stream(self):
        ''' Stop the stream of data '''
        if self.running:
            self.data_thread.stop()
            self.running = False

    def set_callback(self, callback):
        ''' Set the callback to call on each new line of data '''
        self.callback = callback
        pass

    def set_frequency(self, freq):
        ''' Set the radio frequency to listen to '''
        self.frequency = freq

    def set_gain(self, gain):
        ''' Set the level of gain to use, or use the string "auto" to detect
        automatically '''
        self.gain = gain

    def set_ppm(self,ppm):
        ''' Set the ppm offset value to correct offset for the SDR hardware '''
        self.ppm = ppm

    def set_test_mode(self,do_test):
        ''' Set whether or not to use "test mode" '''
        self.test_mode = do_test

def main():
    ''' Useful for testing '''
    def pr(x):
        if x[0] == "N":
            print x
    DS = APRSDataSource(pr)
    DS.start_stream()
    time.sleep(5)
    DS.stop_stream()

if __name__=="__main__":
    main()
