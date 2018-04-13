import numpy as np
class GenerateRandomNumbers:
    def __init__(self):
       pass
    @staticmethod
    def RandomNumbers(RangeOfNumbers=None,SizeOfArray=None):
        generatedArray=np.random.randint(RangeOfNumbers,size=SizeOfArray)
        return generatedArray
    
    @staticmethod
    def RandomCoordinateNumbers(RangeofNumbers=None,SizeOfArray=None):
        xCoordinate=np.random.randint(RangeofNumbers,size=SizeOfArray)
        yCoordinate=np.random.randint(RangeofNumbers,size=SizeOfArray)
        myCoordinateList=[]
        for i in xCoordinate:
            myCoordinateList.append((xCoordinate[i],yCoordinate[i]))
        return myCoordinateList


    
    