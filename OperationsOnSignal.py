from EnumsClasses import CheckOperations
class myOperations:
    def __init__(self):
        pass
    @staticmethod
    def OperationsOnCoordinateSignals(myFirstSignal=None,mySecondSignal=None,myOperation=None,check=None):
        myNewCoordinateList=[]
        if len(myFirstSignal) != len(mySecondSignal):
            tempFirst=list(myFirstSignal)
            tempSecond=list(mySecondSignal)
            myNewCoordinateList=[]
            for i in range(len(myFirstSignal)):
                for j in range(len(mySecondSignal)):
                    if myFirstSignal[i][0] == mySecondSignal[j][0]:
                        tempFirst.remove(myFirstSignal[i])
                        tempSecond.remove(mySecondSignal[j])
                        if myOperation == CheckOperations.Add:
                            myNewCoordinateList.append((myFirstSignal[i][0],myFirstSignal[i][1]+mySecondSignal[j][1]))
                        elif myOperation == CheckOperations.Subtract:
                            myNewCoordinateList.append((myFirstSignal[i][0],abs(myFirstSignal[i][1]-mySecondSignal[j][1])))
            myNewCoordinateList.extend(tempFirst)
            myNewCoordinateList.extend(tempSecond)
            return myNewCoordinateList
        else:
            if check==0:
                xValuesFirstSignal=[x[0] for x in myFirstSignal]
                yValuesFirstSignal=[y[1] for y in myFirstSignal]
                yValuesSecondSignal=[y[1] for y in mySecondSignal]
            else:
                yValuesFirstSignal=[y for y in myFirstSignal]
                yValuesSecondSignal=[y for y in mySecondSignal]
                AddingList=[]
                for i in range(len(yValuesFirstSignal)):
                    if myOperation == CheckOperations.Add:
                        AddingList.append(yValuesFirstSignal[i]+yValuesSecondSignal[i])
                return AddingList
            for i in range(len(xValuesFirstSignal)):
                if myOperation == CheckOperations.Add:
                    yValuesFirstSignal[i]=yValuesFirstSignal[i]+yValuesSecondSignal[i]
                elif myOperation == CheckOperations.Subtract:
                    yValuesFirstSignal[i]=int(yValuesFirstSignal[i])-int(yValuesSecondSignal[i])
            for i in range(len(xValuesFirstSignal)):
                myNewCoordinateList.append((xValuesFirstSignal[i],yValuesFirstSignal[i]))
            return myNewCoordinateList
    @staticmethod
    def ApplyOperationOnOneSignal(mySignal=None,myValue=None,myOperation=None):
        xValuesOfMySignal=[x[0] for x in mySignal]
        yValuesOfMySignal=[y[1] for y in mySignal]
        myResultedSignal=[]
        for i in range(len(xValuesOfMySignal)):    
            if myOperation == CheckOperations.Multiply:
                 yValuesOfMySignal[i]=yValuesOfMySignal[i] * myValue
        for i in range(len(xValuesOfMySignal)):
            myResultedSignal.append((xValuesOfMySignal[i],yValuesOfMySignal[i]))
        return myResultedSignal