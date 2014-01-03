#!/usr/bin/env python

import os
import fnmatch
import random
import Tkinter
from Tkinter import *
import Image,ImageTk
import time
import threading
import random
import Queue
import time

random.seed()

class ManagedGUI:
    def __init__(self, master, queue, imageData, imageDataFilename, endCommand):
        self.master = master
        self.queue = queue
        self.imageData = imageData
        self.imageDataFilename = imageDataFilename

        # master.title("myCanvas")
        master.title("")

        # Add more GUI stuff here

        self.fcanvas = Tkinter.Frame(self.master)
        self.canvas = Tkinter.Canvas(self.fcanvas,bg='#000000') # Black Background
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

                if msg == 'image-msg':

                  self.image = self.imageData.get(0)
                  self.imageFilename = self.imageDataFilename.get(0)
                  geo=self.master.geometry()
                  x=geo.split('+')[0].split('x')[0]
                  y=geo.split('+')[0].split('x')[1]

                  self.image.thumbnail((int(x),int(y)),Image.ANTIALIAS)
                  self.image = ImageTk.PhotoImage(self.image)

                  imX = self.image.width()
                  imY = self.image.height()

                  self.canvas.create_image(((int(x)-int(imX))/2),((int(y)-int(imY))/2),image=self.image,anchor="nw")
                  self.canvas.pack()

                  self.master.title(os.path.splitext(self.imageFilename)[0])

                elif msg == 'test-msg':
                  pass
                else:
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
        self.imageDataFilename = Queue.Queue()

        # Set up the GUI part
        self.gui = ManagedGUI(master, self.queue, self.imageData, self.imageDataFilename, self.endApplication)

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
            self.queue.put("test-msg")
            time.sleep(1.0)

    def wthdImage(self):
        """
        This thread captures and forwards an image to be displayed
        """
        while self.running:
            fileList = []
            for path in listFiles(os.getcwd(),"*.jpg;*.JPG;*.jpeg;*.gif;*.png"):
                if "CVS" in path: continue # Don't process CVS files
                if "svn" in path: continue # Let's not process "svn" files
                fileList.append(path)
            random.shuffle(fileList)
            for path in fileList:
                self.imageFile = path
                self.imageFilename = os.path.basename(self.imageFile)
                self.image = Image.open(self.imageFile)
                self.imageData.put(self.image)
                self.imageDataFilename.put(self.imageFilename)
                self.queue.put("image-msg")
                time.sleep(random.uniform(4,10)) # Random float from 4 -> 10

def listFiles(root, patterns="*", singleLevel=False, yeildFolders=False):
    patterns = patterns.split(";")
    for path,subdirs,files in os.walk(root):
        if yeildFolders:
            files.extend(subdirs)
        for name in files:
            for pattern in patterns:
              if fnmatch.fnmatch(name,pattern):
                yield os.path.join(path,name)
                break
        if singleLevel:
            break

if __name__ == '__main__':
    root = Tkinter.Tk()
    ThreadedGUI(root)
    root.mainloop()
