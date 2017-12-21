import threading
import time

class myThread (threading.Thread):
   def __init__(self, threadID, name,delay,counter):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name
      self.delay = delay
      self.counter = counter
   def run(self):
      print "\nStarting " + self.name
      # Get lock to synchronize threads
      threadLock.acquire()      
      print self.name+ " Acquired lock"
      print_time(self.name, self.delay,self.counter)
      # Free lock to release next thread
      print self.name+ " Lock Released"
      threadLock.release()

def print_time(threadName, delay, counter):
   while counter:
      time.sleep(delay)
      print "%s: %s" % (threadName, time.ctime(time.time()))
      counter -= 1

threadLock = threading.Lock()

# Create new threads
counter = int(raw_input("Enter the Counter"))

thread1 = myThread(1, "Thread-1", 3,counter)
thread2 = myThread(2, "Thread-2", 1,counter)

# Start new Threads
thread1.start()
thread2.start()

