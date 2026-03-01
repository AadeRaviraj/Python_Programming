import hashlib
import os

def CalculateChecksum(FileName):
    fobj = open(FileName, "rb")
    
    hobj = hashlib.md5()
    
    Buffer = fobj.read(1024)
    
    while len(Buffer) > 0 :
        hobj.update(Buffer)
        Buffer = fobj.read(1024)
    
    fobj.close()
    return hobj.hexdigest()


def FindDuplicate(Directoryname ="Marvellous"):
    ret = False
    ret =  os.path.exists(Directoryname)
    
    if ret == False:
        print("There is no such directory ")
        return
    
    ret = os.path.isdir(Directoryname)
    
    if ret == False:
        print("it is not a directory ")
        return
    
    Duplicate = {}
    
    for FolderName , SuBfolderName, FileName  in os.walk(Directoryname):        
        for fname  in FileName:
            
            fname = os.path.join(FolderName, fname)
            CheckSum = CalculateChecksum(fname)
            
            if CheckSum in Duplicate:
                Duplicate[CheckSum].append(fname)
            else:
                Duplicate[CheckSum] = [fname] 
    
    return Duplicate
        

def DisplayResult(Mydict):
    result = list(filter(lambda x: len(x)> 1, Mydict.values()))
    
    Count = 0 
    
    for value in result:
        for subValue in value:
            Count = Count + 1
            print(subValue)
        print("Value of Count is : ", Count)
        Count = 0 

def DeleteDuplicate(Path = "Marvellous"):
    MyDict = FindDuplicate(Path)
    result = list(filter(lambda x: len(x)> 1, MyDict.values()))
    
    Count = 0 
    Cnt = 0 
    
    for value in result:
        for subValue in value:
            Count = Count + 1 
            if Count > 1:
                print("Deleted File : ", subValue)
                os.remove(subValue)
                Cnt = Cnt + 1
        Count = 0
    print("Total Deleted  Files : ", Cnt)        
    
def main():
    
    # ret = FindDuplicate()
    # DisplayResult(ret)
    
    DeleteDuplicate()
if __name__ == "__main__":
    main()