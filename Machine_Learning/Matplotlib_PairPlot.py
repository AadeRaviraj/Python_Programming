import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd 


def main():
    dataframefile ="iris.csv"
    df = pd.read_csv(dataframefile)
    sns.pairplot(df,hue="species")
    plt.show()

if __name__ == "__main__":
    main()