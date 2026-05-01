# Bagging


import pandas as pd
from sklearn.model_selection import train_test_split 
from sklearn.ensemble import AdaBoostClassifier
from sklearn.metrics import accuracy_score,classification_report,confusion_matrix


# ---------------------------------------------------------------------------------------------------------
# Step 1 : Load the dataset
# ---------------------------------------------------------------------------------------------------------

df = pd.read_csv("Breast_cancer.csv")
print("Shape of dataset : ",df.shape)
print("First 5 records : ", df.head())



# ---------------------------------------------------------------------------------------------------------
# Step 2 : Separate feature and labels
# ---------------------------------------------------------------------------------------------------------

X = df.drop("target",axis=1)
Y = df["target"]


# ---------------------------------------------------------------------------------------------------------
# Step 3 : Split Dataset for training and testing 
# ---------------------------------------------------------------------------------------------------------

X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.2,random_state=42)



# ---------------------------------------------------------------------------------------------------------
# Step 4 : Create Boosting model (AdaBoost)
# ---------------------------------------------------------------------------------------------------------

boost_model = AdaBoostClassifier(
    n_estimators=50,  # no of model
    learning_rate=1.0, # increase the weight 
    random_state=42 # testing pattern number
    )


# ---------------------------------------------------------------------------------------------------------
# Step 5 : Train Boosting model
# ---------------------------------------------------------------------------------------------------------

boost_model.fit(X_train,Y_train)

# ---------------------------------------------------------------------------------------------------------
# Step 7 : Test Boosting model
# ---------------------------------------------------------------------------------------------------------

Y_pred = boost_model.predict(X_test)

# ---------------------------------------------------------------------------------------------------------
# Step 8 : Evaluate Boosting model
# ---------------------------------------------------------------------------------------------------------

print("Boosting Accuracy :", accuracy_score(Y_test,Y_pred))
print("Confusion Matrix : \n",confusion_matrix(Y_test,Y_pred))



