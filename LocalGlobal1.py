No = 11     # Global 

def Fun():
    No = 21     # Local 
    print("Value of no from Fun is :", No)   # 21


print("Value Of no is : ", No)   # 11
Fun()