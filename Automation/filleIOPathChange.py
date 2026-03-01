import os

def main():
    FIleName = input("Enter the name of file : ")
    
    Ret = os.path.isabs(FIleName)
    
    if(Ret == True):
        print("It is absolute path")
    else:
        print("it is Relative path")
        NewPath = os.path.abspath(FIleName)
        print("Updated path : ",NewPath)
    

if __name__ == "__main__":
    main()