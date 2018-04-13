import numpy as np
class FastFourierTransform:
    def __init__(self):
        pass                
    def fft(self, s):
        s = np.array(s)
        N = s.shape[0]
        if N <= 1:
            return s
        even = self.fft(s[::2])
        odd = self.fft(s[1::2])
        t = np.exp(np.complex(-2j) * np.pi * np.arange(N // 2) / N)
        complexSignal=np.concatenate((even + t * odd,
                               even - t * odd))
        return complexSignal
    def ifft(self, complexSignal):
        s=np.array(complexSignal)
        Signal=self.fft(s.conjugate()).conjugate().real / s.shape[0]
        return Signal