from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from EnumsClasses import DiscreteOrContinuous,PhaseAndAmplitude,DelayAdvance
import math

class SignalPlotInGui:
    @staticmethod
    def plotCoordinateSignals(root,myArrSignal=None,myxAxisArray=None,numberOfSignals=None,DiscOrCont=None):
        fig = Figure(figsize=(4,4))
        a = fig.add_subplot(111)
        colors=['ko','bo','ro','go','co','mo','yo']
        for i in range(numberOfSignals):
            xvals = [x[0] for x in myArrSignal[i]]
            yvals= [y[1] for y in myArrSignal[i]]
            if DiscOrCont==DiscreteOrContinuous.continuous:
                a.plot(xvals,yvals,marker='o')
            elif DiscOrCont==DiscreteOrContinuous.discrete:
                a.plot(xvals,yvals,colors[i])
        a.set_title ("Signal Grid", fontsize=12)
        a.set_ylabel("Y", fontsize=10)
        a.set_xlabel("X", fontsize=10)
        canvas = FigureCanvasTkAgg(fig, master=root)
        canvas.get_tk_widget().grid(row=8,column=1)
        canvas.show()
        canvas.draw()
    
    @staticmethod
    def PlotResultedSignal(root,myArrSignal=None,myxAxisArray=None,numberOfSignals=None,DiscOrCont=None, check=None,folded=None):
        fig3=Figure(figsize=(4,4))
        b=fig3.add_subplot(111)
        for i in range(numberOfSignals):
            if check==0:
                xvals = [x[0] for x in myArrSignal[i]]
                yvals = [x[1] for x in myArrSignal[i]]
            else:
                xvals = [x for x in myArrSignal]
                yvals = [x for x in myArrSignal]
            if DiscOrCont==DiscreteOrContinuous.continuous:
                b.plot(xvals,yvals,marker='o')
        if DiscOrCont==DiscreteOrContinuous.discrete:
            yvals=[x for x in myArrSignal]
            if folded == DelayAdvance.fold:
                yvals.reverse()
            b.plot(yvals,'bo')
        b.set_title ("Signal Grid", fontsize=12)
        b.set_ylabel("Y", fontsize=10)
        b.set_xlabel("X", fontsize=10)
        canvas3 = FigureCanvasTkAgg(fig3, master=root)
        canvas3.get_tk_widget().grid(row=8,column=2)
        canvas3.show()
        canvas3.draw()
        
    @staticmethod
    def PlotIDFT(root,myArrSignal):
        fig=Figure(figsize=(4,4))
        b=fig.add_subplot(111)
        b.plot(myArrSignal,'o')
        b.set_title ("Signal Grid", fontsize=12)
        b.set_ylabel("Y", fontsize=10)
        b.set_xlabel("X", fontsize=10)
        canvas3 = FigureCanvasTkAgg(fig, master=root)
        canvas3.get_tk_widget().grid(row=8,column=2)
        canvas3.show()
        canvas3.draw()
    
    @staticmethod
    def PlotGeneratedSignal(root,myArrSignal=None,numberOfSignals=None,DiscOrCont=None):
        fig3=Figure(figsize=(4,4))
        colors=['ko','bo','ro','go','co','mo','yo']
        b=fig3.add_subplot(111)
        for i in range(numberOfSignals):
            yvals=[x for x in myArrSignal[i]]
            if DiscOrCont==DiscreteOrContinuous.continuous:
                b.plot(yvals,colors[i])
            if DiscOrCont==DiscreteOrContinuous.discrete:
                 b.plot(yvals,colors[i])
        b.set_title ("Signal Grid", fontsize=12)
        b.set_ylabel("Y", fontsize=10)
        b.set_xlabel("X", fontsize=10)
        canvas3 = FigureCanvasTkAgg(fig3, master=root)
        canvas3.get_tk_widget().grid(row=8,column=1)
        canvas3.show()
        canvas3.draw()
        
    @staticmethod
    def PlotAmplitudeVersusPhase(root,myArrSignal=None,imag=None,RealNumbers=None,PhaseOrAmplitude=None):
        fig=Figure(figsize=(4,4))
        b=fig.add_subplot(111)
        phase=[]
        for i in range(len(RealNumbers)):
            degree=imag[i]/RealNumbers[i]
            x=math.degrees(math.atan(degree))
            phase.append(x)
        b.set_title ("Signal Grid", fontsize=12)
        b.set_ylabel("Y", fontsize=10)
        b.set_xlabel("X", fontsize=10)
        if PhaseOrAmplitude==PhaseAndAmplitude.Phase:
            b.plot(phase,'o')
            canvas3 = FigureCanvasTkAgg(fig, master=root)
            canvas3.get_tk_widget().grid(row=8,column=2)
        elif PhaseOrAmplitude==PhaseAndAmplitude.Amplitude:
            b.plot(myArrSignal,'o')
            canvas3 = FigureCanvasTkAgg(fig, master=root)
            canvas3.get_tk_widget().grid(row=8,column=3)
        canvas3.show()
        canvas3.draw()