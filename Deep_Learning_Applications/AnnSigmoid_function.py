# -------------------------------------------------------------------------------------------------------
# Program : Artificial Neuron with Sigmoid Activation 
# Author :  Raviraj Shankar Aade
# -------------------------------------------------------------------------------------------------------

import math
import matplotlib.pyplot as plt 
import numpy as np 




# Step 1 : Sigmoid Activation Function 


def Sigmoid(value):
    return 1/(1 + math.exp(-value))






# Step 2 : Neuron Forward Pass 
# Performs :
#   1. Weighted sum 
#   2. Add bias
#   3. Apply sigmoid activation

def marvellous_neuron_forward(inputs , weights, bias):
    # Neuron calculaton start 
    print("------ Nauron Calculation Start --------")
    
    # Dispaly inputs and weights 
    print("Input    : ", inputs)
    print("Weights  : ", weights)
    print("Bias     : ", bias)
    
    # Step 2.1 : Weight calculation 
    # z = (x1 * w1 ) + (x2 * w2) + (x3 * w3) + bias
    
    z = sum(w * x for w , x in zip(inputs,weights)) + bias
    
    print("\n----- Weighted Sum calculation --------\n")
    print(" z = w.b + b : ", z)
    
    # Step 2.2 :- Activation function :
    # y_hat = relu(z)
    
    y_hat = Sigmoid(z)
    
    return z, y_hat

# Step 3 : Plot Sigmoid 

def plot_sigmoid():
    # generate the range for z 
    z_value = np.linspace(-10,10,200)
    
    # Apply Sigmoid to range  
    sigmoid_value = 1/(1+ np.exp(-z_value))
        
    plt.figure(figsize = (8,9))
    plt.plot(z_value, sigmoid_value, label = "Sigmoid  Function ",linewidth= 2, color = "blue")
    
    # Axis line 
    plt.axhline(y=0, color = 'black', linewidth= 0.5) 
    plt.axvline(x = 0 , color = 'black', linestyle ='--')
    
    # label and title 
    
    plt.title('Sigmoid  Activation function ', fontsize=17)
    plt.xlabel("Input(z) ", fontsize = 14)    
    plt.ylabel("Output ", fontsize = 14)
    
    # grid and legent 
    plt.grid(True,linestyle ='--',alpha = 0.6)
    plt.legend()
    
    # show Graph 
    plt.show()



def main():
    print("---------- Sigmoid Neuron  Demo --------")
    
    # exampel input 
    inputs = [1.0,2.0,3.0] # 0.6 + 0.8 + 2.8 +0.5 =4.7
    weight = [0.6,0.4,-0.2] # weight 
    bias = 0.5 # bias value 
    
    z, y_hat = marvellous_neuron_forward(inputs, weight,bias)
    
    print("Weightes calculates ",z)
    print("Yhat : ", y_hat)
    
    # plot ReLU Graph 
    plot_sigmoid()
    


if __name__ == "__main__":
    main()
