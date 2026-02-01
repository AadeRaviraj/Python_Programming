import os


def DirectoryScanner(DirectoryName = "Marvellous"):
    
    ret = os.path.exists(DirectoryName)
    
    if ret == False:
        print("There is no such directory")
        return
    
    ret = os.path.isdir(DirectoryName)
    
    if ret == False:
        print("Unable to scan as it not a directory :")
        return
    
    print("Contents of the directory are  : ")   
    i=0
    j = 0 
    for FolderName , SubFolderName , FileName in os.walk(DirectoryName):
        print("Folder  name : ", FolderName)
    
        for subf in SubFolderName:
            i +=1
            print("Sub Folder name : ", subf,"ivalue ",i )
            
        for fname in FileName:
            j+=1
            print("File name : ", fname, "jvalue",j)
    
def main():
    
    DirectoryName = input("Enter the name of directory ")
    DirectoryScanner(DirectoryName)


if __name__ == "__main__":
    main()