#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    if len(sys.argv) - 1 == 0:
        print("{} arguments.".format(len(sys.argv) - 1))
    elif len(sys.argv) - 1 == 1:
        print("{} argument:".format(len(sys.argv) - 1))
        print("{}: {}".format(len(sys.argv) - 1, sys.argv[len(sys.argv) - 1]))
    else:
        print("{} arguments:".format(len(sys.argv) - 1))
        for i in range(1, len(sys.argv)):
            print("{}: {}".format(i, sys.argv[i]))
