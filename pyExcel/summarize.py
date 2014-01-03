"""
PROJECT: Freekick
FILE: summarize.py

Beth Finn
Data Reduction script
"""

from Tkinter import Tk
from excelDocument import *
from time import sleep
import fnmatch


def makeHeader(summaryDoc):    
    summaryDoc.set_value("A1:A1",'Filename')
    summaryDoc.set_value("B1:B1",'Timestamp')
    summaryDoc.set_value("C1:C1",'Test')
    summaryDoc.set_value("D1:D1",'Temp')
    summaryDoc.set_value("E1:E1",'Cycle')
    summaryDoc.set_value("F1:F1",'PDM')
    summaryDoc.set_value("G1:G1",'Freq')
    summaryDoc.set_value("H1:H1",'SNR')
    summaryDoc.set_value("I1:I1",'Power')
    summaryDoc.set_value("I2:I2",'Power')
    summaryDoc.set_value("J1:J1",'Band')
    
    summaryDoc.set_value("K1:K1",'Consistency')
    summaryDoc.set_value("K2:K2",'A Consistency')
    summaryDoc.set_value("L2:L2",'B Consistency')
    
    summaryDoc.set_value("M1:M1",'In Spec')
    summaryDoc.set_value("M2:M2",'A-in Spec')
    summaryDoc.set_value("N2:N2",'B-in Spec')

    fullrange = "A1:N2"    
    summaryDoc.set_border(fullrange, borderBottom)
    summaryDoc.set_border(fullrange, borderTop)
    summaryDoc.set_border(fullrange, borderRight)
    summaryDoc.set_border(fullrange, borderLeft)
    
def insertData(summaryDoc, rowNum, filename):    
    
    # look for input data files in current directory
    workingFile = ExcelDocument(visible=False)
    workingFile.open(filename)
    
    testNum = workingFile.get_value("B1")
    timeStamp = workingFile.get_value("B3")
    pdm = workingFile.get_value("B2")
    freq = workingFile.get_value("B5")
    snr = workingFile.get_value("B8")
    power = workingFile.get_value("B10")
    band = workingFile.get_value("I11")
    consistencyA = workingFile.get_value("J7")
    consistencyB = workingFile.get_value("J8")
    inSpecFreq = workingFile.get_value("J10")
    inSpecPulseWidth = workingFile.get_value("J11")
    testFilename = workingFile.get_value("B4")
    temp = None
    cycle = None

    data = [filename, timeStamp, testNum, 
            temp, cycle, pdm, freq, snr, power, band,
            consistencyA, consistencyB,
            inSpecFreq, inSpecPulseWidth]
    workingFile.close()

    print ("writing data values:")
    print data
    rowRange = "A" + str(rowNum) + ":N" + str(rowNum)
    summaryDoc.set_value(rowRange,data)

""" Generator that returns one file each call
"""
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


def process(summaryDoc):
    print("processing doc")
    makeHeader(summaryDoc)        
    
    # look for input data files in the apropriate directory
    
    root = "C:\Sandbox\SS4"
    #root = os.getcwd()
    numHeaderRows = 2
    pattern = "PhaseData-PDM*.xls"
    filesProcessedCount = 0
    rowToInsert = numHeaderRows + 1
    
    #filename = "PhaseData-PDM1-Ch0-TestId01520.xls"
    #insertData(summaryDoc, 5, filename)
    
    print("looking in "+ root)
    for path in listFiles(root, pattern):
        print ("path = " + path)
        insertData(summaryDoc, rowToInsert, path )
        rowToInsert = rowToInsert + 1
        filesProcessedCount = filesProcessedCount + 1   
    
    print ("filesProcessedCount = " + str(filesProcessedCount) )
   
    # adjust columns
    summaryDoc.fit_column("B") 
    summaryDoc.fit_column("C")  
    summaryDoc.fit_column("D") 
    summaryDoc.fit_column("F")  

    
def run(filename = "default_summary"):
    
    # create a new spreadsheet
    print("creating excel doc  ...")
    # for now create it without a template document
    # summary = excelDocument(filename)    
    summary = ExcelDocument(visible=True)
    
    # add a workbook
    summary.new()  

    # put our data in it 
    print ("calling process")   
    process(summary)
    
    # save it to default dir - will ask for overwrite
    print ("saving")
    summary.save_as(filename, delete_existing=True)     


""" test """    
def test():
    excel.excel_demo()


if __name__ == '__main__':
    # test
    Tk().withdraw()
    #test()
    print("main calling run")
    run("new_summary")
    sleep(1)
    print("summarize completed")
    