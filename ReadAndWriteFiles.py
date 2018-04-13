import numpy as np
class ReadAndWrite:
    @staticmethod
    def ReadFromFile(Path=None):
        myFile=open(Path)
        content=myFile.readlines()
        numbers=[]
        for line in content:
            l=line.split(' ')
            a=int(l[0])
            numbers.append(a)
        myArray=np.array(numbers)
        return myArray
    
    @staticmethod
    def ReadCoordinatesFromFile(Path):
        myFile=open(Path)
        content=myFile.readlines()
        mySeparatedContent=[]
        for i in range(len(content)):
            if i>2:
                mySeparatedContent.append(content[i])
            #mySeparatedContent.append(content[i])
        myCoordinateList=[]
        for line in mySeparatedContent:
                l=line.split(' ')
                a=l[0]
                b=l[1]
                myCoordinateList.append((a,b))
        return myCoordinateList
    
    @staticmethod
    def Read3DCoordinatesFromFile(Path):
        myFile=open(Path)
        content=myFile.readlines()
        mySeparatedContent=[]
        for i in range(len(content)):
            if i>2:
                mySeparatedContent.append(content[i])
            #mySeparatedContent.append(content[i])
        myCoordinateList=[]
        for line in mySeparatedContent:
                l=line.split(' ')
                a=l[0]
                b=l[1]
                c=l[2]
                myCoordinateList.append((a,b,c))
        return myCoordinateList
    
    @staticmethod
    def ReadComplexNumbers(Path=None):
        f=open(Path,"r+")
        complexNumber=[]
        for line in f:
             line=line.split()
             if line: 
                    line=[complex(i) for i in line]
                    complexNumber.append(line)
        s=complex(0)
        complexNumbers=[]
        for i in range(len(complexNumber)):
            s=complexNumber[i]
            complexNumbers.append(s)
        return complexNumbers
        
    @staticmethod
    def WriteToFile(Path=None,myArr=None):
        myFile=open(Path,'w')
        for value in myArr:
            myFile.write("%s\n" % value)
    @staticmethod
    def WriteCoordinatesToFile(Path=None,myCoordinateList=None):
        myFile=open(Path,'w')
        for x,y in myCoordinateList:
            myFile.write('{} {}\n'.format(x,y))
    