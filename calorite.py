class question(object):
    def __init__(self):
        self.q = ""
    def setQuestion(self,ques):
        self.q=ques
    def getQuestion(self):
        return self.q
    def __str__(self):
        return self.q   

def getIncWeightPerDay():
    return 0.015

def getIncWeight(yrs):
    return getIncWeightPerDay()*yrs*365

if __name__ == '__main__':
    print "Welcome to Calorite!"
    print
    print "This Program lets you know your projected weight"
    print "after a period of time based on your habits and current weight."
    print
    raw_input("Shall we begin? Press enter to continue.....")
    print
    cur_weight = float(raw_input("May i know your weight? Please enter your current weight(in kgs.): "))
    ##yrs: time in years to get from user
    yrs = float(raw_input("Cool! Now enter the time from now(in yrs) to check your weight: "))
    inc_weight = 0 ##setting incremented weight to zero
    inc_weight = getIncWeight(yrs) ## getting weight increment/decrement parameters from user and then calculating incremented/decremented weight 
    print
    print "Alright! After all analysis, "
    print "we found that your weight after %0.2f years will be %0.2f kgs." % (yrs, inc_weight+cur_weight)
