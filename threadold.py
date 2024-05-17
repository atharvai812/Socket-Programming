import _thread
import time

def run( threadName):
       for i in range(1,6):
               time.sleep(5)
               print (threadName," - advances by", i)


_thread.start_new_thread( run, ("Thread-1",  ) )

for i in range(1,6):
    time.sleep(5)
    print ('Main Thread -  advances by', i)
