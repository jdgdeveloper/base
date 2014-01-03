#!/usr/bin/env python

import os
import sys
import getopt
import signal
import fnmatch
import time

#####################
# Global declarations
#####################
debug = False
filter = "*"
tempVar = 0
tempFilename = None

##############
# Main routine
##############
def main():
    global debug, filter, tempVar, tempFilename

    signal.signal(signal.SIGINT, onSignal) # Keyboard

    try:
        opts,args = getopt.getopt(sys.argv[1:], \
            "hdf:v:", ["help","debug","filter=","tempVar="])
    except getopt.GetoptError, err:
        print str(err)
        usage()

    output = None
    for o,a in opts:
        if o in ("-h","--help"):
            usage()
        elif o in ("-d","--debug"):
            debug = True
        elif o in ("-f","--filter"):
            filter = a
        elif o in ("-v","--tempVar"):
            tempVar = int(a)
            if (tempVar < 0): usage()
        else:
            assert False, "unhandled option"

    # Assign specified arguments
    if len(args) > 0:
        tempFilename = args[0]
    else:
        print "USAGE ERROR... tempFilename REQUIRED"
        usage()

    dprintf ("Starting...%s Filter=\'%s\" tempVar=%d tempFilename:%s\n",
        os.path.basename(sys.argv[0]),filter,tempVar,tempFilename)

    for path in listFiles(os.getcwd(),filter):
        if "CVS" in path: continue # Don't process CVS files
        if "svn" in path: continue # Let's not process "svn" files
        processFile(path)

    dprintf ("So Long, and Thanks for All the Fish.\n")

#############
# Subroutines
#############
def usage():
    print \
      """"
      Usage (%s):
        arguments:
          [-h,--help]   (displays this Help information)
          [-d,--debug]  (enables Debug mode)
          [-f,--filter] (sets the filter to match against ex: -f '*.py;tk*")
          [-v,--tempVar] VAR
          <tempFilename> (REQUIRED)
        This routine will process the tree at the current
        working directory.

        Ex:
          %s
       """ \
           %(sys.argv[0],sys.argv[0])
    sys.exit(-1)

def onSignal(signum, stackframe):
    if signum == signal.SIGINT:
        print "<CTRL-C> by operator, EXITING..."
    sys.exit(-1)

def printf(format, *args):
    sys.stdout.write(format % args)

def dprintf(format, *args):
    global debug
    if debug:
        printf(format, *args)

def listFiles(root, patterns="*", singleLevel=False, yeildFolders=False):
    patterns = patterns.split(";")
    for path,subdirs,files in os.walk(root):
        if yeildFolders:
            files.extend(subdirs)
        files.sort()
        for name in files:
            for pattern in patterns:
              if fnmatch.fnmatch(name,pattern):
                yield os.path.join(path,name)
                break
        if singleLevel:
            break

def processFile(file):
    dprintf("Processing:%s\n",os.path.basename(file))

################
# Execute script
################
if __name__ == "__main__":
    main()