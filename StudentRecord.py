class StudentRecord:
    lastname_ = ''
    firstname_ = ''
    studentid_ = ''
    hwscores_ = []
    mtscores_ = []
    finalscore_ = 0.0

    # initialize class to zero and fill in all fields
    def __init__(self,datalist,keyslist) :
        self.lastname_ = ''
        self.firstname_ = ''
        self.studentid_ = ''
        self.hwscores_ = []
        self.mtscores_ = []
        self.finalscore_ = 0.0
        self.input(datalist,keyslist)
        
    # print content    
    def __str__(self):
        ln = "Last name: " + str(self.lastname_) + '\n'
        fn = "First name: " + str(self.firstname_) + '\n'
        stid = "Student ID: " + str(self.studentid_) + '\n'
        hwlist = "HW scores: " + str(self.hwscores_) + '\n'
        mtlist = "MT scores: " + str(self.mtscores_) + '\n'
        fs = "Final exam: " + str(self.finalscore_) + '\n'
        return ln + fn + stid + hwlist + mtlist + fs
       
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
                
    def gethwscores(self):
        return self.hwscores_
        
    def getlastname(self):
        return self.lastname_   
        