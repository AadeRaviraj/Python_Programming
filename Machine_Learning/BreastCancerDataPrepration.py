import pandas as pd 
from sklearn.datasets import load_breast_cancer

data = load_breast_cancer()

df = pd.DataFrame(data.data, columns=data.feature_names)   # type: ignore
df["target"] = data.target # type: ignore

df.to_csv("Breast_cancer.csv",index =False)

print("breast_cancer.csv  file gets created succesfully ")