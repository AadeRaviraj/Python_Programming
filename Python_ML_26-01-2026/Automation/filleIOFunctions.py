import os

def main():
    FIleName = input("Enter the name of file : ")
    
    if (os.path.exists(FIleName)): 
        fobj = open(FIleName, "r")
        
        print(fobj.name) # Demo.txt
        
        print(fobj.mode) # R
        
        print(fobj.closed)   # False
        
        fobj.close()
        
        print(fobj.closed)  # True
    else:
        print("There is no such file ")

if __name__ == "__main__":
    main()