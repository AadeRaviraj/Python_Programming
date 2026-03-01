import pandas as pd

import matplotlib.pyplot as plt

import seaborn as sns

from sklearn.model_selection import train_test_split

from sklearn.tree import DecisionTreeClassifier, plot_tree

from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    classification_report,
    ConfusionMatrixDisplay
)

Border = "-" * 50
##############################################################################################
# Step 1 :  Load the data set 
##############################################################################################

print(Border)
print("Step 1 : Load the dataset ")
print(Border)



DataSetPath = "iris.csv"

df = pd.read_csv(DataSetPath)

print("Dataset gets loaded successfully.... ")
print("Initial entries from dataset: ")
print(df.head())



##############################################################################################
# Step 2 :  Data Analysis (EDA) 
##############################################################################################

print(Border)
print("Step 2 : Data Analysis ")
print(Border)

print("Shape of dataset : ",df.shape)
print("Column Names : ", list(df.columns))

print("Missing values (Per Column ) ")
print(df.isnull().sum())

print("Class Distribution (species)")
print(df["species"].value_counts())

print("Statistical report of dataset ")
print(df.describe())



##############################################################################################
# Step 3 :  Decide Independent and Dependent variables 
##############################################################################################

print(Border)
print("Step 3 :  Decide Independent and Dependent variables ")
print(Border)

# X  : Independent Variables  / Feature
# Y  : Dependent Variables  / Label

feature_cols =  [
    "sepal length (cm)",
    "sepal width (cm)",
    "petal length (cm)",
    "petal width (cm)"  
]

X = df[feature_cols]
Y = df["species"]

print("X Shape : ", X.shape)
print("Y Shape : ", Y.shape)


##############################################################################################
# Step 4 : Visualization of Dataset
##############################################################################################

print(Border)
print("Step 4 : Visualization of Dataset")
print(Border)

# Scatter plot 
plt.figure(figsize=(7,5) )

for sp in df["species"].unique():
    temp = df[df["species"] == sp]
    plt.scatter(temp["petal length (cm)"],temp["petal width (cm)"], label = sp)

plt.title("Iris : Petal Length vs Petal Width")
plt.xlabel("petal length (cm)")
plt.ylabel("petal width (cm)")
plt.legend()
plt.grid(True)
plt.show()