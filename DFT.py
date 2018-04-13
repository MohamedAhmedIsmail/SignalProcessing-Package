import math
import cmath
from EnumsClasses import DFTOrIDFT
class DiscreteFourierTransform:
    def __init__(self):
        pass
    def DFT(self,Signal,DftOrIdft=None):
        N = len(Signal)
        ComplexList=[]
        for k in range(N):
            s = complex(0)
            for n in range(N):
                if DftOrIdft== DFTOrIDFT.DFT:
                    angle = (2j* cmath.pi * n * k )/ N
                    s += Signal[n] * cmath.exp(-angle)
                elif DftOrIdft == DFTOrIDFT.IDFT:
                    angle=(2j* cmath.pi * n * k )/ N
                    s += Signal[n] * (cmath.exp(angle)/N)
            ComplexList.append(s)
        return ComplexList
    
    def IDFT(self,Real,Imaginary):
        N, x = len(Real), []
        for n in range(N):
            real= 0
            for k in range(N):    
                theta = k * (2 * math.pi) * (float(n) / N)
                real += (Real[k] * math.cos(theta)) - (Imaginary[k] * math.sin(theta))
            x.append(real)
        return x