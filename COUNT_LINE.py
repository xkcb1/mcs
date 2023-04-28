import sys
import os
#
CountFile = 0 
CountLine = 0
def Traverse(dir):
    global CountFile,CountLine
    list=[]
    for dirpath,dirnamesList,filenamesList in os.walk(dir):
        for filename in filenamesList:
            list.append(dirpath+"\\"+filename)
            if filename.split(".")[-1] == 'py':
                print(CountFile+1,filename,':')
                CountFile = CountFile + 1
                with open(dirpath+"\\"+filename,'r',encoding='utf8') as f:
                    ThisCount = len(f.readlines())
                    
                
                print("\tline:", ThisCount)
                CountLine += ThisCount
        for dirname in dirnamesList:
            list.append(dirpath+"\\"+dirname+"\\")
    return list;
#
if __name__=='__main__':
    Traverse('./')
    print('total count line:',CountLine)