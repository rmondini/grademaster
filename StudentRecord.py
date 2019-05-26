import sys

class StudentRecord:
    lastname_ = ''
    firstname_ = ''
    studentid_ = ''
    hwscores_ = []
    mtscores_ = []
    finalscore_ = 0.0
    totalgrade_ = 0.0
    lettergrade_ = ''
    outofn_ = 0
    finaldone_ = False
    pchw_ = 0.0
    pcmaxmt_ = 0.0
    pcminmt_ = 0.0
    pcfinal_ = 0.0
    
    # initialize class to zero and fill in all fields
    def __init__(self,datalist,keyslist,auxlist) :
        self.lastname_ = ''
        self.firstname_ = ''
        self.studentid_ = ''
        self.hwscores_ = []
        self.mtscores_ = []
        self.finalscore_ = 0.0
        self.totalgrade_ = 0.0
        self.lettergrade_ = ''
        self.outofn_ = 0
        self.finaldone_ = False
        self.pchw_ = 0.0
        self.pcmaxmt_ = 0.0
        self.pcminmt_ = 0.0
        self.pcfinal_ = 0.0
        
        self.input(datalist,keyslist,auxlist)
        self.computetotalgrade()
        
    # print content    
    def __str__(self):
        ln = "Last name: " + str(self.lastname_) + '\n'
        fn = "First name: " + str(self.firstname_) + '\n'
        stid = "Student ID: " + str(self.studentid_) + '\n'
        hwlist = "HW scores: " + str(self.hwscores_) + '\n'
        mtlist = "MT scores: " + str(self.mtscores_) + '\n'
        fs = "Final exam: " + str(self.finalscore_) + '\n'
        tg = "Total grade: " + str(self.totalgrade_) + '/' + str(self.outofn_) + '\n'
        lg = "Letter grade: " + str(self.lettergrade_) + '\n'
        return ln + fn + stid + hwlist + mtlist + fs + tg + lg
       
    # print content in csv format
    def printout(self):
        ln = str(self.lastname_) + ','
        fn = str(self.firstname_) + ','
        stid = str(self.studentid_) + ','
        if self.hwscores_ == []:
            hwlist = ''
        else:    
            hwlist = str(self.hwscores_).strip('[]') + ','
        if self.mtscores_ == []:
            mtlist = ''
        else:        
            mtlist = str(self.mtscores_).strip('[]') + ','
        if self.finaldone_:            
            fs = str(self.finalscore_) + ','
        else:
            fs = ''    
        if self.outofn_ == 0:
            tg=lg=''
        else:    
            tg = str(self.totalgrade_) + ','
            lg = str(self.lettergrade_)
        return ln + fn + stid + hwlist + mtlist + fs + tg + lg + '\n'
      
    # fill in all fields    
    def input(self, datalist, keyslist, auxlist):
        nkeys=len(keyslist)
        if len(datalist)!=nkeys:
            print datalist
            sys.exit("Data/keys mismatch for this student! Stop.")
                   
        for i in range(nkeys):
            key = keyslist[i]
            data = datalist[i]
            if key == "Last name":
                self.lastname_ = data 
            elif key == "First name":
                self.firstname_ = data 
            elif key == "Student ID":
                self.studentid_ = data
            elif 'HW' in key:
                self.hwscores_.append(float(data))
            elif (key == 'M1') or (key == 'M2'):
                self.mtscores_.append(float(data))
            elif key == 'Final':
                self.finalscore_ = float(data)
            else:
                sys.exit("Unknown key! Stop.")
                
        self.outofn_ = auxlist[0]
        self.finaldone_ = auxlist[1]
        self.pchw_ = auxlist[2]/100.0
        self.pcmaxmt_ = auxlist[3]/100.0
        self.pcminmt_ = auxlist[4]/100.0
        self.pcfinal_ = auxlist[5]/100.0
             
    # compute total grade            
    def computetotalgrade(self):
        if self.hwscores_ == []:
            hwavg=0.0
        else:    
            hwavg = sum(self.hwscores_)/len(self.hwscores_)
        if self.mtscores_ == []:
            maxmt=minmt=0.0
        elif len(self.mtscores_)==1:
            maxmt=self.mtscores_[0]
            minmt=0.0    
        else:              
            maxmt = max(self.mtscores_)
            minmt = min(self.mtscores_)   
        final = self.finalscore_
    
        self.totalgrade_ = self.pchw_*hwavg+self.pcmaxmt_*maxmt+self.pcminmt_*minmt+self.pcfinal_*final
        
    def assignlettergrade(self,lg):
        self.lettergrade_ = lg
           
    def gettotalgrade(self):
        return self.totalgrade_

    def getfinalscore(self):
        return self.finalscore_

    def getmt1score(self):
        if self.mtscores_ == []:
            sys.exit("No MT1 yet! Stop.")
        return self.mtscores_[0]
    
    def getmt2score(self):
        if len(self.mtscores_) < 2:
            sys.exit("No MT2 yet! Stop.")
        return self.mtscores_[1]
            
    def getname(self):
        return str(self.lastname_) + ' ' + str(self.firstname_)
    
    def getstudentid(self):
        return self.studentid_ 
     
        