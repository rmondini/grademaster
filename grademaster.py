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

def tot_exec_time_str(time_start):
    time_end = time.time()
    exec_time = time_end-time_start
    tmp_str = "Total execution time: %0.3fs (%dh %dm %0.3fs)" %(exec_time, exec_time/3600, (exec_time%3600)/60,(exec_time%3600)%60)
    return tmp_str

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
    
    #plt.title('Class statistics')
    #plt.xlabel('Score')
    #plt.ylabel('# of students')
    #plt.xticks(range(0,110,10))
    #plt.hist(scorelist, bins=range(0,110,10))
    
    fig = plt.figure()
    ax1 = fig.add_subplot(111)
    ax1.set_title('Class average: %.1f' % compute_avg(recordlist,strkey))
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
    # A (top 10%), A- (next 10%)
    # B+ (next 10%), B (next 10%), B- (next 10%)
    # C+ (next 10%), C (next 10%), C- (next 10%)
    # D (next 10%), F (bottom 10%)
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
    # file with functions
    # grades at different stages of the semester
    # implement different sections
    
    tmp_str = tot_exec_time_str(time_start)
    print tmp_str
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    
if __name__ == "__main__" :
    main()    