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
    
    print(Data)

if __name__ == "__main__":
    main()