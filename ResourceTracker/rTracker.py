#!/usr/bin/env python
import os
import sys
import signal
import getopt
import time
import cStringIO
import shutil
import re
import Image
from myUtility import *
import dirMon

##################################

class Resource (object):
    """ Basic Resource class """
    genericRED  = 'red'
    genericBoy  = 'blue'
    genericGirl = 'green'
    genericBoth = 'black'
    genericNone = 'yellow'
    genericUnknown = 'purple'
    def __init__(self, **kwargs):
        """ Set up arguments allowed and set all defaults to None """
        self._names = ("outDir","thumbSize","boy","girl","summaryColumns","nothing")
        for k in self._names: # Set the defaults
            setattr(self,k,None)
        # Set special default values 
        self.outDir = "~/resource"
        for k,v in kwargs.items():
            assert k in self._names, "Unexpected kwarg: " + k
            setattr(self,k,v)

        # Create directory for output page`
        self.outImages = self.outDir+"/images"
        dprintf ("Create output directory => %s and %s\n",self.outDir,self.outImages)
        if os.path.exists(self.outDir):
            shutil.rmtree(self.outDir)

        os.mkdir(self.outDir)
        os.mkdir(self.outImages)

        # Create stream to use for the output string and generate the page header
        self.output = cStringIO.StringIO()
        self.header = """<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" 
		"http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
		<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">
		<table border=1 cellspacing=5 cellpadding=5>
		""" 
        self.appendStr(self.header)

        # Initialize item count (for the summary column count
        self.count = 1

    def trSummary (self,startFlag=False, stopFlag=False):
        """ Function used to generate table row splits (for summary page) """
        if startFlag:
            myResStr = """<tr>"""
            self.appendStr(myResStr)
        if stopFlag:
            myResStr = """</tr>"""
            self.appendStr(myResStr)

    def fileSummary (self,filename,txtFlag,gender,cost,trac):
        """ Function used to generate the summary page """
        thumbFilename = self.outImages+"/"+os.path.basename(filename)
        if gender == Resource.genericBoy:
            owner = self.boy
        elif gender == Resource.genericGirl:
            owner = self.girl
        elif gender == Resource.genericBoth:
            owner = 'Both'
        else:
            owner = '????'
        if trac == None:
          trac = " "

        if os.path.isfile(thumbFilename):
            print "THUMBFILE: "+thumbFilename+" EXISTS...EXITING"
            sys.exit(-1)
        shutil.copy(filename, self.outImages)
        image = Image.open(thumbFilename)
        image.thumbnail((self.thumbSize,self.thumbSize))
        image.save(thumbFilename)
        if self.count == 1:
            self.trSummary(True,False)
        if txtFlag:
          myResStr = """
           <td>
            <center>
              <a><img src=%s></a>
              <br>
              <font face="verdana, helvetica" size="+0"color="#660000">
                %s<br/><font size="-2"><i>O:%s $:%d [%s]</i></font>
              </font>
            </center>
           </td>
	  """ \
          %(self.stripImagePath(thumbFilename),os.path.splitext(os.path.basename(filename))[0],owner,int(cost),trac)
        else:
          myResStr = """
           <td>
            <center>
              <a><img src=%s></a>
              <br>
              <font face="verdana, helvetica" size="+0"color="#660000">
                %s<br/><font size="-2"><i>MISSING DESCRIPTION FILE</i></font>
              </font>
            </center>
           </td>
	  """ \
          %(self.stripImagePath(thumbFilename),os.path.splitext(os.path.basename(filename))[0])

        self.appendStr(myResStr)

        dprintf ("Count:%d summaryColumns:%d (%d)\n",self.count,self.summaryColumns, self.summaryColumns % self.count)
        if not  self.count % self.summaryColumns:
            self.trSummary(False,True)
            self.trSummary(True,False)
        self.count += 1

    def fileWOdescription(self,filename):
        thumbFilename = self.outImages+"/"+os.path.basename(filename)
        if os.path.isfile(thumbFilename):
            print "THUMBFILE: "+thumbFilename+" EXISTS...EXITING"
            sys.exit(-1)
        shutil.copy(filename, self.outImages)
        image = Image.open(thumbFilename)
        image.thumbnail((self.thumbSize,self.thumbSize))
        image.save(thumbFilename)

        myResStr = """
	<tr>
	  <th rowspan="2"><img src=%s alt="thumbfile"></th>
	  <td><b>title:</b>%s<br/>NEED DESCRIPTION<br/></td>
	</tr>
	<tr>
	 <td valign="bottom">
	   <table border="8" cellspacing="1" align="center" bordercolor=%s>
	     <tr><td>Value: $$$$ </td><td>Tracking Number: #### </td><td>verified [&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;] </td></tr>
	   </table>
	 </td>
	</tr>
	""" \
        %(self.stripImagePath(thumbFilename),os.path.splitext(os.path.basename(filename))[0],Resource.genericRED)
        self.appendStr(myResStr)

    def fileWorWOvalueWOowner(self,filename):
        thumbFilename = self.outImages+"/"+os.path.basename(filename)
        if os.path.isfile(thumbFilename):
            print "THUMBFILE: "+thumbFilename+" EXISTS...EXITING"
            sys.exit(-1)
        shutil.copy(filename, self.outImages)
        image = Image.open(thumbFilename)
        image.thumbnail((self.thumbSize,self.thumbSize))
        image.save(thumbFilename)

        filename,txtFlag,desc,cost,trac,gend,bothOwner = self.processFile(filename)
        if not txtFlag:
            return

        myResStr = """
	<tr>
	  <th rowspan="2"><img src=%s alt="thumbfile"></th>
	  <td><b>title:</b>%s<br/>%s<br/></td>
	</tr>
	<tr>
	 <td valign="bottom">
	""" \
        %(self.stripImagePath(thumbFilename),os.path.splitext(os.path.basename(filename))[0],desc)
        self.appendStr(myResStr)

        myResStr = """
	   <table border="8" cellspacing="1" align="center" bordercolor=%s>
	     <tr><td align="center">LIQUIDATE</td><td align="center">LIQUIDATE</td><td align="center">LIQUIDATE</td></tr>
	     <tr><td>Value: $%d </td><td>Tracking Number: %s </td><td>verified [&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;] </td></tr>
	     <tr><td align="center">LIQUIDATE</td><td align="center">LIQUIDATE</td><td align="center">LIQUIDATE</td></tr>
	   </table>
	  """ \
          %(Resource.genericNone,int (cost),"####")
        self.appendStr(myResStr)


        myResStr = """
	 </td>
	</tr>
	"""
        self.appendStr(myResStr)

    def fileWvalueWowner(self,filename,gendOverride=None, match=None):
        thumbFilename = self.outImages+"/"+os.path.basename(filename)
        if os.path.isfile(thumbFilename):
            if gendOverride == None:
                print "THUMBFILE: "+thumbFilename+" EXISTS...EXITING"
                sys.exit(-1)
        shutil.copy(filename, self.outImages)
        image = Image.open(thumbFilename)
        image.thumbnail((self.thumbSize,self.thumbSize))
        image.save(thumbFilename)

        filename,txtFlag,desc,cost,trac,gend,bothOwner = self.processFile(filename)
        if gendOverride:
            cost = int(cost) / 2
            gend = gendOverride

        if not txtFlag:
            return
        if match:
            if gend == Resource.genericBoy:
                if match != self.boy:
                    return
            if gend == Resource.genericGirl:
                if match != self.girl:
                    return

        myResStr = """
	<tr>
	  <th rowspan="2"><img src=%s alt="thumbfile"></th>
	  <td><b>title:</b>%s<br/>%s<br/></td>
	</tr>
	<tr>
	 <td valign="bottom">
	""" \
        %(self.stripImagePath(thumbFilename),os.path.splitext(os.path.basename(filename))[0],desc)
        self.appendStr(myResStr)

        if trac:
          tracSplit = trac.split(',')
          tracDivide = len(tracSplit)
          for singleTrac in tracSplit:
            if gendOverride:
              if tracDivide > 1:
                tracDivide /= 2
              # If gendor override, assuming equal numbers of track numbers for each boy/girl
              if self.boy in trac and self.girl in trac:
                if gendOverride == Resource.genericBoy:
                    if self.girl in singleTrac:
                      continue
                if gendOverride == Resource.genericGirl:
                    if self.boy in singleTrac:
                      continue
                myResStr = """
	         <table border="4" cellspacing="1" align="center" bordercolor=%s>
	           <tr><td>Value: $%d </td><td>Tracking Number: %s </td><td>verified [&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;] </td></tr>
	         </table>
	        """ \
                %(gend,int(cost)/int(tracDivide),singleTrac)
              else:
                myResStr = """
	         <table border="4" cellspacing="1" align="center" bordercolor=%s>
	           <tr><td>Value: $%d </td><td>Tracking Number: %s </td><td>verified [&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;] </td></tr>
	         </table>
	        """ \
                %(gend,int(cost)/int(tracDivide),singleTrac)
            else:
              myResStr = """
	       <table border="4" cellspacing="1" align="center" bordercolor=%s>
	         <tr><td>Value: $%d </td><td>Tracking Number: %s </td><td>verified [&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;] </td></tr>
	       </table>
	      """ \
              %(gend,int(cost)/int(tracDivide),singleTrac)


            self.appendStr(myResStr)
        else:
            myResStr = """
	     <table border="4" cellspacing="1" align="center" bordercolor=%s>
	       <tr><td>Value: $%d </td><td>Tracking Number: %s </td><td>verified [&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;] </td></tr>
	     </table>
	    """ \
            %(gend,int (cost),"####")
            self.appendStr(myResStr)

        myResStr = """
	 </td>
	</tr>
	"""
        self.appendStr(myResStr)

    def outputSingleRow(self, filename,cost,boyCost,girlCost):
        dprintf ("File:%s Cost:%d Boy:%d Girl:%d\n",filename,cost,boyCost,girlCost)

        thumbFilename = self.outImages+"/"+os.path.basename(filename)
        if os.path.isfile(thumbFilename):
            if gendOverride == None:
                print "THUMBFILE: "+thumbFilename+" EXISTS...EXITING"
                sys.exit(-1)
        shutil.copy(filename, self.outImages)
        image = Image.open(thumbFilename)
        image.thumbnail((self.thumbSize,self.thumbSize))
        image.save(thumbFilename)

        txtFile,oldExt = os.path.splitext(os.path.basename(filename))

        myResStr = """
	<tr>
	  <th rowspan="1"><img src=%s alt="thumbfile"></th><th>%s</th><th>$%d</th><th>$%d</th><th>$%d</th>
	</tr>
	""" \
        %(self.stripImagePath(thumbFilename),txtFile,cost,boyCost,girlCost)

        self.appendStr(myResStr)

    def outputHeaderRow(self,boyName,girlName):
        myResStr = """
	<tr>
	  <th>RESOURCE</th><th>NAME</th><th>VALUE</th><th>%s</th><th>%s</th>
	</tr>
	""" \
        %(boyName,girlName)

        self.appendStr(myResStr)

    def outputFooterRow(self,total,boyTotal,girlTotal):
        myResStr = """
	<tr>
	  <th>TOTAL</th><th></th><th>$%d</th><th>$%d</th><th>$%d</th>
	</tr>
	""" \
        %(total,boyTotal,girlTotal)

        self.appendStr(myResStr)

    def processFile(self,filename):
        txtFlag = False
        desc = ""
        cost = 0
        trac = None
        gend = Resource.genericUnknown
        bothOwner = False
        dprintf ("PROCESS: %s\n",filename)
        txtFile,oldExt = os.path.splitext(filename)
        txtFile += ".txt"
        dprintf ("TXT-FILE: %s\n",txtFile)
        if os.path.isfile(txtFile):
            txtFlag = True
            infile = open(txtFile,"r")
            while infile:
              line = infile.readline()
              if not line:
                  break
              dprintf ("LINE:%s",line)
              line = line.lstrip()
              if len(line) == 0:
                  continue
              if re.match ("^\$",line):
                  line = line.rstrip()
                  cost = re.sub("\D","",line)
                  continue
              if re.match ("^\@",line):
                  if re.match("\@\@",line):
                      bothOwner = True
                      gend = Resource.genericBoth
                  else:
                      line = line.rstrip()
                      if re.search(self.boy,line):
                        gend = Resource.genericBoy
                      elif re.search(self.girl,line):
                        gend = Resource.genericGirl
                      else:
                        gend = Resource.genericUnknown
                  continue
              if re.match ("^\#",line):
                  line = line.rstrip()
                  trac = re.sub("#","",line)
                  continue
              desc += line
        desc = re.sub("\n","<br/>",desc)

        return (filename,txtFlag,desc,cost,trac,gend,bothOwner)

    def appendStr(self,outString):
        self.output.write(outString)

    def outputPage(self):
        if self.summaryColumns:
            self.trSummary(False,True)

        self.footer = """
		</table>
		""" 
        self.appendStr(self.footer)

        self.footer = """
                <hr>
		<br>Report Generated: <u>%s</u><br><br>
                <hr>
                Date: _______________________<br><br>
                Signature (%s): _________________________________________________<br><br>
                <hr>
                Date: _______________________<br><br>
                Signature (%s): _________________________________________________<br><br>
                <hr>
		""" %(time.ctime(),self.boy,self.girl) 
        self.appendStr(self.footer)

        self.footer = """
		</html>
		""" 
        self.appendStr(self.footer)

        self.contents = self.output.getvalue()
        outFd = open(self.outDir+"/index.html","w")
        outFd.write(self.contents)
        outFd.close()

    def stripImagePath(self,path):
        tempStr = path.replace(self.outDir, ".")
        return (tempStr)

def myMain():
    preFilter = None
    thumbSize = 200
    boyName = "Boy"
    girlName = "Girl"
    matchName = None
    summaryColumns = 0
    generateReport = False
    generateGraphicsReport = False

    signal.signal(signal.SIGINT, onSignal) # Keyboard

    try:
        opts, args = getopt.getopt(sys.argv[1:], \
            "hdf:t:b:g:m:s:rR", ["help", "debug", "filter=","thumb=","boy=","girl=","match=","summary=","report","REPORT"])
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
            setPrintDebugFlag (True)
        elif o in ("-f", "--filter"):
            try:
              preFilter = a
            except:
              print "ERROR converting filter argument:",a
              usage()
        elif o in ("-t", "--thumb"):
            try:
              thumbSize = int(a)
            except:
              print "ERROR converting thumb argument:",a, " (MUST BE AN INTEGER)"
              usage()
        elif o in ("-b", "--boy"):
            try:
              boyName = a
            except:
              print "ERROR converting boyname argument:",a
              usage()
        elif o in ("-g", "--girl"):
            try:
              girlName = a
            except:
              print "ERROR converting girlname argument:",a
              usage()
        elif o in ("-m", "--match"):
            try:
              matchName = a
            except:
              print "ERROR converting match argument:",a
              usage()
        elif o in ("-s", "--summary"):
            summaryColumns = int(a)
        elif o in ("-r", "--report"):
            generateReport = True
        elif o in ("-R", "--REPORT"):
            generateGraphicsReport = True
        else:
            assert False, "unhandled option"

    if len(args) > 1:
        inDir = args[0]
        inDir = os.path.abspath(inDir)
        outDir = args[1]
        outDir = os.path.abspath(outDir)
    else:
        print "USAGE ERROR... in-Directory AND out-Directory REQUIRED"
        usage()

    dprintf ("Starting %s thumbSize:%d boy:%s girl:%s summaryCol:%d genReport:%s IN:%s OUT:%s\n", \
        sys.argv[0],thumbSize,boyName,girlName,summaryColumns,generateReport,inDir,outDir)

    myRes = Resource(**{"outDir":outDir,"thumbSize":thumbSize,"boy":boyName,"girl":girlName,"summaryColumns":summaryColumns})
    if preFilter:
      dirFilter = preFilter+"*.jpg;"+preFilter+"*.JPG"
    else:
      dirFilter = "*.jpg;*.JPG"
    dm = dirMon.DirMon(inDir,dirFilter)

    if generateReport:
        reportTypes = ['list','missingTxt','boy','girl','both','liquidate']
        for report in reportTypes:
            dm.reset()
            costTotal = 0
            reportType = report
            if report == 'boy':
                reportType = boyName
            if report == 'girl':
                reportType = girlName
            printf ("++++++++++++++++++++++++ REPORT:%s\n",reportType)
            for nfile in dm.fileLister:
                dprintf ("FILE: %s\n",nfile)
                filename,txtFlag,desc,cost,trac,gend,bothOwner = myRes.processFile(nfile)
                if report == 'list':
                    printf ("FILE:%s Flg:%s c:%s g:%s bO:%s\n",os.path.basename(filename),txtFlag,cost,gend,bothOwner)
                    if txtFlag:
                        costTotal += int(cost)
                if report == 'missingTxt':
                    if not txtFlag:
                        printf ("FILE:%s with missing TXT description-file\n",os.path.basename(filename))
                if report == 'boy':
                    if gend == Resource.genericBoy:
                        printf ("FILE:%s ownership:%s cost:%d\n",os.path.basename(filename),boyName,int(cost))
                        costTotal += int(cost)
                if report == 'girl':
                    if gend == Resource.genericGirl:
                        printf ("FILE:%s ownership:%s cost:%d\n",os.path.basename(filename),girlName,int(cost))
                        costTotal += int(cost)
                if report == 'both':
                    if gend == Resource.genericBoth:
                        printf ("FILE:%s ownership:BOTH cost:%d\n",os.path.basename(filename),int(cost))
                        costTotal += int(cost)
                if report == 'liquidate':
                    if txtFlag and gend == Resource.genericUnknown:
                        printf ("FILE:%s LIQUIDATE-LIQUIDATE cost:%d\n",os.path.basename(filename),int(cost))
                        costTotal += int(cost)
            printf ("TOTAL VALUE:%d\n",costTotal)

        sys.exit(-1)

    if generateGraphicsReport:
        myRes.outputHeaderRow(boyName,girlName)
        total=0
        boyTotal=0
        girlTotal=0

        for nfile in dm.fileLister:
            dprintf ("FILE: %s\n",nfile)
            filename,txtFlag,desc,cost,trac,gend,bothOwner = myRes.processFile(nfile)
            if gend != Resource.genericUnknown:
                total += int(cost)
                boyCost = 0
                girlCost = 0
                if gend == Resource.genericBoy:
                    boyCost = int(cost)
                    boyTotal += boyCost
                elif gend == Resource.genericGirl:
                    girlCost = int(cost)
                    girlTotal += girlCost
                elif gend == Resource.genericBoth:
                    boyCost = int(cost)/2
                    girlCost = int(cost)/2
                    boyTotal += boyCost
                    girlTotal += girlCost

                myRes.outputSingleRow(filename,int(cost),boyCost,girlCost)

        myRes.outputFooterRow(total,boyTotal,girlTotal)
        myRes.outputPage()

        sys.exit(-1)

    for nfile in dm.fileLister:
        filename,txtFlag,desc,cost,trac,gend,bothOwner = myRes.processFile(nfile)
        dprintf ("F:%s Flg:%s desc:%s c:%s t:%s g:%s bO:%s\n",filename,txtFlag,desc,cost,trac,gend,bothOwner)
        if not summaryColumns:
          if txtFlag:
            if gend == Resource.genericUnknown:
              if not matchName:
                  myRes.fileWorWOvalueWOowner(nfile)
            else:
              if bothOwner:
                myRes.fileWvalueWowner(nfile,gendOverride=Resource.genericBoy,match=matchName)
                myRes.fileWvalueWowner(nfile,gendOverride=Resource.genericGirl,match=matchName)
              else:
                myRes.fileWvalueWowner(nfile,match=matchName)
          else:
            myRes.fileWOdescription(nfile)
        else:
          myRes.fileSummary(nfile,txtFlag,gend,cost,trac)

    myRes.outputPage()

def onSignal(signum, stackframe):
    if (signum == signal.SIGINT):
      print "<CTRL-C> by operator, EXITING... "
    sys.exit(-1)

def usage():
    print \
    """
    Usage (%s):
	arguments:
	    [-h,--help] (displays this Help information)
	    [-d,--debug] (enables Debug mode)
            [-f,--filter directory filter <filter>*.jpg
            [-t,--thumb  <thumbfile size>] (sets the thumbfile size)
            [-b,--boy   <name>] (sets the color blue associated with name)
            [-g,--girl  <name>] (sets the color green associated with name)
            [-m,--match  <name>] (sets the match name)
            [-s,--summary <#-of-columns-per-row>] Generate a summary page (ex:-s 4 -t 150)
            [-r,--report] generates an overall report to stdout WARNING-WARNING OUTDIR IS DELETED
            [-R,--REPORT] generates a graphics of all "owners" items and a summation
	This script will process files at the
	current working directory... 

	Ex:
	  %s ~/inputDirectory ~/outputDirectory
    """ \
	%(sys.argv[0],sys.argv[0])
    sys.exit(-1)

main = myMain
if __name__ == '__main__':
    main()

