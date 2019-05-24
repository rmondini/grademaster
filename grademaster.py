#!/usr/bin/env python

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~ Banner

FILE_NAME = "Grademaster"
REVISION_DATE = "2019-05-24"
AUTHOR = "(rmondini@buffalo.edu)"

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~ Weight of each component (%)

# 20% HW, 25% higher MT, 20% lower MT, 35% final
PC_HW = 20
PC_MAXMT = 25
PC_MINMT = 20
PC_FINAL = 35

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

import sys
import time
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
from StudentRecord import StudentRecord
from operator import itemgetter
from lib_grademaster import *

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

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

    # determine how far into the semester we are
    cumuloutof=0
    finaldone = False
    if 'HW1' in keyslist:
        cumuloutof += PC_HW
    if 'M1' in keyslist:
        cumuloutof += PC_MAXMT
    if 'M2' in keyslist:
        cumuloutof += PC_MINMT
    if 'Final' in keyslist:
        cumuloutof += PC_FINAL
        finaldone = True    
            
    # print keys
    print "keys = ",keyslist,"\n"
    
    # create auxiliary list
    auxlist = [cumuloutof,finaldone,PC_HW,PC_MAXMT,PC_MINMT,PC_FINAL]
    
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
        sr = StudentRecord(datalist,keyslist,auxlist)
        recordlist.append(sr)
    
    # print recordlist
#    for sr in recordlist:
#        print sr
            
    # compute class average for 'MT1', 'MT2', 'Final', or 'Total'
    strkey = 'Total'
    strkeyoutofn = 100
    if strkey == 'Total':
        strkeyoutofn = cumuloutof  
    print "Class average for " + strkey + ": %.1f" % compute_avg(recordlist,strkey) + '/' + str(strkeyoutofn) + '\n'

    # create histogram for 'MT1', 'MT2', 'Final', or 'Total'
    strkey = 'Total'
    create_histo(recordlist,strkey,cumuloutof)
        
    # rank students and assign letter grades
    # print out letter/numerical grade conversion
    lglist = rank_students(recordlist,cumuloutof)
    for i in range(len(lglist[0])):
        print "Total >= %.1f" % lglist[0][i] + " -> " + lglist[1][i]
    print '\n'
    
    # print recordlist
#    for sr in recordlist:
#        print sr

    # look up a student record by student id
    # print their record if student is found
    lookupid = 59118211
    studrecpos=get_studrecpos_byid(recordlist,lookupid)
    print "Student ",lookupid, " is at position: ",studrecpos,'\n'
    if isinstance(studrecpos,(int,long)):
        print recordlist[studrecpos]
    
    # write out updated file in csv format
    outfile = open("output.csv", "w+")
    if cumuloutof==0:
        outkeyslist = ', '.join(keyslist) + '\n'
    else:    
        outkeyslist = ', '.join(keyslist) + ',Total,Letter\n'
    outfile.write(outkeyslist)
    for sr in recordlist:
        outfile.write(sr.printout())
    outfile.close()
     
 
     
     

     

     
     
     
            
    #TODO:
    # implement different instructors&sections
    # readme files with features of this code






  
    # measure execution time
    tmp_str = tot_exec_time_str(time_start)
    print tmp_str
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    return

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

if __name__ == "__main__" :
    main()
      