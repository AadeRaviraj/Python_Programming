from sklearn.datasets import load_iris



def main():
    print("Iris Classification case study ")
    
    DataSet = load_iris() 
    
    Border = "-" * 40
    
    print(Border)
    
    for i in range(len(DataSet.target)):
        print("ID %d, Features %s, Label %s"%(i,DataSet.data[i],DataSet.target[i]))
    

if __name__ == "__main__":
    main()