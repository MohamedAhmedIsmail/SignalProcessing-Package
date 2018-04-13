import numpy as np
import tkinter as tk
from tkinter.filedialog import askopenfilename
from GenerateNumberInFiles import GenerateRandomNumbers
from ReadAndWriteFiles import ReadAndWrite
from SignalGenerator import SignalGeneration
#from PlotSignals import PlotMySignals
from EnumsClasses import DiscreteOrContinuous, Operations
from PlotSignalsinGUI import SignalPlotInGui
#from PlotSinWave import sin
from OperationsOnSignal import myOperations
from QuantizedSignal import Quantization
from DFT import DiscreteFourierTransform
from FFT import FastFourierTransform
from DFTAndFFTFunction import DftFft
from OperationsOfDftAndFFT import Operations
from EnumsClasses import bitsOrLevels,SinOrCos,TypeOfNormalization,DFTOrIDFT,PhaseAndAmplitude
from EnumsClasses import DelayAdvance
class DrawingHelperFunctions:
    def __init__(self,gui):
        self.gui=gui
        
        self.my2dArray=[]
        self.my2dArray2=[]
        self.ArrGeneratedSignals=[]
        self.myReadedSignal=None
        #self.obj=sin()
    def Bind(self):
        self.gui.RadioOption1=self.option1
        self.gui.RadioOption2=self.option2
        self.gui.WriteToMyFile=self.WriteToFile
        self.gui.ReadMyFirstSignal=self.plotFirstSignal
        self.gui.PlotMyResultedSignal=self.plotMyResultedSignal
        self.gui.PlotmyGeneratedSignal=self.plotGenerateSignal
        self.gui.InitializeComponents()
        self.checkedfiledialog=tk.IntVar()
        #self.obj.draws(self.gui.root)
        
    def option1(self):
            self.gui.flag=1
            return self.gui.flag
        
    def option2(self):
        self.gui.flag=2
        return self.gui.flag
    
    def callBack(self):
        if self.checkedfiledialog.get() !=True:
            fileName= askopenfilename()
            return fileName
        return None
    
    def WriteToFile(self):
        myFilePath=self.callBack()
        myArray=GenerateRandomNumbers.RandomNumbers(int(self.gui.textbox1.get()),int(self.gui.textbox2.get()))
        ReadAndWrite.WriteToFile(myFilePath,myArray)
        
    def plotFirstSignal(self):
        myFilePath=self.callBack()
        if self.gui.DropDown2.get()=='IDFT' or self.gui.DropDown2.get()=='IFFT':
            self.myReadedSignal=ReadAndWrite.Read3DCoordinatesFromFile(myFilePath)
        else:    
            self.myReadedSignal=ReadAndWrite.ReadCoordinatesFromFile(myFilePath)
        myxAxis=np.arange(len(self.myReadedSignal))
        self.my2dArray.append(self.myReadedSignal)
        
        if self.gui.flag==1:
            SignalPlotInGui.plotCoordinateSignals(self.gui.root,self.my2dArray,myxAxis,len(self.my2dArray),DiscreteOrContinuous.discrete)
        else:
            SignalPlotInGui.plotCoordinateSignals(self.gui.root,self.my2dArray,myxAxis,len(self.my2dArray),DiscreteOrContinuous.continuous)
            
    def plotMyResultedSignal(self):
        myxAxis=np.arange(len(self.myReadedSignal))
        if self.gui.DropDown.get()=="Adding":
            mySignal=myOperations.OperationsOnCoordinateSignals(self.my2dArray[0],self.my2dArray[1],Operations.Add)
            self.my2dArray2.append(mySignal)
            
            if self.gui.flag==1:
                SignalPlotInGui.PlotResultedSignal(self.gui.root,self.my2dArray2,myxAxis,len(self.my2dArray2),DiscreteOrContinuous.discrete,0,DelayAdvance.notFold)
                
            elif self.gui.flag==2:
                SignalPlotInGui.PlotResultedSignal(self.gui.root,self.my2dArray2,myxAxis,len(self.my2dArray2),DiscreteOrContinuous.continuous,0,DelayAdvance.notFold)
     
        elif self.gui.DropDown.get()=="Subtract":    
            mySignal=myOperations.OperationsOnCoordinateSignals(self.my2dArray[0],self.my2dArray[1],Operations.Subtract)
            self.my2dArray2.append(mySignal)
            if self.gui.flag==1:    
                SignalPlotInGui.PlotResultedSignal(self.gui.root,self.my2dArray2,myxAxis,len(self.my2dArray2),DiscreteOrContinuous.discrete,0,DelayAdvance.notFold)
            elif self.gui.flag==2:
                SignalPlotInGui.PlotResultedSignal(self.gui.root,self.my2dArray2,myxAxis,len(self.my2dArray2),DiscreteOrContinuous.continuous,0,DelayAdvance.notFold)
                
        elif self.gui.DropDown.get()=="Multiply":    
            mySignal=myOperations.ApplyOperationOnOneSignal(self.myReadedSignal,int(self.gui.textbox3.get()),Operations.Multiply)
            self.my2dArray2.append(mySignal)
            if self.gui.flag==1:    
                SignalPlotInGui.PlotResultedSignal(self.gui.root,self.my2dArray2,myxAxis,len(self.my2dArray2),DiscreteOrContinuous.discrete,0,DelayAdvance.notFold)
            elif self.gui.flag==2:
                SignalPlotInGui.PlotResultedSignal(self.gui.root,self.my2dArray2,myxAxis,len(self.my2dArray2),DiscreteOrContinuous.continuous,0,DelayAdvance.notFold)
        
        elif self.gui.DropDown.get()=='QuantizationBits':
            myQuantizedSignal,myIntegerList,sampleError=Quantization.calculateQuantization(self.myReadedSignal,int(self.gui.textbox3.get()),bitsOrLevels.bits)
            self.my2dArray2.append(myQuantizedSignal)
            if self.gui.flag==1:    
                SignalPlotInGui.PlotResultedSignal(self.gui.root,myQuantizedSignal,myxAxis,len(myQuantizedSignal),DiscreteOrContinuous.discrete,1,DelayAdvance.notFold)
            elif self.gui.flag==2:
                SignalPlotInGui.PlotResultedSignal(self.gui.root,myQuantizedSignal,myxAxis,len(myQuantizedSignal),DiscreteOrContinuous.continuous,1,DelayAdvance.notFold)
                
        elif self.gui.DropDown.get()=='QuantizationLevels':
            myQuantizedSignal,myIntegerList,sampleError=Quantization.calculateQuantization(self.myReadedSignal,int(self.gui.textbox3.get()),bitsOrLevels.levels)
            self.my2dArray2.append(myQuantizedSignal)
            if self.gui.flag==1:    
                SignalPlotInGui.PlotResultedSignal(self.gui.root,myQuantizedSignal,myxAxis,len(myQuantizedSignal),DiscreteOrContinuous.discrete,1,DelayAdvance.notFold)
            elif self.gui.flag==2:
                SignalPlotInGui.PlotResultedSignal(self.gui.root,myQuantizedSignal,myxAxis,len(myQuantizedSignal),DiscreteOrContinuous.continuous,1,DelayAdvance.notFold)
        elif self.gui.DropDown2.get()=='Normalize01':
            signalObject=SignalGeneration()
            NormalizedSignal=signalObject.NormalizeSignal(self.my2dArray[0],TypeOfNormalization.zeroToOne)
            SignalPlotInGui.PlotResultedSignal(self.gui.root,NormalizedSignal,myxAxis,len(NormalizedSignal),DiscreteOrContinuous.discrete,1,DelayAdvance.notFold)
        elif self.gui.DropDown2.get()=='Normalize-11':
            signalObject=SignalGeneration()
            NormalizedSignal=signalObject.NormalizeSignal(self.my2dArray[0],TypeOfNormalization.negativeOneToOne)
            SignalPlotInGui.PlotResultedSignal(self.gui.root,NormalizedSignal,myxAxis,len(NormalizedSignal),DiscreteOrContinuous.discrete,1,DelayAdvance.notFold)
        elif self.gui.DropDown2.get()=='Moving Average':
            signalObject=SignalGeneration()
            kernal=int(self.gui.textbox4.get())
            AveragedSignal=signalObject.MovingAverage(kernal,self.my2dArray[0])
            SignalPlotInGui.PlotResultedSignal(self.gui.root,AveragedSignal,myxAxis,len(AveragedSignal),DiscreteOrContinuous.discrete,1,DelayAdvance.notFold)
        elif self.gui.DropDown2.get()=='Derivative':
            signalObject=SignalGeneration()
            DerivativeSignal=signalObject.SignalDerivative(self.my2dArray[0])
            SignalPlotInGui.PlotResultedSignal(self.gui.root,DerivativeSignal,myxAxis,len(DerivativeSignal),DiscreteOrContinuous.discrete,1,DelayAdvance.notFold)
        elif self.gui.DropDown2.get()=='DC Component':
            signalObject=SignalGeneration()
            DCComponent=signalObject.RemovingDcComponents(self.my2dArray[0])    
            SignalPlotInGui.PlotResultedSignal(self.gui.root,DCComponent,myxAxis,len(DCComponent),DiscreteOrContinuous.discrete,1,DelayAdvance.notFold)
        elif self.gui.DropDown.get()=='FoldSignal':
            myObj=Operations()
            Signal=myObj.FoldingSignal(self.my2dArray[0])
            #print(Signal)
            SignalPlotInGui.PlotResultedSignal(self.gui.root,Signal,myxAxis,len(Signal),DiscreteOrContinuous.discrete,1,DelayAdvance.notFold)
        elif self.gui.DropDown.get()=='ShiftSignal':
            myObj=Operations()
            shiftedValue=int(self.gui.textbox4.get())
            if(shiftedValue>0):    
                Signal=myObj.DelayingAdvancingSignal(self.my2dArray[0],shiftedValue,DelayAdvance.Delay)
            else:
                Signal=myObj.DelayingAdvancingSignal(self.my2dArray[0],shiftedValue,DelayAdvance.Advance)
            SignalPlotInGui.PlotResultedSignal(self.gui.root,Signal,myxAxis,len(Signal),DiscreteOrContinuous.discrete,1,DelayAdvance.notFold)
        elif self.gui.DropDown.get()=='ShiftFoldedSignal':
            myObj=Operations()
            shiftedValue=int(self.gui.textbox4.get())
            foldedSignal=myObj.FoldingSignal(self.my2dArray[0])
            if(shiftedValue>0):    
                Signal=myObj.DelayAdvanceFoldedSignal(foldedSignal,shiftedValue,DelayAdvance.Delay)
                SignalPlotInGui.PlotResultedSignal(self.gui.root,Signal,myxAxis,len(Signal),DiscreteOrContinuous.discrete,1,DelayAdvance.fold)
            else:
                Signal=myObj.DelayAdvanceFoldedSignal(foldedSignal,shiftedValue,DelayAdvance.Advance)
                SignalPlotInGui.PlotResultedSignal(self.gui.root,Signal,myxAxis,len(Signal),DiscreteOrContinuous.discrete,1,DelayAdvance.notFold)
        elif self.gui.DropDown.get()=='DcComponent':
            myObj=DftFft()
            RemoveDc=myObj.RemoveDcComponents(self.my2dArray[0])
            SignalPlotInGui.PlotResultedSignal(self.gui.root,RemoveDc,myxAxis,len(RemoveDc),DiscreteOrContinuous.discrete,1,DelayAdvance.notFold)
            print(RemoveDc)
        
        elif self.gui.DropDown.get()=='Accumulate':
            myObj=DftFft()
            AccumSignal=myObj.AccumulatedSignal(self.my2dArray[0])
            SignalPlotInGui.PlotResultedSignal(self.gui.root,AccumSignal,myxAxis,len(AccumSignal),DiscreteOrContinuous.discrete,1,DelayAdvance.notFold)
        
        elif self.gui.DropDown.get()=='ZeroCrossing':
            myObj=DftFft()
            zeroCrossing=myObj.ZeroCrossing(self.my2dArray[0])
            SignalPlotInGui.PlotResultedSignal(self.gui.root,zeroCrossing,myxAxis,len(zeroCrossing),DiscreteOrContinuous.discrete,1,DelayAdvance.notFold)
            
            
    def plotGenerateSignal(self):
        signalObject=SignalGeneration()
        if self.gui.DropDown2.get()=='Sin':
            amplitude=int(self.gui.textbox4.get())
            frequency=int(self.gui.textbox5.get())
            noOfSamples=int(self.gui.textbox2.get())
            analogFrequency=int(self.gui.textbox6.get())
            phaseShift=int(self.gui.textbox7.get())
            myGeneratedSignal=signalObject.Signal(noOfSamples,amplitude,frequency,analogFrequency,phaseShift,SinOrCos.sin)
            self.ArrGeneratedSignals.append(myGeneratedSignal)
            SignalPlotInGui.PlotGeneratedSignal(self.gui.root,self.ArrGeneratedSignals,len(self.ArrGeneratedSignals),DiscreteOrContinuous.discrete)
        elif self.gui.DropDown2.get()=='Cosine':
            amplitude=int(self.gui.textbox4.get())
            frequency=int(self.gui.textbox5.get())
            noOfSamples=int(self.gui.textbox2.get())
            analogFrequency=int(self.gui.textbox6.get())
            phaseShift=int(self.gui.textbox7.get())
            myGeneratedSignal=signalObject.Signal(noOfSamples,amplitude,frequency,analogFrequency,phaseShift,SinOrCos.cos)
            self.ArrGeneratedSignals.append(myGeneratedSignal)
            SignalPlotInGui.PlotGeneratedSignal(self.gui.root,self.ArrGeneratedSignals,len(self.ArrGeneratedSignals),DiscreteOrContinuous.discrete)
        elif self.gui.DropDown2.get()=='DFT':
            myDFTObj=DiscreteFourierTransform()
            myFDobj=DftFft()
            mySignal=myFDobj.ReturnNumbersOfSignal(self.my2dArray[0])
            myNewSignal=myDFTObj.DFT(mySignal,DFTOrIDFT.DFT)
            squareList,reals,imag=myFDobj.squareRoot(myNewSignal)
            SignalPlotInGui.PlotAmplitudeVersusPhase(self.gui.root,squareList,imag,reals,PhaseAndAmplitude.Phase)
            SignalPlotInGui.PlotAmplitudeVersusPhase(self.gui.root,squareList,imag,reals,PhaseAndAmplitude.Amplitude)
        elif self.gui.DropDown2.get()=='IDFT':
            myDFTObj=DiscreteFourierTransform()
            myFDobj=DftFft()
            myComplexSignal=myFDobj.convertPolarFormToComplexForm(self.my2dArray)
            lst1,real,img=myFDobj.squareRoot(myComplexSignal)
            finalSignal=myDFTObj.IDFT(real,img)
            SignalPlotInGui.PlotIDFT(self.gui.root,finalSignal)
        elif self.gui.DropDown2.get()=='FFT':
            myFFTObj=FastFourierTransform()
            myFDobj=DftFft()
            mySignal=myFDobj.ReturnNumbersOfSignal(self.my2dArray[0])
            myNewSignal=myFFTObj.fft(mySignal)
            squareList,reals,imag=myFDobj.squareRoot(myNewSignal)
            SignalPlotInGui.PlotAmplitudeVersusPhase(self.gui.root,squareList,imag,reals,PhaseAndAmplitude.Phase)
            SignalPlotInGui.PlotAmplitudeVersusPhase(self.gui.root,squareList,imag,reals,PhaseAndAmplitude.Amplitude)
        elif self.gui.DropDown2.get()=='IFFT':
            myFFTObj=FastFourierTransform()
            myFDobj=DftFft()
            myComplexSignal=myFDobj.convertPolarFormToComplexForm(self.my2dArray)
            mySignal=myFFTObj.ifft(myComplexSignal)
            SignalPlotInGui.PlotIDFT(self.gui.root,mySignal)
        if self.gui.DropDown.get()=="Adding":
            myxAxis=np.arange(noOfSamples)
            myAddingSignal=myOperations.OperationsOnCoordinateSignals(self.ArrGeneratedSignals[0],self.ArrGeneratedSignals[1],Operations.Add,1)
            SignalPlotInGui.PlotResultedSignal(self.gui.root,myAddingSignal,myxAxis,len(self.my2dArray2),DiscreteOrContinuous.discrete,1)
            