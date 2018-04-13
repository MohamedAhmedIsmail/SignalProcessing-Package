from FFT import FastFourierTransform
class ConvolutionSignal:
    def __init__(self):
        pass
    def DirectConvolutionSignal(self,FirstSignal=None,SecondSignal=None):
        N1=len(FirstSignal)
        N2=len(SecondSignal)
        convlutedSignal=[]
        for n in range(N1+N2 - 1):
            summation=0
            idx=0
            for k in range(N1):
                idx=n-k
                if idx<0:
                    break
                elif idx >= N2:
                    continue
                else:
                    summation+=FirstSignal[k]*SecondSignal[idx]
            convlutedSignal.append(summation)
        return convlutedSignal
    
    def FastConvolutionSignal(self,FirstSignal=None,SecondSignal=None):
        myObj=FastFourierTransform()
        newsize=len(FirstSignal)+len(SecondSignal)-1
        handlesize=1<<(newsize - 1).bit_length()
        for i in range(handlesize-len(FirstSignal)):
            FirstSignal.append(0)
        for i in range(handlesize-len(SecondSignal)):
            SecondSignal.append(0)
        fftX=myObj.fft(FirstSignal)
        fftY=myObj.fft(SecondSignal)
        mylst=[]
        for i in range(handlesize):
            mylst.append(fftX[i]*fftY[i])
        res=myObj.ifft(mylst).real[:newsize]
        FastConv=[]
        for i in range(len(res)):
            FastConv.append(round(res[i],1))
        return FastConv