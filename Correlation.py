from EnumsClasses import NormalizedOrNonNormalized
from CorrelationHandelFunctions import HandleCorrelationSignal
from CorrelationHelperFunctions import HelperFunctions     
class CorrelationSignal:
    
    def DirectAutoCorrelation(self,mySignal=None,NormalizedOrNon=None):
        myObj=HelperFunctions()
        myObj2=HandleCorrelationSignal()
        mynewSignal=myObj2.HandleDirectAutoCorrelation(mySignal)
        if NormalizedOrNon==NormalizedOrNonNormalized.NonNormalized:
            return mynewSignal
        elif NormalizedOrNon==NormalizedOrNonNormalized.Normalized:
             Normalized=myObj.NormalizationAuto(mySignal)
             newSignal=[]
             for i in range(len(mynewSignal)):
                 newSignal.append(mynewSignal[i]/Normalized)
             return newSignal
    
    def FastAutoCorrelation(self,mySignal=None,NormalizedOrNon=None):
        myObj=HelperFunctions()
        myObj2=HandleCorrelationSignal()
        mynewSignal=myObj2.HandleDirectFastAutoCorrelation(mySignal)
        if NormalizedOrNon==NormalizedOrNonNormalized.NonNormalized:
            return mynewSignal
        elif NormalizedOrNon==NormalizedOrNonNormalized.Normalized:
            Normalized=myObj.NormalizationAuto(mySignal)
            newSignal=[]
            for i in range(len(mynewSignal)):
                newSignal.append(mynewSignal[i]/Normalized)
            return newSignal
            
    def DirectCrossCorrelation(self,FirstSignal=None,SecondSignal=None,NormalizeOrNon=None):
        myObj=HelperFunctions()
        myObj2=HandleCorrelationSignal()
        FirstSignal=[int(x[1]) for x in FirstSignal]
        SecondSignal=[int(x[1]) for x in SecondSignal]
        myNewSignal1,myNewSignal2=myObj.makeTwoSignalsEqualInLength(FirstSignal,SecondSignal)
        myNewSignal=myObj2.HandleDirectCrossCorrelation(myNewSignal1,myNewSignal2)
        if NormalizeOrNon==NormalizedOrNonNormalized.NonNormalized:
            return myNewSignal
        elif NormalizeOrNon==NormalizedOrNonNormalized.Normalized:
            Normalized=myObj.NormalizationCross(myNewSignal1,myNewSignal2)
            newSignal=[]
            for i in range(len(myNewSignal)):
                newSignal.append(myNewSignal[i]/Normalized)
            return newSignal
    
    def FastCrossCorrelation(self,FirstSignal=None,SecondSignal=None,NormalizeOrNon=None):
        myObj=HelperFunctions()
        myObj2=HandleCorrelationSignal()
        FirstSignal=[int(x[1]) for x in FirstSignal]
        SecondSignal=[int(x[1]) for x in SecondSignal]
        fastCorr=myObj2.HandleFastCrossCorrelation(FirstSignal,SecondSignal)
        if NormalizeOrNon==NormalizedOrNonNormalized.NonNormalized:
            return fastCorr
        elif NormalizeOrNon==NormalizedOrNonNormalized.Normalized:
            Normalized=myObj.NormalizationCross(FirstSignal,SecondSignal)
            newSignal=[]
            for i in range(len(FirstSignal)):
                newSignal.append((fastCorr[i]/Normalized))
            return newSignal