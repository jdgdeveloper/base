#!/usr/bin/python

import sys
#import gdata.docs.service
from gdata.service import GDataService

if len (sys.argv) > 1:
  password = sys.argv[1]
else:
  print "password required (in single quotes)"
  sys.exit(1)

#client=gdata.docs.service.DocsService()
#client.ClientLogin('j.dennis.griffith',password)
#documents_feed=client.GetDocumentListFeed()
#for document_entry in documents_feed.entry:
#  print document_entry.title.text

client = GDataService()
client.email = 'j.dennis.griffith@gmail.com'
client.password = password
client.service = 'finance'

client.ProgrammaticLogin()

baseURL = "http://finance.google.com/finance/feeds/%(email)s/" % {'email':client.email}

positionsFeed = client.GetFeed(baseURL + "portfolios/1/positions?returns=true")

for entry in positionsFeed.entry:
 details = entry.FindExtensions('symbol')[0] 
 symbol = details.attributes['symbol']
 name = details.attributes['fullName']
 print "SYMBOL:", symbol, " NAME:", name

 data = entry.FindExtensions('positionData')[0]
 #totalReturn = round(float(data.attributes['returnOverall']) * 100,2)
 #gainPerc = round(float(data.attributes['gainPercentage']) * 100,2)
 totalReturn = float(data.attributes['returnOverall'])
 gainPerc = float(data.attributes['gainPercentage'])
 
 print name + " (" + symbol + ") Return: " + str(totalReturn) + "% - Gain: " + str(gainPerc) + "%" 




