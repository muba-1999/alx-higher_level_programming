#!/usr/bin/python3
from sys import argv
arg = argv[1:]
args = len(arg)
index = 1
if args == 0:
	print("{:d} arguments.".format(args))
elif args is 1:
	print("{:d} aregument:".format(args))
	print("{:d}: {:s}".format(index, argv[1]))
else:
	print("{:d} arguments:".format(args))
	while index <= args:
		print("{:d}: {:s}".format(index, argv[index]))
		index += 1

	
