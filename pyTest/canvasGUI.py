"""
This recipe describes how to handle asynchronous I/O in an environment where
you are running Tkinter as the graphical user interface. Tkinter is safe
to use as long as all the graphics commands are handled in a single thread.
Since it is more efficient to make I/O channels to block and wait for something
to happen rather than poll at regular intervals, we want I/O to be handled
in separate threads. These can communicate in a threasafe way with the main,
GUI-oriented process through one or several queues. In this solution the GUI
still has to make a poll at a reasonable interval, to check if there is
something in the queue that needs processing. Other solutions are possible,
but they add a lot of complexity to the application.

Created by Jacob Hallen, AB Strakt, Sweden. 2001-10-17
"""
import Tkinter
from Tkinter import *
#from PIL import Image,ImageTk
import Image,ImageTk
import time
import threading
import random
import Queue
import time

class ManagedGUI:
    def __init__(self, master, queue, imageData, endCommand):
        self.master = master
        self.queue = queue
        self.imageData = imageData

        #master.geometry("%dx%d+%d+%d" %(800,400,0,0))
        master.title("RobotI")

        # Add more GUI stuff here

        self.label = Tkinter.Label(self.master)
        self.label.pack()
        self.console = Tkinter.Button(master, text='Quit', command=endCommand)
        self.console.pack()

        self.fcanvas = Tkinter.Frame(self.master)
        self.canvas = Tkinter.Canvas(self.fcanvas,bg='#000000') # Black Background
        #self.canvas.pack(expand=YES,fill=BOTH)
        self.canvas.pack(expand=YES,fill=BOTH,side="top")
        self.fcanvas.pack(expand=YES,fill=BOTH,side="top")

        self.master.protocol ("WM_DELETE_WINDOW",endCommand)
        
    def processQueue(self):
        """
        Handle all the messages currently in the queue (if any).
        This will handle all GUI updates.
        """
        while self.queue.qsize():
            try:
                msg = self.queue.get(0)

                if msg == 'image':
                  self.image = self.imageData.get(0)
                  geo=self.master.geometry()
                  x=geo.split('+')[0].split('x')[0]
                  y=geo.split('+')[0].split('x')[1]

                  # Write image to disk as thumbnail
                  self.thumb = self.image.copy()
                  self.thumb.thumbnail((128,128))
                  self.thumb.save("./thumb.jpg")

                  self.image.thumbnail((int(x),int(y)))

                  self.image = ImageTk.PhotoImage(self.image)


                  self.label.config(text = str(time.ctime())+" ("+str(self.image.width())+"x"+str(self.image.height())+")")
                  iwidth = self.image.width()
                  iheight = self.image.height()
                  #self.canvas.xview_moveto(0)
                  #self.canvas.yview_moveto(0)
                  #self.canvas.create_image(0,0,image=self.image,anchor="nw")
                  self.canvas.create_image(((int(x)-int(iwidth))/2),((int(y)-int(iheight))/2),image=self.image,anchor="nw")
                  #self.canvas.scale(ALL,1,1,200,100)# DOES NOT WORK
                  #self.canvas.scale(ALL,1,1,1,1)# DOES NOT WORK
                  #self.canvas.scale(ALL,.8,.8,2272,1704)# DOES NOT WORK
                  #self.canvas.scale(ALL,.9,.9,2272,1704)# DOES NOT WORK
                  #self.canvas.scale(ALL,.4,.4,1000,1000)# DOES NOT WORK
                  #self.canvas.move(ALL,200,100)
                  self.canvas.pack() #????
                  print self.canvas.cget("width")
                  print ("DisplayX:%d DisplayY:%d ImageX:%d ImageY:%d") %(int(x),int(y), int(iwidth),int(iheight))
                elif msg == 'xyz':
                  pass
                else:
                  #print msg
                  pass

            except Queue.Empty:
                pass

class ThreadedGUI:
    """
    Launch the main part of the GUI and the worker thread. wthdPeriodic and
    endApplication could reside in the GUI part, but putting them here
    means that you have all the thread controls in a single place.
    """
    def __init__(self, master):
        """
        Start the GUI and the asynchronous threads. We are in the main
        thread of the application, which will later be used by
        the GUI. We spawn a new thread for the worker.
        """
        self.master = master

        # Create the queues
        self.queue = Queue.Queue()
        self.imageData = Queue.Queue()

        # Set up the GUI part
        self.gui = ManagedGUI(master, self.queue, self.imageData, self.endApplication)

        # Set up the thread to do asynchronous I/O
        # More can be made if necessary
        self.running = 1
        self.thdMain = threading.Thread(target=self.wthdMain)
        self.thdMain.start()
        self.thdImage = threading.Thread(target=self.wthdImage)
        self.thdImage.start()

        # Start the periodic call in the GUI to check if the queue contains
        # anything
        self.wthdPeriodic()

    def endApplication(self):
        self.running = 0

    def wthdPeriodic(self):
        """
        Check every 250 ms if there is something new in the queue.
        """
        if not self.running:
            # This is the brutal stop of the system. You may want to do
            # some cleanup before actually shutting it down.
            import sys
            sys.exit(1)
        self.gui.processQueue()
        self.master.after(250, self.wthdPeriodic)

    def wthdMain(self):
        """
        This is where we handle the asynchronous I/O.
        For example, it may be a 'select()'.
        One important thing to remember is that the thread has to yield control.
        """
        while self.running:
            # To simulate asynchronous I/O, we create a random number at
            # random intervals. Replace the following 2 lines with the real
            # thing.
            time.sleep(random.random() * 0.3)
            msg = random.random()
            self.queue.put(msg)

    def wthdImage(self):
        """
        This thread captures and forwards an image to be displayed
        """
        while self.running:
            self.imageFile = "chair.jpg"
            #self.imageFile = "Z:/Image/Downloads/test.jpg"
            self.image = Image.open(self.imageFile)
            #scale = 0.1
            #im.thumbnail((int(2272*scale),int(1704*scale)))
            #self.image = ImageTk.PhotoImage(im)
            self.imageData.put(self.image)
            self.queue.put("image")
            time.sleep(1.0)

if __name__ == '__main__':
    root = Tkinter.Tk()
    ThreadedGUI(root)
    root.mainloop()
