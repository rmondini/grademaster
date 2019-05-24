#!/usr/bin/env python

FILE_NAME = "Grademaster"
REVISION_DATE = "2019-05-23"
AUTHOR = "(rmondini@buffalo.edu)"

import sys
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
from StudentRecord import StudentRecord
from operator import itemgetter

def get_studrecpos_byid(recordlist,lookupid):
    
    pos = "No match for this student ID!"
    for i in range(len(recordlist)):
        if recordlist[i].getstudentid() == str(lookupid):
            pos = i
            break
        
    return pos

def compute_avg(recordlist,strkey):

    if strkey == 'MT1':
        scorelist = [i.getmt1score() for i in recordlist]
    elif strkey == 'MT2':   
        scorelist = [i.getmt2score() for i in recordlist]        
    elif strkey == 'Final':
        scorelist = [i.getfinalscore() for i in recordlist]               
    elif strkey == 'Total':
        scorelist = [i.gettotalgrade() for i in recordlist]  
    else:
        sys.exit("Unknown key! Stop.")
                      
    avgscore = sum(scorelist)/len(scorelist)
    return avgscore

def create_histo(recordlist,strkey):
    
    if strkey == 'MT1':
        scorelist = [i.getmt1score() for i in recordlist]
    elif strkey == 'MT2':   
        scorelist = [i.getmt2score() for i in recordlist]        
    elif strkey == 'Final':
        scorelist = [i.getfinalscore() for i in recordlist]               
    elif strkey == 'Total':
        scorelist = [i.gettotalgrade() for i in recordlist]  
    else:
        sys.exit("Unknown key! Stop.")
    
#     plt.title('Class statistics')
#     plt.xlabel('Score')
#     plt.ylabel('# of students')
#     plt.xticks(range(0,110,10))
#     plt.hist(scorelist, bins=range(0,110,10))
    
    fig = plt.figure()
    ax1 = fig.add_subplot(111)
    ax1.set_title('Class statistics')
    ax1.set_xlabel('Score')
    ax1.set_ylabel('# of students')
    ax1.set_xticks(range(0,110,10))
    ax1.yaxis.set_major_locator(mtick.MaxNLocator(integer=True))
    ax1.hist(scorelist, bins=range(0,110,10))
    
    plt.show()
    
def rank_students(recordlist):

    nreclist = len(recordlist)
    
    # create list with only student id and total grade
    idtotgradelist = [[i.getstudentid(),i.gettotalgrade()] for i in recordlist]
    
    # sort students from higher total grade to lowest
    sorted_idtotgradelist = sorted(idtotgradelist,key=itemgetter(1),reverse=True)
    
    # determine 10%
    tenpc=nreclist/10
    
    # assign letter grades:
    # A (10%), A- (10%)
    # B+ (10%), B (10%), B- (10%)
    # C+ (10%), C (10%), C- (10%)
    # D (10%), F (10%)
    for ipos in range(nreclist):
        if 0 <= ipos <= (tenpc-1):
            sorted_idtotgradelist[ipos].append('A')
            studrecpos=get_studrecpos_byid(recordlist,sorted_idtotgradelist[ipos][0])   
            recordlist[studrecpos].assignlettergrade('A')            
        elif tenpc <= ipos <= (2*tenpc-1):
            sorted_idtotgradelist[ipos].append('A-')
            studrecpos=get_studrecpos_byid(recordlist,sorted_idtotgradelist[ipos][0])   
            recordlist[studrecpos].assignlettergrade('A-')                  
        elif 2*tenpc <= ipos <= (3*tenpc-1):
            sorted_idtotgradelist[ipos].append('B+')
            studrecpos=get_studrecpos_byid(recordlist,sorted_idtotgradelist[ipos][0])   
            recordlist[studrecpos].assignlettergrade('B+')             
        elif 3*tenpc <= ipos <= (4*tenpc-1):
            sorted_idtotgradelist[ipos].append('B')
            studrecpos=get_studrecpos_byid(recordlist,sorted_idtotgradelist[ipos][0])   
            recordlist[studrecpos].assignlettergrade('B')                         
        elif 4*tenpc <= ipos <= (5*tenpc-1):
            sorted_idtotgradelist[ipos].append('B-')
            studrecpos=get_studrecpos_byid(recordlist,sorted_idtotgradelist[ipos][0])   
            recordlist[studrecpos].assignlettergrade('B-')                 
        elif 5*tenpc <= ipos <= (6*tenpc-1):
            sorted_idtotgradelist[ipos].append('C+')
            studrecpos=get_studrecpos_byid(recordlist,sorted_idtotgradelist[ipos][0])   
            recordlist[studrecpos].assignlettergrade('C+')             
        elif 6*tenpc <= ipos <= (7*tenpc-1):
            sorted_idtotgradelist[ipos].append('C')
            studrecpos=get_studrecpos_byid(recordlist,sorted_idtotgradelist[ipos][0])   
            recordlist[studrecpos].assignlettergrade('C')                     
        elif 7*tenpc <= ipos <= (8*tenpc-1):
            sorted_idtotgradelist[ipos].append('C-')
            studrecpos=get_studrecpos_byid(recordlist,sorted_idtotgradelist[ipos][0])   
            recordlist[studrecpos].assignlettergrade('C-')                     
        elif 8*tenpc <= ipos <= (9*tenpc-1):
            sorted_idtotgradelist[ipos].append('D')
            studrecpos=get_studrecpos_byid(recordlist,sorted_idtotgradelist[ipos][0])   
            recordlist[studrecpos].assignlettergrade('D')                     
        else:
            sorted_idtotgradelist[ipos].append('F')
            studrecpos=get_studrecpos_byid(recordlist,sorted_idtotgradelist[ipos][0])   
            recordlist[studrecpos].assignlettergrade('F')   

    return

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
    strkey = 'MT1'
    print "Class average for " + strkey + ": ",compute_avg(recordlist,strkey)

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
    lookupid = 59118211
    studrecpos=get_studrecpos_byid(recordlist,lookupid)
    print "Student ",lookupid, " is at position: ",studrecpos
    if isinstance(studrecpos,(int,long)):
        print recordlist[studrecpos]
            
    #TODO:
    # file with functions
    # grades at different stages of the semester
    # implement different sections
    # print output file
    
    
    
    
    
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    
if __name__ == "__main__" :
    main()    