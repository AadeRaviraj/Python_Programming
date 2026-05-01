from sklearn.datasets import  load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score



def main():
    iris = load_iris()
    
    X = iris.data # type: ignore
    Y = iris.target # type: ignore
    
    X_train , X_test, Y_train,Y_test = train_test_split(X,Y,train_size = 0.2)
    model = DecisionTreeClassifier()
    
    model.fit(X_train,Y_train)
    
    Y_pred = model.predict(X_test)
    
    accuracy = accuracy_score(Y_test,Y_pred)
    
    print("Accuracy is :", accuracy * 100)    
        
if __name__ == "__main__":
    main()