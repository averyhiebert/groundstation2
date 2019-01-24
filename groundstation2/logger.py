# Created by Anar Kazimov 11/05/2018

#----------------------Description-------------------------
#Logger class receives the rocket's coordinates
#from the server and then passes them to the
#log file
#The class can Create/Write into/Read From/Delete the log file

#Writing: Whenever you need to write something just pass in the dictionary
#----------------------------------------------------------

import json
import os, errno

class Logger:
    def __init__(self, logFileName):
        self.logFileName = logFileName     
        self.logFile = open(self.logFileName,"a")   
    
    #write the elements of the dictionary in the file
    def append(self, dictionary):
        json.dump(dictionary, self.logFile)

    #close the file when you are done
    def close(self):
        self.logFile.close()   
     
    #delete the file 
    def delete(self):
        try:
            os.remove(self.logFileName)
        except OSError:
            print("There is no such file")

	


#Below is the testing of the program
myLogger = Logger("logFIle.txt")
data = {"time":"2:15","latitude":"150m"}
myLogger.append(data)
myLogger.close()

#myLogger.delete()
