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


def DirectoryWatcher(Directoryname = "Marvellous"):
    ret = False
    ret =  os.path.exists(Directoryname)
    
    if ret == False:
        print("There is no such directory ")
        return
    
    ret = os.path.isdir(Directoryname)
    
    if ret == False:
        print("it is not a directory ")
        return
    
    for FolderName , SuBfolderName, FileName  in os.walk(Directoryname):
        
        for fname  in FileName:
            print(type(fname))
            print(type(FileName))
            fname = os.path.join(FolderName, fname)
            CheckSum = CalculateChecksum(fname)
            
            print(f"File Name : {fname} Checksum : {CheckSum}")
        

def main():
    
    DirectoryWatcher()

if __name__ == "__main__":
    main()