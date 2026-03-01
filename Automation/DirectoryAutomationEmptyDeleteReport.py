import os
import sys

def DirectoryScanner(DirName = "Marvellous"):

    ret = False
    
    ret = os.path.exists(DirName)
    if(ret == False):
        print("There is no such directory ")
        return
    
    ret = os.path.isdir(DirName)
    
    if(ret == False):
        print("It is not a Directory ")
        return
    
    FileCount = 0
    EmptyFileCount = 0
    
    for FolderName , SubFolder, FileName in os.walk(DirName):
        
        for fName in FileName:
            FileCount = FileCount + 1
        
            fName = os.path.join(FolderName, fName)
            print("File name : ",fName)
            print("File Size :", os.path.getsize(fName)) #  
            
            if(os.path.getsize(fName) == 0  ): # empty file 
                EmptyFileCount = EmptyFileCount + 1
                
                os.remove(fName)
    border = "-" * 50 
    print(border) 
    
    print("------------------- Automation Report --------------------")
    print("Total file count :", FileCount)
    
    print("Total empty file found : ", EmptyFileCount)
    print(border)
    
def main():
    border = "-" * 50 
    print(border)    
    print("------------------ Directory Automation ------------------")
    print(border)
    
    if(len(sys.argv) != 2):
        print("Invalid number of arguments ")
        print("Please specify teh nam eof directory ")
        return
    DirectoryScanner(sys.argv[1])
    
    print(border)    
    print("------------------ Thank Your For Using  -----------------")
    print(border)
    

if __name__ == "__main__":
    main()