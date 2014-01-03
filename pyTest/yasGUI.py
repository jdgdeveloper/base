import Tkinter
import time
import threading
import random
import Queue
import time

class GuiPart:
    def __init__(self, master, queue, endCommand):
        self.master = master
        self.queue = queue
        # Set up the GUI
        master.geometry('450x150')
        self.label = Tkinter.Label(self.master)
        self.label.pack()
        self.console = Tkinter.Button(master, text='Done', command=endCommand)
        self.console.pack()

    def processIncoming(self):
        """
        Handle all the messages currently in the queue.
        """
        while self.queue.qsize():
            try:
                self.master.title(time.ctime())
                msg = self.queue.get(0)
                self.label.config(text=msg)
                # Check contents of message and do what it says
                # As a test, we simply print it
                print msg
                
            except Queue.Empty:
                pass

class ThreadedClient:
    """
    Launch the main part of the GUI and the worker thread. periodicCall and
    endApplication could reside in the GUI part, but putting them here
    means that you have all the thread controls in a single place.
    """
    def __init__(self, master):
        """
        Start the GUI and the asynchronous threads. We are in the main
        (original) thread of the application, which will later be used by
        the GUI. We spawn a new thread for the worker.
        """
        self.master = master

        # Create the queue
        self.queue = Queue.Queue()

        # Set up the GUI part
        self.gui = GuiPart(master, self.queue, self.endApplication)

        # Set up the thread to do asynchronous I/O
        # More can be made if necessary
        self.running = 1
    	self.thread1 = threading.Thread(target=self.workerThread)
        self.thread1.start()

        # Start the periodic call in the GUI to check if the queue contains
        # anything
        self.periodicCall()

    def periodicCall(self):
        """
        Check every 100 ms if there is something new in the queue.
        """
        if not self.running:
            # This is the brutal stop of the system. You may want to do
            # some cleanup before actually shutting it down.
            import sys
            sys.exit(1)
        self.gui.processIncoming()
        self.master.after(100, self.periodicCall)

    def workerThread(self):
        """
        This is where we handle the asynchronous I/O. For example, it may be
        a 'select()'.
        One important thing to remember is that the thread has to yield
        control.
        """
        while self.running:
            # To simulate asynchronous I/O, we create a random number at
            # random intervals. Replace the following 2 lines with the real
            # thing.
            time.sleep(random.random() * 0.3)
            msg = random.random()
            self.queue.put(msg)

    def endApplication(self):
        self.running = 0

root = Tkinter.Tk()
client = ThreadedClient(root)
root.mainloop()
