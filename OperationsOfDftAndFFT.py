from EnumsClasses import DelayAdvance
class Operations:
    def __init__(self):
        pass
    
    def DelayingAdvancingSignal(self,Signal=None,kUnits=None,DelayOrAdvance=None):
        HashSignal={}
        N=len(Signal)
        for i in range(N):
            HashSignal[int(Signal[i][0])]=int(Signal[i][1])
        #print(HashSignal)
        myList=[]
        for k in HashSignal.keys():
            if DelayOrAdvance==DelayAdvance.Advance:
                myList.append(k+(-kUnits))
            else:
                myList.append(k-kUnits)
        newHashTable={}
        for i in range(N):
            newHashTable[myList[i]]=int(Signal[i][1])
        return newHashTable
    
    def DelayAdvanceFoldedSignal(self,Signal=None,kUnits=None,DelayOrAdvance=None):
        N=len(Signal)
        myList=[]
        for k in Signal.keys():
            if DelayOrAdvance==DelayAdvance.Advance:
                myList.append(k+kUnits)
            else:
                myList.append(k+kUnits)
        newHashTable={}
        myValueList=[]
        for value in Signal.values():
            myValueList.append(value)
        for i in range(N):
            newHashTable[myList[i]]=myValueList[i]
        return newHashTable
        
    def FoldingSignal(self,Signal=None):
        myList=[]
        N=len(Signal)
        HashSignal={}
        for i in range(N):
            HashSignal[int(Signal[i][0])]=int(Signal[i][1])
        for i in range(N):
            myList.append(int(Signal[i][1]))
        myList.reverse()
        for i in range(N):
            HashSignal[int(Signal[i][0])]=myList[i]
        return HashSignal