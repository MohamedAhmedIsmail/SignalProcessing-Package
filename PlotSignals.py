import matplotlib.pyplot as plt
from EnumsClasses import DiscreteOrContinuous
class PlotMySignals:
    
    @staticmethod
    def plotOneSignal(myArrSignal=None,myxAxisArray=None):
        plt.xticks(myxAxisArray)
        plt.yticks(myArrSignal)
        plt.plot(myArrSignal,'bo')
        plt.show()
        return None
    
    @staticmethod
    def plotCoordinateSignals(myArrSignal=None,myxAxisArray=None,numberOfSignals=None,DiscOrCont=None):
        
        colors=['ko','bo','ro','go','co','mo','yo']
        for i in range(numberOfSignals):
            xvals = [x[0] for x in myArrSignal[i]]
            yvals= [y[1] for y in myArrSignal[i]]
            plt.xticks(myxAxisArray)
            plt.yticks(yvals)
            if DiscOrCont == DiscreteOrContinuous.discrete:
                plt.plot(xvals,yvals,colors[i])
            elif DiscOrCont == DiscreteOrContinuous.continuous:
                plt.plot(xvals,yvals,marker='o')
        plt.show()
        return None