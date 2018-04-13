from FFT import FastFourierTransform
from CorrelationHelperFunctions import HelperFunctions
class HandleCorrelationSignal:
    def HandleDirectAutoCorrelation(self,mySignal=None):
        mylst=[]
        myObj=HelperFunctions()
        for i in range(len(mySignal)):
            
            newSignal=myObj.shift(mySignal,i)
            Res=0
            for j in range(len(mySignal)):
                Res+=mySignal[j]*newSignal[j]
            mylst.append(Res/len(mySignal))
        return mylst
    def HandleDirectFastAutoCorrelation(self,mySignal=None):
        myObj=FastFourierTransform()
        FFTSignal=myObj.fft(mySignal)
        ConjugateSignal=FFTSignal.conjugate()
        multiplyingSignal=FFTSignal*ConjugateSignal
        myResultSignal=myObj.ifft(multiplyingSignal)/len(mySignal)
        return myResultSignal
    def HandleDirectCrossCorrelation(self,myFirstSignal=None,mySecondSignal=None):
        myObj=HelperFunctions()
        mylst=[]
        for i in range(len(myFirstSignal)):
            newSignal=myObj.shift(mySecondSignal,i)
            Res=0
            for j in range(len(myFirstSignal)):
                Res+=myFirstSignal[j]*newSignal[j]
            mylst.append(Res/len(myFirstSignal))
        return mylst
    def HandleFastCrossCorrelation(self,FirstSignal=None,SecondSignal=None):
        mylst=[]
        myObj=FastFourierTransform()
        fftX=myObj.fft(FirstSignal)
        ConjugatefftX=fftX.conjugate()
        fftY=myObj.fft(SecondSignal)
        mylst=[]
        for i in range(len(FirstSignal)):
            mylst.append(ConjugatefftX[i]*fftY[i])
        res=myObj.ifft(mylst).real[:len(FirstSignal)]
        FastCorr=[]
        for i in range(len(res)):
            FastCorr.append(round(res[i],1)/len(res))
        return FastCorr