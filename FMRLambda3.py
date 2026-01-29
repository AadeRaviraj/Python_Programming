from functools import reduce

def main():
    Data = [11, 10 , 15 , 20 , 22 , 27 , 30]    
    print( " Actual Data is : ", Data)
    
    FData = list(filter((lambda  No : No % 2 == 0), Data))
    print(" Data After Filter is : ", FData)
    
    MData = list(map((lambda  No : No + 1),FData))
    print(" Data After Map is : ",MData)
    
    RData = reduce(( lambda No1 , No2 : No1 + No2),MData)
    print(" Data After Reduce is : ",RData)
    

if __name__ == "__main__":
    main()