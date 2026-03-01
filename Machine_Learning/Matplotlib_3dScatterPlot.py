import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd 
from mpl_toolkits.mplot3d import Axes3D
from sklearn.datasets import load_iris



def main():
   
    loadiris = load_iris()
    dataframefile ="iris.csv"
    df = pd.read_csv(dataframefile)
    
    x = loadiris.data
    y = loadiris.target
    
    fig = plt.figure(figsize=(8,6))
    
    ax = fig.add_subplot(111,projection='3d')
    
    ax .scatter(x[:,2],x[:,3],x[:,0],c = y,cmap = "viridis", edgecolor = 'k')
    
    ax.set_xlabel("Petal Length")
    ax.set_ylabel("Petal Width")
    ax.set_zlabel("Sepal Length")
    
    plt.title("3d visualization - iris")
    plt.show()
    
    # sns.pairplot(df,hue="species")
    # plt.show()

if __name__ == "__main__":
    main()