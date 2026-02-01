import sys
import time
import datetime
import schedule
 

def main():  
    Border = "-" * 40
    
    print(Border)
    
    print("--------- Automation --------")
    
    print(Border)
    
    if (len(sys.argv) == 2):
        
        if((sys.argv[1] == "--h") or (sys.argv[1] == "--H") ):
            print("This application is used to perform ____")
            print("This is the automation script ") 
            
        elif((sys.argv[1] == "--u") or (sys.argv[1] == "--U") ):
            print("TUse the give script as")
            print("ScriptName.py Argument1 Argument2 ") 
            print("Argument1 :___________")            
            print("Argument2 :___________")
        else:
            print("Use the give flag as :")
            print("--u : Use to display the usage")
            print("--h : Used to display the hep ")
    else:
        print("invalid number of command line arguments  ")        
        print("Use the give flag as :")
        print("--u : Use to display the usage")
        print("--h : Used to display the hep ")
        
    print(Border)
    print("-------- Thanku for using script -------")
    print("---------  -------")
    
    
    print(Border)
    

if __name__ == "__main__":
    main()