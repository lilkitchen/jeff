#!/usr/bin/python
#
# jeff.py
#

import pexpect
import sys

if len(sys.argv) != 3:
	print("Usage: ./jeff.py emulator1 emulator2")

e1 = pexpect.spawn("./" + sys.argv[1] + " -s")
e2 = pexpect.spawn("./" + sys.argv[2] + " -s")

msg = input("> ")

while True:
	e1.sendline(msg.rstrip())
	e1.expect("\n")
	e1.expect("\n")
	rep = e1.before.decode("utf-8")
	print("\t" + rep)

	e2.sendline(rep.rstrip())
	e2.expect("\n")
	e2.expect("\n")
	msg = e2.before.decode("utf-8")
	print("> ", msg)

	try:
		c = input('')
	except EOFError:
		break

	if c == 'q':
		break

	if len(c):
		msg = c
