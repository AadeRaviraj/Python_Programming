from sklearn import tree

# Rough = 1
# Smooth = 0

# Label : 
        #  Tennis = 1
        # Cricket = 2
        
def main():
    print("Ball Classification case study")

    # Original Encoded Dataset
    # Independent variables (X)
    X = [[35,1],[47,1],[90 , 0], [48,1],[90,0],[35,1],[92,0],[35,1],[35,1],[35,1],[96,0],[43,1],[110,0],[35,1],[95,0]]
    
    
    # Dependent Variables (Y) 
    Y = [1,1,2,1,2,1,2,1,1,1,2,1,2,1,2]
    
        # Independent Variable for training 
    Xtrain =  [[35,1],[47,1],[90 , 0], [48,1],[90,0],[35,1],[92,0],[35,1],[35,1],[35,1],[96,0],[43,1],[110,0]]   
     
    # Independent Variable for testing  
    Xtest =  [[35,1],[95,0]]
    
    # Dependent variables for training 
    Ytrain  =   Y = [1,1,2,1,2,1,2,1,1,1,2,1,2]
    # Dependent variable for testing 
    Ytest =   Y = [1,2]
    
    ModelObj = tree.DecisionTreeClassifier()
    
    
    
    trainedMOdel= ModelObj.fit(Xtrain,Ytrain) # training the model
    
    Result = trainedMOdel.predict(Xtest)  # 1    2 
    
    print("Model Predicts the object  as : ",Result)
    
    



if __name__ == "__main__":
    main()
    
