import math
import numpy as np
from FFT import FastFourierTransform
class DftFft:
    def __init__(self):
        pass
    def omega(self,SamplingFrequency,LengthOfMySignal):
        return (2*math.pi)/(LengthOfMySignal*(1/SamplingFrequency))
    
    def squareRoot(self,ComplexSignal):
        reals=[]
        imagines=[]
        squareRootList=[]
        complexRes=ComplexSignal    
        for i in range(len(complexRes)):
            reals.append(round(complexRes[i].real,2))
            imagines.append(round(complexRes[i].imag,2))
            squareRootList.append(round(math.sqrt(reals[i]**2+imagines[i]**2),3))
        return squareRootList,reals,imagines
    
    def convertPolarFormToComplexForm(self,myTuple):
        myNewTuple=[]
        for a in myTuple:
            for i in range(len(a)):
                myNewTuple.append((float(a[i][0]),float(a[i][1])))
        myComplexList=[]
        for i in range(len(myNewTuple)):
             x=myNewTuple[i][0]*np.cos(myNewTuple[i][1])
             y=myNewTuple[i][0]*np.sin(myNewTuple[i][1])
             res=x+y*1j
             myComplexList.append(res)
        print(myComplexList)
        return myComplexList
    
    def ReturnNumbersOfSignal(self,Signal=None):
        N = len(Signal)
        newList=[]
        for i in range(N):
            for j in range(1,2,2):
                newList.append(int(Signal[i][j]))
        return newList
    
    def AccumulatedSignal(self,Signal):
        print(Signal)
        mylst=[]
        for i in range(len(Signal)):
            mylst.append(int(Signal[i][1]))
        Accum=np.cumsum(mylst)
        return Accum
            
    def ZeroCrossing(self,Signal):
        ySignal=[]
        mylst=[]
        for i in range(len(Signal)):
            mylst.append(int(Signal[i][1]))
        for i in range(len(Signal)):
            if i==0:     
                ySignal.append(mylst[i+1]-2*mylst[i])
            else:
                if i == len(Signal)-1:    
                    ySignal.append(-2*mylst[i]+mylst[i-1])
                else:
                    ySignal.append(mylst[i+1]-2*mylst[i]+mylst[i-1])
        return ySignal
    
    def RemoveDcComponents(self,Signal=None):
        myList=[]
        for i in range(len(Signal)):
            myList.append(float(Signal[i][1]))
        myObj=FastFourierTransform()
        mySignal=myObj.fft(myList)
        mySignal[0]=0.0
        newSignal=myObj.ifft(mySignal)
        return newSignal