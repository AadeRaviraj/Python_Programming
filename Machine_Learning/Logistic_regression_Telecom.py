
import pandas as pd 


from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

from sklearn.metrics import accuracy_score, classification_report


# create the data 

data = {
    "Age": [25,45,30,50,35,60],
    "Monthly_Charges":[500,900,600,1000,700,1200],
    "Tenure":[12,3,24,2,18,1],
    "Support_Calls":[1,5,0,8,2,10],
    "Churn":[0,1,0,1,0,1]
}

df = pd.DataFrame(data)

print(df)