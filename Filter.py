import numpy as np
from EnumsClasses import LowOrHighPassFilter
from EnumsClasses import BandPassOrStop
import math
class Filters:
    def __init__(self):
        self.choose=np.zeros(4)
    def CalculateN(self,stopBandattenuation=None,samplingFreq=None,transitionWidth=None):
        N=0
        if stopBandattenuation<32:
            N=(0.9*samplingFreq)/transitionWidth
            self.choose[0]=1
        elif stopBandattenuation>=32 and stopBandattenuation<44:
            N=(3.1*samplingFreq)/transitionWidth
            self.choose[1]=1
        elif stopBandattenuation<48 and stopBandattenuation>=44:
            N=(3.1*samplingFreq)/transitionWidth
            self.choose[1]=1
        elif stopBandattenuation>=48 and stopBandattenuation<=53:
            N=(3.3*samplingFreq)/transitionWidth
            self.choose[2]=1
        elif stopBandattenuation<60 and stopBandattenuation>53:
            N=(3.3*samplingFreq)/transitionWidth
            self.choose[2]=1
        elif stopBandattenuation>=60:
            N=(5.5*samplingFreq)/transitionWidth
            self.choose[3]=1
        return int(N),self.choose
    def WindowFunctions(self,choose=None,N=None,i=None):
        if choose[0]==1:
            window_map=1
        elif choose[1]==1:
            window_map=0.5 + 0.5*math.cos((2*math.pi*i)/N)
        elif choose[2]==1:
            window_map=0.54 + 0.46*math.cos((2*math.pi*i)/N)
        elif choose[3]==1:
            
            window_map=0.42 + (0.5*math.cos((2*math.pi*i)/(N - 1))) + (0.08*math.cos((4*math.pi*i)/(N - 1)))
        return window_map
    
    def LowAndHighPassFilter(self,passBandEdge=None,transitionWidth=None,stopBandattenuation=None,samplingFreq=None,LowOrHighFilter=None):
        if LowOrHighFilter==LowOrHighPassFilter.Low:    
            fc_dash=(passBandEdge/samplingFreq)+(transitionWidth/(2*samplingFreq))
        else:
            fc_dash=(passBandEdge/samplingFreq)-(transitionWidth/(2*samplingFreq))
        hd_map={}
        window_map={}
        odd_N=0
        N,choose=self.CalculateN(stopBandattenuation,samplingFreq,transitionWidth)
        if N%2==0:
            odd_N=N+1
        for i in range(int(-N/2),int(N/2)+1):
            if i==0 and LowOrHighFilter==LowOrHighPassFilter.Low:
                hd_zero=2*fc_dash
                hd_map[i]=hd_zero
            else:
                hd_zero=1- (2 * fc_dash)
                hd_map[i]=hd_zero
            if i!=0 and LowOrHighFilter==LowOrHighPassFilter.Low:    
                hd_map[i]=(2*fc_dash*math.sin(i*2*math.pi*fc_dash))/(i*2*math.pi*fc_dash)
            elif i!=0 and LowOrHighFilter==LowOrHighPassFilter.High:
                hd_map[i]=(-2*fc_dash*math.sin(i*2*math.pi*fc_dash))/(i*2*math.pi*fc_dash)
            window_map[i]=self.WindowFunctions(choose,odd_N,i)
        coefficients_h={}
        coefficients_h={k:window_map[k]*hd_map[k] for k in window_map}
        return coefficients_h
        
    def BandPassAndBandStopFilter(self,passBandEdge1=None,passBandEdge2=None,transitionWidth=None,stopBandattenuation=None,samplingFreq=None,PassOrStop=None):
        if PassOrStop == BandPassOrStop.Pass:
            fc1_dash=(passBandEdge1/samplingFreq)-(transitionWidth/(2*samplingFreq))
            fc2_dash=(passBandEdge2/samplingFreq)+(transitionWidth/(2*samplingFreq))
        else:
            fc1_dash=(passBandEdge1/samplingFreq)+(transitionWidth/(2*samplingFreq))
            fc2_dash=(passBandEdge2/samplingFreq)-(transitionWidth/(2*samplingFreq))
        hd_map={}
        window_map={}
        odd_N=0
        N,choose=self.CalculateN(stopBandattenuation,samplingFreq,transitionWidth)
        if N%2==0:
            odd_N=N + 1
        for i in range(int(-N/2),int(N/2)+1):
            if i ==0 and PassOrStop == BandPassOrStop.Pass:
                hd_zero=2*(fc2_dash-fc1_dash)
                hd_map[i]=hd_zero
            else:
                hd_zero=1 - 2*(fc2_dash-fc1_dash)
                hd_map[i]=hd_zero
            if i!=0 and PassOrStop==BandPassOrStop.Pass:
                hd_map[i]=((2*fc2_dash*math.sin(i*2*math.pi*fc2_dash))/(i*2*math.pi*fc2_dash)) - ((2*fc1_dash*math.sin(i*2*math.pi*fc1_dash))/(i*2*math.pi*fc1_dash))
            if i!=0 and PassOrStop == BandPassOrStop.stop:
                hd_map[i]=((2*fc1_dash*math.sin(i*2*math.pi*fc1_dash))/(i*2*math.pi*fc1_dash)) - ((2*fc2_dash*math.sin(i*2*math.pi*fc2_dash))/(i*2*math.pi*fc2_dash))
            window_map[i]=self.WindowFunctions(choose,odd_N,i)
        coffecients_h={}
        coffecients_h={k:window_map[k]*hd_map[k] for k in window_map}
        return coffecients_h