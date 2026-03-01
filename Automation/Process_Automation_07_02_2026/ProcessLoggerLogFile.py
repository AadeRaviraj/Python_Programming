# Command line input

import psutil
import sys
import os

def CreateLog(FolderName):
    
    Ret = False
    Ret = os.path.exists(FolderName)
    
    if Ret == True:
        Ret = os.path.isdir(FolderName)
        if Ret == False:
            print("Unable to create folder")
            return
    else:
        os.mkdir(FolderName)
        print("Directory For log files get created successfully")
            
    # if not os.path.exists(FolderName):
    #     os.mkdir(FolderName)
        


def main():
    
    Border = "-" * 60
    print(Border)
    print("----------- Marvellous Platform Surveillance System --------")
    print(Border)
    
    if(len(sys.argv ) == 2):
        if(sys.argv[1] == "--h" or sys.argv[1] == "--H"):
            print("This Script is used to  : ")
            print("1 : Create automatic logs")
            print("2 : Executes periodically")
            print("3 : Sends mail with the log")
            print("4 :  Store information about processes")
            print("5 : Store information about CPU ")
            print("6 : Store information about RAM usages ")
            print("5 : Store information about secondary storage ")
            
        elif (sys.argv[1] == "--u" or sys.argv[1] == "--U"):
            print("Use the automation script as ")
            print("ScriptName.py TimeInterval DirectoryName")
            print("TimeInterval: The time in minutes for periodic scheduling  ")
            print("DirectoryName : Name of decretory to create auto logs ")
            
        else:
            print("Unable tto Proceed as there is no such option ")
            print("Please use --h or --u get more details")
            
    # python demo.py 5 Marvellous
    elif (len(sys.argv) == 3):
        print("Inside projects logic")        
        print("Time interval : ", sys.argv[1])
        print("Directory name : ", sys.argv[2])
        
        CreateLog(sys.argv[2])
    else:
        print("Invalid No of command line arguments")
        print("Unable tto Proceed as there is no such option ")
        print("Please use --h or --u get more detail")
        

    
    
    
    print(Border)
    print("--------------- Thank You for using Our script -------------")
    print(Border)

if __name__ == "__main__":
    main()