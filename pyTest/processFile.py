#!/usr/bin/env python

import os
import sys
import getopt
import signal
import fnmatch
import time
import re

#####################
# Global declarations
#####################
debug = False
inFilename = None
outFilename = None

##############
# Main routine
##############
def main():
    global debug, tempVar, inFilename, outFilename

    signal.signal(signal.SIGINT, onSignal) # Keyboard

    try:
        opts,args = getopt.getopt(sys.argv[1:], \
            "hd", ["help","debug"])
    except getopt.GetoptError, err:
        print str(err)
        usage()

    output = None
    for o,a in opts:
        if o in ("-h","--help"):
            usage()
        elif o in ("-d","--debug"):
            debug = True
        else:
            assert False, "unhandled option"

    # Assign specified arguments
    if len(args) > 1:
        inFilename = args[0]
        outFilename = args[1]
    else:
        print "USAGE ERROR... inFilename and outFilename REQUIRED"
        usage()

    dprintf ("Starting...%s in:%s out:%s\n",
        os.path.basename(sys.argv[0]),inFilename,inFilename)

    processFile(inFilename,outFilename)

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
          <inFilename> (REQUIRED)
          <outFilename> (REQUIRED)
        This routine will process the tree at the current
        working directory.

        Ex:
          %s <inFile> <outFile>
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

def processFile(inFile,outFile):
    dprintf("Processing:%s => %s\n",os.path.basename(inFile),os.path.basename(outFile))
    p = re.compile('<data>.*?</data>')
    try:
        inF = open (inFile, 'r')
        outF = open (outFile, 'w')
    except Exception, e:
        print "Can't process files... ", e
        sys.exit(-1)

    for line in inF.readlines():
        newLine = p.sub('<data></data>',line)
        outF.write(newLine)
    inF.close ()
    outF.close ()
    

################
# Execute script
################
if __name__ == "__main__":
    main()
