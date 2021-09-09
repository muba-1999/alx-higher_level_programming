#!/usr/bin/python3
if __name__ == "__main__":
	from sys import argv
	args = argv[1:]
	arg_count = len(args)
	index = 1
	result = 0
	while index <= arg_count:
		result += int(argv[index])
		index += 1
	print("{:d}".format(result))
