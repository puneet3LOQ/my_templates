#!/usr/bin/python

import sys, getopt

def print_usage():
    print "Usage: -a[--a_arg] <input for a> -b[--b_arg] <input for b> -c <input for c>"

def main(argv):
    try:
        # a,b,c short args (-a, -b, etc)
        # Long args ('a_args' etc) are optional
        opts, args = getopt.getopt(argv, "ha:b:c", ['a_arg=', 'b_arg='])
    except getopt.GetoptError:
        print_usage()
        sys.exit(2)
    
    for opt, arg in opts:
        if opt == '-h':
            print_usage()
        elif opt == '-a':
            print 'Argument with -a: ', arg
        elif opt == '-b':
            print 'Argument with -b:', arg
        elif opt == '-c':
            print 'Argument with -c', arg
        else:
            print_usage()
            
if __name__ == '__main__':
    main(sys.argv[1:])