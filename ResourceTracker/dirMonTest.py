#!/usr/bin/env python
import dirMon

if __name__ == '__main__':
    dm = dirMon.DirMon("./","*.png")
    for nfile in dm.fileLister:
        print "FILE: ",nfile
    dm.reset()
    dm = dirMon.DirMon("./","*.log")
    while (True):
        try:
          nfile=dm.next()
          print "FILE: ",nfile
        except:
            break
    pass

