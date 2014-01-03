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
import os
import Tkinter
from Tkinter import *
from PIL import Image,ImageTk
import StringIO
import time
import threading
import Queue
import time
from socket import *
import sys, os
import ftplib

#########################
hostname = "10.11.66.2"
#########################

portNumber = 50000+0
username = "anonymous"
password = "guest"
remoteDir = "."

class ManagedGUI(object):
    def __init__(self, master, queue, imageFilename, endCommand):
        self.master = master
        self.queue = queue
        self.imageFilename = imageFilename
        self.titleText = "RobotI"
        self.time = 0
        self.toggle = 0
        self.record = False

        self.master.title(self.titleText)

        # Initialize GUI components

        self.frame = Tkinter.Frame(self.master)
        self.modeButton = Tkinter.Button(self.frame,
            text='Play', command=self.modeCommand)
        self.modeButton.pack(side='left')
        self.quitButton = Tkinter.Button(self.frame,
            text='Quit', command=endCommand)
        self.quitButton.pack(side='left')
        self.frame.pack()
        self.fcanvas = Tkinter.Frame(self.master)
        self.canvas = Tkinter.Canvas(self.fcanvas)
        self.canvas.pack(expand=YES,fill=BOTH)
        self.fcanvas.pack(expand=YES,fill=BOTH)

        self.master.protocol ("WM_DELETE_WINDOW",endCommand)

    def modeCommand(self):
      if self.modeButton.configure('text')[4] == 'Play':
          self.modeButton.configure(text="Record")
          self.record = True
      else:
          self.modeButton.configure(text="Play")
          self.record = False



    def processQueue(self):
        """
        Handle all the messages currently in the queue
        """
        while self.queue.qsize():
            try:
                msg = self.queue.get(0)

                if msg == 'imageFile':
                  self.time = time.time()
                  # Set the image TIME
                  self.master.title(self.titleText+"  "+str(time.ctime()))

                  self.imageFile = self.imageFilename.get(0)
                  self.imageRaw = Image.open(self.imageFile)
                  self.geometry=self.master.geometry()
                  self.x=self.geometry.split('+')[0].split('x')[0]
                  self.y=self.geometry.split('+')[0].split('x')[1]
                  self.imageRaw.thumbnail((int(self.x),int(self.y)))
                  self.image = ImageTk.PhotoImage(self.imageRaw)
                  self.canvas.create_image(0,0,image=self.image,anchor='nw')

                  if self.record:
                    self.recordFile = str(int(time.time())) + '.' + self.imageFile
                    os.rename(self.imageFile, self.recordFile)

                elif msg == 'main':
                  if (self.time + 10) > time.time():
                    if self.toggle:
                      self.toggle=0
                      self.modeButton.configure(bg="green")
                    else:
                      self.toggle=1
                      self.modeButton.configure(bg="white")
                  else:
                    self.modeButton.configure(bg="red")
                  pass
                else:
                  pass

            except Queue.Empty:
                pass

class ThreadedGUI(object):
    """
    Launch the main part of the GUI and the worker thread.
    """
    def __init__(self, master):
        """
        Start the GUI and the asynchronous threads. We are in the main
        thread of the application, which will later be used by
        the GUI. We spawn new threads for the workers.
        """
        self.master = master

        # Create the queues
        self.queue = Queue.Queue()
        self.imageData = Queue.Queue()

        # Set up the GUI part
        self.gui = ManagedGUI(master,
          self.queue, self.imageData, self.endApplication)

        # Set up the threaded part
        self.running = 1
        self.thdMain = threading.Thread(target=self.wthdMain)
        self.thdMain.setDaemon(True)
        self.thdMain.start()
        self.thdImage = threading.Thread(target=self.wthdImage)
        self.thdImage.setDaemon(True)
        self.thdImage.start()

        # Start the periodic call in the GUI to check if the
        # queue contains anything
        self.wthdPeriodic()

    def endApplication(self):
        self.running = 0

    def wthdPeriodic(self):
        """
        Check every 250 ms if there is something new in the queue.
        """
        if not self.running:
            # This is the brutal stop of the system.
            import sys
            sys.exit(1)
        self.gui.processQueue()
        self.master.after(250, self.wthdPeriodic)

    def wthdMain(self):
        """
        This is where we handle the asynchronous I/O.
        """
        while self.running:
            time.sleep(1.0)
            self.queue.put("main")

    def wthdImage(self):
        """
        This thread captures and forwards an imageFile for processing
        """
        self.ftp = None
        self.socket = None
        self.connect = None
        self.serverHost = hostname
        self.serverPort = portNumber
        while self.running:
            # Try to establish an FTP connection to the image server
            if not self.ftp:
                try:
                    self.ftp = ftplib.FTP(hostname,username,password)
                except Exception:
                    print "Unable to establish FTP connection with:",hostname
                    time.sleep(5)
                    continue
                try:
                    self.ftp.cwd(remoteDir)
                except Exception:
                    print "Unable to FTP connect and CWD to:",remoteDir
                    time.sleep(5)
                    continue
            if not self.ftp: # Need to connect and FTP session to the host
                continue

            # Then we need a socket (we will be the client) to the host
            if not self.socket:
                self.socket = socket(AF_INET, SOCK_STREAM)
                self.socket.settimeout(10)
            if not self.socket: # Go no further until a socket has been created
                continue

            if not self.connect: # Finally we need to connect to the server
                print "Attempting connection to image server:%s(port:%d)"  %(
                    self.serverHost,self.serverPort)
                try:
                    self.socket.connect((self.serverHost, self.serverPort))
                    self.connect = True
                except:
                    print "Could not connect to image server..."
                    self.ftp = None
                    self.socket = None
                    self.connect = None
                    time.sleep(5)
                    continue  # And try again if unsuccessful

            if self.connect: # Now we can do the work...
                try:
                    self.socket.send("i\n") # Request an imageFile from server
                    self.dataFile = self.socket.recv(256)
                    self.dataFile = self.dataFile.rstrip('\n')
                    if self.dataFile.find("FAILED") < 0:  # Process if good filename
                      # Use the FTP connection to retrieve the file
                      self.gFile = open(self.dataFile, "wb")
                      self.ftp.retrbinary('RETR '+self.dataFile, self.gFile.write)
                      self.gFile.close()

                      # Send file name to be processed
                      self.imageData.put(self.dataFile)
                      self.queue.put("imageFile")

                except:
                    print 'Could not process file from image server'
                    self.ftp = None
                    self.socket = None
                    self.connect = None

if __name__ == '__main__':
    root = Tkinter.Tk()
    gui = ThreadedGUI(root)
    root.mainloop()
