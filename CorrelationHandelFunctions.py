from FFT import FastFourierTransform
from CorrelationHelperFunctions import HelperFunctions
class HandleCorrelationSignal:
    def HandleDirectAutoCorrelation(self,mySignal=None):
        mylst=[]
        mySignal2=[]
        myObj=HelperFunctions()
        for i in range(len(mySignal[0])):
            mySignal2.append(float(mySignal[0][i][1]))
        for i in range(len(mySignal2)):
            newSignal=myObj.shift(mySignal2,i)
            Res=0
            for j in range(len(mySignal2)):
                Res+=mySignal2[j]*newSignal[j]
            mylst.append(Res/len(mySignal2))
        return mylst
    def HandleDirectFastAutoCorrelation(self,mySignal=None):
        myObj=FastFourierTransform()
        mySignal2=[]
        for i in range(len(mySignal[0])):
            mySignal2.append(float(mySignal[0][i][1]))
        FFTSignal=myObj.fft(mySignal2)
        ConjugateSignal=FFTSignal.conjugate()
        multiplyingSignal=FFTSignal*ConjugateSignal
        myResultSignal=myObj.ifft(multiplyingSignal)/len(mySignal2)
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