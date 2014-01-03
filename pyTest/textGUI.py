import sys,os
import time
from Tkinter import *
from ScrolledText import ScrolledText

class LogViewer(Frame):
  def __init__(self,parent,filename):
    Frame.__init__(self,parent)
    self.filename=filename
    self.file=open(filename,'r')
    self.text=ScrolledText(parent)
    self.text.pack(fill=BOTH)
    data=self.file.read()
    self.size=len(data)
    self.text.insert(END,data)
    self.after(100,self.poll)
    self.after(1000,self.pollprint)

  def poll(self):
    if os.path.getsize(self.filename)>self.size:
      data=self.file.read()
      self.size=self.size+len(data)
      self.text.insert(END,data)
    self.after(100,self.poll)

  def pollprint(self):
    print time.ctime()
    self.after(1000,self.pollprint)

if __name__ == "__main__":
  root=Tk()
  viewer=LogViewer(root,sys.argv[1])
  viewer.mainloop()
