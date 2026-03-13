import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression




def main():
    csvFileName = "Advertising.csv"
    
    df = pd.read_csv(csvFileName)
    
    print(df.shape)
    
    
    # Data Cleaning 
    if "Unnamed: 0" in df.columns:
        df.drop(columns=["Unnamed: 0"],inplace= True)
    
    print(df.shape)
    
        

if __name__ == "__main__":
    main()