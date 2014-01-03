#!/usr/bin/python

import sys
import gdata.docs.service

if len (sys.argv) > 1:
  password = sys.argv[1]
else:
  print "password required (in single quotes)"
  sys.exit(1)

client=gdata.docs.service.DocsService()
client.ClientLogin('j.dennis.griffith',password)
documents_feed=client.GetDocumentListFeed()
for document_entry in documents_feed.entry:
  print document_entry.title.text

