#!/usr/bin/python

import sys
import getopt
import signal
import string
import gdata.projecthosting.client
import gdata.projecthosting.data
import gdata.gauth
import gdata.client
import gdata.data
import atom.http_core
import atom.core

flag = False

def main():
    global flag

    signal.signal(signal.SIGINT, onSignal) # Keyboard

    try:
        opts,args = getopt.getopt(sys.argv[1:], \
            "hf", ["help","flag"])
    except getopt.GetoptError, err:
        print str(err)
        usage()

    for o,a in opts:
        if o in ("-h","--help"):
            usage()
        elif o in ("-f","--flag"):
            flag = True
        else:
            assert False, "unhandled option"

    issues_client = gdata.projecthosting.client.ProjectHostingClient()
    #print dir(issues_client)
    query = gdata.projecthosting.client.Query(max_results = 1000)
    feed = issues_client.get_issues("chopshop-166",query=query)
    #print feed

    issueNum = 1
    for issues in feed.entry:
        if not flag:
            if "closed" in issues.state.text:
              continue
        id_text = issues.id.text.split("/")
        id_number = id_text[len(id_text)-1]

        print "\nVVVVVVVVVV Issue Number:%d  ID:%s VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV" %(issueNum,id_number)
        print "TITLE:%s" %(issues.title.text)

        if "New" in issues.status.text:
            print "########################################"
            print "#               NEW ISSUE              #"
            print "#                                      #"
            print "########################################"
        if issues.owner == None:
          username = "NOT ASSIGNED"
        else:
          username = issues.owner.username.text
        print "STATE:%s STATUS:%s USERNAME:%s" %(issues.state.text,issues.status.text,username)
        for i in range(len(issues.label)):
          if "Priority" not in issues.label[i].text:
            continue
          if "Critical" in issues.label[i].text:
            print "########################################"
            print "#            CRITICAL ISSUE            #"
            print "#                                      #"
            print "########################################"
          print "LABEL:",issues.label[i].text

        print "CONTENT:",issues.content.text
        print "--------------------------------------------------"

        comments_feed = issues_client.get_comments("chopshop-166",id_number)
        count=1
        for comment in comments_feed.entry:
          if comment.content.text:
            print count,")",comment.content.text.encode('utf-8')
            count += 1

        print "^^^^^^^^^^ Issue Number:%d  ID:%s ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^" %(issueNum,id_number)

        issueNum += 1

def usage():
    print \
      """"
      Usage (%s):
        arguments:
          [-h,--help] (displays this Help information)
          [-f,--flag] FLAG ON
        This routine will process Google Issues.
        Ex:
          %s
       """ \
           %(sys.argv[0],sys.argv[0])
    sys.exit(-1)

def onSignal(signum, stackframe):
    if signum == signal.SIGINT and stackframe:
        print "<CTRL-C> by operator, EXITING..."
    sys.exit(-1)

if __name__ == "__main__":
    main()

