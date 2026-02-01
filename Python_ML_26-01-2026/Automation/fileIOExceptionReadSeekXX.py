#  seek (kuthe , kuthun)
# Kuthun : 0 / 1 / 2 
# 0 : Starting
# 1 : Current
# 2 : End

def main():

    try :
        fObj= open("Hello.txt","r")
        print("File Gets successfully opened ")
        
        print("current Offset is : ", fObj.tell())  # 0 
        
        fObj.seek(6,1)
        
        print("current Offset is : ", fObj.tell())  # 11
        
        Data = fObj.read(6)
        
        print("current Offset is : ", fObj.tell()) # 17

        
        print("Data from file is : ",Data)
        
        fObj.close()
    except FileNotFoundError:
        print("Unable to open file as there is no such file ")
        
        
    finally:
        print("End of application ")
        
        
        

if __name__ == "__main__":
    main()