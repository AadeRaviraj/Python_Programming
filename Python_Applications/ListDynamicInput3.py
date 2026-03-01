def Summation(arr):
    Sum = 0     
    for i in range(len(arr)):
        Sum = Sum + arr[i]
    return Sum

def main():
    size = 0 
    Value = 0
    
    print("Enter the number of element : ")
    size = int(input())
    
    Data = list()
    
    print("Enter the elements")
    
    for i in range(size):
        Value = int(input())
        Data.append(Value)        
    
    Ret = Summation(Data)
    
    print("Summation is : ",Ret)


if __name__ == "__main__":
    main()