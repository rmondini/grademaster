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
    
    # initialize class to zero and fill in all fields
    def __init__(self,datalist,keyslist) :
        self.lastname_ = ''
        self.firstname_ = ''
        self.studentid_ = ''
        self.hwscores_ = []
        self.mtscores_ = []
        self.finalscore_ = 0.0
        self.totalgrade_ = 0.0
        self.lettergrade_ = ''
        self.outofn_ = 0
        
        self.input(datalist,keyslist)
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
        hwlist = str(self.hwscores_).strip('[]') + ','
        mtlist = str(self.mtscores_).strip('[]') + ','        
        fs = str(self.finalscore_) + ','
        tg = str(self.totalgrade_) + ','
        lg = str(self.lettergrade_) + '\n'
        return ln + fn + stid + hwlist + mtlist + fs + tg + lg
      
    # fill in all fields    
    def input(self, datalist, keyslist):
        nkeys=len(keyslist)
        if len(datalist)!=nkeys:
            sys.exit("Missing data entry for a student! Stop.")
                   
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
                self.outofn_ += 35
            else:
                sys.exit("Unknown key! Stop.")
         
        if 'HW1' in keyslist:
            self.outofn_ += 20
        if 'MT1' in keyslist:
            self.outofn_ += 25
        if 'MT2' in keyslist:
            self.outofn_ += 20                 
             
    # compute total grade            
    def computetotalgrade(self):
        if self.hwscores_ == []:
            hwavg=0.0
        else:    
            hwavg = sum(self.hwscores_)/len(self.hwscores_)
        if self.mtscores_ == []:
            maxmt,minmt=0.0,0.0
        elif len(self.mtscores_)==1:
            maxmt=self.mtscores_[0]
            minmt=0.0    
        else:              
            maxmt = max(self.mtscores_)
            minmt = min(self.mtscores_)   
        final = self.finalscore_
    
        # 20% HW, 25% max MT, 20% min MT, 35% final
        self.totalgrade_ = 0.20*hwavg+0.25*maxmt+0.20*minmt+0.35*final
        
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
    
    def getoutofn(self):
        return self.outofn_ 
     
        