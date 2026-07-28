from sklearn.linear_model import LogisticRegression
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Load Data 
data = load_breast_cancer()

X = data.data
y = data.target

print("X Shape :", X.shape)
print("Y Shape :", y.shape)
#  Split data fro train test split 

X_train, X_test, Y_train, Y_test = train_test_split(
    X,
    y,
    test_size= 0.2,
    random_state= 42
    
)

# create model 

modelLr = LogisticRegression(max_iter=5000)

# model train 

modelLr.fit(X_train, Y_train)

# model predict 

modelPredict = modelLr.predict(X_test)

accuracy = accuracy_score(
    Y_test,modelPredict
)

print(accuracy)

# print("Actual price : ",Y_test)
# print("Model predicted price : ", modelPredict)