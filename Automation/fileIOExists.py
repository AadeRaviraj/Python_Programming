import os

def main():
    FIleName = input("Enter the name of file : ")
    
    ret = os.path.exists(FIleName)
    
    if ret == True :
        fobj = open(FIleName, "r")
        print("file gets successfully open ")
    else:
        print("There is no such file ")
    

if __name__ == "__main__":
    main()