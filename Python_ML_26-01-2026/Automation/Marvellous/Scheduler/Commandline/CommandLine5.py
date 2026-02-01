# python CommandLine3.py 11 21 Pune 89.90

import sys

def main():      
    
    if (len(sys.argv) < 3 or len(sys.argv) > 3 ):
        print("Invalid no of arguments ")
        
    else:        
        res = int(sys.argv[1] ) + int( sys.argv[2])
        print(res)

    
if __name__ == "__main__":
    main()