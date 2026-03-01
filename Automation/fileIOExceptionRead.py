def main():

    try :
        fObj= open("Hello.txt","r")
        print("File Gets successfully opened ")
        
        Data = fObj.read()
        
        print("Data from file is : ",Data)
        fObj.close()
    except FileNotFoundError:
        print("Unable to open file as there is no such file ")
        
        
    finally:
        print("End of application ")
        
        
        

if __name__ == "__main__":
    main()