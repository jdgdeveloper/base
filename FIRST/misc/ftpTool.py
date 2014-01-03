#!/usr/bin/env python
#File:ftpSender.py
import signal, getopt, time, re
import sys, os, fnmatch
import ftplib

#################################################
# Global declarations
#################################################
debug = False
pause = 0
putFlag = False
getFlag = False
removeFlag = False

#filter = "*"
#hostname = "127.0.0.1"
#username = "anyuser"
#password = "anyuserPassword"
#remoteDir = "~/test"

filter = "*.png;*.dbg"
hostname = "10.11.66.2"
username = "anonymous"
password = "guest"
remoteDir = "/pics"

#################################################
# Main routine
#################################################
def main ():
    global debug, filter, pause, putFlag, getFlag, removeFlag, hostname, username, password, remoteDir

    signal.signal(signal.SIGINT, onSignal) # Keyboard
     
    # Extract script arguments
    try:
        opts, args = getopt.getopt(sys.argv[1:], \
            "hdf:s:pgr", ["help", "--debug", "--filter", "--sleep", "--put", "--get", "--remove"])
    except getopt.GetoptError, err:
        # print help information and exit:
        print str(err) # will print something like "option -a not recognized"
        usage()

    # Determine the input parameters
    output = None
    for o, a in opts:
        if o in ("-h", "--help"):
            usage()
            sys.exit(-1)
        elif o in ("-d", "--debug"):
            debug = True
        elif o in ("-f", "--filter"):
            filter = a
        elif o in ("-s", "--sleep"):
            pause = float(a)
            if (pause < 0 or pause > 60): usage()
        elif o in ("-p", "--put"):
            putFlag = True
        elif o in ("-g", "--get"):
            getFlag = True
        elif o in ("-r", "--remove"):
            removeFlag = True
        else:
            assert False, "unhandled option"

    # Assign specified arguments
    if len(args) > 0: hostname  = args[0]
    if len(args) > 1: username  = args[1]
    if len(args) > 2: password  = args[2]
    if len(args) > 3: remoteDir = args[3]
    
    if (putFlag==False and getFlag==False):
        getFlag=True
    
    if ((putFlag==True and getFlag==True)):
        print "ERROR: Invalid options, can only perform either a put or a get"
        usage()
	sys.exit(-1)

    # Process files...
    dprintf ("Starting...%s Filter=\"%s\" Pause=%g Put=%i Get=%i Remove=%i args:%d\n",sys.argv[0], filter, pause, putFlag, getFlag, removeFlag,  len(args))

    # Establish FTP link to remote host
    try:
      ftp = ftplib.FTP(hostname,username,password)
    except Exception:
      print "ERROR: Unable to establish connection with",hostname," EXITING..."
      sys.exit(-1)

    try:
      ftp.cwd(remoteDir)
    except Exception:
      print "ERROR: Unable to cwd to",remoteDir," EXITING..."
      sys.exit(-1)
    
    if (putFlag==True):
      for path in listFiles(os.getcwd(),filter):
        if "CVS" in path: continue # Don't process CVS files
        putFiles (ftp, path)
    elif (getFlag==True):
      getFiles (ftp)
    ftp.quit()
    
    dprintf ("So Long and Thanks for all the Fish!\n")

#################################################
# Subroutines
#################################################
def usage():
  print \
    """
    Usage (%s):
	arguments:
	    [-h,--help] (displays this Help information)
	    [-d,--debug] (enables Debug mode)
            [-f,--filter] (sets the filter ex: -f "*.py")
            [-s,--sleep] (sets the FTP sleep interval; GT:0,LT:60)
	    [-p,--put] (enables Put mode)
	    [-g,--get] (enables Get mode -- DEFAULT)
	    [-r,--remove] (enables Remove remote file only in get mode)
	    <hostname> (DEFAULT:%s)
	    <user> (DEFAULT:%s)
	    <password> (DEFAULT:%s)
	    <remote-directory> (DEFAULT:%s)

	This script will process files at the
	current working directory... 

	Ex:
	  %s host user password directory
    """ \
	%(sys.argv[0],hostname, username, password, remoteDir, sys.argv[0])
  sys.exit(-1)

def onSignal(signum, stackframe):
  if (signum == signal.SIGINT):
    print "<CTRL-C> by operator, EXITING... "
  sys.exit(-1)

def printf (format, *args):
  sys.stdout.write(format % args)

def dprintf (format, *args):
  global debug
  if (debug):
    printf (format, *args)

def listFiles(root, patterns='*', singleLevel=False, yieldFolders=False):
  patterns = patterns.split(';')
  for path,subdirs,files in os.walk(root):
    if yieldFolders:
      files.extend(subdirs)
    files.sort()
    for name in files:
      for pattern in patterns:
        if fnmatch.fnmatch(name,pattern):
	  yield os.path.join(path,name)
	  break
    if singleLevel:
      break
  
def putFiles(ftp, file):
  global hostname, username, password, remoteDir
  
  dprintf ("Processing PUT:%s (H:%s U:%s P:%s D:%s)\n",file,hostname,username,password,remoteDir)

  try:
    putFile = open(file, 'rb')
  except Exception:
    print "ERROR: Unable to open file:",file," EXITING..."
    sys.exit(-1)

  baseFile = os.path.split(file)[1]
  try:
    ftp.storbinary('STOR '+baseFile, putFile)
  except Exception:
    print "ERROR: Unable to FTP file:",file," EXITING..."
    sys.exit(-1)

  putFile.close()

  if (pause > 0): time.sleep(pause)

def getFiles(ftp):
  global hostname, username, password, remoteDir
  
  dprintf ("Processing GET:%s (H:%s U:%s P:%s D:%s)\n",file,hostname,username,password,remoteDir)

  try:
    fileList = ftp.nlst()
  except Exception:
    print "ERROR: Unable to get remote directory listing EXITING..."
    sys.exit(-1)
    
  for currentFile in fileList:
    if fnmatch.fnmatch(currentFile,filter):
      dprintf ("Processing file:%s\n",currentFile)
      gFile = open(currentFile, "wb")
      try:
        ftp.retrbinary('RETR '+currentFile, gFile.write)
      except Exception:
        print "ERROR: Unable to GET file:",currentFile," EXITING..."
        sys.exit(-1)
      gFile.close()
      
      if (removeFlag==True):
        try:
          ftp.delete(currentFile)
        except Exception:
          print "ERROR: Unable to DELETE remote file:",currentFile," EXITING..."
          sys.exit(-1)

      if (pause > 0): time.sleep(pause)

#################################################
# Execute script
#################################################
if __name__ == "__main__":
  main()

