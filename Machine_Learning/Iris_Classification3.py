from sklearn.datasets import load_iris


def main():
    print("Iris Classification case study ")
    
    DataSet = load_iris()
    
    # MetaData Dataset 
    print("Independent Variables are : ")
    print(DataSet.feature_names)
    print("Length of Independent variable  is : ", len(DataSet.feature_names))
    print("Dependent variables are : ")    
    
    print(DataSet.target_names)    
    print("Length of Dependent variable  is : ", len(DataSet.target_names))
    
    

if __name__ == "__main__":
    main()