#!/usr/bin/env python

import sys
import pexpect

if len(sys.argv) <= 1:
    print "NEED PASSWORD"
    sys.exit()

print "+++++++++++++++++++++++++++ ls -al"
outPut = pexpect.run('ls -al')
print outPut
print "+++++++++++++++++++++++++++ ping"
outPut = pexpect.run('ping -c 1 localhost')
print outPut
outPut = pexpect.run('ping -c 1 localhostxxxx')
print outPut
print "+++++++++++++++++++++++++++ ssh"
child = pexpect.spawn('ssh jdg@localhost')
print "Expecting prompt for password"
child.expect ('[Pp]assword:')
child.sendline(sys.argv[1])
print "Expecting prompt"
child.expect ('>')
child.sendline('ls -al')
child.expect ('>')
print child.before

print "+++++++++++++++++++++++++++ xxxx"

if __name__ == '__main__':
    print "TEST-TEST"
    pass
