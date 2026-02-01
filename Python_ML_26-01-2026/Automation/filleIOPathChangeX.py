import os

def main():
    FIleName = input("Enter the name of file : ")
    
    if (os.path.exists(FIleName)):
        Ret = os.path.isabs(FIleName)
        
        if(Ret == True):
            print("It is absolute path")
        else:
            print("it is Relative path")
            NewPath = os.path.abspath(FIleName)
            print("Updated path : ",NewPath)
    else:
        print("There is no such file ")

if __name__ == "__main__":
    main()