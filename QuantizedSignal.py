import numpy as np
import math
from EnumsClasses import bitsOrLevels
class Quantization:
    
    @staticmethod
    def calculateQuantization(SignalArray=None,numberOfLevelsOrBits=None, bitsOrlevels=None):
        yValues=[y[1] for y in SignalArray]
        for i in range(len(yValues)):
            yValues[i]=float(yValues[i])
        maximumNumber=np.max(yValues)
        minimumNumber=np.min(yValues)
        numberOfLevels=None
        if bitsOrlevels==bitsOrLevels.levels:
            numberOfLevels=numberOfLevelsOrBits
        elif bitsOrlevels==bitsOrLevels.bits:
            numberOfLevels=2**numberOfLevelsOrBits
        delta=(maximumNumber-minimumNumber)/float(numberOfLevels)
        myList=[]
        for i in range(numberOfLevels):
            Result=minimumNumber+delta
            myList.append((minimumNumber,Result))
            minimumNumber=Result
        midPointsList=[]
        xValuesFirstSignal=[x[0] for x in myList]
        yValuesFirstSignal=[y[1] for y in myList]
        yValuesFirstSignal[len(yValuesFirstSignal)-1]=math.ceil(yValuesFirstSignal[len(yValuesFirstSignal)-1])
        for i in range(numberOfLevels):
            midPointsList.append((xValuesFirstSignal[i]+yValuesFirstSignal[i])/2)
        indexList=[]
        for i in range(len(yValues)):
            for j in range(len(yValuesFirstSignal)):
                if yValues[i]<=yValuesFirstSignal[j]:
                    indexList.append(j)
                    break
        xqn=[]
        for i in range(len(indexList)):
            xqn.append(midPointsList[indexList[i]])
        sampleError=[]
        for i in range(len(xqn)):
            sampleError.append(xqn[i]-yValues[i])
        return xqn,indexList,sampleError
        
    
    @staticmethod
    def convertToBinary(myIntegerList=None):
        binaryList=[]
        for i in range(len(myIntegerList)):
            binaryList.append(bin(myIntegerList[i])[2:])
        return binaryList