#!/usr/bin/env python

import fnmatch
import os
import time
import traceback

class DirMon (object):
    def __init__(self,root,patterns='*',age=-1,singleLevel=False,yieldFolders=False):
        self.root= root
        self.patterns=patterns.split(';')
        self.age=age
        self.singleLevel=singleLevel
        self.yieldFolders=yieldFolders

        self.fileLister=self.listFiles()

    def next(self):
        return self.fileLister.next()

    def listFiles(self):
        currentTime = int (time.time())
        for path,subdirs,files in os.walk(self.root):
            if self.yieldFolders:
                files.extend(subdirs)
            files.sort()
            for name in files:
                try:
                    myPath=path+"/"+name
                    if (self.age >= 0):
                        aage=currentTime-os.path.getatime(myPath)
                        mage=currentTime-os.path.getmtime(myPath)
                        fileAgeSec=min(aage,mage)
                        if (fileAgeSec < self.age):
                            continue
                    for pattern in self.patterns:
                        if fnmatch.fnmatch(name,pattern):
                            yield os.path.join(path,name)
                            break
                except Exception,e:
                     print 'DirMon Exception: %s accessing %s' %(e,myPath)
                     traceback.print_exc()
            if self.singleLevel:
                break

    def getDirectory(self):
         return self.root

    def setAge(self,age):
        self.age=age
        self.reset()

    def setDirectory(self,new_dir):
        if os.path.isdir(new_dir):
            self.root=new_dir
        else:
            msg="directory not found: "+new_dir
            raise IOError, msg
        self.reset()

    def setFilter(self,patterns):
        self.patters=patterns.split(';')
        self.reset()

    def setSingleLevel(self,singleLevel):
        self.singleLevel=singleLevel
        self.reset()

    def setYieldFolders(self,yieldFolders):
        self.yieldFolders=yieldFolders
        self.reset()

    def reset(self):
        self.fileLister = self.listFiles()

if __name__ == '__main__':
    pass

