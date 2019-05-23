#!/usr/bin/env python

FILE_NAME = "Grademaster"
REVISION_DATE = "2019-05-23"
AUTHOR = "(rmondini@buffalo.edu)"

import sys
from StudentRecord import StudentRecord

def main() :
    
    print "~~~~~~~~~~ " + FILE_NAME + " ~~~~~~~~~~"
    print REVISION_DATE + " " + AUTHOR 
    print
    
    n = len(sys.argv)
    
    if n<2 : 
        sys.exit("No input file. Stop.")
    
    # open file
    datafile = open(sys.argv[n-1])
    
    # read top line of data file
    line = datafile.readline()
    words = line.split(',')

    # extract keys, get rid of empty entries
    keyslist = []
    for word in words:
        if word != '' and word != '\r\n':
            keyslist.append(word)

    #print keys
    print "keys = ",keyslist,"\n"
    
    recordlist = []
    
    # read file and create list of StudentRecord
    for line in datafile.readlines():
        datalist = []
        words = line.split(',')
        for word in words:
            if word != '' and word != '\r\n':
                datalist.append(word)
        sr = StudentRecord(datalist,keyslist)
        recordlist.append(sr)
    
    # print recordlist
    for sr in recordlist:
        print sr
    
    
    
    
    
    
    
    
    
    
    
    
    
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    
if __name__ == "__main__" :
    main()    