import numpy as np 


# ---------------------------------------------------------------------
# Step 1 :- Define the input function 
# ---------------------------------------------------------------------
# these are input coming on x1, x2, x3

input = np.array([2.0,3.0,4.0])


# ---------------------------------------------------------------------
# Step 2 :- Define Weights
# ---------------------------------------------------------------------
# Each input has a corresponding weights (w1,w2,w3)

weights = np.array([0.5,0.3,0.2])



# ---------------------------------------------------------------------
# Step 3 :- Define Bias
# ---------------------------------------------------------------------
# Bias is an additional parameter that helps to shift teh output 
# it allows the model to fit data better 

bias = 1.0 



# ---------------------------------------------------------------------
# Step 4 :- Calculate Weight Sum(Z) 
# ---------------------------------------------------------------------
# Formula :
# Z = (x1*w1 + x2*w2 + x3*w3) + bias
# Using numpy dot product for efficient calculation

weighted_sum = np.dot(input,weights) + bias

# Manual calculation :
# (2.0 * 0.5) + (3.0 * 0.3) + (4.0 * 0.2) + 1.0
#  1.0 + 0.9 + 0.8 +1.0   = 3.7



# ---------------------------------------------------------------------
# Step 5 :- Activation function ReLU 
# ---------------------------------------------------------------------
# ReLU (Rectified Linear Unit ):
# If value >  0 -> Return vale 
# if value <= 0  -> return 0 
#

def relu(x):
    return max(0,x)



# ---------------------------------------------------------------------
# Step 6 :- Final output  
# ---------------------------------------------------------------------
# pass the weighted sum through activation function 

output = relu(weighted_sum)



# ---------------------------------------------------------------------
# Step 7 :- Display Result  
# ---------------------------------------------------------------------

print("Input            : ", input)
print("Weights          : ", weights)
print("Bias             : ", bias)
print("Weighted Sum (Z) : ", weighted_sum)
print("Final Output     : ", output)


