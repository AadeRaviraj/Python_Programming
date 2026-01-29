from functools import reduce


CheckEven = lambda  No : No % 2 == 0
Increment = lambda  No : No + 1
Add = lambda No1 , No2 : No1 + No2


def filterX(Task, Elements):
    Result = list()
    
    
    for no in Elements:
        Ret = Task(no)
        
        if (Ret == True):
            Result.append(no)
    return Result


def mapX(Task , Elements):
    Result = list()
    
    for no in Elements:
        #Result.append(Task(no))   
        Ret = Task(no)
        Result.append(Ret)
    return Result


def main():
    Data = [11, 10 , 15 , 20 , 22 , 27 , 30]    
    print( " Actual Data is : ", Data)
    
    FData = list(filterX(CheckEven, Data))
    print(" Data After Filter is : ", FData)
    
    MData = list(mapX(Increment,FData))
    print(" Data After Map is : ",MData)
    
    RData = reduce(Add,MData)
    print(" Data After Reduce is : ",RData)
    

if __name__ == "__main__":
    main()