import os

def main():
    FIleName = input("Enter the name of file : ")
    
    if (os.path.exists(FIleName)): 
        fobj = open(FIleName, "w")
        
        print(fobj.readable())
        
        print(fobj.writable())
        
        print(fobj.seekable())
        
    else:
        print("There is no such file ")

if __name__ == "__main__":
    main()