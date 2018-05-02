class HelperFunctions:
    def shift(self,mylst=None,indx=None):
        return mylst[indx:]+mylst[:indx]    
    def NormalizationAuto(self,MySignal=None):
        Res=0.0
        Res1=0.0
        Res2=0.0
        mySignal2=[]
        for i in range(len(MySignal[0])):
            mySignal2.append(float(MySignal[0][i][1]))
        for i in range(len(mySignal2)):
            Res1+=mySignal2[i]**2
            Res2+=mySignal2[i]**2
        Res=(Res1*Res2)**0.5
        Res=Res/len(mySignal2)
        return Res
    
    def NormalizationCross(self,FirstSignal=None,SecondSignal=None):
        Res1=0.0
        Res2=0.0
        Res=0.0
        for i in range(len(FirstSignal)):
            Res1+=FirstSignal[i]**2
            Res2+=SecondSignal[i]**2
        Res=(Res1*Res2)**0.5
        Res=Res/len(FirstSignal)
        return Res
        
    def makeTwoSignalsEqualInLength(self,myFirstSignal=None,mySecondSignal=None):
        N=len(myFirstSignal)+len(mySecondSignal)-1
        for i in range(N-len(myFirstSignal)):
            myFirstSignal.append(0)
        for i in range(N-len(mySecondSignal)):
            mySecondSignal.append(0)
        return myFirstSignal,mySecondSignal