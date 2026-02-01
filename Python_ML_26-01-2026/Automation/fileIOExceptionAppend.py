def main():

    try :
        fObj= open("Hello.txt","a")
        print("File Gets successfully opened ")
        
        fObj.write("Python Automation")
        fObj.close()
    except FileNotFoundError:
        print("Unable to open file as there is no such file ")
        
        
    finally:
        print("End of application ")
        
        
        

if __name__ == "__main__":
    main()