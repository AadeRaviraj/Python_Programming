from functools import reduce

# def CheckEven(No):
#     return No %  2 == 0
CheckEven = lambda  No : No % 2 == 0

# def Increment(No):
#     return No + 1

Increment = lambda  No : No + 1

# def Add(No1, No2):
#     return No1 + No2

Add = lambda No1 , No2 : No1 + No2


def main():
    Data = [11, 10 , 15 , 20 , 22 , 27 , 30]    
    print( " Actual Data is : ", Data)
    
    FData = list(filter(CheckEven, Data))
    print(" Data After Filter is : ", FData)
    
    MData = list(map(Increment,FData))
    print(" Data After Map is : ",MData)
    
    RData = reduce(Add,MData)
    print(" Data After Reduce is : ",RData)
    

if __name__ == "__main__":
    main()