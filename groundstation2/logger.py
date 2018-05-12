# Created by Anar Kazimov 11/05/2018

#----------------------Description-------------------------
#Logger class receives the rocket's coordinates
#from the server and then passes them to the
#log file
#The class can Create/Write into/Read From/Delete the log file

#Writing: Whenever you need to write something just pass in the dictionary
#----------------------------------------------------------

import os, errno

class Logger:
    def __init__(self, logFileName):
        self.logFileName = logFileName        
    
    #write the elements of the dictionary in the file
    def write(self, dictionary):
        logFile = open(self.logFileName, "a")
        for param, value in dictionary.iteritems():
            logFile.write("\n" + param + ": " + value)
        
        logFile.close()
     
    #delete the file 
    def delete(self):
        try:
            os.remove(self.logFileName)
        except OSError:
            pass

	


#Below is the testing of the program
myLogger = Logger("logFIle.txt")
data = {"time":"5:15","latitude":"150m"}
myLogger.write(data)

#myLogger.delete()
