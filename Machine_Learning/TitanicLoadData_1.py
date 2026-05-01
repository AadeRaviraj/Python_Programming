import pandas as pd
import numpy as np 
import joblib
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix








#-----------------------------------------------------------------------------------------------------
#   Function name :  DisplayInfo
#   Description :    It Displays the formatted title
#   Parameter :      Title(Str)
#   Return :         None
#   Date :           14/03/2025
#   Author:          Raviraj Aade 
#----------------------------------------------------------------------------------------------------

def DisplayInfo(title):
    print("\n" + "=" * 70 )
    print(title)
    print("=" * 70 )


#-----------------------------------------------------------------------------------------------------
#   Function name :  ShowData
#   Description :    It shows basic information about dataset
#   Parameter :      df 
#                    df ->          Pandas dataframe object
#                    message
#                    message ->     Heading text to display
#   Return :         None
#   Date :           14/03/2025
#   Author:          Raviraj Aade 
#----------------------------------------------------------------------------------------------------

def ShowData(df, message):
    DisplayInfo(message)
    
    print("\nFirst 5 rows of dataset :")
    print(df.head())
    
    print("\nShape of dataset ")
    print(df.shape)
    
    print("\nColumn names : ")
    print(df.columns.tolist())
    
    print("\nMissing values in each column : ")
    print(df.isnull().sum())
    
    
    


#-----------------------------------------------------------------------------------------------------
#   Function name :  MarvellousTitanicLogistic
#   Description :    This is main pipeline Controller
#                    It loads y=the dataset , show raw data 
#                    It Preprocess the dataset & train the model 
#   Parameter :      DataPath of dataset  file
#   Return :         None
#   Date :           14/03/2025
#   Author:          Raviraj Aade 
#----------------------------------------------------------------------------------------------------


def MarvellousTitanicLogistic(DataPath):
    DisplayInfo("Step 1: Loading the dataset ")
    
    df = pd.read_csv(DataPath)
    ShowData(df,"Initial Dataset")
    
    
#-----------------------------------------------------------------------------------------------------
#   Function name :  main
#   Description :    Starting point of application
#   Parameter :      None
#   Return :         None
#   Date :           14/ 03/2025
#   Author:          Raviraj Aade 
#----------------------------------------------------------------------------------------------------

def main():
    MarvellousTitanicLogistic("MarvellousTitanicDataset.csv")

if __name__ == "__main__":
    main()