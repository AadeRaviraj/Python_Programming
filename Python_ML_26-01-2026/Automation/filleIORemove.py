import os

def main():
    FIleName = input("Enter the name of file : ")
    
    if (os.path.exists(FIleName)): 
        os.remove(FIleName)
        print("File gets deleted")
    else:
        print("There is no such file ")

if __name__ == "__main__":
    main()