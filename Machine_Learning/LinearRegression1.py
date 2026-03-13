import numpy as np 
import pandas as pd 
import matplotlib as plt 


def MarvellousPredictor():
    # Load the data 
    X = [1,2,3,4,5]
    Y =[3,4,2,4,5]
    
    print("Values of independent variable  : X - ",X)
    print("Values of Dependent variable  : Y - ",Y)
    
    mean_x = np.mean(X)
    mean_y = np.mean(Y)
    
    print("X_Mean is : ",mean_x)
    print("Y_Mean is : ",mean_y)
    
    
    

def main():
    MarvellousPredictor()

if __name__ == "__main__":
    main()