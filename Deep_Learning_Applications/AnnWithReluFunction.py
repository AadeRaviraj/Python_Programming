import numpy as np 
import matplotlib.pyplot as plt 


# Step 1 Activation function 
def reluX(x):
    return max(0,x)

# Step 2  : - Neuron Forward function

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
    
    y_hat = reluX(z)
    
    return z, y_hat

def plot_relu():
    # generate the range for z 
    z_value = np.linspace(-10,10,200)
    
    # Apply relu for all value 
    relu_value = np.maximum(0,z_value)
    
    plt.figure(figsize = (8,9))
    plt.plot(z_value, relu_value, label = "RelU Function ", color = "green")
    
    # Axis line 
    plt.axhline(y=0, color = 'black', linewidth= 0.5) 
    plt.axvline(x = 0 , color = 'grey', linestyle ='--')
    
    # label and title 
    
    plt.title('Relu Activation function ', fontsize=17)
    plt.xlabel("Input(z) ", fontsize = 14)    
    plt.ylabel("Output ", fontsize = 14)
    
    # grid and legent 
    plt.grid(True,linestyle ='--',alpha = 0.6)
    plt.legend()
    
    # show Graph 
    plt.show()

def main():
    
    print("---------- Nruron Demo --------")
    
    # exampel input 
    inputs = [1.0,2.0,3.0] # 0.6 + 0.8 + 2.8 +0.5 =4.7
    weight = [0.6,0.4,-0.2] # weight 
    bias = 0.5 # bias value 
    
    z, y_hat = marvellous_neuron_forward(inputs, weight,bias)
    
    print("Weightes calculates ",z)
    print("Yhat : ", y_hat)
    
    # plot ReLU Graph 
    plot_relu()
    

if __name__ == "__main__":
    main()