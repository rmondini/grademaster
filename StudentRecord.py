class StudentRecord:
    lastname_ = ''
    firstname_ = ''
    studentid_ = ''
    hwscores_ = []
    mtscores_ = []
    finalscore_ = 0.0
    totalgrade_ = 0.0
    lettergrade_ = ''
    
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
        tg = "Total grade: " + str(self.totalgrade_) + '\n'
        lg = "Letter grade: " + str(self.lettergrade_) + '\n'
        return ln + fn + stid + hwlist + mtlist + fs + tg + lg
       
    # fill in all fields    
    def input(self, datalist, keyslist):
        nkeys=len(keyslist)
                
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
          
    # compute total grade            
    def computetotalgrade(self):
        hwavg = sum(self.hwscores_)/len(self.hwscores_)
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
        return self.mtscores_[0]
    
    def getmt2score(self):
        return self.mtscores_[1]
            
    def getname(self):
        return str(self.lastname_) + ' ' + str(self.firstname_)
    
    def getstudentid(self):
        return self.studentid_  
        