from sklearn import tree

# Feature
# Rough = 1
# Smooth = 0

# Label : 
        #  Tennis = 1
        # Cricket = 2
        
def main():
    print("Ball Classification case study")

    # Independent variables (X)
    Features = [[35,1],[47,1],[90 , 0], [48,1],[90,0],[35,1],[92,0],[35,1],[35,1],[35,1],[96,0],[43,1],[110,0],[35,1],[95,0]]
    
    # Dependent Variables (Y) 
    Labels = [1,1,2,1,2,1,2,1,1,1,2,1,2,1,2]
    
    ModelObj = tree.DecisionTreeClassifier()
    
    trainedMOdel= ModelObj.fit(Features,Labels) # training the model
    
    Result = trainedMOdel.predict([[37,1 ],[94,0]])  # 1    2 
    print("Model Predicts the object  as : ",Result)
    
    

if __name__ == "__main__":
    main()
    
