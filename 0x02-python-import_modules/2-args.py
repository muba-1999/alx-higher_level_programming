#!/usr/bin/python3
import sys
arg = sys.argv[1:]
args = len(arg)
index = 1
if args is 0:
	print("{:d} arguments.".format(args))
elif args is 1:
	print("{:d} aregument:".format(args))
	print("{:d}: {:s}".format(index, sys.argv[1]))
else:
	print("{:d} arguments:".format(args))
	while index <= args:
		print("{:d}: {:s}".format(index, sys.argv[index]))
		index += 1

	
