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