import multiprocessing
import time
import os

def SumEven(No):
    
    print("Pid of sum even :", os.getpid())    # 51
    print("PPid of sum even :", os.getppid())   # 21
    sum = 0 
    
    for i in range(2, No + 1 , 2):
        sum = sum + i
    print("Even Sum is :", sum)
    


def SumOdd(No):
    
    print("Pid of sum even :", os.getpid())   # 101
    print("PPid of sum even :", os.getppid())   # 21 
    sum = 0 
    
    for i in range(1, No + 1 , 2):
        sum = sum + i
    print("Odd Sum is :", sum)  
    

def main(): 
    print("Pid of Main :", os.getpid())   # 21
    print("PPid of Main :", os.getppid())   # CMD  11
    start_time = time.time()
    
    t1 = multiprocessing.Process(target=SumEven, args=(10000000,))
    t2 = multiprocessing.Process(target=SumOdd, args=(10000000,))
    
    t1.start()
    t2.start()
    
    t1.join()
    t2.join()
    
    end_time = time.time()
    
    print("Time required", end_time - start_time)

if __name__ == "__main__":
    main()