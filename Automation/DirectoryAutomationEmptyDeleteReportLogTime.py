import os
import sys
import time

def DirectoryScanner(DirName = "Marvellous"):
    border = "-" * 60
    timestamp = time.ctime()     
    fobj = open("Marvellous.log", "w")        
    fobj.write(border + "\n")
    fobj.write("This is the log file  created by Marvellous Automation\n")
    fobj.write("This is Directory Cleaner Script\n")
    fobj.write(border +"\n")
    
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
            if(os.path.getsize(fName) == 0  ): # empty file 
                EmptyFileCount = EmptyFileCount + 1
                
                os.remove(fName)


    
    fobj.write("Total file count : "+ str(FileCount) + "\n")    
    fobj.write("Total empty file found : "+str (EmptyFileCount) + "\n")
    fobj.write("This Log file created at : " + timestamp + "\n")
    fobj.write(border+"\n")
    
    fobj.close()
    
    
    
    
    
def main():
    border = "-" * 60 
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