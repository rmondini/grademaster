#!/usr/bin/env python

FILE_NAME = "Grademaster"
REVISION_DATE = "2019-05-24"
AUTHOR = "(rmondini@buffalo.edu)"

import sys
import time
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
from StudentRecord import StudentRecord
from operator import itemgetter
from lib_grademaster import *

def main() :
    
    time_start = time.time()
        
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

    # print keys
    print "keys = ",keyslist,"\n"
    
    # read in file
    # create list of StudentRecord
    # fill in all fields
    # compute total grades
    recordlist = []
        
    for line in datafile.readlines():
        datalist = []
        words = line.split(',')
        for word in words:
            if word != '' and word != '\r\n':
                datalist.append(word)
        sr = StudentRecord(datalist,keyslist)
        recordlist.append(sr)
    
    # print recordlist
#    for sr in recordlist:
#        print sr
            
    # compute class average on 'MT1', 'MT2', 'Final', or 'Total'
    strkey = 'Total'
    print "Class average for " + strkey + ": ",compute_avg(recordlist,strkey),'\n'

    # create histogram for 'MT1', 'MT2', 'Final', or 'Total'
    strkey = 'Total'
    create_histo(recordlist,strkey)
        
    # rank students and assign letter grades
    rank_students(recordlist)
    
    # print recordlist
#    for sr in recordlist:
#        print sr

    # look up a student record by student id
    # print their record if student is found
    lookupid = 64954807
    studrecpos=get_studrecpos_byid(recordlist,lookupid)
    print "Student ",lookupid, " is at position: ",studrecpos,'\n'
    if isinstance(studrecpos,(int,long)):
        print recordlist[studrecpos]
    
    # write out updated file in csv format
    outfile = open("output.csv", "w+")
    outkeyslist = ', '.join(keyslist) + ',Total,Letter\n'
    outfile.write(outkeyslist)
    for sr in recordlist:
        outfile.write(sr.printout())
    outfile.close()
     
 
     
     
     
     

     
     
     
            
    #TODO:
    # grades at different stages of the semester
    # implement different sections
    
    tmp_str = tot_exec_time_str(time_start)
    print tmp_str
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    
if __name__ == "__main__" :
    main()
      