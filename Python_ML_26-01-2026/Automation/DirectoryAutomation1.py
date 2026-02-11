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
    
    for FolderName , SubFolder, FileName in os.walk(DirName):
        for fName in FileName:
            print(fName)
    
def main():
    border = "-" * 50 
    print(border)
    
    print("-------------- Directory Automation --------------")
    print(border)
    
    if(len(sys.argv) != 2):
        print("Invalid number of arguments ")
        print("Please specify teh nam eof directory ")
        return
    DirectoryScanner(sys.argv[1])

if __name__ == "__main__":
    main()